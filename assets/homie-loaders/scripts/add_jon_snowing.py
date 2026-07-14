#!/usr/bin/env python3
"""Build the locked-plate Jon-Snowing Marketing loader.

One accepted Marketing Homie, cloak, hands, and sword plate is reused byte for
byte in all four authored phases.  Only deterministic snowflakes outside the
character silhouette and a blade-confined glint move, so the face, anatomy,
wardrobe, sword geometry, crop, scale, and anchor cannot redraw or wiggle.
"""

from __future__ import annotations

import argparse
import hashlib
import math
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage

from repair_movie_style_canonical_six import (
    CELL,
    DURATIONS_MS,
    SEQUENCE,
    SITE_MATTE,
    drop_tiny_alpha_islands,
    recompose_source,
    zero_low_alpha_fringe,
)


ROOT = Path(__file__).resolve().parents[1]
SLUG = "jon-snowing-marketing"
RAW = ROOT / "qa/strict-repairs/raw/jon-snowing-marketing-alpha.png"
RAW_SHA256 = "7c4011d89dd14c4f38d9149114387f6c26a1e4e472b15ac198949e3f9fd46b95"
SAFE_MARGIN = 60

SNOW_BASE = (
    (112, 150, 12),
    (493, 128, 10),
    (86, 300, 9),
    (532, 275, 13),
    (120, 460, 10),
    (505, 475, 9),
)
SNOW_OFFSETS = ((-12, -6), (-4, -2), (4, 2), (12, 6))
GLINT_Y = (330, 390, 450, 510)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_static_plate() -> Image.Image:
    if sha256(RAW) != RAW_SHA256:
        raise ValueError(f"unexpected accepted plate hash: {RAW}")
    plate = Image.open(RAW).convert("RGBA")
    if plate.size != (1254, 1254):
        raise ValueError(f"unexpected accepted plate size: {plate.size}")

    # The accepted subject gets exactly one crop, resize, and anchor shared by
    # every frame.  No per-phase fitting is permitted.
    crop = plate.crop((343, 79, 892, 1119))
    fitted = crop.resize((259, 490), Image.Resampling.LANCZOS)
    static = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    static.alpha_composite(fitted, (184, 68))
    return zero_low_alpha_fringe(drop_tiny_alpha_islands(static, minimum_area=24))


def draw_snowflake(draw: ImageDraw.ImageDraw, cx: int, cy: int, radius: int, scale: int) -> None:
    """Draw one unambiguously intentional six-arm snowflake component."""
    ink = (91, 125, 139, 245)
    ice = (239, 248, 250, 255)
    centre = (cx * scale, cy * scale)
    for angle_deg in (0, 60, 120):
        angle = math.radians(angle_deg)
        dx = math.cos(angle) * radius * scale
        dy = math.sin(angle) * radius * scale
        line = (
            round(centre[0] - dx),
            round(centre[1] - dy),
            round(centre[0] + dx),
            round(centre[1] + dy),
        )
        draw.line(line, fill=ink, width=4 * scale)
        draw.line(line, fill=ice, width=2 * scale)
    core = 3 * scale
    draw.ellipse(
        (centre[0] - core, centre[1] - core, centre[0] + core, centre[1] + core),
        fill=ice,
        outline=ink,
        width=1 * scale,
    )


def draw_snow(phase: int) -> Image.Image:
    scale = 4
    layer = Image.new("RGBA", (CELL * scale, CELL * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    dx, dy = SNOW_OFFSETS[phase]
    for x, y, radius in SNOW_BASE:
        draw_snowflake(draw, x + dx, y + dy, radius, scale)
    return layer.resize((CELL, CELL), Image.Resampling.LANCZOS)


def draw_blade_glint(phase: int, static_alpha: Image.Image) -> Image.Image:
    """Draw a small travelling glint strictly inside the central blade."""
    scale = 4
    layer = Image.new("RGBA", (CELL * scale, CELL * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    x, y = 314 * scale, GLINT_Y[phase] * scale
    draw.line(
        (x - 8 * scale, y + 8 * scale, x + 8 * scale, y - 8 * scale),
        fill=(91, 125, 139, 245),
        width=5 * scale,
    )
    draw.line(
        (x - 6 * scale, y + 6 * scale, x + 6 * scale, y - 6 * scale),
        fill=(255, 255, 252, 255),
        width=2 * scale,
    )
    glint = layer.resize((CELL, CELL), Image.Resampling.LANCZOS)

    blade_box = Image.new("L", (CELL, CELL), 0)
    ImageDraw.Draw(blade_box).rectangle((304, 282, 324, 552), fill=255)
    allowed = ImageChops.multiply(blade_box, static_alpha)
    glint.putalpha(ImageChops.multiply(glint.getchannel("A"), allowed))
    return glint


def build_frames() -> tuple[list[Image.Image], Image.Image, Image.Image]:
    static = build_static_plate()
    static_mask = np.asarray(static.getchannel("A")) > 12
    frames: list[Image.Image] = []
    allowed = Image.new("L", (CELL, CELL), 0)

    for phase in range(4):
        snow = draw_snow(phase)
        snow_mask = np.asarray(snow.getchannel("A")) > 12
        if np.logical_and(static_mask, snow_mask).any():
            raise ValueError(f"phase {phase} snow overlaps the locked character plate")

        glint = draw_blade_glint(phase, static.getchannel("A"))
        frame = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
        frame.alpha_composite(snow)
        frame.alpha_composite(static)
        frame.alpha_composite(glint)
        # The glint changes colour only.  Preserve the static silhouette byte
        # for byte anywhere occupied by the character or sword.
        alpha = ImageChops.lighter(frame.getchannel("A"), static.getchannel("A"))
        frame.putalpha(alpha)
        frame = zero_low_alpha_fringe(drop_tiny_alpha_islands(frame, minimum_area=18))
        frames.append(frame)
        allowed = ImageChops.lighter(allowed, snow.getchannel("A"))
        allowed = ImageChops.lighter(allowed, glint.getchannel("A"))

    allowed_array = ndimage.binary_dilation(np.asarray(allowed) > 0, iterations=2)
    allowed = Image.fromarray((allowed_array * 255).astype(np.uint8), mode="L")
    assert_candidate(frames, static, allowed)
    return frames, static, allowed


def assert_candidate(frames: list[Image.Image], static: Image.Image, allowed: Image.Image) -> None:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError("the four authored snow/glint phases are not unique")

    base = np.asarray(frames[0])
    changed = np.zeros((CELL, CELL), dtype=bool)
    for frame in frames[1:]:
        changed |= np.any(np.asarray(frame) != base, axis=2)
    escaped = changed & ~(np.asarray(allowed) > 0)
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} pixels changed outside snowfall/glint masks")

    static_rgba = np.asarray(static)
    static_opaque = np.asarray(static.getchannel("A")) == 255
    blade_motion = np.zeros((CELL, CELL), dtype=bool)
    blade_motion[282:553, 304:325] = True
    locked_opaque = static_opaque & ~blade_motion
    areas: list[int] = []
    component_counts: list[int] = []

    for index, frame in enumerate(frames):
        rgba = np.asarray(frame)
        if not np.array_equal(rgba[locked_opaque], static_rgba[locked_opaque]):
            raise ValueError(f"phase {index} changed locked opaque character pixels")

        alpha = np.asarray(frame.getchannel("A")) > 12
        ys, xs = np.nonzero(alpha)
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        margin = min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3])
        if margin < SAFE_MARGIN:
            raise ValueError(f"phase {index} margin {margin}px below {SAFE_MARGIN}px; bbox={bbox}")

        labels, count = ndimage.label(alpha, structure=np.ones((3, 3), dtype=np.uint8))
        component_areas = np.bincount(labels.ravel())[1:]
        tiny = component_areas[component_areas < 16]
        if len(tiny):
            raise ValueError(f"phase {index} contains {len(tiny)} tiny debris components")
        significant = component_areas[component_areas >= max(64, round(alpha.sum() * 0.002))]
        if len(significant) != 7:
            raise ValueError(
                f"phase {index} expected one locked subject plus six clear snowflakes, "
                f"got {len(significant)} significant components"
            )
        if count != 7:
            raise ValueError(f"phase {index} expected character + six snowflakes, got {count} components")
        areas.append(int(alpha.sum()))
        component_counts.append(int(count))

    area_span = (max(areas) - min(areas)) / max(areas)
    if area_span > 0.01:
        raise ValueError(f"foreground area span {area_span:.4f} exceeds 1%")
    if len(set(component_counts)) != 1:
        raise ValueError(f"foreground component count changes across phases: {component_counts}")

    motion_ratio = float(changed.sum() / max(1, np.logical_or.reduce([
        np.asarray(frame.getchannel("A")) > 12 for frame in frames
    ]).sum()))
    if not 0.008 <= motion_ratio <= 0.12:
        raise ValueError(f"snow/glint motion ratio {motion_ratio:.5f} outside expected range")
    print(
        f"locked plate assertions: area_span={area_span:.5f} "
        f"components={component_counts} motion_ratio={motion_ratio:.5f}"
    )


def assemble_shared_palette_gif(frames: list[Image.Image], output: Path) -> None:
    """Encode the standard reversible GIF while preserving intentional snow."""
    resized = [frame.resize((256, 256), Image.Resampling.LANCZOS) for frame in frames]
    resized = [zero_low_alpha_fringe(drop_tiny_alpha_islands(frame, minimum_area=4)) for frame in resized]

    composited: list[Image.Image] = []
    for frame in resized:
        matte = Image.new("RGBA", frame.size, SITE_MATTE + (255,))
        composited.append(Image.alpha_composite(matte, frame).convert("RGB"))

    contact = Image.new("RGB", (256 * len(composited), 256), SITE_MATTE)
    for index, frame in enumerate(composited):
        contact.paste(frame, (index * 256, 0))
    palette_reference = contact.quantize(
        colors=110,
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
    static.save(frame_dir / "locked-marketing-cloak-hands-and-sword.png", optimize=True)
    allowed.save(frame_dir / "allowed-snow-and-glint-mask.png", optimize=True)

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
