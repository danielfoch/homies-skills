# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `ricky-bobbying-manager` | PASS | 60px | 1.0px | 0.0011% | 0.6473% | recorded: pass |

## ricky-bobbying-manager — PASS

Concept: A male Manager Homie in a brand-free Homies stock-car suit hoists a giant silver victory trophy while a highlight sweeps across the cup.

Required action: The iconic trophy-hoisting pose, two connected hands, Manager face, racing suit, trophy geometry and checkered finish rail remain locked while only the trophy-surface glint travels.

Full-size contact: `qa/strict-repairs/ricky-bobbying-manager/report-root/contacts/ricky-bobbying-manager-source-full.png`

128px contact: `qa/strict-repairs/ricky-bobbying-manager/report-root/contacts/ricky-bobbying-manager-source-128.png`

GIF contact: `qa/strict-repairs/ricky-bobbying-manager/report-root/contacts/ricky-bobbying-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Root full-size and 128px inspection confirms one canonical male Manager, exactly two clean connected hands, one trophy, a cream/blue/coral Homies racing suit with no real sponsor branding, an intentional finish-rail crop, and no redraw wiggle, debris, duplicate anatomy or palette-wide shimmer.

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

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-manager-face-hands-suit-and-trophy-base | 0.0% | 0.0% |
| locked-checkered-finish-rail | 0.0% | 0.0% |
