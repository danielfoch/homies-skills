# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `david-blaining-manager` | PASS | 65px | 5.385px | 0.7619% | 1.4216% | recorded: pass |
| `cranking-that-marketing` | PASS | 65px | 9.849px | 4.9062% | 13.1596% | recorded: pass |
| `cranking-the-step-marketing` | PASS | 65px | 4.123px | 0.4761% | 5.9271% | recorded: pass |
| `cranking-the-motorbike-marketing` | PASS | 65px | 6.84px | 0.3952% | 5.368% | recorded: pass |

## david-blaining-manager — PASS

Concept: A male canonical Manager Homie in an all-black street-magician outfit makes a visible arc of playing cards fly between his deck and open hand.

Required action: The same complete Manager body, deck, hands and five inner cards stay locked while the detached outer card travels outward and upward through a controlled arc.

Full-size contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/david-blaining-manager-source-full.png`

128px contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/david-blaining-manager-source-128.png`

GIF contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/david-blaining-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent full-cell and decoded-GIF inspection confirms one male Manager, one deck, six visible flying cards, and one controlled outer-card arc; no anatomy, crop, scale, or palette defect.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 46808px | 2 (2/0) | none |
| 1 | 65px | 46810px | 2 (2/0) | none |
| 2 | 65px | 46808px | 2 (2/0) | none |
| 3 | 65px | 46806px | 2 (2/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.6261% | 4.472px | 0.076px | 0.0px | 1.3012% | 1.0 |
| 1→2 | 0.7619% | 5.385px | 0.078px | 0.0px | 1.4216% | 1.0 |
| 2→3 | 0.6389% | 4.123px | 0.075px | 0.0px | 1.2927% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-manager-face-torso-deck-and-inner-card-arc | 0.0% | 0.0% |
| fixed-manager-legs-and-shoes | 0.0% | 0.0% |

## cranking-that-marketing — PASS

Concept: The male canonical Marketing Homie wears the supplied white graffiti jacket and black/yellow Crank That wardrobe while holding the recognizable Superman balance pose.

Required action: Both complete sleeve-arm-hand units sweep in opposite directions around fixed shoulders while the face, cap, wraparound shades, jacket core, red shirt, planted leg and raised rear leg remain locked.

Full-size contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/cranking-that-marketing-source-full.png`

128px contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/cranking-that-marketing-source-128.png`

GIF contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/cranking-that-marketing-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent inspection confirms the requested white graffiti jacket/red shirt/sideways cap/white shades/black-gold trousers and the wide Superman balance pose, with two complete hands and fixed legs.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 83272px | 1 (1/0) | none |
| 1 | 65px | 82836px | 1 (1/0) | none |
| 2 | 65px | 82346px | 1 (1/0) | none |
| 3 | 65px | 82474px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 3.2362% | 5.831px | 0.981px | 0.0px | 10.3577% | 0.9685 |
| 1→2 | 4.9062% | 9.849px | 1.61px | 0.0px | 13.1596% | 0.9531 |
| 2→3 | 3.4066% | 5.657px | 0.754px | 0.0px | 10.6455% | 0.968 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-marketing-cap-shades-and-face | 0.42% | 0.5% |
| fixed-planted-and-raised-legs | 0.0% | 0.0% |

## cranking-the-step-marketing — PASS

Concept: The male canonical Marketing Homie wears the supplied Crank That wardrobe in the crossed-foot small-hop step.

Required action: Two complete bent sleeve-arm-fist units pump around fixed shoulder joins while the cap, wraparound shades, face, jacket core, crossed legs and both shoes remain locked.

Full-size contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/cranking-the-step-marketing-source-full.png`

128px contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/cranking-the-step-marketing-source-128.png`

GIF contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/cranking-the-step-marketing-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent inspection confirms the same requested wardrobe and a distinct crossed-foot small-hop pose; both fists counter-pump with no body redraw or limb overlap.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 66937px | 1 (1/0) | none |
| 1 | 65px | 67008px | 1 (1/0) | none |
| 2 | 65px | 67106px | 1 (1/0) | none |
| 3 | 65px | 67039px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.2729% | 2.828px | 0.139px | 0.0px | 5.1593% | 0.9953 |
| 1→2 | 0.4761% | 4.123px | 0.195px | 0.0px | 5.9271% | 0.9962 |
| 2→3 | 0.3111% | 3.0px | 0.128px | 0.0px | 5.1089% | 0.9963 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-cap-shades-and-face | 0.0393% | 0.5% |
| fixed-crossed-leg-step | 0.0% | 0.0% |

## cranking-the-motorbike-marketing — PASS

Concept: The male canonical Marketing Homie wears the supplied Crank That wardrobe in the low motorcycle-rev dance step.

Required action: Both complete forearm-fist units counter-rotate around fixed elbows like revving handlebars while the head, jacket core, upper sleeves, bent knees, baggy pants and shoes remain locked.

Full-size contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/cranking-the-motorbike-marketing-source-full.png`

128px contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/cranking-the-motorbike-marketing-source-128.png`

GIF contact: `qa/strict-repairs/new-pop-dance-additions/report-independent-root/contacts/cranking-the-motorbike-marketing-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent inspection confirms a third distinct low motorbike-rev pose in the same wardrobe; both fists remain connected, the bent-knee stance stays fixed, and there is no crop or scale pumping.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 73688px | 1 (1/0) | none |
| 1 | 65px | 73688px | 1 (1/0) | none |
| 2 | 65px | 73784px | 1 (1/0) | none |
| 3 | 65px | 73732px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.3171% | 4.0px | 0.044px | 0.0px | 4.6569% | 0.9971 |
| 1→2 | 0.3952% | 6.84px | 0.173px | 0.0px | 5.368% | 0.9951 |
| 2→3 | 0.2167% | 4.006px | 0.091px | 0.0px | 4.5546% | 0.9962 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-cap-shades-and-face | 0.0% | 0.0% |
| fixed-bent-knee-stance | 0.0% | 0.0% |
