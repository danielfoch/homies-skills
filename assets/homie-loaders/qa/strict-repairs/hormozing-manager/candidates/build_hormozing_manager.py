#!/usr/bin/env python3
"""Build the locked-plate Hormozing Manager loader.

One accepted illustrated donor supplies every character, book, limb, wardrobe,
and facial pixel. The four authored phases differ only inside the fixed navy
book cover: deterministic `$100M` title glyphs stay locked while three value
bars stack and a tiny final contact glint appears. This makes the 128px action
read without any generated redraw, scaling, anatomy drift, or frame wiggle.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage

import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))

from repair_movie_style_canonical_six import (  # noqa: E402
    CELL,
    assemble_shared_palette_gif,
    drop_tiny_alpha_islands,
    recompose_source,
    zero_low_alpha_fringe,
)


SLUG = "hormozing-manager"
RAW_SHA256 = "a80c23284d9a2fe9147b765b6ee5be486a408a68694713c2b52a1ecd47692fd2"
RAW_ALPHA_SHA256 = "cf51ec239bff8407868cb4f735911fa75747ce77ee5e306b99ad24d4028ddb0a"
SELECTED_PANEL = 0
SHARED_SCALE = 0.82
SIDE = round(CELL * SHARED_SCALE)
OFFSET = ((CELL - SIDE) // 2, (CELL - SIDE) // 2)
SAFE_MARGIN = 60
SEQUENCE = (0, 1, 2, 3, 2, 1)
DURATIONS_MS = (210, 140, 140, 210, 140, 140)

# Source-panel book cover, mapped once through the same locked transform.
BOOK_POLYGON_RAW = ((314, 282), (452, 269), (457, 442), (314, 451))

# Variable-width 5x7 bitmap glyphs. No machine font or generated lettering is
# used, so `$100M` rebuilds byte-for-byte on every machine.
GLYPHS = {
    "$": (
        "01110",
        "11000",
        "11110",
        "00110",
        "11110",
        "00110",
        "11100",
    ),
    "1": (
        "010",
        "110",
        "010",
        "010",
        "010",
        "010",
        "111",
    ),
    "0": (
        "1111",
        "1001",
        "1001",
        "1001",
        "1001",
        "1001",
        "1111",
    ),
    "M": (
        "10001",
        "11011",
        "10101",
        "10101",
        "10001",
        "10001",
        "10001",
    ),
}


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
    plate = zero_low_alpha_fringe(drop_tiny_alpha_islands(plate, minimum_area=24))
    return plate


def polygon_mask(points: tuple[tuple[int, int], ...]) -> Image.Image:
    mask = Image.new("L", (CELL, CELL), 0)
    ImageDraw.Draw(mask).polygon(points, fill=255)
    return mask


def book_mask() -> Image.Image:
    return polygon_mask(tuple(mapped_point(point) for point in BOOK_POLYGON_RAW))


def bitmap_text_layer(book: Image.Image) -> tuple[Image.Image, Image.Image]:
    text = "$100M"
    pixel = 4
    gap = pixel
    width = sum(len(GLYPHS[char][0]) * pixel for char in text) + gap * (len(text) - 1)
    height = 7 * pixel
    origin = (322, 316)

    layer = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    glyph_mask = Image.new("L", (CELL, CELL), 0)

    def paint(target: Image.Image, dx: int, dy: int, fill: int | tuple[int, int, int, int]) -> None:
        draw = ImageDraw.Draw(target)
        cursor = origin[0] + dx
        for char in text:
            rows = GLYPHS[char]
            for row_index, row in enumerate(rows):
                for column_index, bit in enumerate(row):
                    if bit != "1":
                        continue
                    x0 = cursor + column_index * pixel
                    y0 = origin[1] + dy + row_index * pixel
                    draw.rectangle((x0, y0, x0 + pixel - 1, y0 + pixel - 1), fill=fill)
            cursor += len(rows[0]) * pixel + gap

    paint(layer, 2, 2, (46, 48, 52, 235))
    paint(layer, 0, 0, (246, 213, 142, 255))
    paint(glyph_mask, 0, 0, 255)

    clip = ImageChops.multiply(layer.getchannel("A"), book)
    layer.putalpha(clip)
    glyph_mask = ImageChops.multiply(glyph_mask, book)
    if glyph_mask.getbbox() is None:
        raise ValueError("empty `$100M` glyph mask")
    if width > 104 or height != 28:
        raise ValueError("unexpected deterministic title geometry")
    return layer, glyph_mask


def locked_titled_plate(plate: Image.Image, book: Image.Image) -> tuple[Image.Image, Image.Image]:
    title, glyph_mask = bitmap_text_layer(book)
    titled = plate.copy()
    titled.alpha_composite(title)
    titled.putalpha(plate.getchannel("A"))
    return zero_low_alpha_fringe(titled), glyph_mask


def value_layer(phase: int, book: Image.Image) -> tuple[Image.Image, Image.Image, Image.Image]:
    """Stack one deterministic value slab per phase; add a final book glint."""
    scale = 4
    layer = Image.new("RGBA", (CELL * scale, CELL * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    cards = (
        ((326, 358, 418, 371), (218, 91, 68, 255), (252, 231, 197, 255)),
        ((326, 378, 418, 391), (241, 218, 174, 255), (55, 65, 78, 255)),
        ((326, 398, 418, 411), (230, 168, 45, 255), (55, 65, 78, 255)),
    )

    def box(values: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
        return tuple(value * scale for value in values)

    active = min(phase, 3)
    for index in range(active):
        rect, fill, ink = cards[index]
        draw.rounded_rectangle(box(rect), radius=4 * scale, fill=fill, outline=(44, 48, 53, 255), width=2 * scale)
        x0, y0, x1, y1 = rect
        cx, cy = (x0 + 9) * scale, round((y0 + y1) / 2) * scale
        draw.line((cx - 4 * scale, cy, cx + 4 * scale, cy), fill=ink, width=2 * scale)
        draw.line((cx, cy - 4 * scale, cx, cy + 4 * scale), fill=ink, width=2 * scale)
        draw.line(((x0 + 20) * scale, cy, (x1 - 7) * scale, cy), fill=ink, width=2 * scale)

    glint_mask_large = Image.new("L", layer.size, 0)
    if phase == 3:
        gd = ImageDraw.Draw(glint_mask_large)
        cx, cy, radius = 317 * scale, 350 * scale, 7 * scale
        points = []
        for index in range(8):
            angle = np.deg2rad(-90 + index * 45)
            r = radius if index % 2 == 0 else radius * 0.28
            points.append((round(cx + np.cos(angle) * r), round(cy + np.sin(angle) * r)))
        gd.polygon(points, fill=255)
        glint_rgba = Image.new("RGBA", layer.size, (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glint_rgba)
        gdraw.polygon(points, fill=(255, 248, 213, 255), outline=(177, 118, 31, 255))
        gdraw.ellipse((cx - 2 * scale, cy - 2 * scale, cx + 2 * scale, cy + 2 * scale), fill=(230, 168, 45, 255))
        layer.alpha_composite(glint_rgba)

    layer = layer.resize((CELL, CELL), Image.Resampling.LANCZOS)
    glint_mask = glint_mask_large.resize((CELL, CELL), Image.Resampling.LANCZOS)
    clip = ImageChops.multiply(layer.getchannel("A"), book)
    layer.putalpha(clip)
    motion_mask = clip.point(lambda value: 255 if value > 6 else 0)
    glint_mask = ImageChops.multiply(glint_mask, book)
    return layer, motion_mask, glint_mask


def build_frames(static: Image.Image, book: Image.Image) -> tuple[list[Image.Image], Image.Image, list[int]]:
    frames: list[Image.Image] = []
    allowed = Image.new("L", static.size, 0)
    glint_counts: list[int] = []
    for phase in range(4):
        moving, motion_mask, glint_mask = value_layer(phase, book)
        frame = static.copy()
        frame.alpha_composite(moving)
        # Interior colour motion may never alter the locked silhouette.
        frame.putalpha(static.getchannel("A"))
        frames.append(zero_low_alpha_fringe(frame))
        allowed = ImageChops.lighter(allowed, motion_mask)
        glint_counts.append(int((np.asarray(glint_mask) > 12).sum()))

    allowed_array = ndimage.binary_dilation(np.asarray(allowed) > 0, iterations=4)
    return frames, Image.fromarray((allowed_array * 255).astype(np.uint8), mode="L"), glint_counts


def frame_bbox(frame: Image.Image) -> tuple[int, int, int, int]:
    bbox = frame.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("empty animation phase")
    return bbox


def assert_candidate(
    frames: list[Image.Image],
    static: Image.Image,
    allowed: Image.Image,
    glyph_mask: Image.Image,
    glint_counts: list[int],
) -> dict[str, object]:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError("four authored value-stack phases are not unique")

    arrays = [np.asarray(frame, dtype=np.uint8) for frame in frames]
    alpha_arrays = [array[:, :, 3] for array in arrays]
    if any(not np.array_equal(alpha_arrays[0], alpha) for alpha in alpha_arrays[1:]):
        raise ValueError("locked character silhouette changed between phases")

    changed = np.zeros((CELL, CELL), dtype=bool)
    for array in arrays[1:]:
        changed |= np.any(array != arrays[0], axis=2)
    allowed_array = np.asarray(allowed) > 0
    escaped = changed & ~allowed_array
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} changed pixels escaped the fixed book-effect rig")

    outside = ~allowed_array
    static_rgba = np.asarray(static)
    static_hashes = []
    title_hashes = []
    margins = []
    components = []
    areas = []
    boxes = []
    glyph = np.asarray(glyph_mask) > 0
    for index, frame in enumerate(frames):
        rgba = np.asarray(frame)
        if not np.array_equal(rgba[outside], static_rgba[outside]):
            raise ValueError(f"phase {index} changed a locked body/book pixel")
        static_hashes.append(hashlib.sha256(rgba[outside].tobytes()).hexdigest())
        title_hashes.append(hashlib.sha256(rgba[glyph].tobytes()).hexdigest())
        bbox = frame_bbox(frame)
        boxes.append(list(bbox))
        margins.append(min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3]))
        if margins[-1] < SAFE_MARGIN:
            raise ValueError(f"phase {index} margin {margins[-1]}px below {SAFE_MARGIN}px")
        visible = rgba[:, :, 3] > 12
        areas.append(int(visible.sum()))
        labels, count = ndimage.label(visible, structure=np.ones((3, 3), dtype=np.uint8))
        component_areas = np.bincount(labels.ravel())[1:] if count else np.array([])
        significant = int((component_areas >= max(32, round(visible.sum() * 0.001))).sum())
        components.append(significant)
        if significant != 1:
            raise ValueError(f"phase {index} has {significant} significant foreground components")

    if len(set(static_hashes)) != 1:
        raise ValueError("locked face/body/book registration changed")
    if len(set(title_hashes)) != 1:
        raise ValueError("`$100M` title changed between phases")
    if glint_counts[:3] != [0, 0, 0] or not 25 <= glint_counts[3] <= 500:
        raise ValueError(f"unexpected final-only glint pixel counts: {glint_counts}")

    subject_pixels = int((alpha_arrays[0] > 12).sum())
    changed_ratio = float(changed.sum() / max(1, subject_pixels))
    if not 0.002 <= changed_ratio <= 0.08:
        raise ValueError(f"book-effect changed ratio {changed_ratio:.6f} outside expected range")

    thumbnails = [frame.resize((128, 128), Image.Resampling.LANCZOS) for frame in frames]
    thumb_arrays = [np.asarray(frame, dtype=np.int16) for frame in thumbnails]
    thumbnail_deltas = []
    for left, right in zip(thumb_arrays, thumb_arrays[1:]):
        thumbnail_deltas.append(int((np.max(np.abs(left - right), axis=2) > 8).sum()))
    if min(thumbnail_deltas) < 18:
        raise ValueError(f"128px adjacent motion too small: {thumbnail_deltas}")

    return {
        "selected_panel": SELECTED_PANEL,
        "selected_panel_role": "only immutable character, wardrobe, anatomy, pointing pose, book, and crop source",
        "registration_shift_per_phase": [[0, 0]] * 4,
        "shared_scale_per_phase": [SHARED_SCALE] * 4,
        "authored_value_slabs_per_phase": [0, 1, 2, 3],
        "frame_sha256_rgba": hashes,
        "static_outside_effect_sha256_rgba": static_hashes,
        "title_glyph_sha256_rgba": title_hashes,
        "minimum_margin_px": min(margins),
        "foreground_area_span_px": max(areas) - min(areas),
        "bbox_per_phase": boxes,
        "significant_components_per_phase": components,
        "changed_pixels": int(changed.sum()),
        "changed_pixel_ratio": round(changed_ratio, 6),
        "changed_pixels_outside_allowed_mask": int(escaped.sum()),
        "thumbnail_128_adjacent_changed_pixels": thumbnail_deltas,
        "glint_pixels_per_phase": glint_counts,
        "sequence": list(SEQUENCE),
        "durations_ms": list(DURATIONS_MS),
    }


def save_alpha_sheet(frames: list[Image.Image], output: Path) -> None:
    sheet = Image.new("RGBA", (CELL * 2, CELL * 2), (0, 0, 0, 0))
    for index, frame in enumerate(frames):
        row, column = divmod(index, 2)
        sheet.alpha_composite(frame, (column * CELL, row * CELL))
    sheet.save(output, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE)
    parser.add_argument("--promote", action="store_true")
    args = parser.parse_args()

    raw = HERE / "raw-chroma.png"
    raw_alpha_path = HERE / "raw-alpha.png"
    if sha256(raw) != RAW_SHA256:
        raise ValueError("immutable raw chroma hash mismatch")
    if sha256(raw_alpha_path) != RAW_ALPHA_SHA256:
        raise ValueError("immutable chroma-removal output hash mismatch")

    raw_alpha = Image.open(raw_alpha_path).convert("RGBA")
    plate = locked_plate(raw_alpha)
    book = book_mask()
    static, glyph_mask = locked_titled_plate(plate, book)
    frames, allowed, glint_counts = build_frames(static, book)
    evidence = assert_candidate(frames, static, allowed, glyph_mask, glint_counts)

    output = args.output
    frame_dir = output / "frames" / SLUG
    source_dir = output / "sources" / "wildcard"
    gif_dir = output / "gifs" / "wildcard"
    for directory in (frame_dir, source_dir, gif_dir):
        directory.mkdir(parents=True, exist_ok=True)

    plate.save(output / "locked-plate.png", optimize=True)
    static.save(output / "locked-titled-plate.png", optimize=True)
    book.save(output / "book-mask.png", optimize=True)
    glyph_mask.save(output / "title-glyph-mask.png", optimize=True)
    allowed.save(output / "allowed-book-effect-mask.png", optimize=True)
    save_alpha_sheet(frames, output / "alpha-normalized.png")
    for index, frame in enumerate(frames):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)

    source_out = source_dir / f"{SLUG}.png"
    gif_out = gif_dir / f"{SLUG}.gif"
    direct_source = output / f"{SLUG}.png"
    direct_gif = output / f"{SLUG}.gif"
    recompose_source(frames).save(source_out, optimize=True)
    assemble_shared_palette_gif(frames, gif_out)
    shutil.copy2(source_out, direct_source)
    shutil.copy2(gif_out, direct_gif)

    evidence.update(
        {
            "raw_chroma_sha256": sha256(raw),
            "raw_alpha_sha256": sha256(raw_alpha_path),
            "locked_plate_sha256": sha256(output / "locked-plate.png"),
            "locked_titled_plate_sha256": sha256(output / "locked-titled-plate.png"),
            "title_glyph_mask_sha256": sha256(output / "title-glyph-mask.png"),
            "allowed_mask_sha256": sha256(output / "allowed-book-effect-mask.png"),
            "source_sha256": sha256(source_out),
            "gif_sha256": sha256(gif_out),
        }
    )
    (output / "build-evidence.json").write_text(
        json.dumps(evidence, indent=2) + "\n", encoding="utf-8"
    )

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
