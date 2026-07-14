#!/usr/bin/env python3
"""Build serhanting-manager from one locked buttoning panel and two hand rigs."""

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
    zero_low_alpha_fringe,
)


SLUG = "serhanting-manager"
RAW_SHA256 = "664f0f5c836b4495aed3b9cd101f72cce7e44808ad2f3206814db4ee9b153cf4"
SELECTED_PANEL = 2
CELL = 627
SHARED_SCALE = 0.78
SIDE = round(CELL * SHARED_SCALE)
OFFSET = ((CELL - SIDE) // 2, (CELL - SIDE) // 2)
LEFT_DX = (-16, -8, 0, 3)
RIGHT_DX = (16, 8, 0, -3)
LEFT_HAND_ROI_RAW = (220, 370, 350, 475)
RIGHT_HAND_ROI_RAW = (325, 370, 440, 475)
LEFT_JOINT_RAW = (242, 416)
RIGHT_JOINT_RAW = (418, 420)
JOINT_RADIUS_RAW = 17
STATIC_RECTS_RAW = ((255, 10, 400, 185), (285, 190, 380, 365))
CLICK_RAYS_RAW = (
    ((317, 384), (308, 372)),
    ((351, 384), (360, 372)),
    ((334, 463), (334, 477)),
)


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
    roi_raw: tuple[int, int, int, int],
    joint_raw: tuple[int, int],
) -> tuple[Image.Image, Image.Image, Image.Image]:
    rgba = np.asarray(plate.convert("RGBA"), dtype=np.uint8)
    r, g, b, a = (rgba[:, :, index] for index in range(4))
    skin = (
        (a > 12)
        & (r > 150)
        & (g > 90)
        & (b > 60)
        & (r > g * 1.05)
        & (b < g * 0.92)
    )
    x0, y0 = mapped_point((roi_raw[0], roi_raw[1]))
    x1, y1 = mapped_point((roi_raw[2], roi_raw[3]))
    inside = np.zeros(skin.shape, dtype=bool)
    inside[y0:y1, x0:x1] = True
    selected = ndimage.binary_dilation(skin & inside, iterations=3)
    selected &= inside & (a > 6)
    shape = Image.fromarray((selected * 255).astype(np.uint8), mode="L")
    joint_point = mapped_point(joint_raw)
    radius = round(JOINT_RADIUS_RAW * SHARED_SCALE)
    joint_shape = Image.new("L", plate.size, 0)
    ImageDraw.Draw(joint_shape).ellipse(
        (
            joint_point[0] - radius,
            joint_point[1] - radius,
            joint_point[0] + radius,
            joint_point[1] + radius,
        ),
        fill=255,
    )
    part = mask_layer(plate, shape)
    erase_shape = ImageChops.subtract(shape, joint_shape)
    erase_mask = ImageChops.multiply(erase_shape, plate.getchannel("A"))
    joint = mask_layer(plate, joint_shape)
    return part, erase_mask, joint


def translate_layer(layer: Image.Image, dx: int) -> Image.Image:
    moved = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    moved.alpha_composite(layer, (dx, 0))
    return moved


def inpaint_with_locked_suit(
    plate: Image.Image, erase_masks: tuple[Image.Image, Image.Image]
) -> Image.Image:
    """Fill the hand-underlay only from authored blue-suit pixels, never tie/skin."""
    rgba = np.asarray(plate.convert("RGBA"), dtype=np.uint8).copy()
    r, g, b, a = (rgba[:, :, index] for index in range(4))
    erase = np.zeros(a.shape, dtype=bool)
    for mask in erase_masks:
        erase |= np.asarray(mask) > 12
    eligible = (a > 24) & (b > r * 1.12) & (b > g * 1.03) & ~erase
    if not eligible.any():
        raise ValueError("no authored blue-suit pixels available for hand underlay")
    indices = ndimage.distance_transform_edt(
        ~eligible, return_distances=False, return_indices=True
    )
    yy, xx = indices
    rgba[erase] = rgba[yy[erase], xx[erase]]
    return Image.fromarray(rgba, mode="RGBA")


def build_frames(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    left, left_erase, left_joint = rig_part(
        plate, LEFT_HAND_ROI_RAW, LEFT_JOINT_RAW
    )
    right, right_erase, right_joint = rig_part(
        plate, RIGHT_HAND_ROI_RAW, RIGHT_JOINT_RAW
    )
    base = inpaint_with_locked_suit(plate, (left_erase, right_erase))
    allowed_masks = [left_erase, right_erase]
    frames: list[Image.Image] = []
    for index, (left_dx, right_dx) in enumerate(zip(LEFT_DX, RIGHT_DX)):
        moved_left = translate_layer(left, left_dx)
        moved_right = translate_layer(right, right_dx)
        frame = base.copy()
        frame.alpha_composite(moved_left)
        frame.alpha_composite(moved_right)
        frame.alpha_composite(left_joint)
        frame.alpha_composite(right_joint)
        if index == 3:
            ray_mask = Image.new("L", plate.size, 0)
            ray_draw = ImageDraw.Draw(ray_mask)
            frame_draw = ImageDraw.Draw(frame)
            for start_raw, end_raw in CLICK_RAYS_RAW:
                start, end = mapped_point(start_raw), mapped_point(end_raw)
                ray_draw.line((start, end), fill=255, width=4)
                frame_draw.line((start, end), fill=(230, 168, 45, 255), width=4)
            allowed_masks.append(ray_mask)
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
        raise ValueError("the button/reset phases are not four unique cells")
    fixed = np.asarray(static_mask()) > 0
    arrays = [np.asarray(frame) for frame in frames]
    static_hashes = [hashlib.sha256(array[fixed].tobytes()).hexdigest() for array in arrays]
    if len(set(static_hashes)) != 1:
        raise ValueError("face/torso/suit registration changed outside the hand rig")
    changed = np.zeros((CELL, CELL), dtype=bool)
    for array in arrays[1:]:
        changed |= np.any(array != arrays[0], axis=2)
    escaped = changed & ~(np.asarray(allowed) > 0)
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} changed pixels escaped the hand rig")
    margins: list[int] = []
    for frame in frames:
        bbox = frame.getchannel("A").getbbox()
        if bbox is None:
            raise ValueError("empty button/reset phase")
        margins.append(min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3]))
    if min(margins) < 60:
        raise ValueError(f"minimum margin {min(margins)}px is below 60px")
    return {
        "selected_panel": SELECTED_PANEL,
        "selected_panel_role": "only immutable face, torso, pinstripe suit, lapels, tie, hands and arms source",
        "registration_shift_per_phase": [[0, 0]] * 4,
        "shared_scale_per_phase": [SHARED_SCALE] * 4,
        "left_hand_dx_px": list(LEFT_DX),
        "right_hand_dx_px": list(RIGHT_DX),
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
