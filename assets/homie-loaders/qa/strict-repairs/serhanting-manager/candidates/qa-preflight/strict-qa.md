# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `serhanting-manager` | PASS | 76px | 0.0px | 0.0% | 5.1192% | recorded: pass |

## serhanting-manager — PASS

Concept: Canonical Manager Homie holds one coherent jacket-buttoning pose while two locked hand rigs squeeze and reset around the same button.

Required action: At full size and 128px, read hands fastening and releasing the centre button; face, torso, lapels, tie, pinstripes, crop, and scale stay fixed.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/qa-preflight/contacts/serhanting-manager-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/qa-preflight/contacts/serhanting-manager-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/qa-preflight/contacts/serhanting-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Inspected refreshed full, 128px, and GIF contacts. The four phases read as hands separated, approach, meet, and press; the restrained click rays appear only at the press. Face, torso, lapels, tie, pinstripe pattern, crop, and scale remain locked.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 76px | 99644px | 1 (1/0) | none |
| 1 | 76px | 99644px | 1 (1/0) | none |
| 2 | 76px | 99644px | 1 (1/0) | none |
| 3 | 76px | 99644px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.0% | 0.0px | 0.0px | 0.0px | 5.1192% | 1.0 |
| 1→2 | 0.0% | 0.0px | 0.0px | 0.0px | 4.3083% | 1.0 |
| 2→3 | 0.0% | 0.0px | 0.0px | 0.0px | 2.7207% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-face | 0.0% | 0.1% |
| locked-tie-lapels | 0.0% | 0.1% |
