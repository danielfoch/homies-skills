#!/usr/bin/env python3
"""Turn a chroma-key sprite master into a compact transparent looping GIF."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile
from typing import Any

from PIL import Image, ImageChops, ImageDraw


SITE_MATTE = (251, 249, 246)
DEFAULT_SEQUENCE = (0, 1, 2, 3, 2, 1)
DEFAULT_DURATIONS_MS = (210, 140, 140, 210, 140, 140)
DEFAULT_ALIGNMENT_FILE = Path(__file__).with_name("alignment.json")


def extract_alpha(source: Path, edge_contract: bool = False) -> Image.Image:
    """Apply the image-generation skill's installed chroma-key helper."""
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    helper = codex_home / "skills/.system/imagegen/scripts/remove_chroma_key.py"
    if not helper.exists():
        raise FileNotFoundError(f"missing installed chroma-key helper: {helper}")

    with tempfile.TemporaryDirectory(prefix="homie-loader-") as temp_dir:
        output = Path(temp_dir) / "sprite-alpha.png"
        command = [
            "python3",
            str(helper),
            "--input",
            str(source),
            "--out",
            str(output),
            "--auto-key",
            "border",
            "--soft-matte",
            "--transparent-threshold",
            "12",
            "--opaque-threshold",
            "220",
            "--despill",
        ]
        if edge_contract:
            command.extend(["--edge-contract", "1"])
        subprocess.run(command, check=True, capture_output=True, text=True)
        rgba = Image.open(output).convert("RGBA").copy()

    corners = (rgba.getpixel((0, 0))[3], rgba.getpixel((rgba.width - 1, 0))[3],
               rgba.getpixel((0, rgba.height - 1))[3], rgba.getpixel((rgba.width - 1, rgba.height - 1))[3])
    if max(corners) > 16:
        raise ValueError(f"chroma extraction left opaque corners: {corners}")
    if rgba.getchannel("A").getbbox() is None:
        raise ValueError("chroma extraction removed the entire sprite")
    return rgba


def split_grid(
    sheet: Image.Image,
    columns: int = 2,
    rows: int = 2,
    inset_ratio: float = 0.012,
    crop_offsets: list[dict[str, float]] | None = None,
) -> list[Image.Image]:
    """Split reading-order cells from a regular sprite-sheet grid."""
    if columns <= 0 or rows <= 0:
        raise ValueError(f"grid dimensions must be positive, got {columns}x{rows}")

    w, h = sheet.size
    x_edges = [round(index * w / columns) for index in range(columns + 1)]
    y_edges = [round(index * h / rows) for index in range(rows + 1)]
    boxes = [
        (x_edges[column], y_edges[row], x_edges[column + 1], y_edges[row + 1])
        for row in range(rows)
        for column in range(columns)
    ]
    expected_frames = columns * rows
    if crop_offsets and len(crop_offsets) != expected_frames:
        raise ValueError(
            f"expected {expected_frames} crop offsets, found {len(crop_offsets)}"
        )

    frames: list[Image.Image] = []
    for index, (left, top, right, bottom) in enumerate(boxes):
        offset = crop_offsets[index] if crop_offsets else {}
        dx = round(float(offset.get("dx", 0)))
        dy = round(float(offset.get("dy", 0)))
        left, right = left + dx, right + dx
        top, bottom = top + dy, bottom + dy
        cell_w, cell_h = right - left, bottom - top
        inset_x = round(cell_w * inset_ratio)
        inset_y = round(cell_h * inset_ratio)
        frames.append(sheet.crop((left + inset_x, top + inset_y, right - inset_x, bottom - inset_y)))
    return frames


def grid_dimensions(entry: dict[str, Any]) -> tuple[int, int]:
    """Return an alignment entry's grid dimensions, defaulting to the legacy 2x2."""
    grid = entry.get("grid", {})
    if isinstance(grid, list):
        if len(grid) != 2:
            raise ValueError(f"grid list must contain [columns, rows], found {grid}")
        columns, rows = grid
    else:
        columns = grid.get("columns", 2)
        rows = grid.get("rows", 2)
    columns, rows = int(columns), int(rows)
    if columns <= 0 or rows <= 0:
        raise ValueError(f"grid dimensions must be positive, got {columns}x{rows}")
    return columns, rows


def fit_frame(frame: Image.Image, size: int) -> Image.Image:
    """Fit a cell into a stable square without per-frame content recentering."""
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    scale = min(size / frame.width, size / frame.height)
    resized = frame.resize(
        (max(1, round(frame.width * scale)), max(1, round(frame.height * scale))),
        Image.Resampling.LANCZOS,
    )
    x = (size - resized.width) // 2
    y = (size - resized.height) // 2
    canvas.alpha_composite(resized, (x, y))
    return canvas


def load_alignment_entry(source: Path, alignment_file: Path | None) -> dict[str, Any]:
    """Load optional assembly corrections keyed by ``character/animation``."""
    path = alignment_file or DEFAULT_ALIGNMENT_FILE
    if not path.exists():
        return {}

    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    key = f"{source.parent.name}/{source.stem}"
    entry = data.get(key, {})
    columns, rows = grid_dimensions(entry)
    authored_frame_count = columns * rows
    transforms = entry.get("frames", [])
    if transforms and len(transforms) != authored_frame_count:
        raise ValueError(
            f"{key}: expected {authored_frame_count} alignment transforms, "
            f"found {len(transforms)}"
        )
    crop_offsets = entry.get("crop_offsets", [])
    if crop_offsets and len(crop_offsets) != authored_frame_count:
        raise ValueError(
            f"{key}: expected {authored_frame_count} crop offsets, "
            f"found {len(crop_offsets)}"
        )

    if authored_frame_count != 4 and "sequence" not in entry:
        raise ValueError(f"{key}: non-2x2 grids must declare an output sequence")
    sequence = tuple(int(index) for index in entry.get("sequence", DEFAULT_SEQUENCE))
    if not sequence:
        raise ValueError(f"{key}: output sequence cannot be empty")
    if min(sequence) < 0 or max(sequence) >= authored_frame_count:
        raise ValueError(
            f"{key}: sequence {sequence} references outside "
            f"{authored_frame_count} authored frames"
        )
    durations = tuple(
        int(duration) for duration in entry.get("durations_ms", DEFAULT_DURATIONS_MS)
    )
    if len(durations) != len(sequence):
        raise ValueError(
            f"{key}: found {len(durations)} durations for {len(sequence)} output frames"
        )
    return entry


def apply_frame_transform(frame: Image.Image, transform: dict[str, float]) -> Image.Image:
    """Scale around the canvas centre, then translate without trimming content."""
    dx = round(float(transform.get("dx", 0)))
    dy = round(float(transform.get("dy", 0)))
    scale = float(transform.get("scale", 1))
    scale_x = float(transform.get("scale_x", scale))
    scale_y = float(transform.get("scale_y", scale))
    if scale_x <= 0 or scale_y <= 0:
        raise ValueError(f"alignment scales must be positive, got {scale_x} x {scale_y}")

    layer = frame
    if abs(scale_x - 1) > 0.0001 or abs(scale_y - 1) > 0.0001:
        layer = frame.resize(
            (max(1, round(frame.width * scale_x)), max(1, round(frame.height * scale_y))),
            Image.Resampling.LANCZOS,
        )

    x = round((frame.width - layer.width) / 2) + dx
    y = round((frame.height - layer.height) / 2) + dy
    canvas = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    canvas.alpha_composite(layer, (x, y))
    return canvas


def apply_frame_overlays(
    frames: list[Image.Image], overlays: list[dict[str, Any]]
) -> list[Image.Image]:
    """Copy a masked prop from one corrected frame into another corrected frame."""
    corrected = [frame.copy() for frame in frames]
    donor_frames = [frame.copy() for frame in frames]
    for overlay in overlays:
        source_index = int(overlay["source"])
        target_index = int(overlay["target"])
        polygon = [tuple(point) for point in overlay["polygon"]]
        dx = round(float(overlay.get("dx", 0)))
        dy = round(float(overlay.get("dy", 0)))

        donor = donor_frames[source_index].copy()
        mask = Image.new("L", donor.size, 0)
        ImageDraw.Draw(mask).polygon(polygon, fill=255)
        donor.putalpha(ImageChops.multiply(donor.getchannel("A"), mask))
        corrected[target_index].alpha_composite(donor, (dx, dy))
    return corrected


def apply_frame_replacements(
    frames: list[Image.Image], replacements: list[dict[str, Any]]
) -> list[Image.Image]:
    """Atomically replace a prop patch, then restore target foreground details."""
    originals = [frame.copy() for frame in frames]
    corrected = [frame.copy() for frame in frames]
    for replacement in replacements:
        source_index = int(replacement["source"])
        target_index = int(replacement["target"])
        polygon = [tuple(point) for point in replacement["polygon"]]
        dx = round(float(replacement.get("dx", 0)))
        dy = round(float(replacement.get("dy", 0)))

        ImageDraw.Draw(corrected[target_index]).polygon(
            polygon,
            fill=(0, 0, 0, 0),
        )

        donor = originals[source_index].copy()
        mask = Image.new("L", donor.size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.polygon(polygon, fill=255)
        for excluded in replacement.get("exclude_polygons", []):
            mask_draw.polygon([tuple(point) for point in excluded], fill=0)
        donor.putalpha(ImageChops.multiply(donor.getchannel("A"), mask))
        corrected[target_index].alpha_composite(donor, (dx, dy))

        for restore in replacement.get("restores", []):
            restore_source = int(restore.get("source", target_index))
            restore_polygon = [tuple(point) for point in restore["polygon"]]
            restore_dx = round(float(restore.get("dx", 0)))
            restore_dy = round(float(restore.get("dy", 0)))
            foreground = originals[restore_source].copy()
            foreground_mask = Image.new("L", foreground.size, 0)
            ImageDraw.Draw(foreground_mask).polygon(restore_polygon, fill=255)
            foreground.putalpha(
                ImageChops.multiply(foreground.getchannel("A"), foreground_mask)
            )
            corrected[target_index].alpha_composite(
                foreground,
                (restore_dx, restore_dy),
            )
    return corrected


def apply_frame_clears(
    frames: list[Image.Image], clears: list[dict[str, Any]]
) -> list[Image.Image]:
    """Remove a small panel-bleed fragment after any needed donor copy."""
    corrected = [frame.copy() for frame in frames]
    for clear in clears:
        target_index = int(clear["target"])
        polygon = [tuple(point) for point in clear["polygon"]]
        ImageDraw.Draw(corrected[target_index]).polygon(
            polygon,
            fill=(0, 0, 0, 0),
        )
    return corrected


def rgba_to_gif_frame(frame: Image.Image, colors: int) -> Image.Image:
    """Quantize RGBA with an off-white edge matte and a reserved transparent index."""
    rgba = frame.convert("RGBA")
    alpha = rgba.getchannel("A")
    matte = Image.new("RGBA", rgba.size, SITE_MATTE + (255,))
    composited = Image.alpha_composite(matte, rgba).convert("RGB")
    pal = composited.quantize(colors=max(8, min(255, colors - 1)), method=Image.Quantize.MEDIANCUT)

    # Reserve index 255 for transparent pixels, leaving the visible palette intact.
    palette = pal.getpalette()[: 255 * 3]
    palette.extend([0] * (255 * 3 - len(palette)))
    palette.extend([0, 0, 0])
    pal.putpalette(palette)
    mask = alpha.point(lambda value: 255 if value < 96 else 0)
    pal.paste(255, mask=mask)
    pal.info["transparency"] = 255
    pal.info["background"] = 255
    return pal


def assemble(
    source: Path,
    output: Path,
    size: int,
    colors: int,
    edge_contract: bool,
    alignment_file: Path | None = None,
    align: bool = True,
) -> None:
    sheet = extract_alpha(source, edge_contract=edge_contract)
    alignment = load_alignment_entry(source, alignment_file) if align else {}
    columns, rows = grid_dimensions(alignment)
    inset_ratio = float(alignment.get("inset_ratio", 0.012))
    cells = [
        fit_frame(cell, size)
        for cell in split_grid(
            sheet,
            columns=columns,
            rows=rows,
            inset_ratio=inset_ratio,
            crop_offsets=alignment.get("crop_offsets"),
        )
    ]
    if align:
        transforms = alignment.get("frames", [])
        cells = [
            apply_frame_transform(cell, transforms[index]) if transforms else cell
            for index, cell in enumerate(cells)
        ]
        replacements = alignment.get("replacements", [])
        if replacements:
            cells = apply_frame_replacements(cells, replacements)
        overlays = alignment.get("overlays", [])
        if overlays:
            cells = apply_frame_overlays(cells, overlays)
        clears = alignment.get("clears", [])
        if clears:
            cells = apply_frame_clears(cells, clears)
    sequence = tuple(int(index) for index in alignment.get("sequence", DEFAULT_SEQUENCE))
    durations = tuple(
        int(duration)
        for duration in alignment.get("durations_ms", DEFAULT_DURATIONS_MS)
    )
    frames = [rgba_to_gif_frame(cells[index], colors) for index in sequence]
    output.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        output,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        disposal=2,
        transparency=255,
        optimize=True,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--size", type=int, default=256)
    parser.add_argument("--colors", type=int, default=96)
    parser.add_argument("--edge-contract", action="store_true")
    parser.add_argument("--alignment-file", type=Path)
    parser.add_argument("--no-alignment", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    assemble(
        args.source,
        args.output,
        args.size,
        args.colors,
        args.edge_contract,
        alignment_file=args.alignment_file,
        align=not args.no_alignment,
    )
