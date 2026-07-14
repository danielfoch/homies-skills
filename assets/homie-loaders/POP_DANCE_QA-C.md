# Pop & Dance batch C — QA handoff

> Historical generation/structural record. The final motion-semantic authority is `POP_DANCE_QA-SEMANTIC-REBUILD-2026-07-12.md`.


Status: **PASS — 10/10 masters and 10/10 temp GIFs**.

## Deliverables

- Project masters: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/`
- Temp GIFs: `/tmp/pop-dance-c/gifs/`
- Exact prompts: `/tmp/pop-dance-c-prompts.md`
- Alignment entries: `/tmp/pop-dance-c-alignment.json`
- 128 px playback strips: `/tmp/pop-dance-c/contact/final-gif-strips-128.jpg`
- 256 px authored cells: `/tmp/pop-dance-c/contact/final-authored-256-1.jpg`, `/tmp/pop-dance-c/contact/final-authored-256-2.jpg`
- Restored Disco strip: `/tmp/pop-dance-c/contact/disco-inferno-ing-reports-restored-strip.jpg`

## Structural checks

Every master is exact 1254×1254 RGB, strict 2×2 with exact #00ff00 outer edges and both center axes, four byte-distinct authored cells, and at least 60 px cell clearance. Every GIF is 256×256, transparent at all four corners, loops forever, has six frames in sequence 0,1,2,3,2,1, uses durations 210/140/140/210/140/140 ms, and exposes four distinct visual phases.

| Asset | Source SHA-256 | GIF SHA-256 | Min margin | Source bytes | GIF bytes |
|---|---|---|---:|---:|---:|
| macarena-ing-manager | `f6cb10d94a7a0494ccf95c4f2874521cb0d5a09ea069acada6bd775f6d7a0d42` | `d316ae46ab0c217d849dee6ef3228d195c3cf67d2dbb090be72477d61887d198` | 77px | 298235 | 43476 |
| ymca-ing-cma | `a85813815d6878a53824385acad7a1623695224086025f9c34466cd0219ac5f9` | `4bc535f3d2e45227f323e7021efc994e8347500c2866cfc92357e2175608c3d9` | 77px | 302293 | 45395 |
| cupid-shuffling-crm | `b8f0f7ec27d12a611f005d83a3b01bfc87516a8cc73002b57c2b91d52a6d76ce` | `fb9215d4dc4e1f84359b435189f177ce2893d5688598093a7e593f75c9687ca7` | 77px | 169612 | 40213 |
| cha-cha-sliding-marketing | `9d55bbe1d28739697a4608a0da2c7c558031ad3d566a94cf394dc608e6278959` | `d589d7335c7da7517a8c933f30c7cf9e0302502ab7e661ede5fc3d1da7f0e38a` | 77px | 187579 | 44058 |
| dougie-ing-content | `b10b2c7ffbd6eff2f95118a152aeb6319a38e79bfb167041a71bdc1e946da575` | `890850164785fd3edcbad29fe35de3695f8059a3d1ac78bd52cd8205ac5a8e65` | 77px | 259064 | 40876 |
| rickrolling-manager | `e64a90d0f2b759796966c38e8ff9bcdf1ff04a1665b77e8e490d2413701b76ae` | `ac76b89183f52d4d25677c1f4c5128bbc93e6da7a099d62f3c24d665c3c49bc8` | 77px | 324890 | 45284 |
| harlem-shaking-listings | `ff4b549a2b0c41f1edb6a77d664de510fc54e4564597ab39bdb4be641674d94f` | `01076f683bdabe777d4e3e6b86953719f672ca2ff952995a55a69b5452de8d9c` | 75px | 295913 | 37887 |
| wednesday-ing-offers | `44d8cbef941900696203c0b212595fc259fd46421ac43447ebbaf84395859842` | `f85be1789c341f6eb108ae8c0c38717ceb0b245f9c9e7d45d85432e1c66e24b3` | 77px | 214159 | 45578 |
| napoleon-dynamiting-content | `0853761007abc4382a5021804be0f6f03a3cadc56e9ba80f4dd83ef1e476408b` | `ff656c0888e0f9114bd586b93902015241f40d9ee9b1a1273b3ef4880cd625ce` | 77px | 194989 | 38913 |
| disco-inferno-ing-reports | `6816f5a4518eea035300469debbd4348823f1fabcbe77253787b273b9c6a3b45` | `569ee5e7b7dc397d360712e03e1bd6d616313fdfb15bc5f2619eaf56a4f142aa` | 77px | 295470 | 41008 |

## Registration and continuity

- `macarena-ing-manager`: canonical head/lower-body registration; only the connected arm/hand choreography changes.
- `ymca-ing-cma`: canonical head, torso core, and lower-body registration; arm silhouettes alternate cleanly.
- `cupid-shuffling-crm`: one rigid canonical full-body plate translated by 0/−3/−7/−4 px.
- `cha-cha-sliding-marketing`: one rigid canonical full-body plate translated by 0/−5/+5/+1 px.
- `dougie-ing-content`: canonical head/lower body; localized brushing-arm sequence.
- `rickrolling-manager`: fixed canonical head replacement plus body-anchored finger-point phases.
- `harlem-shaking-listings`: one rigid canonical full-body plate rotated 0/+1.2/−1.2/+0.4° around a fixed hip pivot.
- `wednesday-ing-offers`: canonical head/lower body; localized angular arm phases.
- `napoleon-dynamiting-content`: one rigid canonical full-body plate translated 0/−4/−8/−3 px, with a 1 px lift only at peak.
- `disco-inferno-ing-reports`: all four generated phases normalized to the identical 455 px height, fixed 550 px baseline, and lower-body centroid; inspected clean after restoring the rejected mask experiment.

## Visual QA

The final authored-cell contacts and six-frame strips were inspected at 256 px and 128 px respectively. No crop, extra limb, detached hand, readable text, logo, transparent corner failure, center-axis intrusion, or lingering rectangular mask artifact was found. The Disco source was specifically restored and reinspected after the temporary rejected mask pass; its final source hash is `6816f5a4518eea035300469debbd4348823f1fabcbe77253787b273b9c6a3b45`.
