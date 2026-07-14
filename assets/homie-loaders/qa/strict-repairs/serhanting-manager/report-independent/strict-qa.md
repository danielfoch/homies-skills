# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `serhanting-manager` | PASS | 76px | 0.0px | 0.0% | 5.1192% | recorded: pass |

## serhanting-manager — PASS

Concept: Canonical Manager Homie holds one coherent jacket-buttoning pose while two locked hand rigs squeeze and reset around the same button.

Required action: At full size and 128px, read hands fastening and releasing the centre button; face, torso, lapels, tie, pinstripes, crop, and scale stay fixed.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/serhanting-manager/report-independent/contacts/serhanting-manager-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/serhanting-manager/report-independent/contacts/serhanting-manager-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/serhanting-manager/report-independent/contacts/serhanting-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent review of the 1254px source contact, all four full-size cells, all four 128px cells, and the decoded six-frame 128px GIF contact. At 128px the two hands visibly progress from separated at the jacket fronts, through approach, to contact at the same centre button, with the click phase reinforcing fastening before the reversible reset. The male Manager identity, medium-blue pinstripe jacket, pink tie, lapels, face, torso, crop, and scale remain locked; the pinstripes remain legible at 128px. No hand fusion outside the contact phase, stray ray, redraw drift, crop fault, or green debris is visible.

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
