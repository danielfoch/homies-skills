# Tier-A Movie Night C2B — QA report

Scope: `forrest-gumping-crm`, `mary-poppinsing-reports`, `ace-ventura-ing-marketing`, and `shreking-manager` only.

## Source contract

All four temp sources pass exact `1254 × 1254` RGB, exact `#00ff00` outer edges and centre axes, four distinct cells, and at least 60px content margin.

| Slug | Smallest margin | Unique cells |
|---|---:|---:|
| `forrest-gumping-crm` | 68px | 4 |
| `mary-poppinsing-reports` | 70px | 4 |
| `ace-ventura-ing-marketing` | 65px | 4 |
| `shreking-manager` | 65px | 4 |

Machine record: `/tmp/movie-c2b/source-audit.json`

## Real GIF contract

Both the 256px and 128px GIFs were assembled through the real production chroma helper and sprite assembler. Every file has six frames, four unique authored appearances, sequence `0,1,2,3,2,1`, durations `210/140/140/210/140/140ms`, infinite loop, transparent corners, and no empty frame.

| Slug | 256px bytes | 128px bytes | Result |
|---|---:|---:|---|
| `forrest-gumping-crm` | 42,351 | 14,862 | pass |
| `mary-poppinsing-reports` | 39,300 | 13,687 | pass |
| `ace-ventura-ing-marketing` | 48,055 | 16,050 | pass |
| `shreking-manager` | 62,643 | 20,051 | pass |

Machine record: `/tmp/movie-c2b/gif-audit.json`

## Full-size and 128px visual checks

Actual-GIF contact sheets inspected:

- `/tmp/movie-c2b/contact/gif-full.png`
- `/tmp/movie-c2b/contact/gif-128.png`

Findings:

- `forrest-gumping-crm`: high-knee phases alternate left/right; arms pump opposite each raised knee; the passing phases remain distinct. Head anchoring limits the intentional running bob to 3.24px centroid travel at 128px without static-foot recentering.
- `mary-poppinsing-reports`: exactly one open umbrella remains connected to one hand. The canopy, shaft, hand, body, scarf, and feet are a single rigid plate. The visible float spans 8.71px vertically at 128px and every phase retains clear empty space beneath both shoes.
- `ace-ventura-ing-marketing`: centre/left/right/centre head directions and pompadour follow-through remain obvious at 128px. The loud shirt persists, hands stay in pockets, feet are anchored, and total body centroid drift is only 0.90px.
- `shreking-manager`: cream-white tunic, brown vest, olive-green face/hands, exactly two connected ear-stalks, friendly smile, and hips-on-hands posture persist. Body sway spans 5.40px centroid travel at 128px; alternating ear tip motion remains visible after the real despill pipeline.

Manual rejection gates checked: no crop, no garbage fragment, no extra limb, no disappearing umbrella, no duplicated prop, no detached head/ear, no ear-count drift, no static fake jog, no generic standing-only loop, and no accidental whole-character jitter.

## Accepted temp deliverables

- source masters: `/tmp/movie-c2b/sources/`
- 256px GIFs: `/tmp/movie-c2b/gifs/`
- 128px GIFs: `/tmp/movie-c2b/gifs-128/`
- contact sheets: `/tmp/movie-c2b/contact/`
- build script: `/tmp/build_movie_c2b.py`
- prompts: `/tmp/movie-c2b-prompts.md`

No production manifest, production alignment file, production GIF, deployment, or gallery was touched.

