#!/usr/bin/env python3
"""Build Oops-I-Did-It-Again-ing from one rigid canonical body plate.

The previous production repair moved the whole character between phases.  This
replacement keeps the bun, face, torso, chest hand, pelvis, crossed legs and
both feet byte-identical.  Only the reaching forearm rotates around one fixed
elbow, progressing from a small bend to the supplied straight-arm pose.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage

from assemble_sprite import extract_alpha


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "qa/strict-repairs/raw/oops-i-did-it-again-ing-offers-canonical.png"
EXPECTED_RAW_SHA256 = "7bc52d65e38d7f7f9a75b33749094b5252984fd45dbb2a8440d1799736558b83"
CELL = 627
KEY = (0, 255, 0)
ELBOW_X = 815
# Downward shear slopes, equivalent to a connected forearm progressively
# straightening from about 11 degrees to the exact horizontal reference pose.
PHASES = (0.20, 0.13, 0.065, 0.0)
SAFE_MARGIN = 60
SITE_MATTE = (251, 249, 246)
SEQUENCE = (0, 1, 2, 3, 2, 1)
DURATIONS_MS = (210, 140, 140, 210, 140, 140)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def keep_connected_character(image: Image.Image) -> Image.Image:
    """Discard any disconnected generation debris before the body is rigged."""
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


def masked_layer(image: Image.Image, mask: Image.Image) -> Image.Image:
    layer = image.copy().convert("RGBA")
    layer.putalpha(mask)
    return layer


def build_raw_frames(base: Image.Image) -> list[Image.Image]:
    subject_alpha = base.getchannel("A")

    # Isolate the canonical distal reaching arm and open hand.  The fixed upper
    # arm ends at the elbow; this avoids moving the shoulder or torso.
    forearm_shape = Image.new("L", base.size, 0)
    ImageDraw.Draw(forearm_shape).rectangle(
        (ELBOW_X, 0, base.width, base.height),
        fill=255,
    )
    forearm_alpha = ImageChops.multiply(forearm_shape, subject_alpha)
    forearm = masked_layer(base, forearm_alpha)

    # Split the straight arm exactly at the elbow column.  The moving half is
    # warped with zero displacement at this same column, so the connection is
    # continuous without a synthetic cuff, patch, ghost, or exposed gap.
    keep_alpha = ImageChops.subtract(Image.new("L", base.size, 255), forearm_shape)
    plate_alpha = ImageChops.multiply(subject_alpha, keep_alpha)
    plate = masked_layer(base, plate_alpha)

    frames: list[Image.Image] = []
    for slope in PHASES:
        # Pillow's affine tuple is an inverse map.  This implements the forward
        # warp y' = y + slope * (x - ELBOW_X): zero at the elbow, increasing
        # smoothly toward the open hand.
        moving = forearm.transform(
            base.size,
            Image.Transform.AFFINE,
            (1.0, 0.0, 0.0, -slope, 1.0, slope * ELBOW_X),
            resample=Image.Resampling.BICUBIC,
        )
        frame = plate.copy()
        frame.alpha_composite(moving)
        frames.append(frame)
    return frames


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


def assert_fixed_body(frames: list[Image.Image]) -> None:
    """Prove that all differences stay inside the articulated forearm region."""
    arrays = [np.asarray(frame, dtype=np.int16) for frame in frames]
    changed = np.zeros((CELL, CELL), dtype=bool)
    for frame in arrays[1:]:
        changed |= np.any(frame != arrays[0], axis=2)
    if not changed.any():
        raise ValueError("authored phases are identical")

    # The head/torso/chest-hand/hips/legs/feet occupy the fixed central/left
    # plate.  Any changed pixel left of this boundary would reveal body drift.
    change_x = np.nonzero(changed)[1]
    if int(change_x.min()) < 320:
        raise ValueError(f"motion escaped the reaching forearm: min changed x={change_x.min()}")

    base = arrays[0]
    for index, frame in enumerate(arrays[1:], 1):
        fixed_difference = np.any(frame[:, :320] != base[:, :320], axis=2).sum()
        if fixed_difference:
            raise ValueError(f"frame {index} changed {fixed_difference} fixed-body pixels")


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
    """Encode with one palette so the invariant body cannot colour-flicker."""
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
        pal = composited[index].quantize(
            palette=palette_reference,
            dither=Image.Dither.NONE,
        )
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
        default=Path("/tmp/oops-chest-reach"),
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
    frames = fit_as_one_registered_sequence(build_raw_frames(base))
    assert_fixed_body(frames)
    source = recompose_source(frames)

    source_dir = args.output / "sources/wildcard"
    gif_dir = args.output / "gifs/wildcard"
    frame_dir = args.output / "frames"
    source_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)
    frame_dir.mkdir(parents=True, exist_ok=True)

    source_out = source_dir / "oops-i-did-it-again-ing-offers.png"
    gif_out = gif_dir / "oops-i-did-it-again-ing-offers.gif"
    source.save(source_out, optimize=True)
    for index, frame in enumerate(frames):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)

    assemble_shared_palette_gif(frames, gif_out)

    if args.promote:
        shutil.copy2(source_out, ROOT / "sources/wildcard/oops-i-did-it-again-ing-offers.png")
        shutil.copy2(gif_out, ROOT / "gifs/wildcard/oops-i-did-it-again-ing-offers.gif")

    print(f"source={source_out} sha256={sha256(source_out)}")
    print(f"gif={gif_out} sha256={sha256(gif_out)}")


if __name__ == "__main__":
    main()
