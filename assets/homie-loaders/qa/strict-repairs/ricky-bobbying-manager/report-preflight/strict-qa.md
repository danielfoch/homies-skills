# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `ricky-bobbying-manager` | FAIL | 60px | 1.0px | 0.0011% | 0.6473% | pending |

## ricky-bobbying-manager — FAIL

Concept: (not supplied)

Required action: (not supplied)

Full-size contact: `qa/strict-repairs/ricky-bobbying-manager/report-preflight/contacts/ricky-bobbying-manager-source-full.png`

128px contact: `qa/strict-repairs/ricky-bobbying-manager/report-preflight/contacts/ricky-bobbying-manager-source-128.png`

GIF contact: `qa/strict-repairs/ricky-bobbying-manager/report-preflight/contacts/ricky-bobbying-manager-gif-128.png`

Failures: `VISUAL_REVIEW_REQUIRED`

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: (none)

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 87746px | 1 (1/0) | none |
| 1 | 60px | 87747px | 1 (1/0) | none |
| 2 | 60px | 87747px | 1 (1/0) | none |
| 3 | 60px | 87747px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.0011% | 1.0px | 0.003px | 0.0px | 0.294% | 0.9911 |
| 1→2 | 0.0% | 0.0px | 0.0px | 0.0px | 0.5835% | 0.9954 |
| 2→3 | 0.0% | 0.0px | 0.0px | 0.0px | 0.6473% | 0.9985 |
