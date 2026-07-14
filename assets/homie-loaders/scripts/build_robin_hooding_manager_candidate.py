#!/usr/bin/env python3
"""Build the candidate-only Robin-Hooding Manager loader.

One accepted full-draw archer plate supplies the immutable character and bow.
A frame-shared hue transform gives its green upper garment the requested muted
red/ochre outlaw cue without changing geometry.  The old string and arrow tip
are removed inside explicit masks; the collinear central shaft stays locked
beneath one deterministic rig whose nock travels back toward the cheek while
face, body, bow hand, crop, and scale remain fixed.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage

from repair_movie_style_canonical_six import (
    CELL,
    assemble_shared_palette_gif,
    drop_tiny_alpha_islands,
    recompose_source,
    zero_low_alpha_fringe,
)


ROOT = Path(__file__).resolve().parents[1]
SLUG = "robin-hooding-manager"
RAW = ROOT / "qa/strict-repairs/raw/robin-hooding-manager-alpha.png"
RAW_SHA256 = "a879e15c39c031afa2d6168f07f291c5b7033a8d2c7a576177c94bc4f8c584a7"
OUTPUT = ROOT / f"qa/strict-repairs/{SLUG}/candidates"
SAFE_MARGIN = 60
TARGET_HEIGHT = 497
TOP_STRING = (356, 78)
BOTTOM_STRING = (349, 350)
NOCK_Y = 194
NOCK_XS = (266, 261, 256, 251)
ARROW_LENGTH = 196


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def apply_outlaw_palette(image: Image.Image) -> tuple[Image.Image, Image.Image]:
    """Recolour only authored green upper-garment pixels to muted outlaw red."""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8)
    hsv_image = image.convert("RGB").convert("HSV")
    hsv = np.asarray(hsv_image, dtype=np.uint8).copy()
    spatial = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(spatial)
    # Hat plus upper tunic, sleeves, shoulder/cowl, and skirted hem.  Hue
    # selection below prevents skin, leather, bow, feather, and metal changes.
    draw.polygon(((210, 90), (305, 90), (315, 165), (215, 170)), fill=255)
    draw.polygon(
        ((150, 145), (435, 145), (435, 280), (365, 300), (335, 375),
         (205, 375), (180, 300), (150, 255)),
        fill=255,
    )
    spatial_array = np.asarray(spatial) > 0
    green_fabric = (
        spatial_array
        & (rgba[:, :, 3] > 12)
        & (hsv[:, :, 0] >= 40)
        & (hsv[:, :, 0] <= 80)
        & (hsv[:, :, 1] >= 28)
    )
    if int(green_fabric.sum()) < 14000:
        raise ValueError("outlaw recolour mask did not capture the upper green garment")
    original_alpha = rgba[:, :, 3].copy()
    original_value = hsv[:, :, 2].astype(np.float64)
    original_saturation = hsv[:, :, 1].astype(np.float64)
    hsv[:, :, 0][green_fabric] = 3
    hsv[:, :, 1][green_fabric] = np.clip(
        np.rint(original_saturation[green_fabric] * 1.08 + 20.0),
        90,
        175,
    ).astype(np.uint8)
    hsv[:, :, 2][green_fabric] = np.clip(
        np.rint(original_value[green_fabric] * 1.05 + 4.0),
        0,
        180,
    ).astype(np.uint8)
    recoloured_rgb = np.asarray(Image.fromarray(hsv, mode="HSV").convert("RGB"), dtype=np.uint8)
    out = rgba.copy()
    out[:, :, :3][green_fabric] = recoloured_rgb[green_fabric]
    if not np.array_equal(out[:, :, 3], original_alpha):
        raise ValueError("frame-shared recolour changed plate alpha geometry")
    mask = Image.fromarray((green_fabric * 255).astype(np.uint8), mode="L")
    return Image.fromarray(out, mode="RGBA"), mask


def build_locked_plate() -> tuple[Image.Image, Image.Image]:
    if sha256(RAW) != RAW_SHA256:
        raise ValueError(f"unexpected accepted alpha hash: {RAW}")
    image = Image.open(RAW).convert("RGBA")
    if image.size != (1254, 1254):
        raise ValueError(f"unexpected accepted plate size: {image.size}")
    bbox = image.getchannel("A").getbbox()
    if bbox != (310, 16, 1007, 1172):
        raise ValueError(f"unexpected accepted alpha bbox: {bbox}")

    x0, y0, x1, y1 = bbox
    crop = image.crop((x0 - 12, y0 - 12, x1 + 12, y1 + 12))
    width = round(crop.width * TARGET_HEIGHT / crop.height)
    fitted = crop.resize((width, TARGET_HEIGHT), Image.Resampling.LANCZOS)
    plate = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    plate.alpha_composite(fitted, ((CELL - width) // 2, (CELL - TARGET_HEIGHT) // 2))
    cleaned = zero_low_alpha_fringe(drop_tiny_alpha_islands(plate, minimum_area=18))
    return apply_outlaw_palette(cleaned)


def draw_string_erase_mask(width: int) -> Image.Image:
    """Cover only the generated string, which crosses authored foreground."""
    mask = Image.new("L", (CELL, CELL), 0)
    draw = ImageDraw.Draw(mask)
    old_nock = (251, NOCK_Y)
    # The masks track the accepted plate's thin generated prop closely.  The
    # harmonic fill below blends both sides of each stroke instead of copying
    # a single neighbouring pixel, preserving the face and tunic beneath it.
    draw.line((TOP_STRING, old_nock, BOTTOM_STRING), fill=255, width=width, joint="curve")
    return mask


def draw_background_clear_mask() -> Image.Image:
    """Cover the old tip/shaft pixels that sit wholly right of the bow hand."""
    mask = Image.new("L", (CELL, CELL), 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((437, NOCK_Y - 13, 472, NOCK_Y + 15), fill=255)
    return mask


def harmonic_inpaint(image: Image.Image, erase_mask: Image.Image) -> Image.Image:
    """Fill a narrow prop mask from all surrounding authored pixels.

    RGB is diffused in premultiplied-alpha space so transparent background
    remains transparent while face, skin, and cloth interpolate across the
    removed line without the block artifacts produced by nearest-neighbour
    filling.  Pixels outside the explicit mask remain byte-identical.
    """
    erase = np.asarray(erase_mask, dtype=np.uint8) > 12
    if not erase.any():
        raise ValueError("empty prop erase mask")
    source = np.asarray(image.convert("RGBA"), dtype=np.uint8)
    alpha = source[:, :, 3:4].astype(np.float64) / 255.0
    work = np.concatenate(
        (source[:, :, :3].astype(np.float64) / 255.0 * alpha, alpha),
        axis=2,
    )
    indices = ndimage.distance_transform_edt(
        erase,
        return_distances=False,
        return_indices=True,
    )
    yy, xx = indices
    work[erase] = work[yy[erase], xx[erase]]
    kernel = np.array(
        [[0.0, 0.25, 0.0], [0.25, 0.0, 0.25], [0.0, 0.25, 0.0]],
        dtype=np.float64,
    )
    for _ in range(96):
        for channel in range(4):
            blended = ndimage.convolve(work[:, :, channel], kernel, mode="nearest")
            work[:, :, channel][erase] = blended[erase]
    out_alpha = np.clip(work[:, :, 3:4], 0.0, 1.0)
    out_rgb = np.zeros_like(work[:, :, :3])
    np.divide(
        work[:, :, :3],
        out_alpha,
        out=out_rgb,
        where=out_alpha > 1e-6,
    )
    rebuilt = np.concatenate((out_rgb, out_alpha), axis=2)
    rebuilt = np.clip(np.rint(rebuilt * 255.0), 0, 255).astype(np.uint8)
    rebuilt[~erase] = source[~erase]
    return Image.fromarray(rebuilt, mode="RGBA")


def erase_generated_string(
    image: Image.Image,
    foreground_mask: Image.Image,
    open_space_mask: Image.Image,
) -> Image.Image:
    """Clear the string in open space and inpaint only its foreground crossings."""
    foreground_erase = np.asarray(foreground_mask, dtype=np.uint8) > 12
    open_space_erase = np.asarray(open_space_mask, dtype=np.uint8) > 12
    alpha = np.asarray(image.getchannel("A"), dtype=np.uint8) > 12
    # A bowstring has no thick interior.  Dilating the plate's >=4px-thick
    # foreground core identifies only character/bow crossings, so the long
    # stretches through open space can be made truly transparent.
    thick_core = ndimage.distance_transform_edt(alpha) >= 4.0
    supported = ndimage.binary_dilation(thick_core, iterations=5)
    foreground_crossing = foreground_erase & supported
    crossing_mask = Image.fromarray((foreground_crossing * 255).astype(np.uint8), mode="L")
    rebuilt = harmonic_inpaint(image, crossing_mask)
    array = np.asarray(rebuilt, dtype=np.uint8).copy()
    array[open_space_erase & ~supported] = 0
    return Image.fromarray(array, mode="RGBA")


def draw_arrow_string_rig(phase: int, nock_x: int) -> Image.Image:
    """Draw exactly one continuous string-and-arrow system."""
    scale = 4
    layer = Image.new("RGBA", (CELL * scale, CELL * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    nock = (nock_x * scale, NOCK_Y * scale)
    top = (TOP_STRING[0] * scale, TOP_STRING[1] * scale)
    bottom = (BOTTOM_STRING[0] * scale, BOTTOM_STRING[1] * scale)

    # One taut string, anchored to the immutable bow tips and meeting at the
    # moving nock.  The warm inner line remains visible after 128px reduction.
    draw.line((top, nock, bottom), fill=(55, 45, 37, 255), width=3 * scale, joint="curve")
    draw.line((top, nock, bottom), fill=(205, 154, 87, 255), width=1 * scale, joint="curve")

    tip_x = nock_x + ARROW_LENGTH
    shaft_start = (nock_x * scale, NOCK_Y * scale)
    shaft_end = ((tip_x - 7) * scale, NOCK_Y * scale)
    draw.line((shaft_start, shaft_end), fill=(55, 42, 33, 255), width=5 * scale)
    draw.line((shaft_start, shaft_end), fill=(139, 91, 48, 255), width=2 * scale)

    # One arrowhead and one compact pair of fletching vanes on that shaft.
    draw.polygon(
        (
            (tip_x * scale, NOCK_Y * scale),
            ((tip_x - 11) * scale, (NOCK_Y - 7) * scale),
            ((tip_x - 11) * scale, (NOCK_Y + 7) * scale),
        ),
        fill=(74, 73, 67, 255),
    )
    draw.line(
        (((tip_x - 10) * scale, (NOCK_Y - 5) * scale), (tip_x * scale, NOCK_Y * scale)),
        fill=(180, 178, 160, 255),
        width=1 * scale,
    )
    vane_x0, vane_x1 = nock_x + 5, nock_x + 18
    draw.polygon(
        (
            (vane_x0 * scale, NOCK_Y * scale),
            (vane_x1 * scale, (NOCK_Y - 6) * scale),
            (vane_x1 * scale, NOCK_Y * scale),
        ),
        fill=(151, 65, 45, 255),
    )
    draw.polygon(
        (
            (vane_x0 * scale, NOCK_Y * scale),
            (vane_x1 * scale, (NOCK_Y + 6) * scale),
            (vane_x1 * scale, NOCK_Y * scale),
        ),
        fill=(111, 49, 37, 255),
    )
    collar = 3 * scale
    draw.ellipse(
        (nock[0] - collar, nock[1] - collar, nock[0] + collar, nock[1] + collar),
        fill=(238, 203, 126, 255),
        outline=(73, 48, 31, 255),
        width=1 * scale,
    )

    if phase == 3:
        # Restrained peak glint at the fully drawn nock, attached to the rig.
        gx, gy = nock
        draw.line((gx - 6 * scale, gy, gx + 6 * scale, gy), fill=(255, 250, 220, 235), width=1 * scale)
        draw.line((gx, gy - 6 * scale, gx, gy + 6 * scale), fill=(255, 250, 220, 235), width=1 * scale)

    return zero_low_alpha_fringe(layer.resize((CELL, CELL), Image.Resampling.LANCZOS))


def build_frames() -> tuple[list[Image.Image], Image.Image, Image.Image, Image.Image, Image.Image]:
    locked, palette_mask = build_locked_plate()
    string_foreground_mask = draw_string_erase_mask(width=3)
    string_open_space_mask = draw_string_erase_mask(width=9)
    clear_mask = draw_background_clear_mask()
    base = erase_generated_string(locked, string_foreground_mask, string_open_space_mask)
    base_array = np.asarray(base, dtype=np.uint8).copy()
    base_array[np.asarray(clear_mask) > 0] = 0
    base = Image.fromarray(base_array, mode="RGBA")
    frames: list[Image.Image] = []
    allowed = ImageChops.lighter(string_open_space_mask, clear_mask)
    for phase, nock_x in enumerate(NOCK_XS):
        rig = draw_arrow_string_rig(phase, nock_x)
        frame = base.copy()
        frame.alpha_composite(rig)
        frames.append(frame)
        allowed = ImageChops.lighter(allowed, rig.getchannel("A"))

    allowed_array = ndimage.binary_dilation(np.asarray(allowed) > 0, iterations=3)
    allowed = Image.fromarray((allowed_array * 255).astype(np.uint8), mode="L")
    assert_candidate(frames, locked, allowed)
    return frames, locked, base, allowed, palette_mask


def assert_candidate(frames: list[Image.Image], locked: Image.Image, allowed: Image.Image) -> None:
    if len({hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames}) != 4:
        raise ValueError("the four authored nock-tension cells are not unique")

    arrays = [np.asarray(frame) for frame in frames]
    locked_array = np.asarray(locked)
    permitted = np.asarray(allowed) > 0
    outside = ~permitted
    for index, array in enumerate(arrays):
        mismatch = np.any(array != locked_array, axis=2) & outside
        if mismatch.any():
            raise ValueError(
                f"phase {index} violates immutable-plate contract at "
                f"{int(mismatch.sum())} pixels outside the saved prop-rig mask"
            )

    changed = np.zeros((CELL, CELL), dtype=bool)
    for array in arrays[1:]:
        changed |= np.any(array != arrays[0], axis=2)
    escaped = changed & outside
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} changed pixels escaped the nock/string/shaft mask")

    # Face, bow hand, outfit, and lower body remain byte-identical to the
    # immutable plate. These boxes avoid the explicit string/shaft path while
    # covering the face core, bow-hand/forearm above the shaft, and lower body.
    stable_regions = ((230, 125, 265, 165), (384, 150, 436, 184), (180, 355, 340, 570))
    for box in stable_regions:
        x0, y0, x1, y1 = box
        reference = locked_array[y0:y1, x0:x1]
        for index, array in enumerate(arrays):
            if not np.array_equal(reference, array[y0:y1, x0:x1]):
                raise ValueError(f"phase {index} changed locked archer region {box}")

    areas: list[int] = []
    for index, frame in enumerate(frames):
        alpha = np.asarray(frame.getchannel("A")) > 12
        ys, xs = np.nonzero(alpha)
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        margin = min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3])
        if margin < SAFE_MARGIN:
            raise ValueError(f"phase {index} margin {margin}px below {SAFE_MARGIN}px; bbox={bbox}")
        labels, _ = ndimage.label(alpha, structure=np.ones((3, 3), dtype=np.uint8))
        component_areas = np.bincount(labels.ravel())[1:]
        significant = component_areas[component_areas >= max(24, round(alpha.sum() * 0.0008))]
        if len(significant) != 1:
            raise ValueError(f"phase {index} has {len(significant)} significant components")
        areas.append(int(alpha.sum()))

    area_span = (max(areas) - min(areas)) / max(areas)
    if area_span > 0.035:
        raise ValueError(f"foreground area span {area_span:.4f} exceeds 3.5%")
    union = np.logical_or.reduce([np.asarray(frame.getchannel("A")) > 12 for frame in frames])
    motion_ratio = float(changed.sum() / max(1, union.sum()))
    if not 0.01 <= motion_ratio <= 0.20:
        raise ValueError(f"nock-tension motion ratio {motion_ratio:.5f} outside expected range")
    nock_span = max(NOCK_XS) - min(NOCK_XS)
    if nock_span < 12:
        raise ValueError(f"nock travel {nock_span}px is not materially readable")
    print(
        f"single-prop rig assertions: nock_span={nock_span}px "
        f"area_span={area_span:.5f} motion_ratio={motion_ratio:.5f}"
    )


def main() -> None:
    source_dir = OUTPUT / "sources/wildcard"
    gif_dir = OUTPUT / "gifs/wildcard"
    frame_dir = OUTPUT / "frames" / SLUG
    for directory in (source_dir, gif_dir, frame_dir):
        directory.mkdir(parents=True, exist_ok=True)

    frames, locked, base, allowed, palette_mask = build_frames()
    source = source_dir / f"{SLUG}.png"
    gif = gif_dir / f"{SLUG}.gif"
    recompose_source(frames).save(source, optimize=True)
    assemble_shared_palette_gif(frames, gif)
    for index, frame in enumerate(frames):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)
    locked.save(frame_dir / "immutable-manager-archer-plate.png", optimize=True)
    base.save(frame_dir / "locked-character-and-bow-base.png", optimize=True)
    allowed.save(frame_dir / "allowed-single-string-arrow-nock-rig-mask.png", optimize=True)
    palette_mask.save(frame_dir / "frame-shared-outlaw-recolour-mask.png", optimize=True)
    print(f"{SLUG}: source={sha256(source)} gif={sha256(gif)}")


if __name__ == "__main__":
    main()
