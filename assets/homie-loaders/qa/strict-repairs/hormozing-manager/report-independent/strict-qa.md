# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `hormozing-manager` | PASS | 84px | 0.0px | 0.0% | 1.1825% | recorded: pass |

## hormozing-manager — PASS

Concept: A locked male Manager Homie styled as a brand-free Hormozi homage points to one navy $100M business book while three value bars stack and a tiny gold glint lands.

Required action: At full size and 128px, the fixed pointing pose and exact $100M title remain readable while three value bars visibly stack inside the same book; face, cap, glasses, nasal strip, beard, body, both arms and hands, book geometry, crop, scale, and silhouette remain byte-locked.

Full-size contact: `qa/strict-repairs/hormozing-manager/report-independent/contacts/hormozing-manager-source-full.png`

128px contact: `qa/strict-repairs/hormozing-manager/report-independent/contacts/hormozing-manager-source-128.png`

GIF contact: `qa/strict-repairs/hormozing-manager/report-independent/contacts/hormozing-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent review inspected the full 1254px production source, each of its four 627px cells, the four-cell 128px contact, every decoded 256px GIF frame, and the six-frame 128px GIF contact. Every phase contains exactly one male character, one head, one backward royal-blue cap, one pair of clear glasses, one white nasal strip, one beard, one white sleeveless shirt, two connected arms, two attached hands, and one unchanged navy book. The exact $100M title remains static and readable at 128px. The three bars stack only inside the locked book, and the final gold glint remains book-clipped. No wiggle, scale pulse, crop fault, green debris, extra limb, duplicate character, text change, prop morph, palette spill, registration drift, or continuity issue is visible.

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
