# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `sky-walkering-manager` | PASS | 69px | 80.645px | 83.1185% | 57.5388% | recorded: pass |
| `hyah-ing-listings` | PASS | 81px | 163.369px | 86.0604% | 93.4364% | recorded: pass |
| `master-chiefing-reports` | PASS | 88px | 34.482px | 23.8734% | 69.2137% | recorded: pass |
| `dumbledoring-research` | PASS | 76px | 62.169px | 24.1795% | 53.2308% | recorded: pass |
| `inspector-gadgeting-crm` | PASS | 88px | 22.023px | 54.3467% | 44.2354% | recorded: pass |
| `cutting-red-tape-research` | PASS | 83px | 15.811px | 17.1984% | 42.912% | recorded: pass |
| `glengarrying-offers` | PASS | 81px | 24.607px | 37.7846% | 60.828% | recorded: pass |
| `buzz-lightyearing-manager` | PASS | 74px | 50.0px | 26.1187% | 50.1573% | recorded: pass |

## sky-walkering-manager — PASS

Concept: Black-clad space knight makes a wide connected energy-sword sweep

Required action: The sword arc and attached two-handed sweep must read immediately at 128px.

Full-size contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/sky-walkering-manager-source-full.png`

128px contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/sky-walkering-manager-source-128.png`

GIF contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/sky-walkering-manager-gif-128.png`

Failures: none

Warnings: `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Wide connected sweep reads at 128px; detached lower-frame blade fragment was removed before final reassembly.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 91px | 31025px | 2 (1/1) | none |
| 1 | 91px | 30548px | 2 (1/1) | none |
| 2 | 69px | 30339px | 1 (1/0) | none |
| 3 | 92px | 30319px | 2 (1/1) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 82.1772% | 55.317px | 47.564px | 51.0px | 43.3662% | 0.6039 |
| 1→2 | 21.3305% | 80.645px | 11.35px | 1.0px | 42.9323% | 0.4839 |
| 2→3 | 83.1185% | 53.0px | 39.274px | 49.01px | 57.5388% | 0.6787 |

## hyah-ing-listings — PASS

Concept: Green-clad fantasy hero executes a four-pose sword slash

Required action: The guard, rise, overhead and follow-through poses must form one readable slash at 128px.

Full-size contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/hyah-ing-listings-source-full.png`

128px contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/hyah-ing-listings-source-128.png`

GIF contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/hyah-ing-listings-gif-128.png`

Failures: none

Warnings: `FOREGROUND_AREA_JUMP`, `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: One sword and attached two-hand grip remain coherent across the large intentional body poses.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 116px | 40823px | 1 (1/0) | none |
| 1 | 85px | 47544px | 1 (1/0) | none |
| 2 | 81px | 44062px | 1 (1/0) | none |
| 3 | 81px | 51460px | 3 (1/2) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 86.0604% | 92.776px | 81.149px | 97.637px | 93.4364% | 0.0996 |
| 1→2 | 56.3944% | 68.68px | 15.999px | 22.627px | 92.3929% | -0.0496 |
| 2→3 | 65.8531% | 163.369px | 46.518px | 30.48px | 93.2804% | -0.0396 |

## master-chiefing-reports — PASS

Concept: Armoured supersoldier raises and presents one gold-visored helmet

Required action: The same helmet must visibly travel from waist to shoulder while the armour remains continuous.

Full-size contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/master-chiefing-reports-source-full.png`

128px contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/master-chiefing-reports-source-128.png`

GIF contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/master-chiefing-reports-gif-128.png`

Failures: none

Warnings: `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: The one gold-visored helmet lifts clearly while armour and face remain identifiable.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 88px | 42872px | 1 (1/0) | none |
| 1 | 88px | 43318px | 1 (1/0) | none |
| 2 | 92px | 44895px | 1 (1/0) | none |
| 3 | 90px | 44968px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 23.287% | 10.0px | 7.915px | 8.0px | 61.7702% | 0.8359 |
| 1→2 | 23.8734% | 34.482px | 13.161px | 4.0px | 69.2137% | 0.534 |
| 2→3 | 19.2728% | 7.0px | 5.735px | 7.0px | 52.5955% | 0.7494 |

## dumbledoring-research — PASS

Concept: Wise headmaster wizard conducts a broad wand flourish

Required action: The wand must rise through a broad attached-arm gesture to a compact tip spiral.

Full-size contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/dumbledoring-research-source-full.png`

128px contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/dumbledoring-research-source-128.png`

GIF contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/dumbledoring-research-gif-128.png`

Failures: none

Warnings: `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Broad wand flourish and tip spiral read clearly without detached hands or duplicate props.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 81px | 54012px | 1 (1/0) | none |
| 1 | 81px | 52843px | 1 (1/0) | none |
| 2 | 82px | 60788px | 1 (1/0) | none |
| 3 | 76px | 61992px | 15 (2/7) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 13.6434% | 17.72px | 4.186px | 6.083px | 42.8014% | 0.8535 |
| 1→2 | 24.1795% | 62.169px | 13.886px | 6.083px | 53.2308% | 0.8536 |
| 2→3 | 20.3053% | 39.925px | 11.556px | 7.0px | 35.2817% | 0.8106 |

## inspector-gadgeting-crm — PASS

Concept: Gadget detective deploys a hat rotor and lifts off

Required action: Rotor deployment and foot clearance must be obvious at 128px.

Full-size contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/inspector-gadgeting-crm-source-full.png`

128px contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/inspector-gadgeting-crm-source-128.png`

GIF contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/inspector-gadgeting-crm-gif-128.png`

Failures: none

Warnings: `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: One rotor deploys in stages and lifts the same rigid body with visible foot clearance.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 123px | 28205px | 1 (1/0) | none |
| 1 | 99px | 28903px | 1 (1/0) | none |
| 2 | 101px | 30261px | 1 (1/0) | none |
| 3 | 88px | 31898px | 4 (1/3) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 52.2011% | 19.698px | 21.231px | 21.0px | 23.0007% | 0.9497 |
| 1→2 | 53.1437% | 22.023px | 21.081px | 23.087px | 44.2354% | 0.7965 |
| 2→3 | 54.3467% | 21.0px | 26.691px | 23.259px | 41.6566% | 0.8137 |

## cutting-red-tape-research — PASS

Concept: Research Homie cuts a fixed ceremonial ribbon with giant scissors

Required action: The scissors must close through the ribbon and the fixed post-anchored ribbon ends must separate.

Full-size contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/cutting-red-tape-research-source-full.png`

128px contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/cutting-red-tape-research-source-128.png`

GIF contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/cutting-red-tape-research-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Scissors close at one hinge; two posts and body remain stable while ribbon ends separate.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 83px | 45506px | 1 (1/0) | none |
| 1 | 83px | 45513px | 1 (1/0) | none |
| 2 | 83px | 44844px | 1 (1/0) | none |
| 3 | 83px | 44653px | 3 (3/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 1.8785% | 3.0px | 0.242px | 0.0px | 18.3235% | 0.9786 |
| 1→2 | 17.1984% | 9.0px | 5.386px | 10.0px | 42.912% | 0.5007 |
| 2→3 | 6.7729% | 15.811px | 0.48px | 0.0px | 16.8405% | 0.9965 |

## glengarrying-offers — PASS

Concept: Sales speaker points emphatically at a stable ABC chalkboard

Required action: Neutral, point, open-hand pitch and forward jab must read around a stable readable board.

Full-size contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/glengarrying-offers-source-full.png`

128px contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/glengarrying-offers-source-128.png`

GIF contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/glengarrying-offers-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Frame zero was rebuilt to the same board-left/Homie-right layout; stray crop fragments removed; board text is exact.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 82px | 89764px | 2 (2/0) | none |
| 1 | 81px | 89364px | 1 (1/0) | none |
| 2 | 97px | 83470px | 2 (1/1) | none |
| 3 | 98px | 86055px | 2 (1/1) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 16.3091% | 17.0px | 5.403px | 3.162px | 43.582% | 0.5069 |
| 1→2 | 37.7846% | 23.259px | 16.01px | 25.495px | 60.828% | 0.0822 |
| 2→3 | 27.1952% | 24.607px | 4.508px | 4.123px | 55.7233% | 0.3947 |

## buzz-lightyearing-manager — PASS

Concept: Optimistic winged astronaut deploys one mechanical backpack

Required action: Two consistent wings must visibly progress from folded to fully deployed, ending with a connected fist lift.

Full-size contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/buzz-lightyearing-manager-source-full.png`

128px contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/buzz-lightyearing-manager-source-128.png`

GIF contact: `/tmp/movie-tier-a-root/strict-final-8/contacts/buzz-lightyearing-manager-gif-128.png`

Failures: none

Warnings: `FOREGROUND_AREA_JUMP`, `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: One symmetric backpack wing pair deploys in four clear stages; body, suit and face remain coherent at full size and 128px.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 84px | 44968px | 1 (1/0) | none |
| 1 | 83px | 47872px | 1 (1/0) | none |
| 2 | 84px | 52859px | 1 (1/0) | none |
| 3 | 74px | 61774px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 17.0027% | 40.299px | 6.661px | 4.0px | 38.4593% | 0.8174 |
| 1→2 | 18.6661% | 43.566px | 10.305px | 4.0px | 39.9883% | 0.9008 |
| 2→3 | 26.1187% | 50.0px | 15.032px | 4.0px | 50.1573% | 0.7144 |

