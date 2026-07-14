# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `cha-cha-sliding-marketing` | FAIL | 65px | 4.0px | 1.2811% | 5.1938% | pending |
| `harlem-shaking-listings` | FAIL | 65px | 17.464px | 12.0362% | 16.8089% | pending |
| `umbrella-ing-manager` | FAIL | 65px | 3.0px | 0.2354% | 1.1869% | pending |
| `dougie-ing-content` | FAIL | 64px | 11.0px | 3.4935% | 4.387% | pending |

## cha-cha-sliding-marketing — FAIL

Concept: Marketing Homie in the gold Cha Cha Slide outfit, crossing and sliding his boots.

Required action: Gold jacket, black outfit, long silver chain and crossed-foot cha-cha step read immediately; head, torso and jacket remain locked while only the connected boots slide.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/cha-cha-sliding-marketing-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/cha-cha-sliding-marketing-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/cha-cha-sliding-marketing-gif-128.png`

Failures: `VISUAL_REVIEW_REQUIRED`

Warnings: none

Manual notes: (none)

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 55855px | 1 (1/0) | none |
| 1 | 65px | 55803px | 1 (1/0) | none |
| 2 | 65px | 55728px | 1 (1/0) | none |
| 3 | 65px | 55763px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.6321% | 2.0px | 0.22px | 0.0px | 4.0924% | 1.0 |
| 1→2 | 1.2811% | 4.0px | 0.325px | 0.0px | 5.1938% | 1.0 |
| 2→3 | 0.7453% | 2.236px | 0.153px | 0.0px | 4.3393% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-head-torso-jacket | 0.0% | 0.05% |

## harlem-shaking-listings — FAIL

Concept: Listings Homie in the original bright-pink Harlem Shake suit, counter-swinging both low fists.

Required action: The pink suit, leaned stance and alternating fists match the original meme without a second body, scale pumping or redrawn face.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/harlem-shaking-listings-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/harlem-shaking-listings-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/harlem-shaking-listings-gif-128.png`

Failures: `STATIONARY_REGION_DRIFT:locked-face-and-pink-core`, `VISUAL_REVIEW_REQUIRED`

Warnings: `BBOX_SCALE_OR_PROP_JUMP`

Manual notes: (none)

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 51341px | 1 (1/0) | none |
| 1 | 65px | 50771px | 1 (1/0) | none |
| 2 | 65px | 49893px | 1 (1/0) | none |
| 3 | 65px | 50280px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 6.1839% | 9.487px | 0.932px | 0.0px | 10.8798% | 0.9619 |
| 1→2 | 12.0362% | 17.464px | 1.352px | 0.0px | 16.8089% | 0.9455 |
| 2→3 | 7.1111% | 9.899px | 0.676px | 0.0px | 12.2716% | 0.9605 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-face-and-pink-core | 8.9408% | 0.05% |

## umbrella-ing-manager — FAIL

Concept: Manager Homie physically holding a broad clear umbrella while a highlight travels across the canopy.

Required action: One open transparent umbrella is visibly connected from hooked handle in hand through shaft and ribs to canopy; Manager body and umbrella geometry remain fixed.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/umbrella-ing-manager-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/umbrella-ing-manager-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/umbrella-ing-manager-gif-128.png`

Failures: `VISUAL_REVIEW_REQUIRED`

Warnings: none

Manual notes: (none)

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 53844px | 1 (1/0) | none |
| 1 | 65px | 53943px | 1 (1/0) | none |
| 2 | 65px | 53860px | 1 (1/0) | none |
| 3 | 65px | 53855px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.2354% | 2.236px | 0.254px | 0.0px | 0.91% | 1.0 |
| 1→2 | 0.2057% | 2.236px | 0.213px | 0.0px | 1.1398% | 0.9981 |
| 2→3 | 0.2318% | 3.0px | 0.007px | 0.0px | 1.1869% | 0.9981 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-manager-and-handle | 0.0% | 0.05% |

## dougie-ing-content — FAIL

Concept: Content Homie in a reference-matched mid-Dougie chest-brush pose with one low hand sweeping at the hip.

Required action: White tee, black pants, fixed chest-brush forearm and clean low-hand elbow sweep read as the Dougie; face, shirt, shoulders and legs remain locked.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/dougie-ing-content-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/dougie-ing-content-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/pop-dance-reference-rebuilds/qa-pass-1/contacts/dougie-ing-content-gif-128.png`

Failures: `STATIONARY_REGION_DRIFT:locked-face-shirt-chest-brush`, `VISUAL_REVIEW_REQUIRED`

Warnings: none

Manual notes: (none)

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 64px | 46063px | 1 (1/0) | none |
| 1 | 64px | 46187px | 1 (1/0) | none |
| 2 | 64px | 46175px | 1 (1/0) | none |
| 3 | 64px | 46164px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 1.9366% | 7.0px | 0.343px | 0.0px | 3.2764% | 1.0 |
| 1→2 | 3.4935% | 11.0px | 0.303px | 0.0px | 4.387% | 1.0 |
| 2→3 | 2.2635% | 7.225px | 0.217px | 0.0px | 3.3042% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-face-shirt-chest-brush | 1.8379% | 0.05% |
