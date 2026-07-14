# Movie Night new batch A — QA ledger

Eight new affectionate cinematic-archetype Homie loaders were generated with the built-in image tool, one call per asset and exactly one identity/style reference per call. Every accepted raw output was chroma-extracted with the installed imagegen helper before deterministic canonicalization. No CLI image-generation fallback was used.

## Deterministic anti-wiggle construction

- `paddingtoning-manager`: one frame-0 character plate is canonical. Only the same red hat pixels rotate through `0, -0.8, -1.6, -2.4` degrees about one fixed pivot; all body, coat, hand, toggles, legs, shoes, face, and camera pixels are fixed.
- `peter-panning-listings`: one complete frame-0 character is a rigid unit translated vertically by `0, -3, -6, -8` source pixels. No internal pixels articulate or redraw.
- `tinkerbelling-content`: one frame-0 body/costume plate is canonical. The complete visible wing silhouettes, including their same ink outlines and veins, rotate symmetrically through `0, 3, 6, 9` degrees; one locally drawn opaque four-point sparkle follows a short arc. The body is composited above the wing roots on every frame. A second visual pass removed the initial retained-wing-outline arcs.
- `baymaxing-manager`: one frame-0 body/shell plate is canonical. The same raised arm and five-finger hand rotate through `0, 2, 4, 6` degrees around one fixed shoulder with a protected overlap; all other anatomy and costume pixels are fixed.
- `wall-e-ing-research`: one frame-0 robot/body plate is canonical. The same eye housing compresses horizontally `1.00, 0.96, 0.92, 0.92`; frame 3 squashes the same housing vertically to `0.42` while preserving its bottom contact with the fixed stalk. The body, treads, face, arms, and camera are fixed.
- `marioing-offers`: one complete frame-0 character is a rigid unit translated vertically by `0, -3, -6, -8` source pixels. No internal pixels articulate or redraw.
- `marty-mcflying-manager`: one authored watch-check pose is canonical. The same head/hair patch translates by `0, -1, -2, -3` pixels while the watch, lifted forearm, vest, denim jacket, shirt, lower body, and camera remain fixed. A trial widened-eye overlay was rejected and removed because it read too strongly at loader size.
- `doc-browning-research`: one frame-0 body/hair/coat plate is canonical. The same two-lens goggle assembly translates down by `0, 6, 12, 18` source pixels; the pixels beneath its start position were deterministically nearest-filled while still covered by the moving assembly. A first 28-pixel endpoint was rejected as too low and reduced before acceptance.

All eight frames were uniformly center-scaled to `82%` after motion construction. This guarantees at least 60 source pixels of non-key clearance in every 627 × 627 cell.

## Source validation

Every final master is:

- exact `1254 × 1254`, RGB, four exact `627 × 627` cells;
- mathematical RGB `(0,255,0)` on the full outer field, all four corners, and both center axes;
- free of panel borders, gutters, captions, logos, emblems, readable text, signatures, and watermarks;
- visually inspected at full sheet and individual-frame scale for crop, floating residue, extra/missing hands, switched props, costume morphs, and discontinuities.

Minimum non-key clearances, measured from the authored RGBA frame bounds before recomposition:

| Source | Minimum clearance |
|---|---:|
| `paddingtoning-manager` | 76 px |
| `peter-panning-listings` | 90 px |
| `tinkerbelling-content` | 82 px |
| `baymaxing-manager` | 81 px |
| `wall-e-ing-research` | 76 px |
| `marioing-offers` | 80 px |
| `marty-mcflying-manager` | 74 px |
| `doc-browning-research` | 62 px |

Final source SHA-256 values:

- `paddingtoning-manager.png` — `61a0d051ed222736b41412cf0a44a7fcd8724a5c947afb4ff2bd44cad43a89ca`
- `peter-panning-listings.png` — `67b99ab9eb5028769a83ac185b97d6760c00e9d63fbfd8d3c2058f4a3628b1c8`
- `tinkerbelling-content.png` — `6e2f7707e5b63197c7dbd432ba4a5983291268c2bde1e9c9e5821d59979ba899`
- `baymaxing-manager.png` — `3edbdbeed1b017177b7b86c63bc3456c6e0d381b427f0d0dc8417ac0fcb83560`
- `wall-e-ing-research.png` — `dc6734e3b42791fde464c458f3dd9975940de8d21726b06152771d05699f7e04`
- `marioing-offers.png` — `50c4f0f594df5fc36ed12358c916a1b14b003a9a730e8d53a85425685964c9c6`
- `marty-mcflying-manager.png` — `4f613ae2431280b3f0b5c04d7cdedca670ba0b0deed11404d32a0e6cea8890d3`
- `doc-browning-research.png` — `9d02c7f7aa00646849486a2fd9a53ab88267948ad3e857efbea4006582cb65b5`

## Transparent loop validation

Temporary loops were assembled from the final green masters with the production `scripts/assemble_sprite.py` path at `320 × 320`, 96 colors. All eight loops report:

- exactly six GIF frames in sequence `0,1,2,3,2,1`;
- durations `210,140,140,210,140,140` ms;
- infinite loop (`loop=0`) and disposal method 2;
- transparent alpha at all four corners of every frame;
- no terminal/result frame; frame 3 is only the reversible motion endpoint.

Temporary artifacts:

- GIFs: `/tmp/movie-new-a/gifs/*.gif`
- per-asset four-frame contacts: `/tmp/movie-new-a/contact/*.png`
- individual accepted RGBA frames: `/tmp/movie-new-a/qa/*-frame-*.png`
- processing hashes and bounds: `/tmp/movie-new-a/processing.json`

Visual result: all eight loops passed the final de-wiggle review. Motion is confined to the intended hat, rigid vertical float/hop, wings/sparkle, waving arm, robot eye housing, head glance, or goggles; fixed silhouette layers do not redraw between frames.
