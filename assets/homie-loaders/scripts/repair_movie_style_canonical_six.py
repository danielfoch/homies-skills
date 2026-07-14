#!/usr/bin/env python3
"""Rebuild six rejected movie loaders from canonical Homie plates.

The rejected release was generated as four independently redrawn clay/3D
mascots.  This repair intentionally starts from exactly one role-canonical
ink-and-watercolour plate per loader.  Only one small, explicitly masked part
moves; the remaining character pixels share one crop, scale, anchor and GIF
palette in every phase.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage

from assemble_sprite import extract_alpha


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "qa/strict-repairs/raw"
CELL = 627
KEY = (0, 255, 0)
SITE_MATTE = (251, 249, 246)
SAFE_MARGIN = 60
SEQUENCE = (0, 1, 2, 3, 2, 1)
DURATIONS_MS = (210, 140, 140, 210, 140, 140)


@dataclass(frozen=True)
class AssetSpec:
    slug: str
    raw_name: str
    raw_sha256: str
    min_motion_ratio: float = 0.0002
    max_motion_ratio: float = 0.22


SPECS = {
    "rambo-ing-manager": AssetSpec(
        "rambo-ing-manager",
        "rambo-ing-manager-canonical-v2.png",
        "54c3486172d73c4b5171f6fa20bad11d9b3cc008b8190f272e9d1972d3956636",
    ),
    "godfathering-reports": AssetSpec(
        "godfathering-reports",
        "godfathering-reports-canonical-v2.png",
        "6989561e0b98c580feb7940aa987d2570559c869b24ea16f4821b4c67bc2397b",
        min_motion_ratio=0.00002,
        max_motion_ratio=0.02,
    ),
    "pulp-fictioning-reports": AssetSpec(
        "pulp-fictioning-reports",
        "pulp-fictioning-reports-canonical-v3.png",
        "7c288cca224e3c461c7bd65691cc20ca51a0bc88766921797463a6023761e07c",
        min_motion_ratio=0.01,
        max_motion_ratio=0.26,
    ),
    "waynes-worlding-content": AssetSpec(
        "waynes-worlding-content",
        "waynes-worlding-content-canonical-v2.png",
        "48f5dc838ee78eb9b5afb2169ea3e3b10907d91823b72615f709cb2b30e36062",
        min_motion_ratio=0.005,
        max_motion_ratio=0.16,
    ),
    "bill-and-ted-ing-crm": AssetSpec(
        "bill-and-ted-ing-crm",
        "bill-and-ted-ing-crm-canonical-v2.png",
        "c053b3a5ebb26357b9c020516005939c0c6899d013cfc50064fb05d4ffeb3978",
        min_motion_ratio=0.003,
        max_motion_ratio=0.12,
    ),
    "robocopping-offers": AssetSpec(
        "robocopping-offers",
        "robocopping-offers-canonical-v2.png",
        "0410ebb5b61aff508c7961c295b768fa171329a2ac136c069f25843c2b2181a9",
        min_motion_ratio=0.003,
        max_motion_ratio=0.14,
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def keep_largest_connected_subject(image: Image.Image) -> Image.Image:
    """Drop any disconnected chroma-key speck while retaining the one subject."""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    visible = rgba[:, :, 3] > 12
    labels, count = ndimage.label(visible, structure=np.ones((3, 3), dtype=np.uint8))
    if count == 0:
        raise ValueError("chroma extraction removed the subject")
    areas = np.bincount(labels.ravel())
    areas[0] = 0
    keep = labels == int(np.argmax(areas))
    rgba[~keep, 3] = 0
    return Image.fromarray(rgba, mode="RGBA")


def polygon_mask(size: tuple[int, int], points: tuple[tuple[int, int], ...]) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).polygon(points, fill=255)
    return mask


def roi_colour_mask(
    image: Image.Image,
    roi: tuple[int, int, int, int],
    predicate: str,
) -> Image.Image:
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8)
    r, g, b, a = (rgba[:, :, index] for index in range(4))
    if predicate == "red":
        selected = (a > 12) & (r > 105) & (r > g * 1.28) & (r > b * 1.22)
    elif predicate == "dark":
        selected = (a > 12) & (r < 105) & (g < 105) & (b < 105)
    else:
        raise ValueError(predicate)
    x0, y0, x1, y1 = roi
    inside = np.zeros(selected.shape, dtype=bool)
    inside[y0:y1, x0:x1] = True
    selected &= inside
    return Image.fromarray((selected * 255).astype(np.uint8), mode="L")


def mask_layer(image: Image.Image, mask: Image.Image) -> Image.Image:
    alpha = ImageChops.multiply(image.getchannel("A"), mask)
    layer = image.copy()
    layer.putalpha(alpha)
    return layer


def nearest_inpaint(image: Image.Image, erase_mask: Image.Image, dilate: int = 2) -> Image.Image:
    """Replace a narrow erased overlay with nearest surrounding authored pixels."""
    erase = np.asarray(erase_mask, dtype=np.uint8) > 12
    if dilate:
        erase = ndimage.binary_dilation(erase, iterations=dilate)
    if not erase.any():
        raise ValueError("empty erase mask")
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    indices = ndimage.distance_transform_edt(
        erase,
        return_distances=False,
        return_indices=True,
    )
    yy, xx = indices
    rgba[erase] = rgba[yy[erase], xx[erase]]
    return Image.fromarray(rgba, mode="RGBA")


def rotate_layer(
    layer: Image.Image,
    angle: float,
    pivot: tuple[int, int],
    dx: int = 0,
    dy: int = 0,
) -> Image.Image:
    rotated = layer.rotate(
        angle,
        resample=Image.Resampling.BICUBIC,
        center=pivot,
        expand=False,
    )
    if not dx and not dy:
        return rotated
    moved = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    moved.alpha_composite(rotated, (dx, dy))
    return moved


def mask_union(masks: list[Image.Image]) -> Image.Image:
    out = Image.new("L", masks[0].size, 0)
    for mask in masks:
        out = ImageChops.lighter(out, mask)
    return out


def moving_mask(layer: Image.Image) -> Image.Image:
    return layer.getchannel("A").point(lambda value: 255 if value > 6 else 0)


def drop_tiny_alpha_islands(image: Image.Image, minimum_area: int = 16) -> Image.Image:
    """Remove sub-loader-scale resampling flecks without touching real parts."""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    visible = rgba[:, :, 3] > 6
    labels, count = ndimage.label(visible, structure=np.ones((3, 3), dtype=np.uint8))
    if not count:
        raise ValueError("animation frame has no foreground")
    areas = np.bincount(labels.ravel())
    remove_labels = np.flatnonzero(areas < minimum_area)
    remove_labels = remove_labels[remove_labels != 0]
    if len(remove_labels):
        remove = np.isin(labels, remove_labels)
        rgba[remove, 3] = 0
    return Image.fromarray(rgba, mode="RGBA")


def remove_visible_satellite_components(
    image: Image.Image,
    visibility_threshold: int = 48,
    maximum_expected_area: int = 256,
) -> Image.Image:
    """Remove opaque/semi-opaque flecks hidden by a low-alpha antialias bridge.

    A component can look detached to a human even when a few alpha=7 fringe
    pixels connect it to the body.  Labelling at a visibility threshold catches
    those cases. All intended moving parts in this batch overlap the main body,
    so any visible satellite is generation/resampling debris.
    """
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    high = rgba[:, :, 3] >= visibility_threshold
    labels, count = ndimage.label(high, structure=np.ones((3, 3), dtype=np.uint8))
    if count <= 1:
        return image.copy()
    areas = np.bincount(labels.ravel())
    areas[0] = 0
    main = int(np.argmax(areas))
    satellite_labels = [index for index in range(1, count + 1) if index != main]
    largest_satellite = max(int(areas[index]) for index in satellite_labels)
    if largest_satellite > maximum_expected_area:
        raise ValueError(
            f"unexpected visible detached component of {largest_satellite}px; "
            "the rig may have lost a real part"
        )
    satellites = np.isin(labels, satellite_labels)
    clear = ndimage.binary_dilation(satellites, iterations=2)
    # Never erase the high-alpha main subject if the cleanup halos touch.
    clear &= labels != main
    rgba[clear, 3] = 0
    return Image.fromarray(rgba, mode="RGBA")


def zero_low_alpha_fringe(image: Image.Image, threshold: int = 16) -> Image.Image:
    """Prevent near-transparent coloured wisps from tinting the green master."""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    rgba[rgba[:, :, 3] < threshold, 3] = 0
    return Image.fromarray(rgba, mode="RGBA")


def build_rambo(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    left_mask = roi_colour_mask(plate, (425, 130, 515, 405), "red")
    right_mask = roi_colour_mask(plate, (650, 130, 745, 405), "red")
    if int((np.asarray(left_mask) > 0).sum()) < 1500 or int((np.asarray(right_mask) > 0).sum()) < 1500:
        raise ValueError("Rambo headband-tail masks are unexpectedly small")
    left = mask_layer(plate, left_mask)
    right = mask_layer(plate, right_mask)
    base = nearest_inpaint(nearest_inpaint(plate, left_mask), right_mask)
    angles = ((-7.0, 7.0), (-2.0, 2.0), (7.0, -7.0), (2.0, -2.0))
    frames: list[Image.Image] = []
    allowed = [left_mask, right_mask]
    for left_angle, right_angle in angles:
        l = rotate_layer(left, left_angle, (486, 145))
        r = rotate_layer(right, right_angle, (681, 145))
        frame = base.copy()
        frame.alpha_composite(l)
        frame.alpha_composite(r)
        frames.append(frame)
        allowed.extend([moving_mask(l), moving_mask(r)])
    return frames, mask_union(allowed)


def build_godfather(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    brow_mask = roi_colour_mask(plate, (608, 104, 657, 133), "dark")
    area = int((np.asarray(brow_mask) > 0).sum())
    if not 80 <= area <= 800:
        raise ValueError(f"Godfather eyebrow mask area is unexpected: {area}")
    brow = mask_layer(plate, brow_mask)
    base = nearest_inpaint(plate, brow_mask, dilate=1)
    phases = ((1.5, 0, 2), (0.0, 0, 0), (-5.0, 0, -7), (-2.0, 0, -3))
    frames: list[Image.Image] = []
    allowed = [brow_mask]
    for angle, dx, dy in phases:
        moved = rotate_layer(brow, angle, (633, 121), dx, dy)
        frame = base.copy()
        frame.alpha_composite(moved)
        frames.append(frame)
        allowed.append(moving_mask(moved))
    return frames, mask_union(allowed)


def build_pulp(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    # The revised canonical plate keeps both distal arms in open green space.
    # Counter-rotating them around fixed elbows produces a real twist-dance
    # gesture without moving or redrawing the Reports face, torso, pelvis or legs.
    left_shape = polygon_mask(
        plate.size,
        ((320, 338), (392, 347), (413, 391), (366, 478), (325, 581),
         (275, 596), (236, 568), (247, 523), (286, 444)),
    )
    right_shape = polygon_mask(
        plate.size,
        ((786, 348), (836, 331), (858, 293), (839, 218), (872, 196),
         (916, 216), (915, 276), (883, 369), (856, 457), (808, 468)),
    )
    left_mask = ImageChops.multiply(left_shape, plate.getchannel("A"))
    right_mask = ImageChops.multiply(right_shape, plate.getchannel("A"))
    left_area = int((np.asarray(left_mask) > 12).sum())
    right_area = int((np.asarray(right_mask) > 12).sum())
    if not 10000 <= left_area <= 50000:
        raise ValueError(f"Pulp left-forearm mask area is unexpected: {left_area}")
    if not 10000 <= right_area <= 50000:
        raise ValueError(f"Pulp right-forearm mask area is unexpected: {right_area}")
    left = mask_layer(plate, left_shape)
    right = mask_layer(plate, right_shape)

    yy, xx = np.indices((plate.height, plate.width))
    left_joint_pixels = (xx - 365) ** 2 + (yy - 376) ** 2 <= 20 ** 2
    right_joint_pixels = (xx - 826) ** 2 + (yy - 410) ** 2 <= 20 ** 2
    left_erase = np.asarray(left_shape, dtype=np.uint8).copy()
    right_erase = np.asarray(right_shape, dtype=np.uint8).copy()
    left_erase[left_joint_pixels] = 0
    right_erase[right_joint_pixels] = 0
    left_erase_mask = ImageChops.multiply(
        Image.fromarray(left_erase, mode="L"), plate.getchannel("A")
    )
    right_erase_mask = ImageChops.multiply(
        Image.fromarray(right_erase, mode="L"), plate.getchannel("A")
    )
    base = nearest_inpaint(nearest_inpaint(plate, left_erase_mask, dilate=1), right_erase_mask, dilate=1)
    joints = mask_layer(
        plate,
        Image.fromarray(((left_joint_pixels | right_joint_pixels) * 255).astype(np.uint8), mode="L"),
    )

    phases = ((-7.5, 7.5), (-2.0, 2.0), (7.5, -7.5), (2.0, -2.0))
    frames: list[Image.Image] = []
    allowed = [left_mask, right_mask, left_erase_mask, right_erase_mask]
    for left_angle, right_angle in phases:
        left_moved = rotate_layer(left, left_angle, (365, 376))
        right_moved = rotate_layer(right, right_angle, (826, 410))
        frame = base.copy()
        frame.alpha_composite(left_moved)
        frame.alpha_composite(right_moved)
        frame.alpha_composite(joints)
        frames.append(frame)
        allowed.extend([moving_mask(left_moved), moving_mask(right_moved)])
    return frames, mask_union(allowed)


def build_wayne(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    head_shape = polygon_mask(
        plate.size,
        ((457, 50), (592, 45), (628, 95), (620, 225), (592, 302),
         (558, 320), (500, 300), (468, 235), (450, 135)),
    )
    head_mask = ImageChops.multiply(head_shape, plate.getchannel("A"))
    area = int((np.asarray(head_mask) > 12).sum())
    if not 25000 <= area <= 65000:
        raise ValueError(f"Wayne head mask area is unexpected: {area}")
    head = mask_layer(plate, head_shape)
    # Preserve a small connected neck overlap at the pivot to hide the joint.
    erase_array = np.asarray(head_shape, dtype=np.uint8).copy()
    erase_array[292:, :] = 0
    erase_mask = Image.fromarray(erase_array, mode="L")
    erase_mask = ImageChops.multiply(erase_mask, plate.getchannel("A"))
    base = nearest_inpaint(plate, erase_mask, dilate=1)
    phases = ((-5.0, -2, 2), (-1.5, 0, 0), (4.5, 2, -2), (1.5, 0, 0))
    frames: list[Image.Image] = []
    allowed = [erase_mask, head_mask]
    for angle, dx, dy in phases:
        moved = rotate_layer(head, angle, (550, 300), dx, dy)
        frame = base.copy()
        frame.alpha_composite(moved)
        frames.append(frame)
        allowed.append(moving_mask(moved))
    return frames, mask_union(allowed)


def build_bill_ted(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    arm_shape = polygon_mask(
        plate.size,
        ((674, 360), (718, 389), (753, 410), (925, 250), (952, 292),
         (931, 345), (765, 492), (708, 487), (671, 452)),
    )
    arm_mask = ImageChops.multiply(arm_shape, plate.getchannel("A"))
    area = int((np.asarray(arm_mask) > 12).sum())
    if not 10000 <= area <= 65000:
        raise ValueError(f"Bill/Ted forearm mask area is unexpected: {area}")
    arm = mask_layer(plate, arm_shape)
    erase_array = np.asarray(arm_shape, dtype=np.uint8).copy()
    yy, xx = np.indices(erase_array.shape)
    # A fixed elbow disk covers every resampled joint edge.
    overlap = (xx - 718) ** 2 + (yy - 432) ** 2 <= 18 ** 2
    erase_array[overlap] = 0
    erase_mask = Image.fromarray(erase_array, mode="L")
    erase_mask = ImageChops.multiply(erase_mask, plate.getchannel("A"))
    base = nearest_inpaint(plate, erase_mask, dilate=1)
    joint_mask = Image.fromarray((overlap * 255).astype(np.uint8), mode="L")
    joint = mask_layer(plate, joint_mask)
    phases = (-8.0, -2.5, 7.5, 2.0)
    frames: list[Image.Image] = []
    allowed = [erase_mask, arm_mask]
    for angle in phases:
        moved = rotate_layer(arm, angle, (718, 432))
        frame = base.copy()
        frame.alpha_composite(moved)
        frame.alpha_composite(joint)
        frames.append(frame)
        allowed.append(moving_mask(moved))
    return frames, mask_union(allowed)


def build_robocop(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    arm_shape = polygon_mask(
        plate.size,
        ((302, 194), (386, 196), (405, 244), (412, 430), (401, 492),
         (348, 504), (307, 452), (293, 252)),
    )
    arm_mask = ImageChops.multiply(arm_shape, plate.getchannel("A"))
    area = int((np.asarray(arm_mask) > 12).sum())
    if not 15000 <= area <= 70000:
        raise ValueError(f"RoboCop forearm mask area is unexpected: {area}")
    arm = mask_layer(plate, arm_shape)
    erase_array = np.asarray(arm_shape, dtype=np.uint8).copy()
    yy, xx = np.indices(erase_array.shape)
    overlap = (xx - 382) ** 2 + (yy - 468) ** 2 <= 21 ** 2
    erase_array[overlap] = 0
    erase_mask = Image.fromarray(erase_array, mode="L")
    erase_mask = ImageChops.multiply(erase_mask, plate.getchannel("A"))
    base = nearest_inpaint(plate, erase_mask, dilate=1)
    joint_mask = Image.fromarray((overlap * 255).astype(np.uint8), mode="L")
    joint = mask_layer(plate, joint_mask)
    phases = (-8.0, -2.5, 7.5, 2.0)
    frames: list[Image.Image] = []
    allowed = [erase_mask, arm_mask]
    scanner_x = (535, 549, 565, 553)
    for angle, scan_x in zip(phases, scanner_x):
        moved = rotate_layer(arm, angle, (382, 468))
        frame = base.copy()
        frame.alpha_composite(moved)
        frame.alpha_composite(joint)
        draw = ImageDraw.Draw(frame)
        draw.ellipse((scan_x - 4, 117, scan_x + 4, 125), fill=(255, 225, 205, 245))
        frames.append(frame)
        allowed.append(moving_mask(moved))
    scanner_mask = Image.new("L", plate.size, 0)
    ImageDraw.Draw(scanner_mask).rectangle((525, 108, 578, 135), fill=255)
    allowed.append(scanner_mask)
    return frames, mask_union(allowed)


BUILDERS = {
    "rambo-ing-manager": build_rambo,
    "godfathering-reports": build_godfather,
    "pulp-fictioning-reports": build_pulp,
    "waynes-worlding-content": build_wayne,
    "bill-and-ted-ing-crm": build_bill_ted,
    "robocopping-offers": build_robocop,
}


def fit_registered_sequence(
    frames: list[Image.Image],
    allowed_raw: Image.Image,
) -> tuple[list[Image.Image], Image.Image]:
    """Apply one shared crop/scale/bottom anchor to all phases and the QA mask."""
    union = Image.new("L", frames[0].size, 0)
    for frame in frames:
        union = ImageChops.lighter(union, frame.getchannel("A"))
    bbox = union.getbbox()
    if bbox is None:
        raise ValueError("animation has no visible pixels")
    left, top, right, bottom = bbox
    padding = 12
    crop = (
        max(0, left - padding),
        max(0, top - padding),
        min(frames[0].width, right + padding),
        min(frames[0].height, bottom + padding),
    )
    crop_width, crop_height = crop[2] - crop[0], crop[3] - crop[1]
    scale = min((CELL - SAFE_MARGIN * 2) / crop_width, (CELL - SAFE_MARGIN * 2) / crop_height)
    size = (round(crop_width * scale), round(crop_height * scale))
    x = (CELL - size[0]) // 2
    y = CELL - SAFE_MARGIN - size[1]

    fitted: list[Image.Image] = []
    for frame in frames:
        resized = frame.crop(crop).resize(size, Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
        canvas.alpha_composite(resized, (x, y))
        fitted.append(canvas)
    allowed = allowed_raw.crop(crop).resize(size, Image.Resampling.NEAREST)
    allowed_canvas = Image.new("L", (CELL, CELL), 0)
    allowed_canvas.paste(allowed, (x, y))
    # Lanczos and bicubic resampling can spread a transformed edge by a handful
    # of low-alpha pixels.  Eight fitted pixels is still a tight local guardrail
    # while preventing those deterministic filter fringes from being mislabeled
    # as unrelated character motion.
    allowed_array = ndimage.binary_dilation(np.asarray(allowed_canvas) > 0, iterations=8)
    return fitted, Image.fromarray((allowed_array * 255).astype(np.uint8), mode="L")


def assert_candidate(spec: AssetSpec, frames: list[Image.Image], allowed: Image.Image) -> None:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError(f"{spec.slug}: authored phases are not all unique")
    arrays = [np.asarray(frame, dtype=np.int16) for frame in frames]
    changed = np.zeros((CELL, CELL), dtype=bool)
    for frame in arrays[1:]:
        changed |= np.any(frame != arrays[0], axis=2)
    allowed_array = np.asarray(allowed) > 0
    escaped = changed & ~allowed_array
    if escaped.any():
        raise ValueError(f"{spec.slug}: {int(escaped.sum())} pixels changed outside the rig")

    subject_union = np.zeros((CELL, CELL), dtype=bool)
    areas: list[int] = []
    centroids: list[tuple[float, float]] = []
    for index, frame in enumerate(frames):
        alpha = np.asarray(frame.getchannel("A")) > 12
        subject_union |= alpha
        ys, xs = np.nonzero(alpha)
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        margin = min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3])
        if margin < SAFE_MARGIN:
            raise ValueError(f"{spec.slug}: frame {index} margin {margin}px below {SAFE_MARGIN}px")
        labels, count = ndimage.label(alpha, structure=np.ones((3, 3), dtype=np.uint8))
        component_areas = np.bincount(labels.ravel())[1:]
        significant = component_areas[component_areas >= max(32, round(alpha.sum() * 0.001))]
        if len(significant) != 1:
            raise ValueError(f"{spec.slug}: frame {index} has {len(significant)} significant components")
        areas.append(int(alpha.sum()))
        centroid_y, centroid_x = ndimage.center_of_mass(alpha)
        centroids.append((float(centroid_x), float(centroid_y)))

    ratio = float(changed.sum() / max(1, subject_union.sum()))
    if not spec.min_motion_ratio <= ratio <= spec.max_motion_ratio:
        raise ValueError(
            f"{spec.slug}: changed-pixel ratio {ratio:.6f} outside "
            f"[{spec.min_motion_ratio}, {spec.max_motion_ratio}]"
        )
    area_span = (max(areas) - min(areas)) / max(areas)
    if area_span > 0.05:
        raise ValueError(f"{spec.slug}: foreground area span {area_span:.4f} exceeds 5%")
    anchor = centroids[0]
    max_shift = max(((x - anchor[0]) ** 2 + (y - anchor[1]) ** 2) ** 0.5 for x, y in centroids)
    if max_shift > 2.75:
        raise ValueError(f"{spec.slug}: centroid shift {max_shift:.3f}px exceeds 2.75px")


def recompose_source(frames: list[Image.Image]) -> Image.Image:
    source = Image.new("RGB", (CELL * 2, CELL * 2), KEY)
    for index, frame in enumerate(frames):
        green = Image.new("RGB", (CELL, CELL), KEY)
        green.paste(frame.convert("RGB"), (0, 0), frame.getchannel("A"))
        row, column = divmod(index, 2)
        source.paste(green, (column * CELL, row * CELL))
    return source


def assemble_shared_palette_gif(frames: list[Image.Image], output: Path) -> None:
    resized = [frame.resize((256, 256), Image.Resampling.LANCZOS) for frame in frames]
    # Downsampling can break a faint antialias bridge and create a new 2–3px
    # visible island. Gate the actual GIF-resolution frames before quantizing.
    resized = [remove_visible_satellite_components(frame) for frame in resized]
    resized = [remove_visible_satellite_components(frame, visibility_threshold=64) for frame in resized]
    resized = [remove_visible_satellite_components(frame, visibility_threshold=128) for frame in resized]
    resized = [drop_tiny_alpha_islands(frame, minimum_area=8) for frame in resized]
    resized = [zero_low_alpha_fringe(frame) for frame in resized]
    resized = [drop_tiny_alpha_islands(frame, minimum_area=8) for frame in resized]
    composited: list[Image.Image] = []
    for frame in resized:
        matte = Image.new("RGBA", frame.size, SITE_MATTE + (255,))
        composited.append(Image.alpha_composite(matte, frame).convert("RGB"))

    contact = Image.new("RGB", (256 * len(composited), 256), SITE_MATTE)
    for index, frame in enumerate(composited):
        contact.paste(frame, (index * 256, 0))
    palette_reference = contact.quantize(
        colors=95,
        method=Image.Quantize.MEDIANCUT,
        dither=Image.Dither.NONE,
    )
    palette = palette_reference.getpalette()[: 255 * 3]
    palette.extend([0] * (255 * 3 - len(palette)))
    palette.extend([0, 0, 0])
    palette_reference.putpalette(palette)

    encoded: list[Image.Image] = []
    for index in SEQUENCE:
        frame = resized[index]
        pal = composited[index].quantize(palette=palette_reference, dither=Image.Dither.NONE)
        pal.putpalette(palette)
        transparent = frame.getchannel("A").point(lambda value: 255 if value < 96 else 0)
        pal.paste(255, mask=transparent)
        pal.info["transparency"] = 255
        pal.info["background"] = 255
        encoded.append(pal)

    output.parent.mkdir(parents=True, exist_ok=True)
    encoded[0].save(
        output,
        save_all=True,
        append_images=encoded[1:],
        duration=DURATIONS_MS,
        loop=0,
        disposal=2,
        transparency=255,
        optimize=False,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("/tmp/movie-style-canonical-six"))
    parser.add_argument("--promote", action="store_true")
    args = parser.parse_args()

    source_dir = args.output / "sources/wildcard"
    gif_dir = args.output / "gifs/wildcard"
    frame_root = args.output / "frames"
    source_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)
    frame_root.mkdir(parents=True, exist_ok=True)

    for slug, spec in SPECS.items():
        raw = RAW_DIR / spec.raw_name
        if sha256(raw) != spec.raw_sha256:
            raise ValueError(f"unexpected raw hash for {raw}")
        plate = keep_largest_connected_subject(extract_alpha(raw))
        raw_frames, allowed_raw = BUILDERS[slug](plate)
        raw_frames = [drop_tiny_alpha_islands(frame) for frame in raw_frames]
        frames, allowed = fit_registered_sequence(raw_frames, allowed_raw)
        # Resampling can collapse a previously legitimate antialias fragment
        # into a new 1–24px island. Clean once more at the actual authored cell
        # size so neither the chroma source nor 256px GIF can ship a stray fleck.
        frames = [drop_tiny_alpha_islands(frame, minimum_area=32) for frame in frames]
        frames = [remove_visible_satellite_components(frame) for frame in frames]
        frames = [remove_visible_satellite_components(frame, visibility_threshold=64) for frame in frames]
        frames = [remove_visible_satellite_components(frame, visibility_threshold=128) for frame in frames]
        frames = [drop_tiny_alpha_islands(frame, minimum_area=32) for frame in frames]
        frames = [zero_low_alpha_fringe(frame) for frame in frames]
        frames = [drop_tiny_alpha_islands(frame, minimum_area=32) for frame in frames]
        assert_candidate(spec, frames, allowed)

        source_out = source_dir / f"{slug}.png"
        gif_out = gif_dir / f"{slug}.gif"
        recompose_source(frames).save(source_out, optimize=True)
        assemble_shared_palette_gif(frames, gif_out)
        frame_dir = frame_root / slug
        frame_dir.mkdir(parents=True, exist_ok=True)
        for index, frame in enumerate(frames):
            frame.save(frame_dir / f"cell-{index}.png", optimize=True)
        allowed.save(frame_dir / "allowed-motion-mask.png", optimize=True)

        # The female Reports Pulp plate is retained only for reproducible audit
        # history. The active gallery replaced it with the user-approved male
        # Manager rebuild in repair_character_assignment_batch.py.
        if args.promote and slug != "pulp-fictioning-reports":
            shutil.copy2(source_out, ROOT / f"sources/wildcard/{slug}.png")
            shutil.copy2(gif_out, ROOT / f"gifs/wildcard/{slug}.gif")
        print(f"{slug}: source={sha256(source_out)} gif={sha256(gif_out)}")


if __name__ == "__main__":
    main()
