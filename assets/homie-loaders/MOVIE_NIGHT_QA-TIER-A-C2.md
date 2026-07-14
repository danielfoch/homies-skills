# Tier-A Movie Night C2 — QA report

Scope completed in this resume: `supermanning-marketing`, `spider-manning-crm`, `wolverine-ing-research`, `joker-ing-content`, and `beetlejuicing-listings` only.

## Automated source contract

All five accepted source masters pass:

- exact `1254 × 1254`
- exact `RGB`
- exact `#00ff00` on every outer edge and on both pixels surrounding each centre axis
- four distinct authored cells
- minimum cell-content margin at least `60px`
- no crop at full size

| Slug | Smallest measured margin | Unique authored cells |
|---|---:|---:|
| `supermanning-marketing` | 72px | 4 |
| `spider-manning-crm` | 66px | 4 |
| `wolverine-ing-research` | 70px | 4 |
| `joker-ing-content` | 65px | 4 |
| `beetlejuicing-listings` | 65px | 4 |

Machine record: `/tmp/movie-c2/source-audit.json`

## Real GIF pipeline contract

Both 256px and 128px test GIFs were assembled with the production chroma helper and sprite assembler. Every GIF has six frames, four unique authored appearances, sequence `0,1,2,3,2,1`, durations `210/140/140/210/140/140ms`, infinite loop, transparent corners, and no empty frame.

| Slug | 256px bytes | 128px bytes | Result |
|---|---:|---:|---|
| `supermanning-marketing` | 38,225 | 13,282 | pass |
| `spider-manning-crm` | 23,984 | 9,225 | pass |
| `wolverine-ing-research` | 52,203 | 17,316 | pass |
| `joker-ing-content` | 52,446 | 17,273 | pass |
| `beetlejuicing-listings` | 62,284 | 19,711 | pass |

Machine record: `/tmp/movie-c2/gif-audit.json`

## Full-size and 128px visual gate

Contact sheets inspected from the actual GIF outputs:

- `/tmp/movie-c2/contact/gif-full.png`
- `/tmp/movie-c2/contact/gif-128.png`

Per-action findings:

- `supermanning-marketing`: one exact plate keeps anatomy, badge, and cape continuous. The leading fist stays forward; the flight path travels 12.83px vertically at 128px and the pitch changes visibly. No letter/logo appears in the gold diamond badge.
- `spider-manning-crm`: one exact plate is inverted and pivots around one fixed web attachment. The body remains rigid and travels 23.84px side-to-side at 128px. The suit has persistent red/blue division, black web linework, white lenses, one web line, two arms, and two legs.
- `wolverine-ing-research`: the body/fists are pixel-stable (0.33px maximum centroid variation comes only from extending effects). Exactly three silver claws are present on each fist in every authored cell and extend through four readable lengths, then retract through the reversible sequence.
- `joker-ing-content`: four strong head/card poses survive at 128px. Exactly one blank card is present in every frame, the other hand remains empty, and the olive-green hair/waistcoat survive the actual chroma/despill pipeline.
- `beetlejuicing-listings`: both elbows remain connected and wide; alternating shoulder height and body compression are readable at 128px. Foot anchors remain fixed and no frame crops the pale hair or hands.

Manual rejection gates checked: no trash fragment, no crop, no extra limb, no detached anatomy, no disappearing prop, no card duplication, no claw-count drift, no generic static sequence, and no accidental frame-to-frame recentering.

## Accepted temp deliverables

- source masters: `/tmp/movie-c2/sources/`
- 256px GIFs: `/tmp/movie-c2/gifs/`
- 128px GIFs: `/tmp/movie-c2/gifs-128/`
- contact sheets: `/tmp/movie-c2/contact/`
- build script: `/tmp/build_movie_c2.py`
- prompt ledger: `/tmp/movie-c2-prompts.md`

## Deferred remainder

The original nine-item C2 list still has four deferred items:

- `forrest-gumping-crm` — successful raw already exists and is preserved unprocessed at `/tmp/movie-c2/preserved-unprocessed/forrest-gumping-crm.png`; it was intentionally not built or promoted in this five-item resume.
- `mary-poppinsing-reports` — not generated in this resume.
- `ace-ventura-ing-marketing` — not generated in this resume.
- `shreking-manager` — not generated in this resume.

No production manifest, production alignment JSON, or production GIF was edited.

