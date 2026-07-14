# Homies strict QA report

> **REJECTED / SUPERSEDED (2026-07-13):** this report checked structure and
> motion but failed the primary brand contract. All six assets used unrelated
> clay/3D mascots instead of the assigned canonical Homies. Do not treat the
> PASS rows below as current release approval. Current evidence is
> `qa/strict-repairs/movie-style-canonical-six/report-candidate-v3/strict-qa.md`.

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `bill-and-ted-ing-crm` | PASS | 62px | 22.0px | 3.4024% | 30.7875% | recorded: pass |
| `godfathering-reports` | PASS | 67px | 13.038px | 5.9137% | 39.2808% | recorded: pass |
| `pulp-fictioning-reports` | PASS | 67px | 32.527px | 31.736% | 72.7015% | recorded: pass |
| `rambo-ing-manager` | PASS | 67px | 50.01px | 24.9309% | 36.8567% | recorded: pass |
| `robocopping-offers` | PASS | 67px | 90.516px | 25.7973% | 80.2303% | recorded: pass |
| `waynes-worlding-content` | PASS | 67px | 62.817px | 63.2615% | 78.5384% | recorded: pass |

## bill-and-ted-ing-crm — PASS

Concept: Original scruffy layered-vest retro garage rocker air-guitaring

Required action: The fretting hand must hold one consistent invisible neck across the upper torso while the other forearm alternates down-up-down strums over the same waist-level strings; feet and torso remain anchored.

Full-size contact: `/tmp/movie-tier-a-s2/strict/contacts/bill-and-ted-ing-crm-source-full.png`

128px contact: `/tmp/movie-tier-a-s2/strict/contacts/bill-and-ted-ing-crm-source-128.png`

GIF contact: `/tmp/movie-tier-a-s2/strict/contacts/bill-and-ted-ing-crm-gif-128.png`

Failures: none

Warnings: none

Manual notes: Reworked sheet passed full-size, 128px and GIF review. Scruffy shag hair, blank denim vest, layered waist shirt, ripped jeans and mismatched high-tops provide the retro rocker silhouette. One hand keeps a C-grip on the same invisible neck while the other alternates down-up-down across waist-level strings; torso, feet and shins remain registered.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 62px | 73588px | 1 (1/0) | none |
| 1 | 62px | 72212px | 1 (1/0) | none |
| 2 | 62px | 73457px | 1 (1/0) | none |
| 3 | 62px | 72456px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.9197% | 22.0px | 2.162px | 0.0px | 28.1873% | 0.9773 |
| 1→2 | 3.4024% | 17.0px | 1.713px | 0.0px | 30.7875% | 0.9801 |
| 2→3 | 2.996% | 13.0px | 1.34px | 0.0px | 29.44% | 0.9805 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| registered shins and mismatched high-tops | 0.0% | 1.0% |

## godfathering-reports — PASS

Concept: Original formal executive steepling fingers then making a skeptical head tilt

Required action: Hands must progress separated-to-steepled-to-raised while the final head and eyebrow tilt is unmistakable at 128px.

Full-size contact: `/tmp/movie-tier-a-s2/strict/contacts/godfathering-reports-source-full.png`

128px contact: `/tmp/movie-tier-a-s2/strict/contacts/godfathering-reports-source-128.png`

GIF contact: `/tmp/movie-tier-a-s2/strict/contacts/godfathering-reports-gif-128.png`

Failures: none

Warnings: none

Manual notes: Full-size, 128px, and GIF contacts passed. Fingertips progress separated-to-steepled-to-raised under the chin, followed by a distinct whole-head and single-eyebrow tilt. Suit, slick hair, hands, legs and shoes stay coherent; lower suit plate measures zero change. No cigar, prop or crop.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 67px | 75894px | 1 (1/0) | none |
| 1 | 67px | 76165px | 1 (1/0) | none |
| 2 | 67px | 73132px | 1 (1/0) | none |
| 3 | 67px | 73363px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.6829% | 2.0px | 0.433px | 0.0px | 22.5796% | 0.9056 |
| 1→2 | 5.9137% | 10.05px | 4.664px | 0.0px | 39.2808% | 0.3939 |
| 2→3 | 4.0489% | 13.038px | 2.162px | 0.0px | 24.5489% | 0.6319 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| registered lower suit and shoes | 0.0% | 1.0% |

## pulp-fictioning-reports — PASS

Concept: Original bob-haired retro formal dancer performing a compact twist

Required action: Alternating knees, forearms, and torso must progress left-centre-right-centre and remain obvious at 128px.

Full-size contact: `/tmp/movie-tier-a-s2/strict/contacts/pulp-fictioning-reports-source-full.png`

128px contact: `/tmp/movie-tier-a-s2/strict/contacts/pulp-fictioning-reports-source-128.png`

GIF contact: `/tmp/movie-tier-a-s2/strict/contacts/pulp-fictioning-reports-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size, 128px, and reversible GIF contacts passed. Dark bob, black suit, white shirt and bolo clasp persist. Knees, forearms, head direction, and torso alternate left-centre-right-centre with connected anatomy and no crop or fragment.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 67px | 58234px | 1 (1/0) | none |
| 1 | 67px | 62469px | 1 (1/0) | none |
| 2 | 68px | 55267px | 1 (1/0) | none |
| 3 | 68px | 62124px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 30.9292% | 32.527px | 9.812px | 2.236px | 72.7015% | 0.105 |
| 1→2 | 31.736% | 31.623px | 6.519px | 8.062px | 69.4585% | 0.2597 |
| 2→3 | 30.5533% | 29.698px | 4.369px | 6.0px | 70.6986% | 0.2461 |

## rambo-ing-manager — PASS

Concept: Original outdoor athlete tightening and releasing a red headband

Required action: Both connected hands must grip, pull the cloth visibly taut, reach behind the head, then release while the red band persists.

Full-size contact: `/tmp/movie-tier-a-s2/strict/contacts/rambo-ing-manager-source-full.png`

128px contact: `/tmp/movie-tier-a-s2/strict/contacts/rambo-ing-manager-source-128.png`

GIF contact: `/tmp/movie-tier-a-s2/strict/contacts/rambo-ing-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Full-size, 128px, and GIF contacts passed. Both connected hands grip, pull the same red cloth taut, reach behind the head, then release to shoulder height. Band, vest, pendant, cargo trousers and boots persist; the fixed lower plate measures zero change. No weapon or crop.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 67px | 71345px | 1 (1/0) | none |
| 1 | 67px | 71770px | 1 (1/0) | none |
| 2 | 67px | 71266px | 1 (1/0) | none |
| 3 | 67px | 69353px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 11.8369% | 24.759px | 0.101px | 0.0px | 30.1424% | 0.9188 |
| 1→2 | 19.1707% | 36.069px | 4.425px | 0.0px | 35.4893% | 0.8758 |
| 2→3 | 24.9309% | 50.01px | 15.29px | 0.0px | 36.8567% | 0.8625 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| registered cargo trousers and boots | 0.0% | 1.0% |

## robocopping-offers — PASS

Concept: Original silver service cyborg making a mechanical turn and servo lift

Required action: Helmet/chest orientation must read left-centre-right-centre while one attached forearm rises to a crisp servo angle and lowers halfway.

Full-size contact: `/tmp/movie-tier-a-s2/strict/contacts/robocopping-offers-source-full.png`

128px contact: `/tmp/movie-tier-a-s2/strict/contacts/robocopping-offers-source-128.png`

GIF contact: `/tmp/movie-tier-a-s2/strict/contacts/robocopping-offers-gif-128.png`

Failures: none

Warnings: `BBOX_SCALE_OR_PROP_JUMP`

Manual notes: Full-size review caught and rejected a temporary detached-fist plate artifact; final reconstruction was rebuilt and re-reviewed with exactly two connected hands. Helmet/chest orientation reads left-centre-right-centre while one forearm makes a stepped servo lift/lower. No weapon, crop, logo or stray fragment; shins and boots are exact-stable.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 67px | 83654px | 1 (1/0) | none |
| 1 | 67px | 82882px | 1 (1/0) | none |
| 2 | 67px | 84937px | 1 (1/0) | none |
| 3 | 67px | 79369px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 25.7973% | 88.6px | 18.01px | 9.22px | 80.2303% | 0.3723 |
| 1→2 | 8.1542% | 15.811px | 3.702px | 1.414px | 66.8681% | 0.5436 |
| 2→3 | 18.4625% | 90.516px | 13.105px | 4.0px | 72.0764% | 0.4836 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| registered shins and boots | 0.0% | 1.0% |

## waynes-worlding-content — PASS

Concept: Original long-haired metal fan headbanging with one compact air-guitar beat

Required action: The head must travel upright-forward-back-settle with large hair follow-through, while both hands maintain a coherent air-guitar mime.

Full-size contact: `/tmp/movie-tier-a-s2/strict/contacts/waynes-worlding-content-source-full.png`

128px contact: `/tmp/movie-tier-a-s2/strict/contacts/waynes-worlding-content-source-128.png`

GIF contact: `/tmp/movie-tier-a-s2/strict/contacts/waynes-worlding-content-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size, 128px, and GIF contacts passed. The head travels upright-forward-back-settle and the long hair follows through in a large readable arc; cap, blank tee, ripped jeans, hands and shoes persist without crop or extra anatomy.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 67px | 71899px | 1 (1/0) | none |
| 1 | 67px | 65365px | 1 (1/0) | none |
| 2 | 67px | 72879px | 1 (1/0) | none |
| 3 | 67px | 72471px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 61.1054% | 55.964px | 29.245px | 68.0px | 75.4166% | 0.1212 |
| 1→2 | 63.2615% | 62.817px | 30.994px | 79.0px | 78.5384% | 0.4314 |
| 2→3 | 43.1768% | 34.0px | 31.896px | 38.0px | 50.0606% | 0.456 |
