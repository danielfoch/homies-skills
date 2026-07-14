# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `jon-snowing-marketing` | FAIL | 65px | 8.062px | 2.1157% | 3.0347% | pending |

## jon-snowing-marketing — FAIL

Concept: (not supplied)

Required action: (not supplied)

Full-size contact: `qa/strict-repairs/jon-snowing-marketing/report-preflight/contacts/jon-snowing-marketing-source-full.png`

128px contact: `qa/strict-repairs/jon-snowing-marketing/report-preflight/contacts/jon-snowing-marketing-source-128.png`

GIF contact: `qa/strict-repairs/jon-snowing-marketing/report-preflight/contacts/jon-snowing-marketing-gif-128.png`

Failures: `VISUAL_REVIEW_REQUIRED`

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: (none)

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 86237px | 7 (7/0) | none |
| 1 | 71px | 86237px | 7 (7/0) | none |
| 2 | 71px | 86237px | 7 (7/0) | none |
| 3 | 69px | 86237px | 7 (7/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.1157% | 8.062px | 0.155px | 0.0px | 3.0324% | 1.0 |
| 1→2 | 2.1157% | 8.062px | 0.155px | 0.0px | 3.0347% | 1.0 |
| 2→3 | 2.1157% | 8.062px | 0.155px | 0.0px | 3.0209% | 1.0 |
