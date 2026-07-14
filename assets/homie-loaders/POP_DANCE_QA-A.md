# Pop & Dance batch A — final QA

> Historical generation/structural record. The final motion-semantic authority is `POP_DANCE_QA-SEMANTIC-REBUILD-2026-07-12.md`.


**Status: PASS — 12/12 source masters and 12/12 temporary GIFs. No remaining blocker.**

## Deliverables

- Project masters: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/<slug>.png`
- Temporary GIFs: `/tmp/pop-dance-a/gifs/<slug>.gif`
- Exact accepted prompts: `/tmp/pop-dance-a-prompts.md`
- Alignment entries: `/tmp/pop-dance-a-alignment.json`
- 2x2 source contact: `/tmp/pop-dance-a/contact/final-sources.jpg`
- 128 px six-frame loop contact: `/tmp/pop-dance-a/contact/gif-strips-128.jpg`
- Individual 256 px six-frame strips: `/tmp/pop-dance-a/contact/strips/<slug>.png`
- Full authored-frame strips: `/tmp/pop-dance-a/contact/source-strips/<slug>.jpg`
- Deterministic registration log: `/tmp/pop-dance-a/processing.log`

## Checks completed

- All masters are exact `1254×1254` RGB 2x2 sheets.
- Outer edges and both centre axes are exact flat `#00ff00`.
- Every master has four byte-distinct authored cells.
- Minimum measured subject clearance is 60 px; every asset meets the requested minimum.
- One frame-zero character plate is canonicalized per asset. Action changes are localized connected patches; bounce/glide-style actions use rigid translation of that canonical plate.
- Detached chroma/keying flecks were removed deterministically; no extra limbs, cropped anatomy, phone discontinuity, or rectangular patch seams remain in the accepted loops.
- Every temporary GIF is `256×256`, six frames, transparent at all four corners, loops forever, and uses reversible sequence `0,1,2,3,2,1`.
- Every GIF duration vector is exactly `210,140,140,210,140,140` ms.
- Every GIF has four visually distinct decoded RGBA frames and is below 63 KB.
- Final source sheets were inspected at authored size; GIF strips were inspected at 256 px and on the 128 px aggregate contact.

## Per-asset result

| Slug | Source min margin | GIF bytes | Result |
|---|---:|---:|---|
| `sell-phoning-manager` | 60 px | 62,509 | PASS — user-reference rebuild |
| `back-togethering-content` | 71 px | 42,866 | PASS |
| `shake-it-offing-research` | 66 px | 44,920 | PASS |
| `twenty-two-ing-crm` | 67 px | 46,173 | PASS |
| `single-ladying-offers` | 68 px | 35,701 | PASS |
| `thrillering-marketing` | 69 px | 52,704 | PASS |
| `moonwalking-content` | 66 px | 45,564 | PASS |
| `bad-romancing-reports` | 64 px | 48,610 | PASS |
| `poker-facing-listings` | 67 px | 48,917 | PASS |
| `gangnam-styling-cma` | 62 px | 44,052 | PASS |
| `call-me-maybeing-research` | 64 px | 43,352 | PASS |
| `bye-bye-bye-ing-listings` | 71 px | 36,798 | PASS |

## Sell-phoning superseding review

The original beige-puffer, hand-only sway was rejected during direct user review. The production source now uses the supplied Hotline Bling screenshots and a saturated safety-orange oversized puffer. Its four authored silhouettes are a deep low finger-flick crouch, an open stop-palm weight shift, an opposite-side point/rear-hand sweep, and a half-rise face-level bob. Independent review of every 627px cell, the 128px source strip, and the real ABCDCB GIF found exactly two connected arms/hands and two legs, stable wardrobe/identity, no debris, and a recognizable reference action rather than a generic sway.

- Source SHA-256: `a7904b843e559e0a13d746d46b6dbfd2fbe85f91ffa879610ccc053e7b57a45d`
- GIF SHA-256: `c70112813d19ae6fe7311001bad7a62d57611cfad0d346999241688b388e8234`
- Strict evidence: `/tmp/sell-phoning-redo/strict/`
