#!/usr/bin/env python3
"""Build the fixed-pivot Tarzaning Manager loader.

The character is one accepted, immutable Homies plate.  A deterministic vine
is drawn once behind the locked plate, the two are fused into one rig, and the
entire rig is rotated around one pixel-fixed overhead pivot.  No character,
hand, face, clothing, or vine geometry is redrawn between phases.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

from repair_movie_style_canonical_six import (
    CELL,
    assemble_shared_palette_gif,
    drop_tiny_alpha_islands,
    recompose_source,
    zero_low_alpha_fringe,
)


ROOT = Path(__file__).resolve().parents[1]
SLUG = "tarzaning-manager"
RAW = ROOT / "qa/strict-repairs/raw/tarzaning-manager-alpha-v2.png"
RAW_SHA256 = "33e4ea830ec94f4b0c2bf0f6d346b41eb42aaa2c405df5149eaf6b102e090228"

SAFE_MARGIN = 60
PIVOT = (245, 70)
HAND_POINT = (245, 151)
# Authored left-to-right.  The standard runtime sequence 0,1,2,3,2,1 then
# returns through the same intermediate poses for a genuinely smooth loop.
ANGLES = (-9.0, -3.0, 3.0, 9.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def draw_vine() -> Image.Image:
    """Draw the one authored vine, including an overlap behind both hands."""
    scale = 4
    layer = Image.new("RGBA", (CELL * scale, CELL * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    points = [
        (PIVOT[0] * scale, PIVOT[1] * scale),
        ((PIVOT[0] - 1) * scale, 91 * scale),
        ((PIVOT[0] + 2) * scale, 119 * scale),
        (HAND_POINT[0] * scale, (HAND_POINT[1] + 18) * scale),
    ]
    ink = (58, 48, 39, 255)
    bark = (111, 75, 49, 255)
    light = (173, 126, 82, 210)
    draw.line(points, fill=ink, width=18 * scale, joint="curve")
    draw.line(points, fill=bark, width=11 * scale, joint="curve")
    highlight = [(x + 2 * scale, y) for x, y in points]
    draw.line(highlight, fill=light, width=3 * scale, joint="curve")

    # Rounded caps prevent anti-alias pinholes at the fixed pivot and hand grip.
    for x, y in (points[0], points[-1]):
        radius = 5 * scale
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=bark, outline=ink, width=2 * scale)
    return layer.resize((CELL, CELL), Image.Resampling.LANCZOS)


def draw_fixed_pivot_cap() -> Image.Image:
    """Mask sub-pixel rotation changes at the overhead anchor with one fixed knot."""
    scale = 4
    layer = Image.new("RGBA", (CELL * scale, CELL * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    x, y = PIVOT[0] * scale, PIVOT[1] * scale
    draw.ellipse(
        (x - 8 * scale, y - 8 * scale, x + 8 * scale, y + 8 * scale),
        fill=(111, 75, 49, 255),
        outline=(58, 48, 39, 255),
        width=3 * scale,
    )
    draw.arc(
        (x - 4 * scale, y - 5 * scale, x + 5 * scale, y + 5 * scale),
        start=205,
        end=510,
        fill=(179, 132, 87, 255),
        width=2 * scale,
    )
    return layer.resize((CELL, CELL), Image.Resampling.LANCZOS)


def build_locked_rig() -> Image.Image:
    if sha256(RAW) != RAW_SHA256:
        raise ValueError(f"unexpected accepted plate hash: {RAW}")
    plate = Image.open(RAW).convert("RGBA")
    if plate.size != (1254, 1254):
        raise ValueError(f"unexpected accepted plate size: {plate.size}")

    # One shared crop, scale, and anchor.  The accepted figure is never fitted
    # independently per phase.
    crop = plate.crop((333, 14, 950, 1050))
    fitted = crop.resize((229, 385), Image.Resampling.LANCZOS)
    character = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    character.alpha_composite(fitted, (222, 137))

    rig = draw_vine()
    rig.alpha_composite(character)
    rig = zero_low_alpha_fringe(drop_tiny_alpha_islands(rig, minimum_area=24))

    alpha = np.asarray(rig.getchannel("A")) > 16
    labels, count = ndimage.label(alpha, structure=np.ones((3, 3), dtype=np.uint8))
    areas = np.bincount(labels.ravel())[1:]
    significant = areas[areas >= 32]
    if count < 1 or len(significant) != 1:
        raise ValueError(f"locked vine-character rig has {len(significant)} significant components")
    return rig


def build_frames() -> tuple[list[Image.Image], Image.Image, Image.Image]:
    rig = build_locked_rig()
    cap = draw_fixed_pivot_cap()
    frames: list[Image.Image] = []
    for angle in ANGLES:
        frame = rig.rotate(
            angle,
            resample=Image.Resampling.BICUBIC,
            center=PIVOT,
            expand=False,
            fillcolor=(0, 0, 0, 0),
        )
        frame.alpha_composite(cap)
        frame = zero_low_alpha_fringe(drop_tiny_alpha_islands(frame, minimum_area=24))
        frames.append(frame)

    pivot_mask = Image.new("L", (CELL, CELL), 0)
    ImageDraw.Draw(pivot_mask).ellipse(
        (PIVOT[0] - 4, PIVOT[1] - 4, PIVOT[0] + 4, PIVOT[1] + 4),
        fill=255,
    )
    assert_candidate(frames, rig, pivot_mask)
    return frames, rig, pivot_mask


def assert_candidate(frames: list[Image.Image], rig: Image.Image, pivot_mask: Image.Image) -> None:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError("the four authored pendulum phases are not unique")

    arrays = [np.asarray(frame) for frame in frames]
    alphas = [array[:, :, 3] > 16 for array in arrays]
    areas: list[int] = []
    centroids: list[tuple[float, float]] = []
    bboxes: list[tuple[int, int, int, int]] = []
    for index, alpha in enumerate(alphas):
        ys, xs = np.nonzero(alpha)
        if not len(xs):
            raise ValueError(f"phase {index} is empty")
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        bboxes.append(bbox)
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
    if area_span > 0.035:
        raise ValueError(f"foreground area span {area_span:.4f} exceeds 3.5%")

    # The small knot core is drawn after rotation and must be byte-identical.
    pivot = np.asarray(pivot_mask) > 0
    first_pivot = arrays[0][pivot]
    for index, array in enumerate(arrays[1:], start=1):
        if not np.array_equal(array[pivot], first_pivot):
            raise ValueError(f"phase {index} changed the fixed pivot core")

    union = np.logical_or.reduce(alphas)
    changed = np.zeros((CELL, CELL), dtype=bool)
    for array in arrays[1:]:
        changed |= np.any(array != arrays[0], axis=2)
    motion_ratio = float(changed.sum() / max(1, union.sum()))
    if not 0.35 <= motion_ratio <= 1.65:
        raise ValueError(f"pendulum motion ratio {motion_ratio:.4f} outside expected range")

    # A real swing should move the locked mass horizontally in both directions
    # while the pivot remains fixed; the figure itself never needs redrawing.
    centroid_x = [point[0] for point in centroids]
    if max(centroid_x) - min(centroid_x) < 35:
        raise ValueError(f"pendulum arc is too subtle: centroid span {max(centroid_x) - min(centroid_x):.2f}px")

    print(
        "rig assertions: "
        f"bboxes={bboxes} area_span={area_span:.4f} "
        f"centroid_x_span={max(centroid_x) - min(centroid_x):.2f}px "
        f"motion_ratio={motion_ratio:.4f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / f"qa/strict-repairs/{SLUG}/candidates",
    )
    parser.add_argument("--promote", action="store_true")
    args = parser.parse_args()

    source_dir = args.output / "sources/wildcard"
    gif_dir = args.output / "gifs/wildcard"
    frame_dir = args.output / "frames" / SLUG
    source_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)
    frame_dir.mkdir(parents=True, exist_ok=True)

    frames, rig, pivot_mask = build_frames()
    source_out = source_dir / f"{SLUG}.png"
    gif_out = gif_dir / f"{SLUG}.gif"
    recompose_source(frames).save(source_out, optimize=True)
    assemble_shared_palette_gif(frames, gif_out)
    for index, frame in enumerate(frames):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)
    rig.save(frame_dir / "locked-character-and-vine-rig.png", optimize=True)
    pivot_mask.save(frame_dir / "fixed-pivot-mask.png", optimize=True)

    if args.promote:
        production_source = ROOT / f"sources/wildcard/{SLUG}.png"
        production_gif = ROOT / f"gifs/wildcard/{SLUG}.gif"
        production_source.parent.mkdir(parents=True, exist_ok=True)
        production_gif.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_out, production_source)
        shutil.copy2(gif_out, production_gif)

    print(f"{SLUG}: source={sha256(source_out)} gif={sha256(gif_out)}")


if __name__ == "__main__":
    main()
