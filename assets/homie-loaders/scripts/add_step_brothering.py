#!/usr/bin/env python3
"""Build the Step-Brothering two-Homie portrait loader.

The accepted Manager + CRM illustration is one immutable transparent plate.
Every authored phase reuses that exact plate, crop, scale and anchor.  Only a
small camera-flash star behind the pair changes, so no face, hand, argyle
pattern, body or portrait-frame pixel can redraw or wiggle between frames.
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
    DURATIONS_MS,
    KEY,
    SEQUENCE,
    SITE_MATTE,
    drop_tiny_alpha_islands,
    recompose_source,
    zero_low_alpha_fringe,
)


ROOT = Path(__file__).resolve().parents[1]
SLUG = "step-brothering-manager-crm"
RAW = ROOT / "qa/strict-repairs/raw/step-brothering-manager-crm-alpha-v2.png"
RAW_SHA256 = "ad76fae1104bb1fcdf107762a6a09dc86dd55b9b950e5145b7e1b00de44f60e4"
SAFE_MARGIN = 60


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def draw_flash(phase: int) -> Image.Image:
    """Return one connected, anti-aliased camera-flash phase.

    The lowest ray touches the portrait frame's top-right corner so the flash
    remains one intentional foreground system instead of detached debris.
    """
    scale = 4
    size = CELL * scale
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    cx, cy = 477 * scale, 132 * scale
    radii = (22, 31, 43, 34)
    radius = radii[phase] * scale

    # Eight-point warm flash star. Alternating radii keep it hand-drawn and
    # readable without introducing any generated-frame anatomy changes.
    points: list[tuple[int, int]] = []
    for index in range(16):
        angle = np.deg2rad(-90 + index * 22.5)
        r = radius if index % 2 == 0 else radius * 0.34
        points.append((round(cx + np.cos(angle) * r), round(cy + np.sin(angle) * r)))
    draw.polygon(points, fill=(244, 172, 58, 238), outline=(60, 53, 47, 245), width=2 * scale)

    core = max(8, round(radius / scale * 0.28)) * scale
    draw.ellipse(
        (cx - core, cy - core, cx + core, cy + core),
        fill=(255, 247, 221, 255),
        outline=(60, 53, 47, 245),
        width=2 * scale,
    )

    # Two connected accent strokes push the motion into a clearly visible
    # camera-flash pulse at 128px while staying inside the safe margin.
    accent_length = (20, 34, 48, 37)[phase] * scale
    for angle_deg in (-12, 58):
        angle = np.deg2rad(angle_deg)
        start = radius * 0.86
        x0 = round(cx + np.cos(angle) * start)
        y0 = round(cy + np.sin(angle) * start)
        x1 = round(cx + np.cos(angle) * (start + accent_length))
        y1 = round(cy + np.sin(angle) * (start + accent_length))
        draw.line((x0, y0, x1, y1), fill=(231, 93, 69, 245), width=7 * scale)
        draw.line((x0, y0, x1, y1), fill=(255, 229, 148, 255), width=3 * scale)

    return layer.resize((CELL, CELL), Image.Resampling.LANCZOS)


def build_static_portrait() -> Image.Image:
    if sha256(RAW) != RAW_SHA256:
        raise ValueError(f"unexpected accepted plate hash: {RAW}")
    plate = Image.open(RAW).convert("RGBA")
    if plate.size != (1069, 1471):
        raise ValueError(f"unexpected accepted plate size: {plate.size}")

    # The supplied Step Brothers reference is a tight studio portrait.  This
    # fixed crop retains both faces, both stacked hands and both argyle vests,
    # then hides the intentional lower-body crop behind the photo-frame rail.
    crop = plate.crop((260, 52, 832, 756))
    fitted = crop.resize((404, 497), Image.Resampling.LANCZOS)

    portrait = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    portrait.alpha_composite(fitted, (111, 80))

    # Clip the immutable pair to the transparent photo window.  The lower
    # border is drawn over the cut, so it reads as a framed portrait rather
    # than an accidental character crop.
    window = Image.new("L", (CELL, CELL), 0)
    ImageDraw.Draw(window).rounded_rectangle((92, 79, 535, 547), radius=20, fill=255)
    portrait.putalpha(ImageChops.multiply(portrait.getchannel("A"), window))

    frame = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    ink = (60, 53, 47, 255)
    cream = (248, 241, 226, 255)
    warm = (221, 188, 126, 255)
    draw.rounded_rectangle((72, 60, 555, 566), radius=30, outline=ink, width=15)
    draw.rounded_rectangle((80, 68, 547, 558), radius=25, outline=cream, width=10)
    draw.rounded_rectangle((88, 76, 539, 550), radius=22, outline=warm, width=5)

    # A slightly deeper bottom rail gives the portrait a clear physical base
    # and masks the fixed crop on every phase.
    draw.rounded_rectangle((72, 524, 555, 566), radius=18, fill=cream, outline=ink, width=10)
    draw.line((98, 540, 529, 540), fill=warm, width=5)

    static = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    static.alpha_composite(portrait)
    static.alpha_composite(frame)
    return zero_low_alpha_fringe(drop_tiny_alpha_islands(static, minimum_area=32))


def build_frames() -> tuple[list[Image.Image], Image.Image, Image.Image]:
    static = build_static_portrait()
    flashes = [draw_flash(index) for index in range(4)]
    frames: list[Image.Image] = []
    allowed = Image.new("L", (CELL, CELL), 0)
    for flash in flashes:
        frame = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
        frame.alpha_composite(flash)
        frame.alpha_composite(static)
        frame = zero_low_alpha_fringe(drop_tiny_alpha_islands(frame, minimum_area=24))
        frames.append(frame)
        allowed = ImageChops.lighter(allowed, flash.getchannel("A"))

    allowed_array = ndimage.binary_dilation(np.asarray(allowed) > 0, iterations=3)
    allowed = Image.fromarray((allowed_array * 255).astype(np.uint8), mode="L")
    assert_candidate(frames, static, allowed)
    return frames, static, allowed


def assert_candidate(frames: list[Image.Image], static: Image.Image, allowed: Image.Image) -> None:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError("the four authored flash phases are not unique")

    base = np.asarray(frames[0], dtype=np.int16)
    changed = np.zeros((CELL, CELL), dtype=bool)
    for frame in frames[1:]:
        changed |= np.any(np.asarray(frame, dtype=np.int16) != base, axis=2)
    escaped = changed & ~(np.asarray(allowed) > 0)
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} pixels changed outside the flash rig")

    # Prove the entire pair + frame is byte-identical in all four phases.  The
    # flash sits behind this immutable layer and cannot alter its pixel values.
    static_alpha = np.asarray(static.getchannel("A")) > 16
    static_rgba = np.asarray(static)
    for index, frame in enumerate(frames):
        rgba = np.asarray(frame)
        # Wherever the static layer is fully opaque, its rendered pixels must
        # equal the locked static plate exactly.
        opaque = np.asarray(static.getchannel("A")) == 255
        if not np.array_equal(rgba[opaque], static_rgba[opaque]):
            raise ValueError(f"phase {index} changed opaque portrait/frame pixels")

        alpha = np.asarray(frame.getchannel("A")) > 12
        ys, xs = np.nonzero(alpha)
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        margin = min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3])
        if margin < SAFE_MARGIN:
            raise ValueError(f"phase {index} margin {margin}px below {SAFE_MARGIN}px")
        if int(np.logical_and(alpha, static_alpha).sum()) < 90_000:
            raise ValueError(f"phase {index} lost the locked portrait plate")

    changed_ratio = float(changed.sum() / max(1, static_alpha.sum()))
    if not 0.005 <= changed_ratio <= 0.14:
        raise ValueError(f"flash changed-pixel ratio {changed_ratio:.5f} outside expected range")


def assemble_shared_palette_gif(frames: list[Image.Image], output: Path) -> None:
    """Encode the standard reversible six-frame transparent GIF.

    Unlike the one-character rig helper, this encoder intentionally preserves
    the portrait frame and connected flash geometry instead of treating them as
    detached animation debris.
    """
    resized = [frame.resize((256, 256), Image.Resampling.LANCZOS) for frame in frames]
    resized = [zero_low_alpha_fringe(drop_tiny_alpha_islands(frame, minimum_area=6)) for frame in resized]
    composited: list[Image.Image] = []
    for frame in resized:
        matte = Image.new("RGBA", frame.size, SITE_MATTE + (255,))
        composited.append(Image.alpha_composite(matte, frame).convert("RGB"))

    contact = Image.new("RGB", (256 * len(composited), 256), SITE_MATTE)
    for index, frame in enumerate(composited):
        contact.paste(frame, (index * 256, 0))
    palette_reference = contact.quantize(colors=95, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
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
    static.save(frame_dir / "locked-static-portrait.png", optimize=True)
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
