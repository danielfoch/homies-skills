#!/usr/bin/env python3
"""Rebuild four user-rejected Pop & Dance loaders from locked Homie plates.

Each asset starts from one SHA-pinned, role-canonical ink-and-watercolour plate.
The body/camera never scales or translates between cells: only explicit connected
parts (or, for the umbrella, an in-canopy glint) move.  A single union crop,
bottom anchor, GIF palette, reversible playback pattern and timing table are
shared across the four authored phases.
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
from repair_character_assignment_batch import colour_isolated_part, connected_part
from repair_movie_style_canonical_six import (
    AssetSpec,
    RAW_DIR,
    ROOT,
    assemble_shared_palette_gif,
    drop_tiny_alpha_islands,
    fit_registered_sequence,
    keep_largest_connected_subject,
    mask_layer,
    mask_union,
    moving_mask,
    recompose_source,
    remove_visible_satellite_components,
    rotate_layer,
    sha256,
    zero_low_alpha_fringe,
)


SPECS = {
    "cha-cha-sliding-marketing": AssetSpec(
        "cha-cha-sliding-marketing",
        "cha-cha-sliding-marketing-canonical-v2.png",
        "7f242ff118d985aff66108d598dc86f22e3d25a17b727114c8d857c5051cea4a",
        min_motion_ratio=0.002,
        max_motion_ratio=0.16,
    ),
    "harlem-shaking-listings": AssetSpec(
        "harlem-shaking-listings",
        "harlem-shaking-listings-canonical-v2.png",
        "0be1cc09e8f797cd2250c57201a6318dfaa7267e60b05fef65e0081d297c5af8",
        min_motion_ratio=0.015,
        max_motion_ratio=0.30,
    ),
    "umbrella-ing-manager": AssetSpec(
        "umbrella-ing-manager",
        "umbrella-ing-manager-canonical-v2.png",
        "d3b1b96dc05c723126f025f16e670e43288851f70803db08b25e192b9ce4239d",
        min_motion_ratio=0.00002,
        max_motion_ratio=0.08,
    ),
    "dougie-ing-content": AssetSpec(
        "dougie-ing-content",
        "dougie-ing-content-canonical-v3.png",
        "bdfb8b3e273fb1f27f2b91ea63b558b7423ffd6890747252270ebfe03e05d3c8",
        min_motion_ratio=0.008,
        max_motion_ratio=0.20,
    ),
}


def translate_layer(layer: Image.Image, dx: int = 0, dy: int = 0) -> Image.Image:
    moved = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    moved.alpha_composite(layer, (dx, dy))
    return moved


def build_cha_cha(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    """Keep the gold-jacket body fixed while the crossed boots execute a slide."""
    left_pivot = (504, 1082)
    left, left_erase, left_joint, left_mask = connected_part(
        plate,
        ((438, 1055), (528, 1048), (555, 1080), (561, 1157),
         (535, 1192), (469, 1184), (435, 1142)),
        left_pivot,
        21,
    )
    right_pivot = (681, 1100)
    right, right_erase, right_joint, right_mask = connected_part(
        plate,
        ((620, 1065), (710, 1062), (751, 1103), (761, 1164),
         (728, 1217), (657, 1222), (628, 1181)),
        right_pivot,
        22,
    )
    from repair_movie_style_canonical_six import nearest_inpaint

    base = nearest_inpaint(nearest_inpaint(plate, left_erase, 1), right_erase, 1)
    # A crossed-step opens, reaches and returns without moving the torso/camera.
    phases = ((-5, 4, -1.5, 1.0), (-1, 1, -0.4, 0.2),
              (7, -5, 2.0, -1.4), (2, -2, 0.7, -0.5))
    frames: list[Image.Image] = []
    allowed = [left_mask, right_mask, left_erase, right_erase]
    for left_dx, right_dx, left_angle, right_angle in phases:
        moved_left = rotate_layer(left, left_angle, left_pivot, left_dx, 0)
        moved_right = rotate_layer(right, right_angle, right_pivot, right_dx, 0)
        frame = base.copy()
        frame.alpha_composite(moved_left)
        frame.alpha_composite(moved_right)
        frame.alpha_composite(left_joint)
        frame.alpha_composite(right_joint)
        frames.append(frame)
        allowed.extend([moving_mask(moved_left), moving_mask(moved_right)])
    return frames, mask_union(allowed)


def build_harlem(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    """Counter-swing the low fists from the one iconic pink-suit plate."""
    left_pivot = (421, 337)
    left, left_erase, left_joint, left_mask = connected_part(
        plate,
        ((386, 300), (465, 319), (463, 397), (437, 482),
         (443, 555), (481, 607), (485, 651), (454, 681),
         (412, 673), (388, 629), (370, 537), (371, 441)),
        left_pivot,
        25,
    )
    right_pivot = (697, 336)
    right, right_erase, right_joint, right_mask = connected_part(
        plate,
        ((663, 302), (718, 312), (739, 388), (783, 456),
         (836, 510), (889, 528), (922, 552), (919, 584),
         (892, 607), (852, 590), (804, 552), (756, 520),
         (712, 472), (685, 400)),
        right_pivot,
        25,
    )
    from repair_movie_style_canonical_six import nearest_inpaint

    base = nearest_inpaint(nearest_inpaint(plate, left_erase, 1), right_erase, 1)
    phases = ((-7.0, 7.0), (-2.0, 2.0), (8.0, -8.0), (2.5, -2.5))
    frames: list[Image.Image] = []
    allowed = [left_mask, right_mask, left_erase, right_erase]
    for left_angle, right_angle in phases:
        moved_left = rotate_layer(left, left_angle, left_pivot)
        moved_right = rotate_layer(right, right_angle, right_pivot)
        frame = base.copy()
        frame.alpha_composite(moved_left)
        frame.alpha_composite(moved_right)
        frame.alpha_composite(left_joint)
        frame.alpha_composite(right_joint)
        frames.append(frame)
        allowed.extend([moving_mask(moved_left), moving_mask(moved_right)])
    return frames, mask_union(allowed)


def build_umbrella(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    """Animate a highlight entirely inside the held clear canopy; body stays exact."""
    canopy = Image.new("L", plate.size, 0)
    ImageDraw.Draw(canopy).polygon(
        ((345, 242), (365, 180), (430, 115), (520, 65), (670, 42),
         (820, 75), (925, 145), (978, 245), (884, 285), (465, 286)),
        fill=255,
    )
    canopy = ImageChops.multiply(canopy, plate.getchannel("A"))
    x_positions = (455, 515, 585, 525)
    frames: list[Image.Image] = []
    allowed: list[Image.Image] = [canopy]
    for x in x_positions:
        stroke = Image.new("RGBA", plate.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(stroke)
        draw.line((x, 86, x - 34, 238), fill=(255, 255, 255, 62), width=12)
        draw.line((x + 14, 91, x - 18, 233), fill=(255, 255, 255, 28), width=5)
        stroke.putalpha(ImageChops.multiply(stroke.getchannel("A"), canopy))
        frame = plate.copy()
        frame.alpha_composite(stroke)
        frames.append(frame)
        allowed.append(stroke.getchannel("A").point(lambda value: 255 if value else 0))
    return frames, mask_union(allowed)


def build_dougie(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    """Keep the chest-brush pose fixed; sweep one clean low distal forearm."""
    pivot = (704, 488)
    forearm, erase, joint, authored_mask = colour_isolated_part(
        plate,
        ((666, 451), (728, 454), (770, 500), (786, 575),
         (784, 650), (776, 713), (782, 760), (758, 806),
         (700, 810), (670, 763), (674, 694), (690, 628),
         (693, 554), (674, 512)),
        pivot,
        24,
    )
    from repair_movie_style_canonical_six import nearest_inpaint

    base = nearest_inpaint(plate, erase, 1)
    phases = (-8.0, -2.0, 8.0, 2.0)
    frames: list[Image.Image] = []
    allowed = [authored_mask, erase]
    for angle in phases:
        moved = rotate_layer(forearm, angle, pivot)
        frame = base.copy()
        frame.alpha_composite(moved)
        frame.alpha_composite(joint)
        frames.append(frame)
        allowed.append(moving_mask(moved))
    return frames, mask_union(allowed)


BUILDERS = {
    "cha-cha-sliding-marketing": build_cha_cha,
    "harlem-shaking-listings": build_harlem,
    "umbrella-ing-manager": build_umbrella,
    "dougie-ing-content": build_dougie,
}


def clean_frame(frame: Image.Image) -> Image.Image:
    frame = drop_tiny_alpha_islands(frame, minimum_area=32)
    frame = remove_visible_satellite_components(frame)
    frame = remove_visible_satellite_components(frame, visibility_threshold=64)
    frame = remove_visible_satellite_components(frame, visibility_threshold=128)
    frame = drop_tiny_alpha_islands(frame, minimum_area=32)
    frame = zero_low_alpha_fringe(frame)
    return drop_tiny_alpha_islands(frame, minimum_area=32)


def assert_locked_candidate(
    spec: AssetSpec,
    frames: list[Image.Image],
    allowed: Image.Image,
) -> dict[str, float]:
    """Prove fixed-core registration while allowing intentional wide arm gestures."""
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError(f"{spec.slug}: authored phases are not all unique")
    arrays = [np.asarray(frame, dtype=np.int16) for frame in frames]
    changed = np.zeros((frames[0].height, frames[0].width), dtype=bool)
    for candidate in arrays[1:]:
        changed |= np.any(candidate != arrays[0], axis=2)
    allowed_array = np.asarray(allowed) > 0
    escaped = changed & ~allowed_array
    if escaped.any():
        raise ValueError(f"{spec.slug}: {int(escaped.sum())} changed pixels escaped the rig")

    union = np.zeros_like(changed)
    areas: list[int] = []
    centroids: list[tuple[float, float]] = []
    for index, frame in enumerate(frames):
        alpha = np.asarray(frame.getchannel("A")) > 12
        union |= alpha
        ys, xs = np.nonzero(alpha)
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        margin = min(bbox[0], bbox[1], frame.width - bbox[2], frame.height - bbox[3])
        if margin < 60:
            raise ValueError(f"{spec.slug}: frame {index} margin {margin}px below 60px")
        labels, count = ndimage.label(alpha, structure=np.ones((3, 3), dtype=np.uint8))
        component_areas = np.bincount(labels.ravel())[1:]
        significant = component_areas[component_areas >= max(32, round(alpha.sum() * 0.001))]
        if len(significant) != 1:
            raise ValueError(f"{spec.slug}: frame {index} has {len(significant)} significant components")
        areas.append(int(alpha.sum()))
        cy, cx = ndimage.center_of_mass(alpha)
        centroids.append((float(cx), float(cy)))

    motion_ratio = float(changed.sum() / max(1, union.sum()))
    if not spec.min_motion_ratio <= motion_ratio <= spec.max_motion_ratio:
        raise ValueError(
            f"{spec.slug}: motion ratio {motion_ratio:.6f} outside "
            f"[{spec.min_motion_ratio}, {spec.max_motion_ratio}]"
        )
    area_span = (max(areas) - min(areas)) / max(areas)
    if area_span > 0.08:
        raise ValueError(f"{spec.slug}: foreground area span {area_span:.4f} exceeds 8%")
    anchor = centroids[0]
    centroid_shift = max(
        ((x - anchor[0]) ** 2 + (y - anchor[1]) ** 2) ** 0.5
        for x, y in centroids
    )
    max_shift = 3.5
    if centroid_shift > max_shift:
        raise ValueError(
            f"{spec.slug}: centroid shift {centroid_shift:.3f}px exceeds {max_shift}px"
        )
    return {
        "motion_ratio": motion_ratio,
        "area_span": area_span,
        "centroid_shift": centroid_shift,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "qa/strict-repairs/pop-dance-reference-rebuilds/candidates",
    )
    parser.add_argument("--promote", action="store_true")
    args = parser.parse_args()

    source_dir = args.output / "sources/wildcard"
    gif_dir = args.output / "gifs/wildcard"
    frame_root = args.output / "frames"
    source_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)
    frame_root.mkdir(parents=True, exist_ok=True)

    for slug, spec in SPECS.items():
        raw = RAW_DIR / spec.raw_name
        if sha256(raw) != spec.raw_sha256:
            raise ValueError(f"unexpected raw hash for {raw}")
        plate = keep_largest_connected_subject(extract_alpha(raw))
        raw_frames, allowed_raw = BUILDERS[slug](plate)
        raw_frames = [drop_tiny_alpha_islands(frame) for frame in raw_frames]
        frames, allowed = fit_registered_sequence(raw_frames, allowed_raw)
        frames = [clean_frame(frame) for frame in frames]
        metrics = assert_locked_candidate(spec, frames, allowed)

        source_out = source_dir / f"{slug}.png"
        gif_out = gif_dir / f"{slug}.gif"
        recompose_source(frames).save(source_out, optimize=True)
        assemble_shared_palette_gif(frames, gif_out)
        frame_dir = frame_root / slug
        frame_dir.mkdir(parents=True, exist_ok=True)
        for index, frame in enumerate(frames):
            frame.save(frame_dir / f"cell-{index}.png", optimize=True)
        allowed.save(frame_dir / "allowed-motion-mask.png", optimize=True)

        if args.promote:
            shutil.copy2(source_out, ROOT / f"sources/wildcard/{slug}.png")
            shutil.copy2(gif_out, ROOT / f"gifs/wildcard/{slug}.gif")
        print(
            f"{slug}: source={sha256(source_out)} gif={sha256(gif_out)} "
            f"motion={metrics['motion_ratio']:.6f} area_span={metrics['area_span']:.6f} "
            f"centroid={metrics['centroid_shift']:.3f}px"
        )


if __name__ == "__main__":
    main()
