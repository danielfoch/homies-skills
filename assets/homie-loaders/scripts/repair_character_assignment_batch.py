#!/usr/bin/env python3
"""Deterministically rebuild the latest identity-correction loader batch.

Every loader starts from one SHA-locked canonical ink-and-watercolour plate.
Only explicit connected parts move; the character core, shared crop, anchor and
GIF palette remain identical across the loop.  This is intentionally separate
from the generic sprite assembler because independently fit frames reintroduce
the registration wiggle this batch is meant to remove.
"""

from __future__ import annotations

import argparse
import shutil
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops
from scipy import ndimage

from assemble_sprite import extract_alpha
from repair_movie_style_canonical_six import (
    AssetSpec,
    RAW_DIR,
    ROOT,
    assert_candidate,
    assemble_shared_palette_gif,
    drop_tiny_alpha_islands,
    fit_registered_sequence,
    keep_largest_connected_subject,
    mask_layer,
    mask_union,
    moving_mask,
    nearest_inpaint,
    polygon_mask,
    recompose_source,
    remove_visible_satellite_components,
    rotate_layer,
    sha256,
    zero_low_alpha_fringe,
)


SPECS = {
    "barbie-ing-listings": AssetSpec(
        "barbie-ing-listings",
        "barbie-ing-listings-female-canonical-v2.png",
        "d92ad128433f92dc39618c915f84fe124d7bfe2317b4a002eba2d811c92980e2",
        min_motion_ratio=0.015,
        max_motion_ratio=0.24,
    ),
    "pulp-fictioning-manager": AssetSpec(
        "pulp-fictioning-manager",
        "pulp-fictioning-manager-canonical-v1.png",
        "0c31fa822b4fbc02f48eed1cc93d6da94aeb7d06c4bcc89e2ac175bb788671e2",
        min_motion_ratio=0.012,
        max_motion_ratio=0.28,
    ),
    "michael-burrying-manager": AssetSpec(
        "michael-burrying-manager",
        "michael-burrying-manager-canonical-v2.png",
        "c55e7eca21c8cc53353274932aa827899739ebd3c994ce7faef60838c7be8c10",
        min_motion_ratio=0.012,
        max_motion_ratio=0.30,
    ),
    "harvey-spectering-manager": AssetSpec(
        "harvey-spectering-manager",
        "harvey-spectering-manager-canonical-v1.png",
        "8da32e0fc4997570f0ff484a860250b5710f628a1cd05c047b6365ff91063e5f",
        min_motion_ratio=0.004,
        max_motion_ratio=0.16,
    ),
}


def connected_part(
    plate: Image.Image,
    polygon: tuple[tuple[int, int], ...],
    pivot: tuple[int, int],
    joint_radius: int,
) -> tuple[Image.Image, Image.Image, Image.Image, Image.Image]:
    """Return part, erase mask, fixed joint and authored part mask."""
    shape = polygon_mask(plate.size, polygon)
    part_mask = ImageChops.multiply(shape, plate.getchannel("A"))
    part = mask_layer(plate, shape)
    yy, xx = np.indices((plate.height, plate.width))
    joint_pixels = (xx - pivot[0]) ** 2 + (yy - pivot[1]) ** 2 <= joint_radius ** 2
    erase = np.asarray(shape, dtype=np.uint8).copy()
    erase[joint_pixels] = 0
    erase_mask = ImageChops.multiply(
        Image.fromarray(erase, mode="L"), plate.getchannel("A")
    )
    joint_mask = Image.fromarray((joint_pixels * 255).astype(np.uint8), mode="L")
    joint = mask_layer(plate, joint_mask)
    return part, erase_mask, joint, part_mask


def colour_isolated_part(
    plate: Image.Image,
    polygon: tuple[tuple[int, int], ...],
    pivot: tuple[int, int],
    joint_radius: int,
) -> tuple[Image.Image, Image.Image, Image.Image, Image.Image]:
    """Select skin/wood arm-stick pixels without lifting the blue shirt below."""
    rgba = np.asarray(plate.convert("RGBA"), dtype=np.uint8)
    r, g, b, a = (rgba[:, :, index] for index in range(4))
    skin = (a > 12) & (r > 138) & (g > 78) & (b > 48) & (r > g * 1.07)
    wood = (a > 12) & (r > 118) & (g > 62) & (b < 118) & (r > g * 1.18)
    selected = skin | wood
    shape = np.asarray(polygon_mask(plate.size, polygon), dtype=np.uint8) > 0
    selected &= shape
    # Recover the authored ink contour around the selected skin and sticks.
    selected = ndimage.binary_dilation(selected, iterations=3) & shape & (a > 6)
    mask = Image.fromarray((selected * 255).astype(np.uint8), mode="L")
    part = mask_layer(plate, mask)
    yy, xx = np.indices(selected.shape)
    joint_pixels = (xx - pivot[0]) ** 2 + (yy - pivot[1]) ** 2 <= joint_radius ** 2
    erase = selected & ~joint_pixels
    erase_mask = Image.fromarray((erase * 255).astype(np.uint8), mode="L")
    joint_mask = Image.fromarray((joint_pixels * 255).astype(np.uint8), mode="L")
    joint = mask_layer(plate, joint_mask)
    return part, erase_mask, joint, mask


def build_barbie(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    arm_pivot = (704, 420)
    arm, arm_erase, arm_joint, arm_mask = connected_part(
        plate,
        ((668, 367), (738, 380), (783, 365), (862, 328), (981, 287),
         (1012, 303), (992, 333), (891, 368), (779, 444), (715, 469),
         (669, 438)),
        arm_pivot,
        20,
    )
    tail_pivot = (440, 157)
    tail, tail_erase, tail_joint, tail_mask = connected_part(
        plate,
        ((377, 112), (454, 113), (478, 153), (465, 203), (424, 250),
         (363, 296), (294, 310), (275, 281), (308, 246), (336, 190)),
        tail_pivot,
        18,
    )
    base = nearest_inpaint(nearest_inpaint(plate, arm_erase, 1), tail_erase, 1)
    phases = ((-4.5, 5.5), (-1.0, 1.5), (5.0, -5.5), (1.5, -1.5))
    frames: list[Image.Image] = []
    allowed = [arm_mask, tail_mask, arm_erase, tail_erase]
    for arm_angle, tail_angle in phases:
        moved_arm = rotate_layer(arm, arm_angle, arm_pivot)
        moved_tail = rotate_layer(tail, tail_angle, tail_pivot)
        frame = base.copy()
        frame.alpha_composite(moved_arm)
        frame.alpha_composite(moved_tail)
        frame.alpha_composite(arm_joint)
        frame.alpha_composite(tail_joint)
        frames.append(frame)
        allowed.extend([moving_mask(moved_arm), moving_mask(moved_tail)])
    return frames, mask_union(allowed)


def build_pulp(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    left_pivot = (331, 414)
    left, left_erase, left_joint, left_mask = connected_part(
        plate,
        ((277, 350), (357, 376), (367, 431), (319, 484), (254, 535),
         (190, 599), (143, 618), (132, 584), (175, 535), (232, 453)),
        left_pivot,
        21,
    )
    right_pivot = (877, 413)
    right, right_erase, right_joint, right_mask = connected_part(
        plate,
        ((830, 358), (900, 355), (933, 317), (941, 250), (951, 207),
         (986, 194), (1012, 220), (1007, 267), (975, 330), (930, 410),
         (891, 464), (844, 445)),
        right_pivot,
        21,
    )
    base = nearest_inpaint(nearest_inpaint(plate, left_erase, 1), right_erase, 1)
    phases = ((-7.5, 7.5), (-2.0, 2.0), (7.5, -7.5), (2.0, -2.0))
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


def build_michael(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    left_pivot = (359, 624)
    left, left_erase, left_joint, left_mask = colour_isolated_part(
        plate,
        ((303, 390), (483, 374), (565, 744), (592, 774), (563, 790),
         (524, 759), (438, 569), (420, 717), (359, 737), (316, 694)),
        left_pivot,
        23,
    )
    right_pivot = (1083, 635)
    right, right_erase, right_joint, right_mask = colour_isolated_part(
        plate,
        ((963, 388), (1140, 396), (1136, 694), (1089, 746), (1028, 724),
         (1004, 581), (913, 765), (883, 785), (866, 754), (956, 511)),
        right_pivot,
        23,
    )
    left_area = int((np.asarray(left_mask) > 12).sum())
    right_area = int((np.asarray(right_mask) > 12).sum())
    if not 23000 <= left_area <= 90000 or not 23000 <= right_area <= 90000:
        raise ValueError(f"Michael arm masks unexpected: {left_area}, {right_area}")
    base = nearest_inpaint(nearest_inpaint(plate, left_erase, 1), right_erase, 1)
    phases = ((-4.0, 4.0), (8.0, 1.0), (-1.0, -8.0), (6.0, -6.0))
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


def build_harvey(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    pivot = (748, 477)
    forearm, erase, joint, authored_mask = connected_part(
        plate,
        ((688, 390), (753, 407), (799, 474), (783, 532), (725, 558),
         (673, 484), (626, 407), (594, 361), (596, 303), (647, 291),
         (686, 331)),
        pivot,
        22,
    )
    base = nearest_inpaint(plate, erase, 1)
    phases = (-9.0, -2.5, 9.0, 2.5)
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
    "barbie-ing-listings": build_barbie,
    "pulp-fictioning-manager": build_pulp,
    "michael-burrying-manager": build_michael,
    "harvey-spectering-manager": build_harvey,
}


def extract_plate(raw: Path, slug: str) -> Image.Image:
    """Extract one raw plate, padding edge-touching furniture when required."""
    if slug != "michael-burrying-manager":
        return keep_largest_connected_subject(extract_alpha(raw))
    # The intentionally full-width desk touches the source's lower corners.
    # Put an exact green guard band around the immutable raw before invoking the
    # installed chroma helper; this changes neither the authored plate nor its
    # locked hash and gives border auto-keying an unambiguous sample.
    source = Image.open(raw).convert("RGB")
    border = 96
    padded = Image.new("RGB", (source.width + border * 2, source.height + border * 2), (0, 255, 0))
    padded.paste(source, (border, border))
    with tempfile.TemporaryDirectory(prefix="michael-burry-pad-") as temp_dir:
        padded_path = Path(temp_dir) / "padded.png"
        padded.save(padded_path, optimize=True)
        extracted = keep_largest_connected_subject(extract_alpha(padded_path))
        return extracted.crop((border, border, border + source.width, border + source.height))


def clean_frame(frame: Image.Image, minimum_area: int) -> Image.Image:
    frame = drop_tiny_alpha_islands(frame, minimum_area=minimum_area)
    for threshold in (48, 64, 96, 128):
        frame = remove_visible_satellite_components(
            frame, visibility_threshold=threshold, maximum_expected_area=320
        )
    frame = zero_low_alpha_fringe(frame)
    return drop_tiny_alpha_islands(frame, minimum_area=minimum_area)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("/tmp/character-assignment-batch"))
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
        actual = sha256(raw)
        if actual != spec.raw_sha256:
            raise ValueError(f"unexpected raw hash for {raw}: {actual}")
        plate = extract_plate(raw, slug)
        raw_frames, allowed_raw = BUILDERS[slug](plate)
        raw_frames = [clean_frame(frame, 16) for frame in raw_frames]
        frames, allowed = fit_registered_sequence(raw_frames, allowed_raw)
        frames = [clean_frame(frame, 32) for frame in frames]
        assert_candidate(spec, frames, allowed)

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
        print(f"{slug}: source={sha256(source_out)} gif={sha256(gif_out)}")


if __name__ == "__main__":
    main()
