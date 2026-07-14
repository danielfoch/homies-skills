#!/usr/bin/env python3
"""Strict, read-only QA for Homies chroma-key source sheets and production GIFs.

This tool intentionally does not edit source masters, GIFs, manifests, or alignment
configuration.  It generates evidence, measurable proxy flags, and a mandatory
visual-review gate.  Semantic action quality and anatomy cannot be proven from
pixels alone, so an asset cannot pass until a reviewer records full-size and
128px checks for every authored cell.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage, signal


KEY = np.array([0, 255, 0], dtype=np.uint8)
CONTENT_KEY_DISTANCE = 40.0
MATTE = (251, 249, 246, 255)
EXPECTED_DURATIONS = [210, 140, 140, 210, 140, 140]
EXPECTED_PATTERN = [0, 1, 2, 3, 2, 1]
REVIEW_CELL_FIELDS = [
    "full_size_inspected",
    "thumbnail_128_inspected",
    "crop_clear",
    "anatomy_clear",
    "prop_continuity_clear",
    "no_unintended_redraw_wiggle",
]
REVIEW_ASSET_FIELDS = [
    "signature_action_readable",
    "stationary_elements_stable",
    "loop_motion_natural",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def content_mask(rgb: np.ndarray) -> np.ndarray:
    """Foreground proxy tolerant of a bad/graded green key.

    Exact key geometry is checked separately and still fails.  A tolerant mask
    lets the report describe motion and continuity even for a malformed master
    whose nominally green background is a gradient rather than #00ff00.
    """
    distance = np.linalg.norm(rgb.astype(np.float32) - KEY.astype(np.float32), axis=2)
    return distance > CONTENT_KEY_DISTANCE


def load_json(path: Path | None) -> dict[str, Any]:
    if not path:
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def bbox_from_mask(mask: np.ndarray) -> tuple[int, int, int, int] | None:
    ys, xs = np.nonzero(mask)
    if not len(xs):
        return None
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def shift_array(array: np.ndarray, dx: int, dy: int, fill: Any) -> np.ndarray:
    """Translate without wraparound."""
    output = np.empty_like(array)
    output[...] = fill
    h, w = array.shape[:2]
    sx0, sx1 = max(0, -dx), min(w, w - dx)
    sy0, sy1 = max(0, -dy), min(h, h - dy)
    dx0, dx1 = max(0, dx), min(w, w + dx)
    dy0, dy1 = max(0, dy), min(h, h + dy)
    if sx1 > sx0 and sy1 > sy0:
        output[dy0:dy1, dx0:dx1] = array[sy0:sy1, sx0:sx1]
    return output


def best_translation(reference: np.ndarray, candidate: np.ndarray) -> tuple[int, int, float]:
    """Estimate the whole-plate translation maximizing foreground correlation."""
    ref = reference.astype(np.float32)
    cand = candidate.astype(np.float32)
    corr = signal.fftconvolve(ref, cand[::-1, ::-1], mode="same")
    peak_y, peak_x = np.unravel_index(np.argmax(corr), corr.shape)
    # This is the shift applied to candidate to align it with reference.
    dx = int(peak_x - reference.shape[1] // 2)
    dy = int(peak_y - reference.shape[0] // 2)
    shifted = shift_array(candidate, dx, dy, False)
    union = np.logical_or(reference, shifted).sum()
    iou = float(np.logical_and(reference, shifted).sum() / union) if union else 0.0
    return dx, dy, iou


def normalized_correlation(a: np.ndarray, b: np.ndarray, mask: np.ndarray) -> float | None:
    values_a = a[mask].astype(np.float32)
    values_b = b[mask].astype(np.float32)
    if values_a.size < 64:
        return None
    values_a -= values_a.mean()
    values_b -= values_b.mean()
    denominator = float(np.linalg.norm(values_a) * np.linalg.norm(values_b))
    return float((values_a * values_b).sum() / denominator) if denominator else None


def components(mask: np.ndarray) -> dict[str, Any]:
    labels, count = ndimage.label(mask, structure=np.ones((3, 3), dtype=np.uint8))
    if count == 0:
        return {
            "count": 0,
            "significant_count": 0,
            "tiny_count": 0,
            "areas": [],
            "largest_area": 0,
        }
    areas = np.bincount(labels.ravel())[1:]
    total = int(mask.sum())
    significant_floor = max(64, round(total * 0.002))
    return {
        "count": int(count),
        "significant_count": int((areas >= significant_floor).sum()),
        "tiny_count": int((areas < 16).sum()),
        "small_count": int((areas < significant_floor).sum()),
        "significant_floor": int(significant_floor),
        "areas": [int(v) for v in sorted(areas.tolist(), reverse=True)[:12]],
        "largest_area": int(areas.max()),
    }


def cell_metrics(rgb: np.ndarray, index: int) -> dict[str, Any]:
    mask = content_mask(rgb)
    bbox = bbox_from_mask(mask)
    if bbox:
        x0, y0, x1, y1 = bbox
        margins = [x0, rgb.shape[1] - x1, y0, rgb.shape[0] - y1]
        centroid_y, centroid_x = ndimage.center_of_mass(mask)
        centroid = [round(float(centroid_x), 3), round(float(centroid_y), 3)]
    else:
        margins = [0, 0, 0, 0]
        centroid = None
    return {
        "index": index,
        "sha256_rgb": sha256_bytes(rgb.tobytes()),
        "foreground_pixels": int(mask.sum()),
        "foreground_pct": round(float(mask.mean() * 100), 4),
        "bbox": list(bbox) if bbox else None,
        "margins": margins,
        "minimum_margin": int(min(margins)),
        "centroid": centroid,
        "components": components(mask),
    }


def pair_metrics(reference_rgb: np.ndarray, candidate_rgb: np.ndarray) -> dict[str, Any]:
    ref_mask = content_mask(reference_rgb)
    cand_mask = content_mask(candidate_rgb)
    union = np.logical_or(ref_mask, cand_mask)
    xor = np.logical_xor(ref_mask, cand_mask)
    union_count = int(union.sum())
    mask_xor_pct = float(xor.sum() * 100 / union_count) if union_count else 0.0

    # Silhouette displacement ignores the overlapping interior and reports a
    # robust distance for the changed contour.  Tiny <=3px bobbing stays tiny.
    distance_to_candidate = ndimage.distance_transform_edt(~cand_mask)
    distance_to_reference = ndimage.distance_transform_edt(~ref_mask)
    distances = np.concatenate(
        [
            distance_to_candidate[np.logical_and(ref_mask, ~cand_mask)],
            distance_to_reference[np.logical_and(cand_mask, ~ref_mask)],
        ]
    )
    silhouette_p95 = float(np.percentile(distances, 95)) if distances.size else 0.0
    silhouette_max = float(distances.max()) if distances.size else 0.0

    ref_centroid = ndimage.center_of_mass(ref_mask) if ref_mask.any() else (0.0, 0.0)
    cand_centroid = ndimage.center_of_mass(cand_mask) if cand_mask.any() else (0.0, 0.0)
    centroid_shift = math.hypot(
        float(cand_centroid[1] - ref_centroid[1]),
        float(cand_centroid[0] - ref_centroid[0]),
    )

    dx, dy, registration_iou = best_translation(ref_mask, cand_mask)
    aligned_rgb = shift_array(candidate_rgb, dx, dy, KEY)
    aligned_mask = content_mask(aligned_rgb)
    aligned_union = np.logical_or(ref_mask, aligned_mask)
    delta = np.max(
        np.abs(reference_rgb.astype(np.int16) - aligned_rgb.astype(np.int16)),
        axis=2,
    )
    residual = np.logical_and(delta > 12, aligned_union)
    registered_residual_pct = (
        float(residual.sum() * 100 / aligned_union.sum()) if aligned_union.any() else 0.0
    )

    ref_bbox = bbox_from_mask(ref_mask)
    if ref_bbox:
        x0, y0, x1, y1 = ref_bbox
        width, height = x1 - x0, y1 - y0
        # A conservative head/upper-centre anchor.  It is a redraw proxy, not
        # an anatomy verdict; intentional turns still require human review.
        hx0 = max(0, x0 + round(width * 0.28))
        hx1 = min(ref_mask.shape[1], x1 - round(width * 0.28))
        hy0 = y0
        hy1 = min(ref_mask.shape[0], y0 + round(height * 0.38))
        roi = np.zeros_like(ref_mask)
        roi[hy0:hy1, hx0:hx1] = True
        compare_mask = np.logical_and(roi, np.logical_or(ref_mask, aligned_mask))
        gray_ref = np.dot(reference_rgb[..., :3], [0.299, 0.587, 0.114])
        gray_aligned = np.dot(aligned_rgb[..., :3], [0.299, 0.587, 0.114])
        upper_ncc = normalized_correlation(gray_ref, gray_aligned, compare_mask)
    else:
        upper_ncc = None

    return {
        "mask_xor_pct": round(mask_xor_pct, 4),
        "silhouette_motion_p95_px": round(silhouette_p95, 3),
        "silhouette_motion_max_px": round(silhouette_max, 3),
        "centroid_shift_px": round(centroid_shift, 3),
        "registration_shift": [dx, dy],
        "registration_shift_px": round(math.hypot(dx, dy), 3),
        "registration_iou": round(registration_iou, 4),
        "registered_residual_pct": round(registered_residual_pct, 4),
        "upper_anchor_ncc": round(upper_ncc, 4) if upper_ncc is not None else None,
    }


def crop_source_cells(
    source: Path,
    columns: int,
    rows: int,
) -> tuple[Image.Image, list[Image.Image]]:
    image = Image.open(source)
    if image.width % columns or image.height % rows:
        raise ValueError(f"{source}: dimensions do not divide evenly by {columns}x{rows}")
    cw, ch = image.width // columns, image.height // rows
    cells = []
    for row in range(rows):
        for column in range(columns):
            cells.append(image.crop((column * cw, row * ch, (column + 1) * cw, (row + 1) * ch)))
    return image, cells


def save_visual_evidence(slug: str, cells: list[Image.Image], output: Path) -> dict[str, str]:
    cell_dir = output / "cells" / slug
    contact_dir = output / "contacts"
    cell_dir.mkdir(parents=True, exist_ok=True)
    contact_dir.mkdir(parents=True, exist_ok=True)
    for index, cell in enumerate(cells):
        cell.convert("RGB").save(cell_dir / f"cell-{index}-full.png")
        cell.convert("RGB").resize((128, 128), Image.Resampling.LANCZOS).save(
            cell_dir / f"cell-{index}-128.png"
        )
    full = Image.new("RGB", (cells[0].width * len(cells), cells[0].height), (0, 255, 0))
    small = Image.new("RGB", (128 * len(cells), 128), (0, 255, 0))
    for index, cell in enumerate(cells):
        full.paste(cell.convert("RGB"), (index * cells[0].width, 0))
        small.paste(
            cell.convert("RGB").resize((128, 128), Image.Resampling.LANCZOS),
            (index * 128, 0),
        )
    full_path = contact_dir / f"{slug}-source-full.png"
    small_path = contact_dir / f"{slug}-source-128.png"
    full.save(full_path)
    small.save(small_path)
    return {"source_full_contact": str(full_path), "source_128_contact": str(small_path)}


def equality_pattern(hashes: list[str]) -> list[int]:
    seen: list[str] = []
    pattern = []
    for value in hashes:
        if value not in seen:
            seen.append(value)
        pattern.append(seen.index(value))
    return pattern


def gif_metrics(path: Path, slug: str, output: Path) -> tuple[dict[str, Any], list[str]]:
    failures: list[str] = []
    if not path.exists():
        return {"path": str(path), "exists": False}, ["GIF_MISSING"]
    image = Image.open(path)
    initial_info = dict(image.info)
    frames: list[Image.Image] = []
    hashes: list[str] = []
    durations: list[int | None] = []
    corner_alphas: list[list[int]] = []
    bboxes: list[list[int] | None] = []
    for index in range(image.n_frames):
        image.seek(index)
        durations.append(image.info.get("duration"))
        frame = image.convert("RGBA")
        frames.append(frame.copy())
        hashes.append(sha256_bytes(frame.tobytes()))
        corner_alphas.append(
            [
                frame.getpixel((0, 0))[3],
                frame.getpixel((frame.width - 1, 0))[3],
                frame.getpixel((0, frame.height - 1))[3],
                frame.getpixel((frame.width - 1, frame.height - 1))[3],
            ]
        )
        alpha_bbox = frame.getchannel("A").getbbox()
        bboxes.append(list(alpha_bbox) if alpha_bbox else None)
    pattern = equality_pattern(hashes)
    if image.size != (256, 256):
        failures.append("GIF_SIZE")
    if image.n_frames != 6:
        failures.append("GIF_FRAME_COUNT")
    if len(set(hashes)) != 4:
        failures.append("GIF_UNIQUE_PHASES")
    if pattern != EXPECTED_PATTERN:
        failures.append("GIF_NOT_EXACTLY_REVERSIBLE")
    if durations != EXPECTED_DURATIONS:
        failures.append("GIF_TIMING")
    if initial_info.get("loop") != 0:
        failures.append("GIF_LOOP")
    if "transparency" not in initial_info:
        failures.append("GIF_TRANSPARENCY")
    if any(max(corners) != 0 for corners in corner_alphas):
        failures.append("GIF_OPAQUE_CORNERS")
    if any(bbox is None for bbox in bboxes):
        failures.append("GIF_EMPTY_FRAME")

    contact_path = output / "contacts" / f"{slug}-gif-128.png"
    contact_path.parent.mkdir(parents=True, exist_ok=True)
    contact = Image.new("RGBA", (128 * len(frames), 128), MATTE)
    for index, frame in enumerate(frames):
        resized = frame.resize((128, 128), Image.Resampling.LANCZOS)
        panel = Image.new("RGBA", (128, 128), MATTE)
        panel.alpha_composite(resized)
        contact.alpha_composite(panel, (128 * index, 0))
    contact.convert("RGB").save(contact_path)

    return {
        "path": str(path),
        "exists": True,
        "sha256": sha256_bytes(path.read_bytes()),
        "bytes": path.stat().st_size,
        "size": list(image.size),
        "frame_count": image.n_frames,
        "unique_phases": len(set(hashes)),
        "equality_pattern": pattern,
        "durations_ms": durations,
        "loop": initial_info.get("loop"),
        "has_transparency": "transparency" in initial_info,
        "corner_alphas": corner_alphas,
        "alpha_bboxes": bboxes,
        "loop_closure_exact": len(hashes) == 6 and hashes[5] == hashes[1] and hashes[4] == hashes[2],
        "contact": str(contact_path),
    }, failures


def axis_key_failures(rgb: np.ndarray, columns: int, rows: int) -> dict[str, int]:
    h, w = rgb.shape[:2]
    outer = np.concatenate(
        [rgb[0], rgb[-1], rgb[:, 0], rgb[:, -1]],
        axis=0,
    )
    gutter_pixels = []
    for column in range(1, columns):
        edge = round(column * w / columns)
        gutter_pixels.extend([rgb[:, edge - 1], rgb[:, edge]])
    for row in range(1, rows):
        edge = round(row * h / rows)
        gutter_pixels.extend([rgb[edge - 1], rgb[edge]])
    gutter = np.concatenate(gutter_pixels, axis=0) if gutter_pixels else np.empty((0, 3), dtype=np.uint8)
    return {
        "outer_edge_non_key_pixels": int(np.any(outer != KEY, axis=1).sum()),
        "gutter_axis_non_key_pixels": int(np.any(gutter != KEY, axis=1).sum()),
    }


def stationary_region_metrics(
    rgbs: list[np.ndarray],
    regions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    if not regions:
        return []
    h, w = rgbs[0].shape[:2]
    output = []
    for region in regions:
        box = region["box"]
        if all(isinstance(value, (float, int)) and 0 <= float(value) <= 1 for value in box):
            x0, y0, x1, y1 = [round(float(value) * dim) for value, dim in zip(box, [w, h, w, h])]
        else:
            x0, y0, x1, y1 = [round(float(value)) for value in box]
        ref = rgbs[0][y0:y1, x0:x1]
        changes = []
        for candidate in rgbs[1:]:
            patch = candidate[y0:y1, x0:x1]
            delta = np.max(np.abs(ref.astype(np.int16) - patch.astype(np.int16)), axis=2)
            changes.append(round(float((delta > 12).mean() * 100), 4))
        output.append(
            {
                "name": region.get("name", "stationary-region"),
                "box_pixels": [x0, y0, x1, y1],
                "change_pct_vs_cell0": changes,
                "max_change_pct": max(changes, default=0.0),
                "max_allowed_change_pct": float(region.get("max_change_pct", 1.0)),
            }
        )
    return output


def review_template(slugs: list[str], cell_count: int, policies: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for slug in slugs:
        result[slug] = {
            "cells": [
                {field: False for field in REVIEW_CELL_FIELDS}
                for _ in range(cell_count)
            ],
            "signature_action_readable": False,
            "stationary_elements_stable": False,
            "loop_motion_natural": False,
            "action_expectation": policies.get(slug, {}).get("action_expectation", ""),
            "notes": "",
        }
    return result


def check_manual_review(
    slug: str,
    review: dict[str, Any] | None,
    cell_count: int,
    signature_action: bool,
) -> tuple[dict[str, Any], list[str]]:
    failures: list[str] = []
    if not review or slug not in review:
        return {"complete": False}, ["VISUAL_REVIEW_REQUIRED"]
    item = review[slug]
    cells = item.get("cells", [])
    if len(cells) != cell_count:
        failures.append("VISUAL_REVIEW_CELL_COUNT")
    for index in range(min(len(cells), cell_count)):
        for field in REVIEW_CELL_FIELDS:
            if cells[index].get(field) is not True:
                failures.append(f"VISUAL_CELL_{index}_{field.upper()}")
    if signature_action and item.get("signature_action_readable") is not True:
        failures.append("SIGNATURE_ACTION_NOT_READABLE")
    if item.get("stationary_elements_stable") is not True:
        failures.append("VISUAL_STATIONARY_DRIFT_OR_UNREVIEWED")
    if item.get("loop_motion_natural") is not True:
        failures.append("VISUAL_LOOP_NOT_NATURAL")
    return {
        "complete": not failures,
        "signature_action_readable": item.get("signature_action_readable"),
        "stationary_elements_stable": item.get("stationary_elements_stable"),
        "loop_motion_natural": item.get("loop_motion_natural"),
        "notes": item.get("notes", ""),
    }, failures


def analyze_asset(
    source: Path,
    output: Path,
    policy: dict[str, Any],
    review: dict[str, Any] | None,
    gif_root: Path,
    columns: int,
    rows: int,
) -> dict[str, Any]:
    slug = source.stem
    failures: list[str] = []
    warnings: list[str] = []
    image, cells = crop_source_cells(source, columns, rows)
    rgb_sheet = np.asarray(image.convert("RGB"), dtype=np.uint8)
    rgbs = [np.asarray(cell.convert("RGB"), dtype=np.uint8) for cell in cells]
    evidence = save_visual_evidence(slug, cells, output)
    axes = axis_key_failures(rgb_sheet, columns, rows)
    if image.size != (1254, 1254):
        failures.append("SOURCE_SIZE")
    if image.mode != "RGB":
        failures.append("SOURCE_MODE")
    if axes["outer_edge_non_key_pixels"]:
        failures.append("SOURCE_OUTER_EDGE_KEY")
    if axes["gutter_axis_non_key_pixels"]:
        failures.append("SOURCE_GUTTER_KEY")

    cells_report = [cell_metrics(rgb, index) for index, rgb in enumerate(rgbs)]
    minimum_margin = int(policy.get("min_margin_px", 60))
    max_tiny = int(policy.get("max_tiny_components", 12))
    max_significant = int(policy.get("max_significant_components_per_cell", 10))
    for item in cells_report:
        cell_flags = []
        if item["foreground_pixels"] == 0:
            cell_flags.append("EMPTY_FOREGROUND")
        if item["minimum_margin"] < minimum_margin:
            cell_flags.append(f"MARGIN_BELOW_{minimum_margin}px")
        if item["components"]["tiny_count"] > max_tiny:
            cell_flags.append("MANY_TINY_COMPONENTS")
        if item["components"]["significant_count"] > max_significant:
            cell_flags.append("FOREGROUND_FRAGMENTATION")
        item["artifact_flags"] = cell_flags
    if any(item["foreground_pixels"] == 0 for item in cells_report):
        failures.append("SOURCE_EMPTY_CELL")
    if any(item["minimum_margin"] < minimum_margin for item in cells_report):
        failures.append("SOURCE_CROP_OR_MARGIN")
    if len({item["sha256_rgb"] for item in cells_report}) != len(cells_report):
        failures.append("SOURCE_DUPLICATE_CELLS")
    for item in cells_report:
        if item["components"]["tiny_count"] > max_tiny:
            warnings.append(f"CELL_{item['index']}_MANY_TINY_COMPONENTS")
        if item["components"]["significant_count"] > max_significant:
            warnings.append(f"CELL_{item['index']}_FOREGROUND_FRAGMENTATION")

    pairs = [pair_metrics(rgbs[index - 1], rgbs[index]) for index in range(1, len(rgbs))]
    max_silhouette = max((item["silhouette_motion_p95_px"] for item in pairs), default=0.0)
    max_xor = max((item["mask_xor_pct"] for item in pairs), default=0.0)
    max_centroid = max((item["centroid_shift_px"] for item in pairs), default=0.0)
    max_registration_shift = max((item["registration_shift_px"] for item in pairs), default=0.0)
    max_registered_residual = max((item["registered_residual_pct"] for item in pairs), default=0.0)
    upper_scores = [item["upper_anchor_ncc"] for item in pairs if item["upper_anchor_ncc"] is not None]
    min_upper_ncc = min(upper_scores, default=None)

    foreground_areas = [item["foreground_pixels"] for item in cells_report]
    median_area = float(np.median(foreground_areas)) or 1.0
    area_span_pct = float((max(foreground_areas) - min(foreground_areas)) * 100 / median_area)
    bbox_widths = [item["bbox"][2] - item["bbox"][0] for item in cells_report if item["bbox"]]
    bbox_heights = [item["bbox"][3] - item["bbox"][1] for item in cells_report if item["bbox"]]
    width_span_pct = (
        float((max(bbox_widths) - min(bbox_widths)) * 100 / np.median(bbox_widths))
        if bbox_widths else 0.0
    )
    height_span_pct = (
        float((max(bbox_heights) - min(bbox_heights)) * 100 / np.median(bbox_heights))
        if bbox_heights else 0.0
    )
    significant_counts = [item["components"]["significant_count"] for item in cells_report]
    significant_component_span = max(significant_counts) - min(significant_counts)

    signature = bool(policy.get("signature_action", False))
    min_silhouette = float(policy.get("min_silhouette_motion_px", 3.01))
    if signature and max_silhouette < min_silhouette:
        failures.append("SIGNATURE_ACTION_TOO_SMALL_OR_GENERIC")
    if signature and max_xor < float(policy.get("min_mask_xor_pct", 0.75)):
        failures.append("SIGNATURE_ACTION_MASK_CHANGE_TOO_SMALL")
    if not policy.get("allow_global_motion", True) and max_registration_shift > float(
        policy.get("max_global_drift_px", 3.0)
    ):
        failures.append("GLOBAL_SUBJECT_OR_CAMERA_DRIFT")
    if policy.get("fixed_character_plate", False):
        if max_registered_residual > float(policy.get("max_registered_residual_pct", 18.0)):
            failures.append("FIXED_PLATE_REDRAW_RESIDUAL")
        if min_upper_ncc is not None and min_upper_ncc < float(policy.get("min_upper_anchor_ncc", 0.88)):
            failures.append("UPPER_BODY_IDENTITY_DRIFT")
    if area_span_pct > float(policy.get("max_foreground_area_span_pct", 18.0)):
        warnings.append("FOREGROUND_AREA_JUMP")
    if max(width_span_pct, height_span_pct) > float(policy.get("max_bbox_span_pct", 15.0)):
        warnings.append("BBOX_SCALE_OR_PROP_JUMP")
    if significant_component_span > int(policy.get("max_significant_component_span", 2)):
        warnings.append("SIGNIFICANT_COMPONENT_COUNT_JUMP")

    stationary = stationary_region_metrics(rgbs, policy.get("stationary_regions", []))
    for item in stationary:
        if item["max_change_pct"] > item["max_allowed_change_pct"]:
            failures.append(f"STATIONARY_REGION_DRIFT:{item['name']}")
    if not stationary:
        warnings.append("STATIONARY_REGIONS_NOT_ANNOTATED")

    gif_path = gif_root / source.parent.name / f"{slug}.gif"
    gif_report, gif_failures = gif_metrics(gif_path, slug, output)
    failures.extend(gif_failures)

    manual_report, manual_failures = check_manual_review(
        slug,
        review,
        len(cells),
        signature,
    )
    failures.extend(manual_failures)

    # Deduplicate without losing deterministic order.
    failures = list(dict.fromkeys(failures))
    warnings = list(dict.fromkeys(warnings))
    return {
        "slug": slug,
        "concept": policy.get("concept", ""),
        "action_expectation": policy.get("action_expectation", ""),
        "source": str(source),
        "source_sha256": sha256_bytes(source.read_bytes()),
        "source_size": list(image.size),
        "source_mode": image.mode,
        "grid": [columns, rows],
        "key_geometry": axes,
        "cells": cells_report,
        "pair_metrics": pairs,
        "aggregate": {
            "max_silhouette_motion_p95_px": round(max_silhouette, 3),
            "max_mask_xor_pct": round(max_xor, 4),
            "max_centroid_shift_px": round(max_centroid, 3),
            "max_registration_shift_px": round(max_registration_shift, 3),
            "max_registered_residual_pct": round(max_registered_residual, 4),
            "minimum_upper_anchor_ncc": min_upper_ncc,
            "foreground_area_span_pct": round(area_span_pct, 4),
            "bbox_width_span_pct": round(width_span_pct, 4),
            "bbox_height_span_pct": round(height_span_pct, 4),
            "significant_component_count_span": significant_component_span,
        },
        "stationary_regions": stationary,
        "gif": gif_report,
        "visual_evidence": evidence,
        "manual_review": manual_report,
        "failures": failures,
        "warnings": warnings,
        "passed": not failures,
    }


def markdown_report(results: list[dict[str, Any]]) -> str:
    lines = [
        "# Homies strict QA report",
        "",
        "> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.",
        "",
        "| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for item in results:
        minimum_margin = min(cell["minimum_margin"] for cell in item["cells"])
        aggregate = item["aggregate"]
        lines.append(
            f"| `{item['slug']}` | {'PASS' if item['passed'] else 'FAIL'} | {minimum_margin}px | "
            f"{aggregate['max_silhouette_motion_p95_px']}px | {aggregate['max_mask_xor_pct']}% | "
            f"{aggregate['max_registered_residual_pct']}% | "
            f"{'recorded: pass' if item['manual_review'].get('complete') else ('recorded: fail' if item['manual_review'].get('notes') else 'pending')} |"
        )
    for item in results:
        lines.extend(
            [
                "",
                f"## {item['slug']} — {'PASS' if item['passed'] else 'FAIL'}",
                "",
                f"Concept: {item['concept'] or '(not supplied)'}",
                "",
                f"Required action: {item['action_expectation'] or '(not supplied)'}",
                "",
                f"Full-size contact: `{item['visual_evidence']['source_full_contact']}`",
                "",
                f"128px contact: `{item['visual_evidence']['source_128_contact']}`",
                "",
                f"GIF contact: `{item['gif'].get('contact', '(missing)')}`",
                "",
                "Failures: " + (", ".join(f"`{value}`" for value in item["failures"]) or "none"),
                "",
                "Warnings: " + (", ".join(f"`{value}`" for value in item["warnings"]) or "none"),
                "",
                "Manual notes: " + (item["manual_review"].get("notes") or "(none)"),
                "",
                "| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |",
                "|---:|---:|---:|---:|---|",
            ]
        )
        for cell in item["cells"]:
            component = cell["components"]
            flags = ", ".join(cell.get("artifact_flags", [])) or "none"
            lines.append(
                f"| {cell['index']} | {cell['minimum_margin']}px | {cell['foreground_pixels']}px | "
                f"{component['count']} ({component['significant_count']}/{component['tiny_count']}) | {flags} |"
            )
        lines.extend(
            [
                "",
                "| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |",
                "|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for transition, pair in enumerate(item["pair_metrics"], start=1):
            lines.append(
                f"| {transition - 1}→{transition} | {pair['mask_xor_pct']}% | "
                f"{pair['silhouette_motion_p95_px']}px | {pair['centroid_shift_px']}px | "
                f"{pair['registration_shift_px']}px | {pair['registered_residual_pct']}% | "
                f"{pair['upper_anchor_ncc']} |"
            )
        if item["stationary_regions"]:
            lines.extend(
                [
                    "",
                    "| Stationary region | Max change | Allowed |",
                    "|---|---:|---:|",
                ]
            )
            for region in item["stationary_regions"]:
                lines.append(
                    f"| {region['name']} | {region['max_change_pct']}% | {region['max_allowed_change_pct']}% |"
                )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("sources", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--gif-root", type=Path, required=True)
    parser.add_argument("--policy", type=Path)
    parser.add_argument("--review", type=Path)
    parser.add_argument("--alignment", type=Path)
    parser.add_argument("--columns", type=int, default=2)
    parser.add_argument("--rows", type=int, default=2)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    policies = load_json(args.policy)
    review = load_json(args.review) if args.review else None
    alignment = load_json(args.alignment)

    results = []
    for source in args.sources:
        key = f"{source.parent.name}/{source.stem}"
        entry = alignment.get(key, {})
        grid = entry.get("grid", {})
        if isinstance(grid, list) and len(grid) == 2:
            columns, rows = int(grid[0]), int(grid[1])
        else:
            columns = int(grid.get("columns", args.columns)) if isinstance(grid, dict) else args.columns
            rows = int(grid.get("rows", args.rows)) if isinstance(grid, dict) else args.rows
        results.append(
            analyze_asset(
                source,
                args.output,
                policies.get(source.stem, {}),
                review,
                args.gif_root,
                columns,
                rows,
            )
        )

    template = review_template([source.stem for source in args.sources], args.columns * args.rows, policies)
    (args.output / "visual-review-template.json").write_text(
        json.dumps(template, indent=2) + "\n", encoding="utf-8"
    )
    (args.output / "strict-qa.json").write_text(
        json.dumps({"results": results}, indent=2) + "\n", encoding="utf-8"
    )
    (args.output / "strict-qa.md").write_text(markdown_report(results), encoding="utf-8")
    passed = sum(item["passed"] for item in results)
    print(f"strict QA: {passed}/{len(results)} passed")
    print(args.output / "strict-qa.md")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

