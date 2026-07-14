# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `ron-burgunding-cma` | PASS | 84px | 3.606px | 1.0761% | 10.0332% | recorded: pass |

## ron-burgunding-cma — PASS

Concept: Canonical CMA Homie holds one continuous raised tumbler while a single locked arm-and-glass rig makes a restrained reversible toast.

Required action: At full size and 128px, read one coherent amber tumbler toast with stable hand, moustache, face, burgundy suit, crop, and scale.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/qa-final/contacts/ron-burgunding-cma-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/qa-final/contacts/ron-burgunding-cma-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/qa-final/contacts/ron-burgunding-cma-gif-128.png`

Failures: none

Warnings: none

Manual notes: Inspected full, 128px, and GIF contacts. Tumbler, grip, moustache, face, burgundy suit, crop, and scale remain coherent and locked.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 84px | 94043px | 1 (1/0) | none |
| 1 | 84px | 94143px | 1 (1/0) | none |
| 2 | 84px | 94222px | 1 (1/0) | none |
| 3 | 84px | 94328px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.933% | 3.606px | 0.019px | 0.0px | 9.7415% | 0.943 |
| 1→2 | 0.9963% | 3.606px | 0.037px | 0.0px | 9.8834% | 0.937 |
| 2→3 | 1.0761% | 3.606px | 0.001px | 0.0px | 10.0332% | 0.9372 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-face | 0.0% | 0.1% |
| locked-suit-core | 0.0% | 0.1% |
