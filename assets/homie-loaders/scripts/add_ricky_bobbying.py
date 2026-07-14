#!/usr/bin/env python3
"""Build the locked-plate Ricky-Bobbying Manager loader.

One accepted Manager illustration supplies every character, suit, hand and
trophy pixel.  The four authored phases differ only inside a tiny trophy-glint
mask, so the victory pose cannot redraw, rescale or wiggle between frames.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage

from repair_movie_style_canonical_six import (
    CELL,
    assemble_shared_palette_gif,
    drop_tiny_alpha_islands,
    recompose_source,
    zero_low_alpha_fringe,
)


ROOT = Path(__file__).resolve().parents[1]
SLUG = "ricky-bobbying-manager"
RAW = ROOT / "qa/strict-repairs/raw/ricky-bobbying-manager-alpha.png"
RAW_SHA256 = "17046de6956f55ecd746537b041e96f3b5331801f3a7d7201509f9e1d7c2ccc9"
SAFE_MARGIN = 60


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def draw_podium_rail() -> Image.Image:
    """Mask the intentional thigh-up crop with a fixed finish-line rail."""
    scale = 4
    layer = Image.new("RGBA", (CELL * scale, CELL * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    ink = (54, 51, 48, 255)
    cream = (248, 242, 229, 255)
    navy = (38, 76, 119, 255)
    coral = (218, 76, 58, 255)

    def box(values: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
        return tuple(value * scale for value in values)

    draw.rounded_rectangle(box((103, 517, 524, 566)), radius=14 * scale, fill=cream, outline=ink, width=8 * scale)
    x0, y0, x1, y1 = 121, 529, 506, 553
    columns = 11
    square = (x1 - x0) / columns
    for column in range(columns):
        left = round((x0 + column * square) * scale)
        right = round((x0 + (column + 1) * square) * scale)
        midpoint = round((y0 + y1) / 2 * scale)
        top, bottom = y0 * scale, y1 * scale
        first = navy if column % 2 == 0 else cream
        second = cream if column % 2 == 0 else navy
        draw.rectangle((left, top, right, midpoint), fill=first)
        draw.rectangle((left, midpoint, right, bottom), fill=second)
    draw.rectangle(box((118, 526, 509, 530)), fill=coral)
    draw.rectangle(box((118, 552, 509, 556)), fill=coral)
    draw.rounded_rectangle(box((103, 517, 524, 566)), radius=14 * scale, outline=ink, width=8 * scale)
    return layer.resize((CELL, CELL), Image.Resampling.LANCZOS)


def build_static_plate() -> Image.Image:
    if sha256(RAW) != RAW_SHA256:
        raise ValueError(f"unexpected accepted plate hash: {RAW}")
    plate = Image.open(RAW).convert("RGBA")
    if plate.size != (1254, 1254):
        raise ValueError(f"unexpected accepted plate size: {plate.size}")

    # A single shared crop and transform is applied exactly once.  The bottom
    # is intentionally clipped behind the fixed checkered rail, never at a
    # visible limb edge.
    crop = plate.crop((270, 15, 1035, 1115))
    fitted = crop.resize((344, 495), Image.Resampling.LANCZOS)
    static = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    static.alpha_composite(fitted, (141, 62))
    static.alpha_composite(draw_podium_rail())
    static = zero_low_alpha_fringe(drop_tiny_alpha_islands(static, minimum_area=32))
    return static


def draw_glint(phase: int, static_alpha: Image.Image) -> Image.Image:
    """Draw one trophy-only shine phase and clip it to the static silhouette."""
    scale = 4
    layer = Image.new("RGBA", (CELL * scale, CELL * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    centres = ((350, 92), (374, 101), (401, 113), (425, 124))
    radii = (6, 9, 14, 10)
    cx, cy = centres[phase]
    radius = radii[phase]
    cx *= scale
    cy *= scale
    radius *= scale
    ink = (65, 57, 49, 245)
    gold = (240, 177, 68, 250)
    white = (255, 252, 236, 255)

    points: list[tuple[int, int]] = []
    for index in range(8):
        angle = np.deg2rad(-90 + index * 45)
        r = radius if index % 2 == 0 else radius * 0.25
        points.append((round(cx + np.cos(angle) * r), round(cy + np.sin(angle) * r)))
    draw.polygon(points, fill=white, outline=ink)
    draw.ellipse((cx - 2 * scale, cy - 2 * scale, cx + 2 * scale, cy + 2 * scale), fill=gold)

    streak = (10, 15, 23, 17)[phase] * scale
    draw.line(
        (cx - streak, cy + streak, cx + streak, cy - streak),
        fill=white,
        width=3 * scale,
    )
    glint = layer.resize((CELL, CELL), Image.Resampling.LANCZOS)
    # The glint never grows the silhouette or creates a detached satellite.
    glint.putalpha(ImageChops.multiply(glint.getchannel("A"), static_alpha))
    return glint


def build_frames() -> tuple[list[Image.Image], Image.Image, Image.Image]:
    static = build_static_plate()
    frames: list[Image.Image] = []
    allowed = Image.new("L", (CELL, CELL), 0)
    for phase in range(4):
        glint = draw_glint(phase, static.getchannel("A"))
        frame = static.copy()
        frame.alpha_composite(glint)
        # Alpha-compositing over a partially antialiased trophy edge can raise
        # that edge's numeric alpha even when the silhouette is visually fixed.
        # Restore the accepted static alpha byte-for-byte after adding colour.
        frame.putalpha(static.getchannel("A"))
        frames.append(frame)
        allowed = ImageChops.lighter(allowed, glint.getchannel("A"))

    allowed_array = ndimage.binary_dilation(np.asarray(allowed) > 0, iterations=3)
    allowed = Image.fromarray((allowed_array * 255).astype(np.uint8), mode="L")
    assert_candidate(frames, static, allowed)
    return frames, static, allowed


def assert_candidate(frames: list[Image.Image], static: Image.Image, allowed: Image.Image) -> None:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError("the four authored trophy-glint phases are not unique")

    arrays = [np.asarray(frame, dtype=np.int16) for frame in frames]
    alpha_masks = [np.asarray(frame.getchannel("A")) for frame in frames]
    if any(not np.array_equal(alpha_masks[0], alpha) for alpha in alpha_masks[1:]):
        raise ValueError("the locked character/trophy silhouette changed between phases")

    changed = np.zeros((CELL, CELL), dtype=bool)
    for candidate in arrays[1:]:
        changed |= np.any(candidate != arrays[0], axis=2)
    escaped = changed & ~(np.asarray(allowed) > 0)
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} pixels changed outside the trophy-glint rig")

    static_rgba = np.asarray(static)
    outside = ~(np.asarray(allowed) > 0)
    for index, frame in enumerate(frames):
        if not np.array_equal(np.asarray(frame)[outside], static_rgba[outside]):
            raise ValueError(f"phase {index} changed pixels outside the allowed glint")
        alpha = np.asarray(frame.getchannel("A")) > 12
        ys, xs = np.nonzero(alpha)
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        margin = min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3])
        if margin < SAFE_MARGIN:
            raise ValueError(f"phase {index} margin {margin}px below {SAFE_MARGIN}px")
        labels, count = ndimage.label(alpha, structure=np.ones((3, 3), dtype=np.uint8))
        areas = np.bincount(labels.ravel())[1:]
        significant = areas[areas >= max(32, round(alpha.sum() * 0.001))]
        if len(significant) != 1:
            raise ValueError(f"phase {index} has {len(significant)} significant components")

    ratio = float(changed.sum() / max(1, (alpha_masks[0] > 12).sum()))
    if not 0.00025 <= ratio <= 0.035:
        raise ValueError(f"glint changed-pixel ratio {ratio:.6f} outside expected range")


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

    frames, static, allowed = build_frames()
    source_out = source_dir / f"{SLUG}.png"
    gif_out = gif_dir / f"{SLUG}.gif"
    recompose_source(frames).save(source_out, optimize=True)
    assemble_shared_palette_gif(frames, gif_out)
    for index, frame in enumerate(frames):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)
    static.save(frame_dir / "locked-static-manager-trophy.png", optimize=True)
    allowed.save(frame_dir / "allowed-motion-mask.png", optimize=True)

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
