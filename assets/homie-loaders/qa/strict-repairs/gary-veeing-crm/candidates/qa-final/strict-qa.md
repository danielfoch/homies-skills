# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `gary-veeing-crm` | PASS | 83px | 2.236px | 1.6745% | 6.9925% | recorded: pass |

## gary-veeing-crm — PASS

Concept: Canonical male CRM Homie holds both open hands wide around shoulder/head height while two locked arm rigs make a restrained reversible speaker emphasis.

Required action: At full size and 128px, read two coherent raised open hands around shoulder/head height on the male CRM identity, with stable face, beanie, torso, crop, and scale.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/qa-final/contacts/gary-veeing-crm-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/qa-final/contacts/gary-veeing-crm-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/qa-final/contacts/gary-veeing-crm-gif-128.png`

Failures: none

Warnings: none

Manual notes: Inspected refreshed full, 128px, and GIF contacts after switching to the reference-faithful shoulder-height locked panel. Both five-finger hands remain coherent, the male CRM identity and navy-shirt silhouette stay fixed, and the restrained reversible speaker emphasis remains readable without crop or redraw wiggle.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 83px | 70233px | 1 (1/0) | none |
| 1 | 83px | 70354px | 1 (1/0) | none |
| 2 | 83px | 70467px | 1 (1/0) | none |
| 3 | 83px | 70552px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 1.5625% | 2.0px | 0.195px | 0.0px | 6.6284% | 1.0 |
| 1→2 | 1.6745% | 2.236px | 0.306px | 0.0px | 6.9925% | 1.0 |
| 2→3 | 1.5326% | 2.0px | 0.231px | 0.0px | 6.7104% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-male-face | 0.0% | 0.1% |
| locked-shirt-core | 0.0% | 0.1% |
