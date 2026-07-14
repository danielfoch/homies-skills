#!/usr/bin/env python3
"""Rebuild Cher-Horowitzing from one unmistakably female canonical plate.

The rejected source preserved the male Marketing Homie's beard beneath a blond
wig.  This replacement uses one canonical adult woman in the yellow-plaid
fashion look.  Her face, hair, body, clothing, hands, lower phone, legs and feet
stay pixel-registered; only the connected upper lid opens while its blank
display wakes through four levels.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops
from scipy import ndimage

from assemble_sprite import extract_alpha


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "qa/strict-repairs/raw/cher-horowitzing-marketing-female-canonical.png"
EXPECTED_RAW_SHA256 = "bcb764f57481dac48482e23e74c4da155e09c3cc1965667631d3253126f1cd91"
SLUG = "cher-horowitzing-marketing"
CELL = 627
KEY = (0, 255, 0)
SAFE_MARGIN = 60
SITE_MATTE = (251, 249, 246)
SEQUENCE = (0, 1, 2, 3, 2, 1)
DURATIONS_MS = (210, 140, 140, 210, 140, 140)

# The inner blank display on the generated canonical phone.  The detection is
# deliberately bounded away from the bezel, hinge, hand and face.
SCREEN_ROI = (423, 122, 469, 192)
PHONE_LID_ROI = (407, 104, 490, 205)
PHONE_HINGE_Y = 205
LID_VERTICAL_SCALES = (0.58, 0.72, 0.86, 1.0)
SCREEN_COLORS = (
    (22, 25, 29),
    (72, 78, 84),
    (146, 157, 164),
    (222, 231, 235),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def keep_connected_character(image: Image.Image) -> Image.Image:
    """Discard disconnected generation debris before the plate is fitted."""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    visible = rgba[:, :, 3] > 12
    labels, count = ndimage.label(visible, structure=np.ones((3, 3), dtype=np.uint8))
    if count == 0:
        raise ValueError("chroma extraction removed the character")
    areas = np.bincount(labels.ravel())
    areas[0] = 0
    keep = labels == int(np.argmax(areas))
    rgba[~keep, 3] = 0
    return Image.fromarray(rgba, mode="RGBA")


def detect_phone_screen(base: Image.Image) -> np.ndarray:
    """Return the connected neutral-gray inner-display pixels only."""
    rgba = np.asarray(base.convert("RGBA"), dtype=np.uint8)
    rgb = rgba[:, :, :3]
    luminance = np.dot(rgb.astype(np.float32), [0.299, 0.587, 0.114])
    neutral = np.ptp(rgb.astype(np.int16), axis=2) < 24
    candidate = neutral & (luminance > 82) & (luminance < 210) & (rgba[:, :, 3] > 220)

    x0, y0, x1, y1 = SCREEN_ROI
    roi = np.zeros(candidate.shape, dtype=bool)
    roi[y0:y1, x0:x1] = True
    candidate &= roi

    labels, count = ndimage.label(candidate, structure=np.ones((3, 3), dtype=np.uint8))
    if count == 0:
        raise ValueError("could not find the canonical flip-phone display")
    areas = np.bincount(labels.ravel())
    areas[0] = 0
    screen = labels == int(np.argmax(areas))
    screen = ndimage.binary_fill_holes(screen)
    if not 900 <= int(screen.sum()) <= 4200:
        raise ValueError(f"unexpected screen mask area: {int(screen.sum())}")
    return screen


def build_raw_frames(base: Image.Image) -> tuple[list[Image.Image], np.ndarray]:
    screen = detect_phone_screen(base)
    original = np.asarray(base.convert("RGBA"), dtype=np.uint8)
    original_image = Image.fromarray(original, mode="RGBA")

    lid_box = Image.new("L", base.size, 0)
    lid_box.paste(255, PHONE_LID_ROI)
    lid_alpha = ImageChops.multiply(lid_box, base.getchannel("A"))
    lid_area = int(np.asarray(lid_alpha).astype(bool).sum())
    if not 3000 <= lid_area <= 9000:
        raise ValueError(f"unexpected canonical flip-phone lid area: {lid_area}")
    keep_alpha = ImageChops.subtract(Image.new("L", base.size, 255), lid_box)
    plate_alpha = ImageChops.multiply(base.getchannel("A"), keep_alpha)
    plate = original_image.copy()
    plate.putalpha(plate_alpha)

    frames: list[Image.Image] = []

    for screen_color, lid_scale in zip(SCREEN_COLORS, LID_VERTICAL_SCALES, strict=True):
        rgba = original.copy()
        source = original[:, :, :3].astype(np.float32)
        target = np.empty_like(source)
        target[...] = np.asarray(screen_color, dtype=np.float32)
        # Retain 12% of the canonical screen shading so the blank display stays
        # integrated with the illustrated phone while the wake pulse reads at
        # the dashboard's 128px size.
        lit = np.clip(target * 0.88 + source * 0.12, 0, 255)
        rgba[screen, :3] = lit[screen, :3].astype(np.uint8)
        lid = Image.fromarray(rgba, mode="RGBA")
        lid.putalpha(lid_alpha)
        moving_lid = lid.transform(
            base.size,
            Image.Transform.AFFINE,
            (
                1.0,
                0.0,
                0.0,
                0.0,
                1.0 / lid_scale,
                PHONE_HINGE_Y * (1.0 - 1.0 / lid_scale),
            ),
            resample=Image.Resampling.BICUBIC,
        )
        frame = plate.copy()
        frame.alpha_composite(moving_lid)
        frames.append(frame)

    # Prove that the canonical woman is identical outside the connected lid.
    motion_zone = np.zeros(screen.shape, dtype=bool)
    motion_zone[78:210, 395:502] = True
    for index, frame in enumerate(frames[1:], 1):
        changed = np.any(np.asarray(frame) != np.asarray(frames[0]), axis=2)
        escaped = changed & ~motion_zone
        if escaped.any():
            raise ValueError(f"frame {index} changed {int(escaped.sum())} pixels outside phone lid")
    return frames, motion_zone


def fit_as_one_registered_sequence(frames: list[Image.Image]) -> list[Image.Image]:
    """Crop and resample every phase through one shared transform."""
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
    return fitted


def assert_fitted_plate(frames: list[Image.Image]) -> None:
    """Reject body drift, palette drift, or changes outside the phone lid."""
    arrays = [np.asarray(frame, dtype=np.int16) for frame in frames]
    changed = np.zeros((CELL, CELL), dtype=bool)
    for frame in arrays[1:]:
        changed |= np.any(frame != arrays[0], axis=2)
    if not changed.any():
        raise ValueError("authored phases are identical")
    ys, xs = np.nonzero(changed)
    bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
    if bbox[2] > 320 or bbox[3] > 190 or bbox[0] < 175 or bbox[1] < 70:
        raise ValueError(f"motion escaped the upper-left phone display: {bbox}")
    if int(changed.sum()) > 1900:
        raise ValueError(f"phone-lid motion changed too many fitted pixels: {int(changed.sum())}")

    # The entire lower 70% and right 45% contain the face, torso, hair, plaid,
    # hip hand, legs and feet.  They must be byte-identical in every phase.
    fixed = np.zeros((CELL, CELL), dtype=bool)
    fixed[190:, :] = True
    fixed[:, 320:] = True
    for index, frame in enumerate(arrays[1:], 1):
        count = int(np.any(frame != arrays[0], axis=2)[fixed].sum())
        if count:
            raise ValueError(f"frame {index} changed {count} fixed-character pixels")


def recompose_source(frames: list[Image.Image]) -> Image.Image:
    source = Image.new("RGB", (CELL * 2, CELL * 2), KEY)
    for index, frame in enumerate(frames):
        bbox = frame.getchannel("A").getbbox()
        if bbox is None:
            raise ValueError(f"frame {index} is empty")
        left, top, right, bottom = bbox
        margin = min(left, top, CELL - right, CELL - bottom)
        if margin < SAFE_MARGIN:
            raise ValueError(f"frame {index} margin {margin}px is below {SAFE_MARGIN}px: {bbox}")
        green = Image.new("RGB", (CELL, CELL), KEY)
        green.paste(frame.convert("RGB"), (0, 0), frame.getchannel("A"))
        row, column = divmod(index, 2)
        source.paste(green, (column * CELL, row * CELL))
    return source


def assemble_shared_palette_gif(frames: list[Image.Image], output: Path) -> None:
    """Encode with one palette so the fixed woman cannot colour-flicker."""
    resized = [frame.resize((256, 256), Image.Resampling.LANCZOS) for frame in frames]
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
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("/tmp/cher-horowitz-female"),
        help="candidate/evidence directory",
    )
    parser.add_argument(
        "--promote",
        action="store_true",
        help="replace the production source and GIF after candidate QA",
    )
    args = parser.parse_args()

    if sha256(RAW) != EXPECTED_RAW_SHA256:
        raise ValueError(f"unexpected raw hash for {RAW}")
    base = keep_connected_character(extract_alpha(RAW))
    raw_frames, _ = build_raw_frames(base)
    frames = fit_as_one_registered_sequence(raw_frames)
    assert_fitted_plate(frames)
    source = recompose_source(frames)

    source_dir = args.output / "sources/wildcard"
    gif_dir = args.output / "gifs/wildcard"
    frame_dir = args.output / "frames"
    source_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)
    frame_dir.mkdir(parents=True, exist_ok=True)

    source_out = source_dir / f"{SLUG}.png"
    gif_out = gif_dir / f"{SLUG}.gif"
    source.save(source_out, optimize=True)
    for index, frame in enumerate(frames):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)
    assemble_shared_palette_gif(frames, gif_out)

    if args.promote:
        shutil.copy2(source_out, ROOT / f"sources/wildcard/{SLUG}.png")
        shutil.copy2(gif_out, ROOT / f"gifs/wildcard/{SLUG}.gif")

    print(f"source={source_out} sha256={sha256(source_out)}")
    print(f"gif={gif_out} sha256={sha256(gif_out)}")


if __name__ == "__main__":
    main()
