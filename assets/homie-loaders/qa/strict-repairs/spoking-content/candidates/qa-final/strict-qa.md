# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `spoking-content` | PASS | 86px | 4.0px | 2.0569% | 7.7987% | recorded: pass |

## spoking-content — PASS

Concept: Canonical Content Homie holds one anatomically correct five-finger split salute while one locked arm rig makes a restrained reversible motion.

Required action: At full size and 128px, read a clear 2+2 finger grouping with thumb out; the same hand, face, torso, uniform, crop, and scale persist through the loop.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/qa-final/contacts/spoking-content-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/qa-final/contacts/spoking-content-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/qa-final/contacts/spoking-content-gif-128.png`

Failures: none

Warnings: none

Manual notes: Inspected full, 128px, and GIF contacts. The same anatomically correct hand is used in all phases; face, torso, uniform, crop, and scale are locked.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 86px | 90841px | 1 (1/0) | none |
| 1 | 86px | 90750px | 1 (1/0) | none |
| 2 | 86px | 90659px | 1 (1/0) | none |
| 3 | 86px | 90579px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.0569% | 4.0px | 0.336px | 0.0px | 7.7404% | 0.975 |
| 1→2 | 2.0482% | 4.0px | 0.32px | 0.0px | 7.7987% | 0.9771 |
| 2→3 | 2.0468% | 4.0px | 0.322px | 0.0px | 7.7985% | 0.9847 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-face | 0.0% | 0.1% |
| locked-torso | 0.0% | 0.1% |
