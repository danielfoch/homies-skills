# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `step-brothering-manager-crm` | PASS | 60px | 15.716px | 0.8865% | 1.6154% | recorded: pass |

## step-brothering-manager-crm — PASS

Concept: Manager and CRM Homies recreate the awkward two-brother studio portrait while a camera flash pulses beside them.

Required action: The two male Homies, their two stacked shoulder hands, blue shirts, complementary argyle vests and portrait frame stay perfectly fixed while only the upper-right camera flash changes size.

Full-size contact: `qa/strict-repairs/step-brothering-manager-crm/report-production/contacts/step-brothering-manager-crm-source-full.png`

128px contact: `qa/strict-repairs/step-brothering-manager-crm/report-production/contacts/step-brothering-manager-crm-source-128.png`

GIF contact: `qa/strict-repairs/step-brothering-manager-crm/report-production/contacts/step-brothering-manager-crm-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent full-size, 128px and decoded-GIF inspection confirms two canonical male Homies, exactly two clean stacked Manager hands, correct blue shirts and contrasting argyle vests, a deliberate frame-masked crop, transparent corners and no redraw wiggle, debris, duplicate anatomy, palette shimmer or loop discontinuity.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 149125px | 2 (2/0) | none |
| 1 | 60px | 149864px | 3 (2/0) | none |
| 2 | 60px | 150893px | 3 (3/0) | none |
| 3 | 60px | 150088px | 3 (2/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.6355% | 15.716px | 1.441px | 0.0px | 1.0295% | 1.0 |
| 1→2 | 0.8865% | 13.42px | 1.938px | 0.0px | 1.6154% | 1.0 |
| 2→3 | 0.6907% | 11.636px | 1.516px | 0.0px | 1.4555% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-two-homie-faces-hands-and-argyle | 0.0% | 0.0% |
| locked-portrait-bottom-rail | 0.0% | 0.0% |
