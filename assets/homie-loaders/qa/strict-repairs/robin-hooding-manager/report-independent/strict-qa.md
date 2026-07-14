# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `robin-hooding-manager` | PASS | 70px | 2.828px | 1.9842% | 5.7368% | recorded: pass |

## robin-hooding-manager — PASS

Concept: Canonical Manager Homie as a muted red-and-olive forest outlaw at full draw

Required action: Across four authored phases, the nock and its one connected arrow retreat 15px toward the cheek while both string ends stay fixed to the immutable bow tips; the arrowhead travels with the shaft and the shared burgundy, olive, and tan character plate remains fixed.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/report-independent/contacts/robin-hooding-manager-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/report-independent/contacts/robin-hooding-manager-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/report-independent/contacts/robin-hooding-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: PASS after an independent re-audit of the corrected candidate. I inspected the full 1254px source contact, all four original 627px cells, every 128px cell, the string-erased matte base, and all six decoded GIF phases. The same canonical male Manager and frame-shared burgundy, olive, and tan outfit persist throughout. The generated old string is absent from the erased base, including zero residual alpha pixels along its open-space path. Every final phase has exactly one continuous V-shaped string meeting at one nock, one connected arrow shaft with one fletching assembly and one arrowhead, and no doubled string or old-tip trace. The string endpoints remain fixed at the same top and bottom bow-tip coordinates while the nock and arrowhead translate together 15px toward the cheek; this is approximately 3.06 delivery pixels and is visibly progressive in the 128px cells. Bow geometry, bow hand, face, body, outfit, lower body, crop, anchor, and scale remain fixed. Direct comparison finds zero changes outside the saved single string/arrow rig mask. No geometry drift, crop fault, green debris, redraw, disconnected prop, or duplicate arrow is visible.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 70px | 36951px | 2 (1/1) | none |
| 1 | 70px | 36899px | 2 (1/1) | none |
| 2 | 70px | 36863px | 2 (1/1) | none |
| 3 | 70px | 36784px | 2 (1/1) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 1.9842% | 2.828px | 0.223px | 0.0px | 5.4592% | 0.894 |
| 1→2 | 1.795% | 2.828px | 0.207px | 0.0px | 5.5032% | 0.8811 |
| 2→3 | 1.7364% | 2.236px | 0.329px | 0.0px | 5.7368% | 0.8743 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked face core | 0.0% | 0.0% |
| locked bow hand and upper forearm | 0.0% | 0.0% |
| locked lower body and boots | 0.0% | 0.0% |
