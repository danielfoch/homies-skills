# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `rambo-ing-manager` | FAIL | 65px | 7.0px | 1.6184% | 2.7218% | recorded: pass |
| `godfathering-reports` | PASS | 65px | 0.0px | 0.0% | 0.3789% | recorded: pass |
| `pulp-fictioning-reports` | PASS | 65px | 0.0px | 0.0% | 1.9521% | recorded: pass |
| `waynes-worlding-content` | PASS | 65px | 6.0px | 1.6476% | 6.708% | recorded: pass |
| `bill-and-ted-ing-crm` | FAIL | 64px | 9.849px | 2.0024% | 3.4531% | recorded: pass |
| `robocopping-offers` | FAIL | 64px | 11.692px | 3.758% | 8.2765% | recorded: pass |

## rambo-ing-manager — FAIL

Concept: The canonical male Manager Homie tightens a red commando headband in an ink-and-watercolour tactical costume.

Required action: The two connected red cloth tails cinch and counter-swing around fixed hand contacts while the Manager face, hands, arms, torso, legs and feet remain fixed.

Full-size contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/rambo-ing-manager-source-full.png`

128px contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/rambo-ing-manager-source-128.png`

GIF contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/rambo-ing-manager-gif-128.png`

Failures: `STATIONARY_REGION_DRIFT:fixed-manager-face-and-centre`

Warnings: none

Manual notes: Full-size and 128px source/GIF contacts inspected. Exact Manager face, swept hair and slim ink/watercolour identity retained. The same single body plate is reused; only the connected red tail pixels move. No clay/3D styling, redraw, seam, ghost arm, debris, crop, palette shimmer or whole-body jiggle.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 49372px | 3 (1/1) | none |
| 1 | 65px | 49307px | 2 (1/1) | none |
| 2 | 65px | 49032px | 5 (1/3) | none |
| 3 | 65px | 49060px | 2 (1/1) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 1.6184% | 7.0px | 0.191px | 0.0px | 2.523% | 0.9959 |
| 1→2 | 1.2952% | 6.0px | 0.542px | 0.0px | 2.7218% | 0.9895 |
| 2→3 | 0.5044% | 3.0px | 0.007px | 0.0px | 2.4649% | 0.9924 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-manager-lower-body | 0.0% | 0.0% |
| fixed-manager-face-and-centre | 4.6494% | 0.0% |

## godfathering-reports — PASS

Concept: The canonical female Reports Homie adopts a composed formal crime-boss steeple pose in a black three-piece suit.

Required action: One authored eyebrow lifts in a deliberate calculating loop while the Reports face, hair, steepled hands, suit, legs and feet remain fixed.

Full-size contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/godfathering-reports-source-full.png`

128px contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/godfathering-reports-source-128.png`

GIF contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/godfathering-reports-gif-128.png`

Failures: none

Warnings: none

Manual notes: Female Reports face, long dark hair, adult proportions and editorial ink/watercolour treatment are retained. The steeple pose supplies the joke; one local eyebrow patch makes the deliberate loop. The full body and hands remain exact with no redraw, drift, seams, debris or crop.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 40906px | 1 (1/0) | none |
| 1 | 65px | 40906px | 1 (1/0) | none |
| 2 | 65px | 40906px | 1 (1/0) | none |
| 3 | 65px | 40906px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.0% | 0.0px | 0.0px | 0.0px | 0.2616% | 0.9966 |
| 1→2 | 0.0% | 0.0px | 0.0px | 0.0px | 0.3789% | 0.9908 |
| 2→3 | 0.0% | 0.0px | 0.0px | 0.0px | 0.3129% | 0.9922 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-reports-body-below-brow | 0.0% | 0.0% |
| fixed-reports-left-face-hair | 0.0% | 0.0% |

## pulp-fictioning-reports — PASS

Concept: The canonical female Reports Homie wears a black bob and black-and-white twist-dance suit.

Required action: The bolo tie swings left-to-right over one fixed bent-knee dance plate; the Reports face, bob, hands, suit, legs and shoes remain fixed.

Full-size contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/pulp-fictioning-reports-source-full.png`

128px contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/pulp-fictioning-reports-source-128.png`

GIF contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/pulp-fictioning-reports-gif-128.png`

Failures: none

Warnings: none

Manual notes: The black bob is a costume, while the canonical female Reports face, proportions and ink/wash medium stay recognizable. Only the narrow tie layer moves; face, hair, hands, body and feet are exact across all phases. No morph, camera motion, seam, debris, crop or shimmer.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 44158px | 1 (1/0) | none |
| 1 | 65px | 44158px | 1 (1/0) | none |
| 2 | 65px | 44158px | 1 (1/0) | none |
| 3 | 65px | 44158px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.0% | 0.0px | 0.0px | 0.0px | 1.8434% | 0.938 |
| 1→2 | 0.0% | 0.0px | 0.0px | 0.0px | 1.8841% | 0.9383 |
| 2→3 | 0.0% | 0.0px | 0.0px | 0.0px | 1.9521% | 0.9213 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-reports-dance-lower-body | 0.0% | 0.0% |
| fixed-reports-bob-and-face | 0.0% | 0.0% |

## waynes-worlding-content — PASS

Concept: The canonical male Content Homie headbangs in a backward cap, black tee and ripped jeans while holding an air-guitar stance.

Required action: One rigid Content head-and-cap layer rocks around a fixed neck pivot; shirt, hands, hips, legs and feet remain pixel-stable.

Full-size contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/waynes-worlding-content-source-full.png`

128px contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/waynes-worlding-content-source-128.png`

GIF contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/waynes-worlding-content-gif-128.png`

Failures: none

Warnings: none

Manual notes: Exact Content face, skin tone, short black hair and slim 2D ink/watercolour character system retained. The head/cap is one rigid layer; shirt, arms, hands, pelvis, legs and shoes never move. Joint overlap inspected at full size and 128px with no neck hole, duplicate head, redraw wiggle or palette shimmer.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 52236px | 1 (1/0) | none |
| 1 | 65px | 52282px | 1 (1/0) | none |
| 2 | 65px | 52335px | 1 (1/0) | none |
| 3 | 65px | 52298px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.8991% | 3.362px | 0.304px | 0.0px | 5.3415% | 0.8907 |
| 1→2 | 1.6476% | 6.0px | 0.455px | 0.0px | 6.708% | 0.8446 |
| 2→3 | 0.7104% | 3.0px | 0.227px | 0.0px | 4.9673% | 0.9119 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-content-body-below-neck | 0.0% | 0.0% |
| fixed-content-air-guitar-arm | 0.0% | 0.0% |

## bill-and-ted-ing-crm — FAIL

Concept: The canonical bald male CRM Homie air-guitars in a denim vest, burgundy tee, plaid waist shirt and mismatched high-tops.

Required action: Only the connected fretting forearm rotates around one fixed elbow; CRM face, bald head, torso, other hand, hips, legs and shoes remain fixed.

Full-size contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/bill-and-ted-ing-crm-source-full.png`

128px contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/bill-and-ted-ing-crm-source-128.png`

GIF contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/bill-and-ted-ing-crm-gif-128.png`

Failures: `STATIONARY_REGION_DRIFT:fixed-crm-face-torso-left-core`

Warnings: none

Manual notes: Exact bald CRM face, smile, skin tone and tall ink/watercolour proportions retained. One forearm rotates rigidly at a fixed elbow cap; the other hand, head, torso, plaid waist shirt, legs and mismatched shoes remain exact. No broken elbow, extra hand, redraw, debris, crop or jitter.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 64px | 53554px | 1 (1/0) | none |
| 1 | 64px | 53431px | 1 (1/0) | none |
| 2 | 64px | 53163px | 1 (1/0) | none |
| 3 | 64px | 53270px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 1.2503% | 5.657px | 0.37px | 0.0px | 2.547% | 0.994 |
| 1→2 | 2.0024% | 9.849px | 0.9px | 0.0px | 3.4531% | 0.9944 |
| 2→3 | 1.201% | 5.657px | 0.357px | 0.0px | 2.6299% | 0.9969 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-crm-face-torso-left-core | 0.0627% | 0.0% |
| fixed-crm-lower-body | 0.0% | 0.0% |

## robocopping-offers — FAIL

Concept: The canonical female Offers Homie wears a hand-inked silver cyborg-police costume with her face and signature bun visible.

Required action: The raised arm makes one mechanical servo sweep and the red visor scanner pulses; Offers face, bun, armour core, other arm, legs and boots remain fixed.

Full-size contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/robocopping-offers-source-full.png`

128px contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/robocopping-offers-source-128.png`

GIF contact: `qa/strict-repairs/movie-style-canonical-six/report-candidate/contacts/robocopping-offers-gif-128.png`

Failures: `STATIONARY_REGION_DRIFT:fixed-offers-armour-core-right-side`

Warnings: none

Manual notes: The loader clearly reads as the female Offers Homie wearing armour, not a replacement robot: face, warm colouring and signature bun remain visible in the original ink/watercolour system. One forearm rotates around a fixed circular elbow cap and the red scanner dot moves. Armour core, other arm, hips, legs and boots remain exact. The chroma cleanup removed the raw four-pixel speck; no debris, seam, morph, crop or shimmer remains.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 64px | 39677px | 1 (1/0) | none |
| 1 | 64px | 39754px | 1 (1/0) | none |
| 2 | 64px | 39985px | 1 (1/0) | none |
| 3 | 64px | 39876px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.0362% | 6.403px | 0.387px | 0.0px | 7.1528% | 0.9976 |
| 1→2 | 3.758% | 11.692px | 0.932px | 0.0px | 8.2765% | 0.9977 |
| 2→3 | 2.2949% | 6.325px | 0.459px | 0.0px | 7.1545% | 0.9975 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-offers-armour-core-right-side | 0.6438% | 0.0% |
| fixed-offers-lower-body | 0.0% | 0.0% |
