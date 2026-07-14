#!/usr/bin/env python3
"""Build the candidate-only Tyler-Durdening Listings loader.

One immutable generated plate is split into a locked body and two authored
forearm rigs.  The forearms rotate around pixel-fixed elbow pivots to perform a
controlled left/right shadow-boxing action; face, torso, legs, crop, and scale
never move or redraw.
"""

from __future__ import annotations

import hashlib
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage

from repair_movie_style_canonical_six import (
    CELL,
    assemble_shared_palette_gif,
    drop_tiny_alpha_islands,
    mask_layer,
    mask_union,
    moving_mask,
    polygon_mask,
    recompose_source,
    rotate_layer,
    zero_low_alpha_fringe,
)


ROOT = Path(__file__).resolve().parents[1]
SLUG = "tyler-durdening-listings"
RAW = ROOT / "qa/strict-repairs/raw/tyler-durdening-listings-alpha.png"
RAW_SHA256 = "ba9e1e5fa3b1d65c9cbc7c9ecb404b493a95779a09cc7f5e49dd699233c360a5"
OUTPUT = ROOT / f"qa/strict-repairs/{SLUG}/candidates"
SAFE_MARGIN = 60
TARGET_HEIGHT = 497
LEFT_PIVOT = (218, 202)
RIGHT_PIVOT = (409, 202)
# Left jab retracts to guard, then the right jab extends.  Perspective scaling
# is local to the moving forearm/fist; the body plate is never scaled or moved.
# The standard 0,1,2,3,2,1 playback reverses through the same intermediates.
ARM_PHASES = (
    (-42.0, 1.14, 0.0, 1.0, "left", 1.0),
    (-20.0, 1.07, 0.0, 1.0, "left", 0.58),
    (0.0, 1.0, 0.0, 1.0, None, 0.0),
    (0.0, 1.0, 42.0, 1.14, "right", 1.0),
)
LEFT_FIST = (233, 154)
RIGHT_FIST = (383, 153)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_locked_plate() -> Image.Image:
    if sha256(RAW) != RAW_SHA256:
        raise ValueError(f"unexpected accepted alpha hash: {RAW}")
    image = Image.open(RAW).convert("RGBA")
    if image.size != (1254, 1254):
        raise ValueError(f"unexpected accepted plate size: {image.size}")
    bbox = image.getchannel("A").getbbox()
    if bbox != (392, 23, 887, 1230):
        raise ValueError(f"unexpected accepted alpha bbox: {bbox}")

    x0, y0, x1, y1 = bbox
    crop = image.crop((x0 - 12, y0 - 12, x1 + 12, y1 + 12))
    width = round(crop.width * TARGET_HEIGHT / crop.height)
    fitted = crop.resize((width, TARGET_HEIGHT), Image.Resampling.LANCZOS)
    plate = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    plate.alpha_composite(fitted, ((CELL - width) // 2, (CELL - TARGET_HEIGHT) // 2))
    return zero_low_alpha_fringe(drop_tiny_alpha_islands(plate, minimum_area=24))


def ellipse_mask(center: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", (CELL, CELL), 0)
    x, y = center
    ImageDraw.Draw(mask).ellipse((x - radius, y - radius, x + radius, y + radius), fill=255)
    return mask


def transform_forearm(
    layer: Image.Image,
    angle: float,
    scale: float,
    pivot: tuple[int, int],
) -> Image.Image:
    rotated = rotate_layer(layer, angle, pivot)
    if abs(scale - 1.0) < 1e-6:
        return rotated
    inverse = 1.0 / scale
    px, py = pivot
    return rotated.transform(
        rotated.size,
        Image.Transform.AFFINE,
        (inverse, 0.0, px - px * inverse, 0.0, inverse, py - py * inverse),
        resample=Image.Resampling.BICUBIC,
    )


def transformed_point(
    point: tuple[int, int],
    pivot: tuple[int, int],
    angle: float,
    scale: float,
) -> tuple[float, float]:
    """Match Pillow's image-coordinate rotation, then local pivot scaling."""
    theta = math.radians(angle)
    dx, dy = point[0] - pivot[0], point[1] - pivot[1]
    x = math.cos(theta) * dx + math.sin(theta) * dy
    y = -math.sin(theta) * dx + math.cos(theta) * dy
    return pivot[0] + x * scale, pivot[1] + y * scale


def draw_tapered_motion_marks(
    side: str | None,
    strength: float,
    angle: float,
    scale_factor: float,
) -> Image.Image:
    if not side:
        return Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    pivot = LEFT_PIVOT if side == "left" else RIGHT_PIVOT
    original = LEFT_FIST if side == "left" else RIGHT_FIST
    end_x, end_y = transformed_point(original, pivot, angle, scale_factor)
    dx, dy = original[0] - end_x, original[1] - end_y
    length = max(1.0, math.hypot(dx, dy))
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    supersample = 4
    layer = Image.new("RGBA", (CELL * supersample, CELL * supersample), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    trail = 14.0 + 5.0 * strength
    # Two short tapered wedges begin inside the rear edge of the moving fist.
    # The arm is composited over them, so neither can read as a detached rod.
    for offset in (-4.5, 4.5):
        attach_x = end_x + ux * 8.0 + px * offset
        attach_y = end_y + uy * 8.0 + py * offset
        tail_x = end_x + ux * trail + px * offset * 1.12
        tail_y = end_y + uy * trail + py * offset * 1.12
        half_width = 2.4
        outer = [
            (round(tail_x * supersample), round(tail_y * supersample)),
            (round((attach_x + px * half_width) * supersample), round((attach_y + py * half_width) * supersample)),
            (round((attach_x - px * half_width) * supersample), round((attach_y - py * half_width) * supersample)),
        ]
        draw.polygon(outer, fill=(105, 42, 36, round(170 + 75 * strength)))
        inner_attach_x = end_x + ux * 9.0 + px * offset
        inner_attach_y = end_y + uy * 9.0 + py * offset
        inner_tail_x = end_x + ux * (trail - 2.0) + px * offset * 1.08
        inner_tail_y = end_y + uy * (trail - 2.0) + py * offset * 1.08
        inner = [
            (round(inner_tail_x * supersample), round(inner_tail_y * supersample)),
            (round((inner_attach_x + px * 1.15) * supersample), round((inner_attach_y + py * 1.15) * supersample)),
            (round((inner_attach_x - px * 1.15) * supersample), round((inner_attach_y - py * 1.15) * supersample)),
        ]
        draw.polygon(inner, fill=(248, 224, 178, round(190 + 60 * strength)))
    return zero_low_alpha_fringe(layer.resize((CELL, CELL), Image.Resampling.LANCZOS))


def build_rig(plate: Image.Image) -> tuple[Image.Image, Image.Image, Image.Image, Image.Image, Image.Image]:
    left_shape = polygon_mask(
        plate.size,
        ((217, 128), (241, 128), (251, 143), (248, 162), (238, 174),
         (230, 194), (222, 213), (207, 207), (205, 181), (212, 154)),
    )
    right_shape = polygon_mask(
        plate.size,
        ((365, 128), (402, 125), (415, 145), (413, 174), (410, 195),
         (407, 205), (397, 204), (391, 188), (383, 175), (368, 166), (363, 148)),
    )
    left_mask = ImageChops.multiply(left_shape, plate.getchannel("A"))
    right_mask = ImageChops.multiply(right_shape, plate.getchannel("A"))
    left_area = int((np.asarray(left_mask) > 12).sum())
    right_area = int((np.asarray(right_mask) > 12).sum())
    if not 900 <= left_area <= 8000 or not 900 <= right_area <= 8000:
        raise ValueError(f"unexpected forearm mask areas: left={left_area} right={right_area}")

    left = mask_layer(plate, left_shape)
    right = mask_layer(plate, right_shape)
    cap_mask = ImageChops.lighter(ellipse_mask(LEFT_PIVOT, 23), ellipse_mask(RIGHT_PIVOT, 23))
    caps = mask_layer(plate, cap_mask)
    erase_mask = ImageChops.lighter(ImageChops.lighter(left_mask, right_mask), cap_mask)
    erase = np.asarray(erase_mask) > 0
    rgba = np.asarray(plate, dtype=np.uint8).copy()
    rgba[erase] = 0
    base = Image.fromarray(rgba, mode="RGBA")

    # A peak jab must not leave any skin from the original guard fist behind.
    base_array = np.asarray(base)
    r, g, b, a = (base_array[:, :, index] for index in range(4))
    skin = (a > 12) & (r > 165) & (g > 125) & (b > 100) & (r > g)
    fist_rois = ((216, 132, 252, 178), (363, 130, 405, 178))
    for roi in fist_rois:
        x0, y0, x1, y1 = roi
        retained = int(skin[y0:y1, x0:x1].sum())
        if retained:
            raise ValueError(f"guard-fist erase retained {retained} skin pixels in {roi}")

    return base, left, right, caps, erase_mask


def build_frames() -> tuple[list[Image.Image], Image.Image, Image.Image]:
    plate = build_locked_plate()
    base, left, right, caps, original_motion = build_rig(plate)
    frames: list[Image.Image] = []
    allowed_masks = [original_motion]
    for left_angle, left_scale, right_angle, right_scale, arc_side, arc_strength in ARM_PHASES:
        moved_left = zero_low_alpha_fringe(transform_forearm(left, left_angle, left_scale, LEFT_PIVOT))
        moved_right = zero_low_alpha_fringe(transform_forearm(right, right_angle, right_scale, RIGHT_PIVOT))
        arc_angle = left_angle if arc_side == "left" else right_angle
        arc_scale = left_scale if arc_side == "left" else right_scale
        arc = draw_tapered_motion_marks(arc_side, arc_strength, arc_angle, arc_scale)
        frame = base.copy()
        frame.alpha_composite(arc)
        frame.alpha_composite(moved_left)
        frame.alpha_composite(moved_right)
        frame.alpha_composite(caps)
        frames.append(frame)
        allowed_masks.extend((moving_mask(moved_left), moving_mask(moved_right), moving_mask(arc)))

    allowed = mask_union(allowed_masks)
    allowed_array = ndimage.binary_dilation(np.asarray(allowed) > 0, iterations=3)
    allowed = Image.fromarray((allowed_array * 255).astype(np.uint8), mode="L")
    assert_candidate(frames, plate, allowed)
    return frames, plate, allowed


def assert_candidate(frames: list[Image.Image], plate: Image.Image, allowed: Image.Image) -> None:
    if len({hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames}) != 4:
        raise ValueError("the four authored boxing cells are not unique")

    arrays = [np.asarray(frame) for frame in frames]
    plate_array = np.asarray(plate)
    permitted = np.asarray(allowed) > 0
    outside = ~permitted
    for index, array in enumerate(arrays):
        mismatch = np.any(array != plate_array, axis=2) & outside
        if mismatch.any():
            raise ValueError(
                f"phase {index} violates immutable-plate contract at "
                f"{int(mismatch.sum())} pixels outside the saved allowed mask"
            )

    changed = np.zeros((CELL, CELL), dtype=bool)
    for array in arrays[1:]:
        changed |= np.any(array != arrays[0], axis=2)
    escaped = changed & outside
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} pixels changed outside the two arm rigs")

    # The face, torso core, pelvis, legs, and shoes must be byte-identical.
    stable_regions = ((275, 68, 352, 143), (275, 220, 352, 285), (245, 285, 390, 570))
    for box in stable_regions:
        x0, y0, x1, y1 = box
        reference = plate_array[y0:y1, x0:x1]
        for index, array in enumerate(arrays):
            if not np.array_equal(reference, array[y0:y1, x0:x1]):
                raise ValueError(f"phase {index} changed locked body region {box}")

    areas: list[int] = []
    centroids: list[tuple[float, float]] = []
    for index, frame in enumerate(frames):
        alpha = np.asarray(frame.getchannel("A")) > 12
        ys, xs = np.nonzero(alpha)
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        margin = min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3])
        if margin < SAFE_MARGIN:
            raise ValueError(f"phase {index} margin {margin}px below {SAFE_MARGIN}px; bbox={bbox}")
        labels, _ = ndimage.label(alpha, structure=np.ones((3, 3), dtype=np.uint8))
        component_areas = np.bincount(labels.ravel())[1:]
        significant = component_areas[component_areas >= max(32, round(alpha.sum() * 0.001))]
        if len(significant) != 1:
            raise ValueError(f"phase {index} has {len(significant)} significant components")
        areas.append(int(alpha.sum()))
        cy, cx = ndimage.center_of_mass(alpha)
        centroids.append((float(cx), float(cy)))

    area_span = (max(areas) - min(areas)) / max(areas)
    if area_span > 0.045:
        raise ValueError(f"foreground area span {area_span:.4f} exceeds 4.5%")
    anchor = centroids[2]
    max_shift = max(((x - anchor[0]) ** 2 + (y - anchor[1]) ** 2) ** 0.5 for x, y in centroids)
    if max_shift > 5.0:
        raise ValueError(f"arm-motion centroid proxy {max_shift:.3f}px exceeds 5px")

    union = np.logical_or.reduce([np.asarray(frame.getchannel("A")) > 12 for frame in frames])
    motion_ratio = float(changed.sum() / max(1, union.sum()))
    if not 0.06 <= motion_ratio <= 0.55:
        raise ValueError(f"boxing motion ratio {motion_ratio:.5f} outside expected range")
    if int(changed[110:245, 190:280].sum()) < 900 or int(changed[110:245, 350:435].sum()) < 900:
        raise ValueError("both forearms must contribute visible controlled motion")
    print(
        f"arm-rig assertions: area_span={area_span:.5f} "
        f"centroid_shift={max_shift:.3f}px motion_ratio={motion_ratio:.5f}"
    )


def main() -> None:
    source_dir = OUTPUT / "sources/wildcard"
    gif_dir = OUTPUT / "gifs/wildcard"
    frame_dir = OUTPUT / "frames" / SLUG
    for directory in (source_dir, gif_dir, frame_dir):
        directory.mkdir(parents=True, exist_ok=True)

    frames, plate, allowed = build_frames()
    source = source_dir / f"{SLUG}.png"
    gif = gif_dir / f"{SLUG}.gif"
    recompose_source(frames).save(source, optimize=True)
    assemble_shared_palette_gif(frames, gif)
    for index, frame in enumerate(frames):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)
    plate.save(frame_dir / "immutable-generated-listings-plate.png", optimize=True)
    allowed.save(frame_dir / "allowed-left-and-right-forearm-mask.png", optimize=True)
    print(f"{SLUG}: source={sha256(source)} gif={sha256(gif)}")


if __name__ == "__main__":
    main()
