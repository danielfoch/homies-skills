#!/usr/bin/env python3
"""Build the candidate-only Tony-Starking Marketing loader.

The accepted generated Homie is fitted exactly once.  Every authored phase
reuses that immutable RGBA plate byte-for-byte; only two deterministic light
overlays pulse over the existing palm emitter and chest reactor.
"""

from __future__ import annotations

import hashlib
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
SLUG = "tony-starking-marketing"
RAW = ROOT / "qa/strict-repairs/raw/tony-starking-marketing-alpha.png"
RAW_SHA256 = "4d5c485655b1ce4d963fcf6ab7e5e6c7fe5247fd743d66e2c2ff3b68f5fa5725"
OUTPUT = ROOT / f"qa/strict-repairs/{SLUG}/candidates"
SAFE_MARGIN = 60
TARGET_HEIGHT = 497
PHASE_LEVELS = (0.34, 0.55, 0.78, 1.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_locked_plate() -> Image.Image:
    if sha256(RAW) != RAW_SHA256:
        raise ValueError(f"unexpected accepted alpha hash: {RAW}")
    image = Image.open(RAW).convert("RGBA")
    if image.size != (1254, 1254):
        raise ValueError(f"unexpected accepted plate size: {image.size}")
    bbox = image.getchannel("A").getbbox()
    if bbox != (328, 21, 830, 1207):
        raise ValueError(f"unexpected accepted alpha bbox: {bbox}")

    x0, y0, x1, y1 = bbox
    crop = image.crop((x0 - 12, y0 - 12, x1 + 12, y1 + 12))
    width = round(crop.width * TARGET_HEIGHT / crop.height)
    fitted = crop.resize((width, TARGET_HEIGHT), Image.Resampling.LANCZOS)
    plate = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    plate.alpha_composite(fitted, ((CELL - width) // 2, (CELL - TARGET_HEIGHT) // 2))
    return zero_low_alpha_fringe(drop_tiny_alpha_islands(plate, minimum_area=24))


def draw_energy_pulse(level: float) -> Image.Image:
    scale = 4
    layer = Image.new("RGBA", (CELL * scale, CELL * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    # Centres are measured on the one fitted plate, directly over the two
    # authored circular insets.  The pulse expands without altering the suit.
    for (cx, cy), base_radius in (((228, 174), 6), ((318, 190), 8)):
        radius = round((base_radius + 5 * level) * scale)
        halo = round((base_radius + 10 * level) * scale)
        x, y = cx * scale, cy * scale
        draw.ellipse(
            (x - halo, y - halo, x + halo, y + halo),
            fill=(116, 225, 255, round(24 + 46 * level)),
        )
        draw.ellipse(
            (x - radius, y - radius, x + radius, y + radius),
            fill=(211, 247, 255, round(155 + 85 * level)),
            outline=(56, 135, 166, 245),
            width=2 * scale,
        )
        core = max(2 * scale, round(radius * 0.48))
        draw.ellipse(
            (x - core, y - core, x + core, y + core),
            fill=(255, 255, 252, 255),
        )
    return layer.resize((CELL, CELL), Image.Resampling.LANCZOS)


def build_frames() -> tuple[list[Image.Image], Image.Image, Image.Image]:
    locked = build_locked_plate()
    frames: list[Image.Image] = []
    allowed = Image.new("L", (CELL, CELL), 0)
    for level in PHASE_LEVELS:
        pulse = draw_energy_pulse(level)
        frame = locked.copy()
        frame.alpha_composite(pulse)
        frame = zero_low_alpha_fringe(drop_tiny_alpha_islands(frame, minimum_area=18))
        frames.append(frame)
        allowed = ImageChops.lighter(allowed, pulse.getchannel("A"))

    allowed_array = ndimage.binary_dilation(np.asarray(allowed) > 0, iterations=2)
    allowed = Image.fromarray((allowed_array * 255).astype(np.uint8), mode="L")
    assert_candidate(frames, locked, allowed)
    return frames, locked, allowed


def assert_candidate(frames: list[Image.Image], locked: Image.Image, allowed: Image.Image) -> None:
    if len({hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames}) != 4:
        raise ValueError("the four authored pulse cells are not unique")

    arrays = [np.asarray(frame) for frame in frames]
    changed = np.zeros((CELL, CELL), dtype=bool)
    for array in arrays[1:]:
        changed |= np.any(array != arrays[0], axis=2)
    escaped = changed & ~(np.asarray(allowed) > 0)
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} changed pixels escaped the two pulse masks")

    locked_array = np.asarray(locked)
    immutable = (np.asarray(locked.getchannel("A")) > 12) & ~(np.asarray(allowed) > 0)
    for index, array in enumerate(arrays):
        if not np.array_equal(array[immutable], locked_array[immutable]):
            raise ValueError(f"phase {index} altered the immutable face/body/suit plate")

    areas: list[int] = []
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

    area_span = (max(areas) - min(areas)) / max(areas)
    if area_span > 0.025:
        raise ValueError(f"foreground area span {area_span:.4f} exceeds 2.5%")
    union = np.logical_or.reduce([np.asarray(frame.getchannel("A")) > 12 for frame in frames])
    motion_ratio = float(changed.sum() / max(1, union.sum()))
    if not 0.003 <= motion_ratio <= 0.10:
        raise ValueError(f"pulse motion ratio {motion_ratio:.5f} outside expected range")
    print(f"locked pulse assertions: area_span={area_span:.5f} motion_ratio={motion_ratio:.5f}")


def main() -> None:
    source_dir = OUTPUT / "sources/wildcard"
    gif_dir = OUTPUT / "gifs/wildcard"
    frame_dir = OUTPUT / "frames" / SLUG
    for directory in (source_dir, gif_dir, frame_dir):
        directory.mkdir(parents=True, exist_ok=True)

    frames, locked, allowed = build_frames()
    source = source_dir / f"{SLUG}.png"
    gif = gif_dir / f"{SLUG}.gif"
    recompose_source(frames).save(source, optimize=True)
    assemble_shared_palette_gif(frames, gif)
    for index, frame in enumerate(frames):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)
    locked.save(frame_dir / "locked-character-suit-and-emitters.png", optimize=True)
    allowed.save(frame_dir / "allowed-palm-and-chest-pulse-mask.png", optimize=True)
    print(f"{SLUG}: source={sha256(source)} gif={sha256(gif)}")


if __name__ == "__main__":
    main()
