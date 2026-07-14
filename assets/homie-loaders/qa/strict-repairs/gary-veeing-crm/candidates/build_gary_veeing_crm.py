#!/usr/bin/env python3
"""Build gary-veeing-crm from one locked raised-hands panel and two rigid arm rigs."""

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


SLUG = "gary-veeing-crm"
RAW_SHA256 = "14a1f3e3897946029de271ec038e06a55fe0755abb594326df7ec926dedf8b4e"
SELECTED_PANEL = 1
CELL = 627
SHARED_SCALE = 0.78
SIDE = round(CELL * SHARED_SCALE)
OFFSET = ((CELL - SIDE) // 2, (CELL - SIDE) // 2)
LEFT_ANGLES = (2.0, 0.7, -0.7, -2.0)
RIGHT_ANGLES = (-2.0, -0.7, 0.7, 2.0)
LEFT_ARM_POLYGON_RAW = (
    (20, 260), (155, 260), (175, 330), (205, 355), (180, 415),
    (165, 480), (115, 500), (70, 470), (60, 400), (35, 350),
)
RIGHT_ARM_POLYGON_RAW = (
    (455, 260), (580, 260), (590, 350), (560, 410), (535, 470),
    (490, 500), (445, 470), (430, 415), (400, 355), (420, 330),
)
LEFT_PIVOT_RAW = (180, 360)
RIGHT_PIVOT_RAW = (420, 360)
JOINT_RADIUS_RAW = 40
STATIC_RECTS_RAW = ((220, 100, 340, 260), (230, 300, 390, 590))


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


def rig_part(
    plate: Image.Image,
    polygon_raw: tuple[tuple[int, int], ...],
    pivot_raw: tuple[int, int],
) -> tuple[Image.Image, Image.Image, Image.Image, tuple[int, int]]:
    shape = polygon_mask(plate.size, tuple(mapped_point(point) for point in polygon_raw))
    pivot = mapped_point(pivot_raw)
    radius = round(JOINT_RADIUS_RAW * SHARED_SCALE)
    joint_shape = Image.new("L", plate.size, 0)
    ImageDraw.Draw(joint_shape).ellipse(
        (pivot[0] - radius, pivot[1] - radius, pivot[0] + radius, pivot[1] + radius),
        fill=255,
    )
    part = mask_layer(plate, shape)
    erase_shape = ImageChops.subtract(shape, joint_shape)
    erase_mask = ImageChops.multiply(erase_shape, plate.getchannel("A"))
    joint = mask_layer(plate, joint_shape)
    return part, erase_mask, joint, pivot


def build_frames(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    left, left_erase, left_joint, left_pivot = rig_part(
        plate, LEFT_ARM_POLYGON_RAW, LEFT_PIVOT_RAW
    )
    right, right_erase, right_joint, right_pivot = rig_part(
        plate, RIGHT_ARM_POLYGON_RAW, RIGHT_PIVOT_RAW
    )
    base = nearest_inpaint(plate, left_erase, dilate=1)
    base = nearest_inpaint(base, right_erase, dilate=1)
    core_mask = static_mask()
    allowed_masks = [left_erase, right_erase]
    frames: list[Image.Image] = []
    for left_angle, right_angle in zip(LEFT_ANGLES, RIGHT_ANGLES):
        moved_left = rotate_layer(left, left_angle, left_pivot)
        moved_right = rotate_layer(right, right_angle, right_pivot)
        frame = base.copy()
        frame.alpha_composite(moved_left)
        frame.alpha_composite(moved_right)
        frame.alpha_composite(left_joint)
        frame.alpha_composite(right_joint)
        frame.paste(base, (0, 0), core_mask)
        frames.append(zero_low_alpha_fringe(frame))
        allowed_masks.extend([moving_mask(moved_left), moving_mask(moved_right)])
    allowed = Image.new("L", plate.size, 0)
    for mask in allowed_masks:
        allowed = ImageChops.lighter(allowed, mask)
    allowed_array = ndimage.binary_dilation(np.asarray(allowed) > 0, iterations=8)
    return frames, Image.fromarray((allowed_array * 255).astype(np.uint8), mode="L")


def assert_locked_sequence(
    frames: list[Image.Image], allowed: Image.Image
) -> dict[str, object]:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError("the rigid raised-hands phases are not four unique cells")
    fixed = np.asarray(static_mask()) > 0
    arrays = [np.asarray(frame) for frame in frames]
    static_hashes = [hashlib.sha256(array[fixed].tobytes()).hexdigest() for array in arrays]
    if len(set(static_hashes)) != 1:
        raise ValueError("male face/torso registration changed outside the arm rigs")
    changed = np.zeros((CELL, CELL), dtype=bool)
    for array in arrays[1:]:
        changed |= np.any(array != arrays[0], axis=2)
    escaped = changed & ~(np.asarray(allowed) > 0)
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} changed pixels escaped the arm rigs")
    margins: list[int] = []
    for frame in frames:
        bbox = frame.getchannel("A").getbbox()
        if bbox is None:
            raise ValueError("empty raised-hands phase")
        margins.append(min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3]))
    if min(margins) < 60:
        raise ValueError(f"minimum margin {min(margins)}px is below 60px")
    return {
        "selected_panel": SELECTED_PANEL,
        "selected_panel_role": "only immutable male CRM face, torso, beanie, shirt, arms and hands source",
        "registration_shift_per_phase": [[0, 0]] * 4,
        "shared_scale_per_phase": [SHARED_SCALE] * 4,
        "left_angles_degrees": list(LEFT_ANGLES),
        "right_angles_degrees": list(RIGHT_ANGLES),
        "frame_sha256_rgba": hashes,
        "static_face_torso_sha256_rgba": static_hashes,
        "minimum_margin_px": min(margins),
        "changed_pixels_outside_rigs": int(escaped.sum()),
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
    evidence = assert_locked_sequence(frames, allowed)
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
