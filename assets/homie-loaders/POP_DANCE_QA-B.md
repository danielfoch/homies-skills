# Pop & Dance B — Sprite/GIF QA

> Historical generation/structural record. The final motion-semantic authority is `POP_DANCE_QA-SEMANTIC-REBUILD-2026-07-12.md`.


Status: **PASS — 13/13 project-bound masters and 13/13 temp GIFs**

## Anti-wiggle construction

- Each accepted built-in generation was used only as an art-direction source.
- One complete full-body phase was keyed, cropped, and resized once into a canonical rigid RGBA character plate per asset.
- The exact same plate was reused in all four authored cells. Dance/float motion is deterministic whole-plate translation/rotation; no independently redrawn torso, face, hair, hands, legs, or footwear was accepted frame-to-frame.
- `material-girling-reports` and `fireworking-offers` additionally use screen-stable, fully opaque, locally drawn star/glint effects. No translucent smoke, glow, or particles were introduced.
- Output construction was re-keyed to exact RGB `#00ff00`, then the outer edges and both centre axes were explicitly reasserted after compositing.
- Playback is the reversible authored sequence `0,1,2,3,2,1` with durations `210,140,140,210,140,140 ms`.

## Master-sheet checks

All masters are exact **1254×1254 RGB**, split into four 627×627 cells, with:

- exact `#00ff00` on all four outer edges;
- exact `#00ff00` on both pixels of each centre axis;
- four distinct authored cell hashes;
- one complete character per cell;
- no text, logos, emblems, watermarks, extra people, crops, detached pieces, or duplicate limbs;
- at least 60 px of subject/effect clearance in every direction.

| Master | Minimum clearance | Visual continuity |
|---|---:|---|
| `oops-i-did-it-again-ing-offers` | 68 px | Canonical red-jumpsuit plate; compact hip/head sway |
| `hit-me-baby-one-more-timing-research` | 66 px | Canonical school-pop plate; compact hair/shoulder sway |
| `voguing-reports` | 68 px | Canonical angular-glove pose; tiny reversible groove |
| `material-girling-reports` | 68 px | Canonical pink-satin plate; localized jewelry glint |
| `fireworking-offers` | 68 px | Canonical sparkly-suit plate; localized opaque star pulses |
| `roaring-research` | 67 px | Canonical paw pose; compact rigid jungle-pop sway |
| `flowers-ing-manager` | 67 px | Canonical self-hug plate; tiny reversible head/torso sway |
| `espresso-ing-content` | 67 px | Canonical cup-at-lips plate; compact sip bob |
| `good-as-hell-ing-marketing` | 66 px | Canonical glam/wig plate; small confidence bounce |
| `levitating-cma` | 63 px | Canonical plate; rigid vertical translation only |
| `dont-start-now-ing-listings` | 67 px | Canonical disco hand pose; tiny shoulder/hand groove |
| `umbrella-ing-manager` | 67 px | Canonical handle-and-dip pose; rigid compact dip |
| `pon-de-replaying-crm` | 68 px | Canonical island-pop plate; reversible shoulder bounce |

## GIF checks

All 13 temporary GIFs pass:

- exact **256×256** canvas;
- exactly **6 output frames** and **4 unique frame hashes**;
- loop metadata `0` (infinite);
- exact durations `210,140,140,210,140,140 ms`;
- fully transparent corners;
- no crop at 128 px review size or full 256 px review size;
- no green fringe visible after chroma extraction/despill;
- no extra limbs, three-hand frames, continuity substitutions, disappearing furniture, or top/bottom wrap artefacts.

## Visual evidence and machine-readable reports

- 128 px six-frame strip: `/tmp/pop-dance-b/contact/contact-128.jpg`
- Full 256 px six-frame strips: `/tmp/pop-dance-b/contact/gif-full-batch-1.jpg` through `gif-full-batch-5.jpg`
- 256 px authored-cell strips: `/tmp/pop-dance-b/contact/source-batch-1.jpg` through `source-batch-4.jpg`
- All-source contact: `/tmp/pop-dance-b/contact/contact-source-256.jpg`
- GIF metadata report: `/tmp/pop-dance-b-gif-qa.json`
- Master structural report: `/tmp/pop-dance-b-source-qa.json`
- Deterministic construction record: `/tmp/pop-dance-b-processing.json`
- Reproducible canonicalization script: `/tmp/process_pop_dance_b.py`
