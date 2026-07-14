# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `hormozing-manager` | PASS | 84px | 0.0px | 0.0% | 1.1825% | recorded: pass |

## hormozing-manager — PASS

Concept: A locked male Manager Homie styled as a brand-free Hormozi homage points to one navy $100M business book while three value bars stack and a tiny gold glint lands.

Required action: At full size and 128px, the fixed pointing pose and exact $100M title remain readable while three value bars visibly stack inside the same book; face, cap, glasses, nasal strip, beard, body, both arms and hands, book geometry, crop, scale, and silhouette remain byte-locked.

Full-size contact: `qa/strict-repairs/hormozing-manager/candidates/report-final/contacts/hormozing-manager-source-full.png`

128px contact: `qa/strict-repairs/hormozing-manager/candidates/report-final/contacts/hormozing-manager-source-128.png`

GIF contact: `qa/strict-repairs/hormozing-manager/candidates/report-final/contacts/hormozing-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Root review inspected the full 1254px source contact, every 627px cell, the four-cell 128px contact, and the decoded six-frame 128px GIF contact. Exactly one male Manager appears in every phase with one head, two connected arms, two attached five-finger hands, one stable navy book, one fixed left-hand grip, and one fixed pointing gesture. The backward blue cap, clear glasses, white nasal strip, thick beard, white sleeveless shirt, watch, face, anatomy, book edges, $100M title, crop, scale, and silhouette are locked. The three value bars stack clearly inside the same book and reverse cleanly; only the final phase adds one tiny book-clipped gold glint. No extra hand, duplicate character, changing text, green debris, crop fault, scale pulse, registration drift, palette spill, redraw wiggle, or continuity break is visible.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 84px | 102072px | 1 (1/0) | none |
| 1 | 84px | 102072px | 1 (1/0) | none |
| 2 | 84px | 102072px | 1 (1/0) | none |
| 3 | 84px | 102072px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.0% | 0.0px | 0.0px | 0.0px | 1.16% | 1.0 |
| 1→2 | 0.0% | 0.0px | 0.0px | 0.0px | 1.158% | 1.0 |
| 2→3 | 0.0% | 0.0px | 0.0px | 0.0px | 1.1825% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-cap-face-glasses-strip-and-beard | 0.0% | 0.0% |
| locked-pointing-hand-and-upper-torso | 0.0% | 0.0% |
| locked-lower-torso-book-grip-and-watch | 0.0% | 0.0% |
