# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `disco-inferno-ing-reports` | PASS | 65px | 8.944px | 3.9181% | 7.2371% | recorded: pass |
| `rickrolling-manager` | PASS | 65px | 5.099px | 1.0907% | 3.301% | recorded: pass |
| `ymca-ing-cma` | PASS | 60px | 78.435px | 21.2411% | 29.8567% | recorded: pass |
| `wednesday-ing-offers` | PASS | 65px | 9.487px | 2.3381% | 3.5104% | recorded: pass |

## disco-inferno-ing-reports — PASS

Concept: Reports Homie holds a locked disco stance while the connected pointing arm pumps through a clean up-and-down arc.

Required action: Only the complete connected raised arm rotates around one fixed shoulder; face, hair, suit, planted arm, torso, hips, legs and shoes remain fixed without body scaling.

Full-size contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/disco-inferno-ing-reports-source-full.png`

128px contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/disco-inferno-ing-reports-source-128.png`

GIF contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/disco-inferno-ing-reports-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent full-cell and 128px review confirms one character, one connected moving arm, stable suit and legs, no scale pumping, overlap, crop, redraw debris or palette shimmer.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 37826px | 1 (1/0) | none |
| 1 | 65px | 37821px | 1 (1/0) | none |
| 2 | 65px | 37810px | 1 (1/0) | none |
| 3 | 65px | 37809px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 3.8811% | 8.944px | 0.397px | 0.0px | 7.1917% | 0.9693 |
| 1→2 | 3.8819% | 8.944px | 0.405px | 0.0px | 7.2088% | 0.965 |
| 2→3 | 3.9181% | 8.773px | 0.401px | 0.0px | 7.2371% | 0.9599 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-suit-core-legs-shoes | 0.0% | 0.0% |

## rickrolling-manager — PASS

Concept: Manager Homie performs a compact Rickroll finger-point in the recognizable striped top and tan coat.

Required action: Exactly one connected pointing arm pivots around its fixed shoulder while the single head, coat, pocket hand, torso, legs and shoes remain fixed.

Full-size contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/rickrolling-manager-source-full.png`

128px contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/rickrolling-manager-source-128.png`

GIF contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/rickrolling-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent review confirms exactly one locked character plate and one attached pointing arm; head, coat, pocket hand, legs and shoes remain stable with no overlap, crop, debris or shimmer.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 48565px | 1 (1/0) | none |
| 1 | 65px | 48373px | 1 (1/0) | none |
| 2 | 65px | 48169px | 1 (1/0) | none |
| 3 | 65px | 47940px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.9037% | 4.472px | 0.757px | 0.0px | 3.0356% | 0.9814 |
| 1→2 | 0.8622% | 4.472px | 0.811px | 0.0px | 3.0487% | 0.9814 |
| 2→3 | 1.0907% | 5.099px | 0.909px | 0.0px | 3.301% | 0.9776 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-lower-coat-legs-shoes | 0.0% | 0.0% |

## ymca-ing-cma — PASS

Concept: CMA Homie performs four distinct Y, M, C and A letter silhouettes with one stable body and one connected pair of arms.

Required action: The two complete articulated arms form Y, bent M, open C and overhead A in order; face, jacket core, shirt, hips, flared trousers and shoes remain fixed with no duplicate limbs or scale pumping.

Full-size contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/ymca-ing-cma-source-full.png`

128px contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/ymca-ing-cma-source-128.png`

GIF contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/ymca-ing-cma-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent full-cell and 128px inspection confirms all four letters, one fixed face and torso, stable flared trousers and shoes, and no duplicate limbs, old arm remnants, scaling, crop or debris.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 63px | 48771px | 1 (1/0) | none |
| 1 | 65px | 47825px | 1 (1/0) | none |
| 2 | 60px | 46372px | 1 (1/0) | none |
| 3 | 65px | 48131px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 20.7002% | 78.435px | 8.753px | 0.0px | 28.0135% | 0.8799 |
| 1→2 | 21.2411% | 45.541px | 5.374px | 0.0px | 29.8567% | 0.8607 |
| 2→3 | 17.223% | 56.881px | 8.635px | 0.0px | 27.6652% | 0.8174 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-trouser-legs-and-shoes | 0.0% | 0.0% |

## wednesday-ing-offers — PASS

Concept: Offers Homie performs a restrained Wednesday-style hand dance in a locked black dress and braided-hair pose.

Required action: One connected raised forearm and hand pivots around a fixed elbow; the other connected arm, face, braids, collar, dress, legs and shoes remain fixed, with exactly two hands in every frame.

Full-size contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/wednesday-ing-offers-source-full.png`

128px contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/wednesday-ing-offers-source-128.png`

GIF contact: `qa/strict-repairs/pop-dance-hand-cleanup/report-independent-root/contacts/wednesday-ing-offers-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent review confirms exactly two hands in every frame and no sustained ghost hand; braids, collar, dress, legs and shoes remain stable with no redraw, crop, debris or shimmer.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 45248px | 1 (1/0) | none |
| 1 | 65px | 45123px | 1 (1/0) | none |
| 2 | 65px | 45082px | 1 (1/0) | none |
| 3 | 65px | 45135px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.2689% | 8.955px | 0.463px | 0.0px | 3.3476% | 0.9998 |
| 1→2 | 2.3381% | 9.487px | 0.24px | 0.0px | 3.5104% | 1.0 |
| 2→3 | 2.2641% | 8.944px | 0.212px | 0.0px | 3.4236% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-dress-legs-shoes | 0.0% | 0.0% |
