# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `robin-hooding-manager` | FAIL | 70px | 1.0px | 0.1619% | 3.0973% | pending |

## robin-hooding-manager — FAIL

Concept: (not supplied)

Required action: (not supplied)

Full-size contact: `qa/strict-repairs/robin-hooding-manager/report-preflight/contacts/robin-hooding-manager-source-full.png`

128px contact: `qa/strict-repairs/robin-hooding-manager/report-preflight/contacts/robin-hooding-manager-source-128.png`

GIF contact: `qa/strict-repairs/robin-hooding-manager/report-preflight/contacts/robin-hooding-manager-gif-128.png`

Failures: `VISUAL_REVIEW_REQUIRED`

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: (none)

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 70px | 36394px | 1 (1/0) | none |
| 1 | 70px | 36453px | 1 (1/0) | none |
| 2 | 70px | 36468px | 1 (1/0) | none |
| 3 | 70px | 36516px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.1619% | 1.0px | 0.257px | 0.0px | 1.9285% | 0.991 |
| 1→2 | 0.0411% | 1.0px | 0.041px | 0.0px | 1.7001% | 0.9819 |
| 2→3 | 0.1314% | 1.0px | 0.132px | 0.0px | 3.0973% | 0.9715 |
