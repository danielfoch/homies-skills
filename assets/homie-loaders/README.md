# Homies AI Loading Animations

Live gallery: https://homies-loading-gallery.vercel.app  
Google Drive package: https://drive.google.com/drive/folders/19x9h9uso4AAFRUsz_PSOzw4mufi6JfKp

This package contains small looping job animations for the nine individual
Homies, plus Manager-led Teamwork, all-purpose Wildcard, Movie Night, and Pop &
Dance collections. The library currently contains 371 GIFs: 125
individual-Homie loaders, 28 two-Homie workflows, 89 Wildcard finishing moves
and odd jobs, 94 cinematic Easter eggs, and 35 music-video, fitness, and dance-floor
loops. Every GIF has matching live loading copy in `manifest.json`.

## Runtime use

- Render GIFs at `128x128` CSS pixels on desktop and about `96x96` on mobile.
- Keep the phrase as HTML text next to the GIF; it is intentionally not baked
  into the artwork.
- GIF edges are matted for the live site canvas colour `#FBF9F6` while the canvas uses
  binary transparency.
- Respect `prefers-reduced-motion` by displaying the first frame only.

## File layout

- `gifs/<homie>/<animation>.gif`: production assets.
- `sources/<homie>/<animation>.png`: generated 2x2, 2x3, or 3x2 sprite masters.
- `manifest.json`: job descriptions, loading copy, asset paths, and alt text.
- `GENERATION_PROMPTS-*.md`: exact built-in image-generation prompt records
  for the Teamwork, Wildcard, Movie Night, and Pop & Dance additions.
- `preview.html`: local visual QA gallery.
- `scripts/assemble_sprite.py`: chroma removal, frame extraction, and GIF export.
- `scripts/alignment.json`: character-anchored per-panel registration corrections.
- `scripts/verify.py`: structural, alpha, dimension, duration, and file-size checks.
- `scripts/strict_qa.py`: full-size and 128px cell contacts, continuity metrics,
  and a mandatory recorded human visual gate.
- `scripts/verify_live.py`: deployed manifest and per-GIF byte-for-byte checks.
- `STRICT_QA_CHECKLIST.md`: the no-trash, no-crop, continuity, action-readability,
  and loop-stability release checklist.

## Animation contract

- Canvas: `256x256` GIF, intended for `128x128` display.
- Sequence: most loops play four authored poses as `1-2-3-4-3-2`; selected
  Reports actions use six authored poses directly.
- Timing: 140 ms per frame, with a slightly longer rest at the ends.
- Looping: infinite.
- Background: transparent where possible; edge matte `#FBF9F6`.
- Recommended maximum: 750 KB per GIF.
