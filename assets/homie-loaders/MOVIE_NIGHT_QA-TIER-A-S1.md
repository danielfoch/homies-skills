# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `yoda-ing-cma` | PASS | 65px | 50.09px | 10.4453% | 44.0276% | recorded: pass |
| `darth-vadering-offers` | PASS | 67px | 50.606px | 5.2098% | 16.4205% | recorded: pass |
| `terminatoring-reports` | PASS | 67px | 7.297px | 2.7268% | 14.5764% | recorded: pass |
| `batmaning-manager` | PASS | 66px | 99.0px | 56.8334% | 75.0962% | recorded: pass |

## yoda-ing-cma — PASS

Concept: Small tan-robed green wise-alien homage lifting one hand and one pebble

Required action: The connected hand must rise from waist to face while the single pebble rises at least a head-height; both motions must read at 128px.

Full-size contact: `/tmp/movie-tier-a-s1/strict/contacts/yoda-ing-cma-source-full.png`

128px contact: `/tmp/movie-tier-a-s1/strict/contacts/yoda-ing-cma-source-128.png`

GIF contact: `/tmp/movie-tier-a-s1/strict/contacts/yoda-ing-cma-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. One connected hand rises through four clearly separated poses and the same single pebble rises from knee level to above the head. Exactly two hands/arms and one pebble per frame; no crop or stray fragment.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 67px | 74732px | 2 (2/0) | none |
| 1 | 67px | 75357px | 2 (1/0) | none |
| 2 | 67px | 77534px | 2 (2/0) | none |
| 3 | 65px | 80441px | 3 (2/1) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 5.8985% | 50.09px | 3.49px | 0.0px | 31.85% | 0.8553 |
| 1→2 | 10.4453% | 49.149px | 8.459px | 0.0px | 40.7548% | 0.8348 |
| 2→3 | 9.742% | 41.326px | 5.035px | 0.0px | 44.0276% | 0.5903 |

## darth-vadering-offers — PASS

Concept: Black masked space-villain homage raising one connected gripping hand

Required action: One attached gloved hand must travel from hip through chest to a strong forward grip while the cape remains visually fixed.

Full-size contact: `/tmp/movie-tier-a-s1/strict/contacts/darth-vadering-offers-source-full.png`

128px contact: `/tmp/movie-tier-a-s1/strict/contacts/darth-vadering-offers-source-128.png`

GIF contact: `/tmp/movie-tier-a-s1/strict/contacts/darth-vadering-offers-gif-128.png`

Failures: none

Warnings: none

Manual notes: Full-size and 128px review passed after body-anchor registration. The attached gloved arm travels hip-to-waist-to-shoulder-to-forward grip; the other arm, helmet, torso, boots and outer cape remain visually registered. Chest panel is identical and logo-free.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 67px | 100158px | 1 (1/0) | none |
| 1 | 67px | 100217px | 1 (1/0) | none |
| 2 | 67px | 103963px | 1 (1/0) | none |
| 3 | 67px | 106013px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.1496% | 15.582px | 1.086px | 1.0px | 16.4205% | 0.8259 |
| 1→2 | 4.5208% | 50.606px | 7.38px | 1.0px | 16.3528% | 0.8419 |
| 2→3 | 5.2098% | 26.249px | 3.199px | 2.0px | 15.8214% | 0.7532 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| outer viewer-right cape strip | 8.546% | 16.0% |

## terminatoring-reports — PASS

Concept: Black-leather android homage turning its head while one red lens pulses

Required action: The head must turn clearly left-centre-right-centre and the one contained red lens must pulse while the body remains fixed.

Full-size contact: `/tmp/movie-tier-a-s1/strict/contacts/terminatoring-reports-source-full.png`

128px contact: `/tmp/movie-tier-a-s1/strict/contacts/terminatoring-reports-source-128.png`

GIF contact: `/tmp/movie-tier-a-s1/strict/contacts/terminatoring-reports-gif-128.png`

Failures: none

Warnings: none

Manual notes: Full-size and 128px review passed. The connected head turns left-centre-right-centre while hair and glasses follow as one layer; the one red lens progresses from dim/off to medium to bright pulse. Torso and legs change under 1% in the annotated fixed region.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 67px | 49444px | 1 (1/0) | none |
| 1 | 67px | 48946px | 1 (1/0) | none |
| 2 | 67px | 49132px | 1 (1/0) | none |
| 3 | 67px | 48928px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.7268% | 7.297px | 1.948px | 0.0px | 14.5764% | 0.3678 |
| 1→2 | 1.5098% | 5.589px | 0.812px | 0.0px | 12.6083% | 0.4287 |
| 2→3 | 1.6987% | 6.004px | 0.946px | 0.0px | 13.3488% | 0.3961 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed torso and legs | 0.8282% | 1.0% |

## batmaning-manager — PASS

Concept: Dark cowled guardian opening one cape into a broad scalloped wing silhouette

Required action: Cape width must progress from wrapped to half-open to broad to fully wing-wide, unmistakably at 128px.

Full-size contact: `/tmp/movie-tier-a-s1/strict/contacts/batmaning-manager-source-full.png`

128px contact: `/tmp/movie-tier-a-s1/strict/contacts/batmaning-manager-source-128.png`

GIF contact: `/tmp/movie-tier-a-s1/strict/contacts/batmaning-manager-gif-128.png`

Failures: none

Warnings: `FOREGROUND_AREA_JUMP`, `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. The cape changes from a wrapped narrow cocoon to half-open, broad, then fully wing-wide with large scallops. Exactly two connected arms/hands; cowl, body and feet remain coherent, with 60px minimum clearance in the widest frame.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 66px | 37743px | 1 (1/0) | none |
| 1 | 66px | 85008px | 1 (1/0) | none |
| 2 | 66px | 98209px | 1 (1/0) | none |
| 3 | 66px | 113406px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 56.8334% | 99.0px | 18.126px | 7.0px | 75.0962% | 0.4022 |
| 1→2 | 18.9859% | 38.079px | 11.983px | 8.602px | 33.6181% | 0.082 |
| 2→3 | 16.3734% | 40.162px | 10.387px | 8.0px | 25.4404% | 0.3532 |

