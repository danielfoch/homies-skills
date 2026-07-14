# Pop & Dance C — Independent QA

> Historical generation/structural record. The final motion-semantic authority is `POP_DANCE_QA-SEMANTIC-REBUILD-2026-07-12.md`.


Status: **PASS — 10/10 masters, 10/10 independently assembled GIFs**

Audit mode: read-only. I did not modify any Pop & Dance C source, project alignment, manifest, documentation, deployment file, or Drive asset.

## Structural master-sheet audit

Every source passed the complete master contract:

- exact 1254×1254 RGB;
- exact flat `#00ff00` on all four outside edges;
- exact flat `#00ff00` across both pixels of the horizontal and vertical centre axes;
- four distinct authored-cell byte hashes;
- one complete full-body Homie per 627×627 cell;
- at least 60 px clearance on every side;
- no crop, extra person, duplicate limb, detached hand, disappearing clothing, or wraparound artefact.

| Source | Minimum cell clearance | Result |
|---|---:|---|
| `macarena-ing-manager` | 77 px | PASS |
| `ymca-ing-cma` | 77 px | PASS |
| `cupid-shuffling-crm` | 77 px | PASS |
| `cha-cha-sliding-marketing` | 77 px | PASS |
| `dougie-ing-content` | 77 px | PASS |
| `rickrolling-manager` | 77 px | PASS |
| `harlem-shaking-listings` | 75 px | PASS |
| `wednesday-ing-offers` | 77 px | PASS |
| `napoleon-dynamiting-content` | 77 px | PASS |
| `disco-inferno-ing-reports` | 77 px | PASS |

Machine-readable structural results: `/tmp/pop-dance-c-independent-source-qa.json`

## Full-size authored-frame inspection

I inspected all 40 authored cells at 256 px (the production GIF canvas size) and again at 128 px.

- `macarena-ing-manager`: torso/head/legs stay registered; hand positions progress deliberately; no hand duplication or sleeve substitution.
- `ymca-ing-cma`: arms form a deliberate reversible letter-like progression; face, jacket, trousers, and foot baseline remain continuous.
- `cupid-shuffling-crm`: one canonical outfit/pose with small side-step motion; no anatomy or costume change.
- `cha-cha-sliding-marketing`: compact rigid slide with stable head/beard/jacket/feet; no global redraw shimmer.
- `dougie-ing-content`: compact shoulder-brush groove; hand remains connected, and face/hoodie/trousers/feet stay continuous.
- `rickrolling-manager`: chest-hand to pointing gesture and small foot step read intentionally; trench, stripes, face, and anatomy stay continuous; no extra fingers/hands.
- `harlem-shaking-listings`: subtle whole-body wobble is deliberate; party hat/glasses/outfit remain present and uncropped in every phase.
- `wednesday-ing-offers`: stiff alternating hand shapes are an intentional dance-pose change; body, braids, dress, legs, and baseline remain stable with no extra arms.
- `napoleon-dynamiting-content`: tiny awkward side-step/hand groove stays registered; glasses, hair, outfit, boots, and limb count are continuous.
- `disco-inferno-ing-reports`: pointing arm moves through a clear arc while the other arm, face, suit, legs, and baseline stay stable.

No global model-redraw wiggle, unintended prop switching, head/foot crop, or continuity blocker was found.

Authored-frame evidence:

- Full 256 px contacts: `/tmp/pop-dance-c-independent/contact/authored-full-1.jpg` through `authored-full-4.jpg`
- 128 px contact: `/tmp/pop-dance-c-independent/contact/authored-128.jpg`

## Independent GIF assembly and contract

I independently assembled all ten sources with `scripts/assemble_sprite.py` using `/tmp/pop-dance-c-alignment.json`, which matches the intended production assumptions: zero inset, identity frame transforms, reversible sequence `0,1,2,3,2,1`, and durations `210,140,140,210,140,140 ms`.

Every assembled GIF passed:

- 256×256;
- 6 output frames;
- 4 unique output-frame hashes;
- exact reversible duration sequence;
- infinite loop metadata (`loop=0`);
- transparent corners and clean chroma removal/despill;
- no visible crop or green fringe at 256 px or 128 px.

GIF evidence:

- Temporary GIFs: `/tmp/pop-dance-c-independent/gifs/`
- Full 256 px six-frame strips: `/tmp/pop-dance-c-independent/contact/gif-full-1.jpg` through `gif-full-5.jpg`
- 128 px six-frame strip: `/tmp/pop-dance-c-independent/contact/gif-128.jpg`
- Machine-readable GIF results: `/tmp/pop-dance-c-independent-gif-qa.json`

## Blockers

None.

## Correction re-audit — restored `disco-inferno-ing-reports`

Re-audited after the 21:14 deterministic restore. **PASS.** The restored source SHA-256 is exactly `6816f5a4518eea035300469debbd4348823f1fabcbe77253787b273b9c6a3b45`. Full-resolution inspection of all four authored cells, including isolated bottom 180 px strips, confirms the prior bottom-left jacket/leg sliver is absent; the bottom-left 120×120 corner zone contains zero non-key pixels in every cell. The production GIF also passes at 256 px and 128 px: 256×256, 6 frames, 4 unique phases, exact reversible durations, infinite loop, transparent corners, no crop, and no residual sliver. Evidence: `/tmp/pop-dance-c-independent/restored-disco/`.
