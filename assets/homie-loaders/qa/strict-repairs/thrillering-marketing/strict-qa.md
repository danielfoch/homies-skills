# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `thrillering-marketing` | PASS | 60px | 74.041px | 42.5794% | 78.1497% | recorded: pass |

## thrillering-marketing — PASS

Concept: (not supplied)

Required action: (not supplied)

Full-size contact: `/tmp/thrillering-marketing-claw/strict-final/contacts/thrillering-marketing-source-full.png`

128px contact: `/tmp/thrillering-marketing-claw/strict-final/contacts/thrillering-marketing-source-128.png`

GIF contact: `/tmp/thrillering-marketing-claw/strict-final/contacts/thrillering-marketing-gif-128.png`

Failures: none

Warnings: `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px contacts inspected. All four cells have one intact character, two connected arms/hands and two connected legs/feet, no crop or debris. The scale warning is expected articulated silhouette change. Integer registration fixes one shoe baseline while the body performs the intended side-to-side crouch and arm sweep.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 62px | 70782px | 1 (1/0) | none |
| 1 | 67px | 63283px | 1 (1/0) | none |
| 2 | 60px | 70016px | 1 (1/0) | none |
| 3 | 67px | 62791px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 40.0122% | 73.824px | 22.683px | 4.472px | 78.1066% | 0.225 |
| 1→2 | 42.5794% | 74.041px | 21.778px | 15.0px | 78.1497% | 0.3687 |
| 2→3 | 39.2089% | 73.741px | 20.585px | 4.123px | 77.3047% | 0.3027 |
