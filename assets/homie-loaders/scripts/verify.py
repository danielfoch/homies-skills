#!/usr/bin/env python3
"""Verify the production contract for every Homies loader GIF."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image


def verify_gif(path: Path, expected_size: int, max_bytes: int) -> list[str]:
    errors: list[str] = []
    try:
        image = Image.open(path)
    except Exception as exc:  # pragma: no cover - CLI diagnostic
        return [f"cannot open: {exc}"]

    if image.format != "GIF":
        errors.append(f"format is {image.format}, expected GIF")
    if image.size != (expected_size, expected_size):
        errors.append(f"size is {image.size}, expected {expected_size}x{expected_size}")
    frame_count = getattr(image, "n_frames", 1)
    if frame_count != 6:
        errors.append(f"has {frame_count} frames, expected 6")
    if image.info.get("loop") != 0:
        errors.append("not configured to loop forever")
    if "transparency" not in image.info:
        errors.append("missing GIF transparency index")
    if path.stat().st_size > max_bytes:
        errors.append(f"{path.stat().st_size} bytes exceeds {max_bytes}")

    expected_durations = (210, 140, 140, 210, 140, 140)
    unique_frames: set[str] = set()
    for index in range(frame_count):
        image.seek(index)
        duration = image.info.get("duration")
        if index < len(expected_durations) and duration != expected_durations[index]:
            errors.append(f"frame {index} duration is {duration}, expected {expected_durations[index]}")
        rgba = image.convert("RGBA")
        unique_frames.add(hashlib.sha256(rgba.tobytes()).hexdigest())
        corners = (
            rgba.getpixel((0, 0))[3],
            rgba.getpixel((rgba.width - 1, 0))[3],
            rgba.getpixel((0, rgba.height - 1))[3],
            rgba.getpixel((rgba.width - 1, rgba.height - 1))[3],
        )
        if max(corners) != 0:
            errors.append(f"frame {index} has opaque corner alpha {corners}")
        if rgba.getchannel("A").getbbox() is None:
            errors.append(f"frame {index} has no visible subject")
    if len(unique_frames) < 4:
        errors.append(f"only {len(unique_frames)} visually distinct frames, expected at least 4")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--size", type=int, default=256)
    parser.add_argument("--max-kb", type=int, default=750)
    args = parser.parse_args()

    manifest_path = args.root / "manifest.json"
    data = json.loads(manifest_path.read_text())
    failures: list[tuple[Path, list[str]]] = []
    assets: list[Path] = []
    for homie in data["homies"]:
        for animation in homie["animations"]:
            path = args.root / animation["asset"]
            assets.append(path)
            errors = verify_gif(path, args.size, args.max_kb * 1024)
            if errors:
                failures.append((path, errors))

    print(f"checked {len(assets)} GIFs")
    if failures:
        for path, errors in failures:
            print(f"FAIL {path}: {'; '.join(errors)}")
        return 1
    print("all GIFs satisfy the production contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
