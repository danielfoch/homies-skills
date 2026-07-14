#!/usr/bin/env python3
"""Build spoking-content from one locked salute panel and one rigid arm rig."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage


HERE = Path(__file__).resolve().parent
LOADER_ROOT = HERE.parents[3]
sys.path.insert(0, str(LOADER_ROOT / "scripts"))

from assemble_sprite import extract_alpha  # noqa: E402
from repair_movie_style_canonical_six import (  # noqa: E402
    assemble_shared_palette_gif,
    mask_layer,
    moving_mask,
    nearest_inpaint,
    polygon_mask,
    recompose_source,
    rotate_layer,
    zero_low_alpha_fringe,
)


SLUG = "spoking-content"
RAW_SHA256 = "a8d083ef3e8d9032836010231b3b9ebfd0d37757e01a16583ee33d0e4c8ea1e1"
SELECTED_PANEL = 2
CELL = 627
SHARED_SCALE = 0.78
SIDE = round(CELL * SHARED_SCALE)
OFFSET = ((CELL - SIDE) // 2, (CELL - SIDE) // 2)
ANGLES = (-3.0, -1.0, 1.0, 3.0)
ARM_POLYGON_RAW = (
    (64, 460), (58, 365), (104, 292), (137, 244), (140, 102),
    (220, 102), (251, 194), (223, 252), (229, 307), (191, 420),
    (132, 462),
)
PIVOT_RAW = (222, 298)
JOINT_RADIUS_RAW = 27
STATIC_RECTS_RAW = ((260, 25, 415, 250), (270, 275, 500, 545))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mapped_point(point: tuple[int, int]) -> tuple[int, int]:
    return (
        OFFSET[0] + round(point[0] * SHARED_SCALE),
        OFFSET[1] + round(point[1] * SHARED_SCALE),
    )


def locked_plate(raw_alpha: Image.Image) -> Image.Image:
    row, column = divmod(SELECTED_PANEL, 2)
    panel = raw_alpha.crop(
        (column * CELL, row * CELL, (column + 1) * CELL, (row + 1) * CELL)
    )
    plate = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    plate.alpha_composite(panel.resize((SIDE, SIDE), Image.Resampling.LANCZOS), OFFSET)
    return zero_low_alpha_fringe(plate)


def static_mask() -> Image.Image:
    mask = Image.new("L", (CELL, CELL), 0)
    draw = ImageDraw.Draw(mask)
    for x0, y0, x1, y1 in STATIC_RECTS_RAW:
        draw.rectangle((*mapped_point((x0, y0)), *mapped_point((x1, y1))), fill=255)
    return mask


def build_frames(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    shape = polygon_mask(plate.size, tuple(mapped_point(point) for point in ARM_POLYGON_RAW))
    pivot = mapped_point(PIVOT_RAW)
    radius = round(JOINT_RADIUS_RAW * SHARED_SCALE)
    joint_shape = Image.new("L", plate.size, 0)
    ImageDraw.Draw(joint_shape).ellipse(
        (pivot[0] - radius, pivot[1] - radius, pivot[0] + radius, pivot[1] + radius),
        fill=255,
    )
    part = mask_layer(plate, shape)
    erase_shape = ImageChops.subtract(shape, joint_shape)
    erase_mask = ImageChops.multiply(erase_shape, plate.getchannel("A"))
    base = nearest_inpaint(plate, erase_mask, dilate=1)
    joint = mask_layer(plate, joint_shape)
    allowed_masks = [shape, erase_mask]
    frames: list[Image.Image] = []
    for angle in ANGLES:
        moved = rotate_layer(part, angle, pivot)
        frame = base.copy()
        frame.alpha_composite(moved)
        frame.alpha_composite(joint)
        frames.append(zero_low_alpha_fringe(frame))
        allowed_masks.append(moving_mask(moved))
    allowed = Image.new("L", plate.size, 0)
    for mask in allowed_masks:
        allowed = ImageChops.lighter(allowed, mask)
    allowed_array = ndimage.binary_dilation(np.asarray(allowed) > 0, iterations=8)
    return frames, Image.fromarray((allowed_array * 255).astype(np.uint8), mode="L")


def assert_locked_sequence(
    plate: Image.Image, frames: list[Image.Image], allowed: Image.Image
) -> dict[str, object]:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError("the rigid salute phases are not four unique cells")
    fixed = np.asarray(static_mask()) > 0
    arrays = [np.asarray(frame) for frame in frames]
    static_hashes = [hashlib.sha256(array[fixed].tobytes()).hexdigest() for array in arrays]
    if len(set(static_hashes)) != 1:
        raise ValueError("face/torso registration changed outside the arm rig")
    changed = np.zeros((CELL, CELL), dtype=bool)
    for array in arrays[1:]:
        changed |= np.any(array != arrays[0], axis=2)
    escaped = changed & ~(np.asarray(allowed) > 0)
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} changed pixels escaped the salute rig")
    margins: list[int] = []
    for frame in frames:
        bbox = frame.getchannel("A").getbbox()
        if bbox is None:
            raise ValueError("empty salute phase")
        margins.append(min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3]))
    if min(margins) < 60:
        raise ValueError(f"minimum margin {min(margins)}px is below 60px")
    return {
        "selected_panel": SELECTED_PANEL,
        "selected_panel_role": "only immutable face, torso, garment, arm and five-finger salute source",
        "registration_shift_per_phase": [[0, 0]] * 4,
        "shared_scale_per_phase": [SHARED_SCALE] * 4,
        "angles_degrees": list(ANGLES),
        "frame_sha256_rgba": hashes,
        "static_face_torso_sha256_rgba": static_hashes,
        "minimum_margin_px": min(margins),
        "changed_pixels_outside_rig": int(escaped.sum()),
        "sequence": [0, 1, 2, 3, 2, 1],
        "durations_ms": [210, 140, 140, 210, 140, 140],
    }


def save_alpha_plate(frames: list[Image.Image], output: Path) -> None:
    sheet = Image.new("RGBA", (CELL * 2, CELL * 2), (0, 0, 0, 0))
    for index, frame in enumerate(frames):
        row, column = divmod(index, 2)
        sheet.alpha_composite(frame, (column * CELL, row * CELL))
    sheet.save(output)


def main() -> None:
    raw = HERE / "raw-chroma.png"
    if sha256(raw) != RAW_SHA256:
        raise ValueError("immutable raw chroma hash mismatch")
    raw_alpha = extract_alpha(raw, edge_contract=True)
    raw_alpha.save(HERE / "raw-alpha.png")
    plate = locked_plate(raw_alpha)
    plate.save(HERE / "locked-plate.png")
    frames, allowed = build_frames(plate)
    evidence = assert_locked_sequence(plate, frames, allowed)
    evidence.update(
        {
            "raw_chroma_sha256": sha256(raw),
            "raw_alpha_sha256": sha256(HERE / "raw-alpha.png"),
            "locked_plate_sha256": sha256(HERE / "locked-plate.png"),
        }
    )
    save_alpha_plate(frames, HERE / "alpha-normalized.png")
    recompose_source(frames).save(HERE / f"{SLUG}.png")
    assemble_shared_palette_gif(frames, HERE / f"{SLUG}.gif")
    (HERE / "build-evidence.json").write_text(
        json.dumps(evidence, indent=2) + "\n", encoding="utf-8"
    )
    for name in (
        "raw-chroma.png", "raw-alpha.png", "locked-plate.png",
        "alpha-normalized.png", f"{SLUG}.png", f"{SLUG}.gif",
    ):
        path = HERE / name
        print(f"{sha256(path)}  {path}")


if __name__ == "__main__":
    main()
