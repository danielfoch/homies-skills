# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `step-brothering-manager-crm` | FAIL | 60px | 15.716px | 0.8865% | 1.6154% | pending |

## step-brothering-manager-crm — FAIL

Concept: (not supplied)

Required action: (not supplied)

Full-size contact: `qa/strict-repairs/step-brothering-manager-crm/report-preflight/contacts/step-brothering-manager-crm-source-full.png`

128px contact: `qa/strict-repairs/step-brothering-manager-crm/report-preflight/contacts/step-brothering-manager-crm-source-128.png`

GIF contact: `qa/strict-repairs/step-brothering-manager-crm/report-preflight/contacts/step-brothering-manager-crm-gif-128.png`

Failures: `VISUAL_REVIEW_REQUIRED`

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: (none)

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
