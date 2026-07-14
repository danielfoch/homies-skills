#!/usr/bin/env python3
"""Propose whole-frame transforms by registering each sprite's head/upper torso.

This is a QA helper, not an automatic production writer. It prints alignment.json
entries for review so intentional prop/limb motion is not mistaken for camera jiggle.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage, signal

from assemble_sprite import extract_alpha, fit_frame, split_grid


def feature(image: Image.Image) -> np.ndarray:
    rgba = np.asarray(image.convert("RGBA"), dtype=np.float32)
    alpha = rgba[..., 3] / 255.0
    rgb = rgba[..., :3]
    gray = 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]
    gx = ndimage.sobel(gray, axis=1)
    gy = ndimage.sobel(gray, axis=0)
    edges = np.hypot(gx, gy)
    if edges.max() > 0:
        edges /= edges.max()
    alpha_edges = np.hypot(
        ndimage.sobel(alpha, axis=1), ndimage.sobel(alpha, axis=0)
    )
    if alpha_edges.max() > 0:
        alpha_edges /= alpha_edges.max()
    return (0.72 * edges + 0.28 * alpha_edges) * (0.35 + 0.65 * alpha)


def scale_about_center(image: Image.Image, scale: float) -> Image.Image:
    if abs(scale - 1.0) < 1e-6:
        return image
    width = max(1, round(image.width * scale))
    height = max(1, round(image.height * scale))
    layer = image.resize((width, height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", image.size, (0, 0, 0, 0))
    canvas.alpha_composite(
        layer,
        (round((image.width - width) / 2), round((image.height - height) / 2)),
    )
    return canvas


def head_roi(reference: Image.Image) -> tuple[int, int, int, int]:
    alpha = np.asarray(reference.getchannel("A"))
    ys, xs = np.nonzero(alpha > 40)
    if not len(xs):
        raise ValueError("reference frame is empty")
    x0, x1 = int(xs.min()), int(xs.max()) + 1
    y0, y1 = int(ys.min()), int(ys.max()) + 1
    height = y1 - y0
    upper_bottom = min(reference.height, y0 + round(height * 0.46))
    upper = alpha[y0:upper_bottom]
    upper_columns = np.where((upper > 40).sum(axis=0) > 2)[0]
    if len(upper_columns):
        center_x = int(np.median(upper_columns))
    else:
        center_x = (x0 + x1) // 2
    half_width = max(30, round((x1 - x0) * 0.23))
    left = max(0, center_x - half_width)
    right = min(reference.width, center_x + half_width)
    bottom = min(reference.height, y0 + max(56, round(height * 0.42)))
    return left, y0, right, bottom


def normalized_score(template: np.ndarray, patch: np.ndarray) -> float:
    a = template - template.mean()
    b = patch - patch.mean()
    denominator = float(np.linalg.norm(a) * np.linalg.norm(b))
    return float((a * b).sum() / denominator) if denominator else -1.0


def register(
    reference: Image.Image,
    candidate: Image.Image,
    scales: list[float],
    search: int,
) -> tuple[int, int, float, float]:
    ref_feature = feature(reference)
    left, top, right, bottom = head_roi(reference)
    template = ref_feature[top:bottom, left:right]
    best = (0, 0, 1.0, -1.0)
    for scale in scales:
        transformed = scale_about_center(candidate, scale)
        candidate_feature = feature(transformed)
        sx0 = max(0, left - search)
        sy0 = max(0, top - search)
        sx1 = min(candidate.width, right + search)
        sy1 = min(candidate.height, bottom + search)
        haystack = candidate_feature[sy0:sy1, sx0:sx1]
        corr = signal.fftconvolve(haystack, template[::-1, ::-1], mode="valid")
        peak_y, peak_x = np.unravel_index(np.argmax(corr), corr.shape)
        actual_left = sx0 + int(peak_x)
        actual_top = sy0 + int(peak_y)
        patch = candidate_feature[
            actual_top : actual_top + template.shape[0],
            actual_left : actual_left + template.shape[1],
        ]
        score = normalized_score(template, patch)
        dx = left - actual_left
        dy = top - actual_top
        if score > best[3]:
            best = (dx, dy, scale, score)
    return best


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("sources", nargs="+", type=Path)
    parser.add_argument("--size", type=int, default=256)
    parser.add_argument("--search", type=int, default=28)
    args = parser.parse_args()
    scales = [round(value, 3) for value in np.arange(0.94, 1.061, 0.01)]
    output: dict[str, dict] = {}
    for source in args.sources:
        sheet = extract_alpha(source)
        cells = [fit_frame(cell, args.size) for cell in split_grid(sheet)]
        frames: list[dict[str, float]] = [{}]
        diagnostics = [1.0]
        for candidate in cells[1:]:
            dx, dy, scale, score = register(cells[0], candidate, scales, args.search)
            transform: dict[str, float] = {}
            if dx:
                transform["dx"] = dx
            if dy:
                transform["dy"] = dy
            if abs(scale - 1.0) >= 0.005:
                transform["scale"] = scale
            frames.append(transform)
            diagnostics.append(round(score, 4))
        key = f"{source.parent.name}/{source.stem}"
        output[key] = {"frames": frames, "registrationScores": diagnostics}
    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
