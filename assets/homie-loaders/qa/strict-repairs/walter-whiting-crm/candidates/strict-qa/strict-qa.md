# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `walter-whiting-crm` | PASS | 74px | 0.0px | 0.0% | 0.5174% | recorded: pass |

## walter-whiting-crm — PASS

Concept: One canonical dark-skinned bald male CRM Homie broods in a yellow hazmat suit with glasses, a respirator at his neck, and exactly one briefcase.

Required action: The CRM identity, face, body, hands, hazmat suit, respirator geometry, and single briefcase remain pixel-locked while only a glasses glint and respirator-filter highlight pulse locally.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/walter-whiting-crm/candidates/strict-qa/contacts/walter-whiting-crm-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/walter-whiting-crm/candidates/strict-qa/contacts/walter-whiting-crm-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/walter-whiting-crm/candidates/strict-qa/contacts/walter-whiting-crm-gif-128.png`

Failures: none

Warnings: none

Manual notes: Inspected the corrected full-size four-cell contact, 128px four-cell contact, and six-phase GIF contact. The canonical dark-skinned bald male CRM identity remains clear; one pair of glasses, one neck respirator, exactly one briefcase, two connected hands, and two legs remain continuous. The body, face, suit, briefcase, crop, scale, and anchor are static while only the masked glasses/filter highlights change. No cardboard tilt, AI redraw, extra equipment, text, glyphs, or debris is present.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 74px | 52381px | 1 (1/0) | none |
| 1 | 74px | 52381px | 1 (1/0) | none |
| 2 | 74px | 52381px | 1 (1/0) | none |
| 3 | 74px | 52381px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.0% | 0.0px | 0.0px | 0.0px | 0.2921% | 0.9844 |
| 1→2 | 0.0% | 0.0px | 0.0px | 0.0px | 0.5174% | 0.9653 |
| 2→3 | 0.0% | 0.0px | 0.0px | 0.0px | 0.5135% | 0.9654 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| empty-transparent-canvas-corner | 0.0% | 0.0% |
| locked-body-hands-suit-and-briefcase | 0.0% | 0.0% |
