# Pop & Dance D — Canonicalization and QA

> Historical generation/structural record. The final motion-semantic authority is `POP_DANCE_QA-SEMANTIC-REBUILD-2026-07-12.md`.


## Scope

| Asset | Homie | Loading line |
|---|---|---|
| `wrecking-ball-riding-research` | Research | Riding the wrecking ball… |
| `popping-my-collar-manager` | Manager | Popping my collar… |
| `dirt-off-your-shoulders-marketing` | Marketing | Getting that dirt off your shoulders… |

## Anti-wiggle construction

- Each production master was rebuilt from exactly one accepted RGBA subject plate. No frame-to-frame AI redraws remain.
- `wrecking-ball-riding-research`: raw cell 2 supplies one identical rider, ball and shortened chain. The assembly is resized once, placed with its chain top at 70 px, then rigidly rotated `0° / -2.2° / +2.2° / -0.8°` around one fixed in-frame chain pivot. A screen-stable two-tone pivot cap conceals the shortened chain end.
- `popping-my-collar-manager`: raw cell 1 supplies one complete hands-at-collar Manager plate. Four phases use only a tiny deterministic rigid pose, at most 2 px translation and 0.4° rotation; face, clothing, anatomy and collar art remain the same pixels.
- `dirt-off-your-shoulders-marketing`: raw cell 0 supplies one complete shoulder-brushing Marketing plate. Four phases use only a tiny deterministic rigid pose, at most 2 px translation and 0.3° rotation, plus `0 / 2 / 3 / 1` tiny opaque dust flecks close to the brushed shoulder.
- Reproducible construction script: `/tmp/process_pop_dance_d.py`.
- Exact assembly config: `/tmp/pop-dance-d-alignment.json` with `inset_ratio: 0`, identity assembly transforms, sequence `0,1,2,3,2,1`, and durations `210,140,140,210,140,140` ms.

## Source-master checks

| Asset | Master | Mode | Authored cells | Minimum cell clearance | Continuity result |
|---|---:|---:|---:|---:|---|
| `wrecking-ball-riding-research` | 1254×1254 | RGB | 4 distinct | 68 px | Fixed pivot; identical rider/ball/chain plate; no crop or redraw |
| `popping-my-collar-manager` | 1254×1254 | RGB | 4 distinct | 67 px | One canonical full-body plate; no extra limbs or detached collar pieces |
| `dirt-off-your-shoulders-marketing` | 1254×1254 | RGB | 4 distinct | 67 px | One canonical full-body plate; dust remains tiny, opaque and shoulder-local |

All three masters have exact `#00ff00` outer corners, outer edges, and both two-pixel central axes. No gutter, cast shadow, text, logo, watermark, extra subject, or cropped anatomy was found in the production cells.

## Temporary GIF checks

- GIF directory: `/tmp/pop-dance-d/gifs/`
- Full-resolution contact: `/tmp/pop-dance-d/contact/final-4frame-contact.jpg`
- 128 px playback contact: `/tmp/pop-dance-d/contact/gif-128-contact.jpg`
- Machine report: `/tmp/pop-dance-d/temp-gif-qa.json`
- Every GIF is 256×256, transparent, six frames, loop forever, reversible, and has exactly four visually distinct phases.
- Every GIF uses durations `210 / 140 / 140 / 210 / 140 / 140` ms.
- File sizes are 52,086 bytes, 46,152 bytes and 46,291 bytes respectively, safely below the 750 KB production ceiling.
- Full-size and 128 px contacts were visually inspected for crop, anatomy, continuity, object connection, green spill and stray fragments. All three pass.
