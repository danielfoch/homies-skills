#!/usr/bin/env python3
"""Build Elle-Woodsing from one rigid female Homie and dog plate.

The woman, sunglasses, ponytail, hot-pink suit, handbag, holding arm, dog body,
legs and feet are literal canonical pixels in every phase.  Only the dog's
connected outer forepaw rotates around one fixed wrist to make a small wave.
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
RAW = ROOT / "qa/strict-repairs/raw/elle-woodsing-reports-female-canonical.png"
EXPECTED_RAW_SHA256 = "dc5425bc305869f361004ad6f3ad3b366ffd2d924c502e329e84cf1b5085f1b2"
SLUG = "elle-woodsing-reports"
CELL = 627
KEY = (0, 255, 0)
SAFE_MARGIN = 60
SITE_MATTE = (251, 249, 246)
SEQUENCE = (0, 1, 2, 3, 2, 1)
DURATIONS_MS = (210, 140, 140, 210, 140, 140)

# Tight raw-image polygon around only the dog's raised tan forepaw.  The purple
# sweater cuff stays on the fixed plate and makes a stable wrist connection.
PAW_POLYGON = (
    (655, 493),
    (646, 479),
    (652, 454),
    (663, 417),
    (681, 405),
    (706, 414),
    (710, 439),
    (693, 467),
    (676, 496),
    (665, 503),
)
PAW_PIVOT = (658, 499)
PAW_ANGLES = (-18.0, -6.0, 6.0, 18.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def keep_connected_subject(image: Image.Image) -> Image.Image:
    """Remove any disconnected generation debris before rigging."""
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


def masked_layer(image: Image.Image, mask: Image.Image) -> Image.Image:
    layer = image.copy().convert("RGBA")
    layer.putalpha(mask)
    return layer


def build_raw_frames(base: Image.Image) -> list[Image.Image]:
    subject_alpha = base.getchannel("A")
    paw_shape = Image.new("L", base.size, 0)
    ImageDraw.Draw(paw_shape).polygon(PAW_POLYGON, fill=255)
    paw_alpha = ImageChops.multiply(paw_shape, subject_alpha)
    paw_area = int((np.asarray(paw_alpha) > 12).sum())
    if not 2200 <= paw_area <= 3600:
        raise ValueError(f"unexpected raised-paw mask area: {paw_area}")
    paw = masked_layer(base, paw_alpha)

    # Keep a 7px wrist overlap on the fixed plate.  It hides subpixel seams at
    # the pivot without leaving a second visible paw as the outer paw waves.
    erase_shape = paw_shape.copy()
    erase_array = np.asarray(erase_shape, dtype=np.uint8).copy()
    erase_array[492:, :] = 0
    erase_shape = Image.fromarray(erase_array, mode="L")
    keep_alpha = ImageChops.subtract(Image.new("L", base.size, 255), erase_shape)
    plate_alpha = ImageChops.multiply(subject_alpha, keep_alpha)
    plate = masked_layer(base, plate_alpha)

    frames: list[Image.Image] = []
    for angle in PAW_ANGLES:
        moving = paw.rotate(
            angle,
            resample=Image.Resampling.BICUBIC,
            center=PAW_PIVOT,
            expand=False,
        )
        frame = plate.copy()
        frame.alpha_composite(moving)
        frames.append(frame)

    # Everything outside the dog's small upper-right paw box must be identical.
    arrays = [np.asarray(frame, dtype=np.int16) for frame in frames]
    allowed = np.zeros(arrays[0].shape[:2], dtype=bool)
    allowed[380:530, 615:735] = True
    for index, frame in enumerate(arrays[1:], 1):
        escaped = np.any(frame != arrays[0], axis=2) & ~allowed
        if escaped.any():
            raise ValueError(f"frame {index} changed {int(escaped.sum())} pixels outside paw")
    return frames


def fit_as_one_registered_sequence(frames: list[Image.Image]) -> list[Image.Image]:
    """Crop and resample every phase with one shared transform."""
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


def assert_fixed_plate(frames: list[Image.Image]) -> None:
    """Prove the fitted woman, handbag and dog body never move or redraw."""
    arrays = [np.asarray(frame, dtype=np.int16) for frame in frames]
    changed = np.zeros((CELL, CELL), dtype=bool)
    for frame in arrays[1:]:
        changed |= np.any(frame != arrays[0], axis=2)
    if not changed.any():
        raise ValueError("authored phases are identical")
    ys, xs = np.nonzero(changed)
    bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
    if bbox[0] < 365 or bbox[2] > 425 or bbox[1] < 150 or bbox[3] > 230:
        raise ValueError(f"motion escaped the fitted dog-paw region: {bbox}")
    if int(changed.sum()) > 1100:
        raise ValueError(f"paw wave changed too many fitted pixels: {int(changed.sum())}")

    fixed = np.zeros((CELL, CELL), dtype=bool)
    fixed[:, :365] = True
    fixed[230:, :] = True
    for index, frame in enumerate(arrays[1:], 1):
        count = int(np.any(frame != arrays[0], axis=2)[fixed].sum())
        if count:
            raise ValueError(f"frame {index} changed {count} fixed-subject pixels")


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
    """Encode with one palette so the fixed illustration cannot shimmer."""
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
        default=Path("/tmp/elle-woodsing-paw"),
        help="candidate/evidence directory",
    )
    parser.add_argument(
        "--promote",
        action="store_true",
        help="install the new production source and GIF after candidate QA",
    )
    args = parser.parse_args()

    if sha256(RAW) != EXPECTED_RAW_SHA256:
        raise ValueError(f"unexpected raw hash for {RAW}")
    base = keep_connected_subject(extract_alpha(RAW))
    frames = fit_as_one_registered_sequence(build_raw_frames(base))
    assert_fixed_plate(frames)
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
