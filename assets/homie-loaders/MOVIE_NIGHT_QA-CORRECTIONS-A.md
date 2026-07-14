# Movie Corrections A — QA report

## Accepted outputs

| slug | source contract | minimum cell margin | authored cells | temp GIF |
|---|---|---:|---:|---|
| `sell-phoning-manager` | 1254×1254 RGB, exact key | 67 px | 4 distinct | 256×256, 6 frames, 4 unique, 62,445 bytes |
| `neo-ing-offers` | 1254×1254 RGB, exact key | 63 px | 4 distinct | 256×256, 6 frames, 4 unique, 69,364 bytes |
| `mavericking-manager` | 1254×1254 RGB, exact key | 67 px | 4 distinct | 256×256, 6 frames, 4 unique, 58,819 bytes |
| `frodo-bagginsing-crm` | 1254×1254 RGB, exact key | 68 px | 4 distinct | 256×256, 6 frames, 4 unique, 67,640 bytes |
| `peter-panning-listings` | 1254×1254 RGB, exact key | 63 px | 4 distinct | 256×256, 6 frames, 4 unique, 38,511 bytes |
| `tinkerbelling-content` | 1254×1254 RGB, exact key | 63 px | 4 distinct | 256×256, 6 frames, 4 unique, 43,109 bytes |
| `marioing-offers` | 1254×1254 RGB, exact key | 67 px | 4 distinct | 256×256, 6 frames, 4 unique, 36,981 bytes |
| `mario-riding-yoshi-offers` | 1254×1254 RGB, exact key | 75 px | 4 distinct | 256×256, 6 frames, 4 unique, 71,941 bytes |
| `jack-sparrowing-marketing` | 1254×1254 RGB, exact key | 63 px | 4 distinct | 256×256, 6 frames, 4 unique, 75,548 bytes |

Every master is RGB, has exact `#00ff00` corners, outer borders and central split axes, and contains one complete subject group in each cell. Every temp GIF loops forever with sequence `[0,1,2,3,2,1]`, durations `[210,140,140,210,140,140]`, transparent corners and four unique visual phases.

Machine-readable checks:

- `/tmp/movie-corrections-a/source-audit.json`
- `/tmp/movie-corrections-a/gif-audit.json`
- `/tmp/movie-corrections-a-alignment.json`

## Rebuild and continuity checks

- `sell-phoning-manager`: one exact deeply crouched palm-away plate and its exact mirror form the alternating hand-dance beats. The orange puffer, beige turtleneck and bent knees read clearly at 128 px.
- `neo-ing-offers`: one exact full-body/coat plate rotates around a fixed heel-area pivot through four large backbend phases. Identical deterministic silver bullets remain horizontal and advance over the torso.
- `mavericking-manager`: four accepted connected helmet/forearm positions are normalized onto one fixed canvas. Olive G-suit, survival vest, flotation collar, aviators, boots and striped helmet retain consistent scale and silhouette; no bomber jacket.
- `frodo-bagginsing-crm`: the connected sword-hand lift is preserved from low beside the knee through an emphatic forward/up pose. Cloak, vest, cropped trousers and attached hairy feet remain registered and recognizable.
- `peter-panning-listings`: one exact horizontal flying plate performs a large vertical/pitch bob; no standing phase exists.
- `tinkerbelling-content`: four actual diagonal-hover wing configurations are registered to one fixed canvas. The feminine body, bun, dress and pointed feet retain a consistent diagonal silhouette while the wing spread changes dramatically.
- `marioing-offers`: one exact fist-up/knee-up jump plate moves through a 70 raw-pixel vertical arc with controlled squash/stretch; no hands-in-pockets or standing pose.
- `mario-riding-yoshi-offers`: one exact rider/dinosaur/saddle group moves rigidly as a mounted unit through a large bounce/rock. Rider hips, knees, hands, reins and saddle contact never separate.
- `jack-sparrowing-marketing`: one exact arms-wide crossing-step plate and its exact mirror create alternating sea-leg steps, with strong pivoted lean and no upright idle frame.

Muted-green costumes/creature areas in Peter Pan, Tinkerbell and the mounted dinosaur were processed with a narrow sampled-key matte and shifted safely away from the pure key hue. Full-size inspection confirmed no internal key holes or chroma-eaten texture.

## Visual hard-gate inspection

Inspected every 1254×1254 master cell at full size and every reversible strip at both 256 and 128 px on the site off-white matte:

- no cropped head, hat, hand, wing, sword, bullet, helmet, boot, coat tail, dinosaur snout or tail;
- no extra/detached limbs, duplicate riders/creatures, floating saddle, disconnected feet, loose trash fragments, text, logos or watermarks;
- all nine signature actions read in any single frame at 128 px;
- frame 3 is a clear action extreme and the reverse sequence returns cleanly without a wrap jump.

Contact sheets:

- full pages: `/tmp/movie-corrections-a/contact/page-1.jpg`, `page-2.jpg`, `page-3.jpg`
- per-asset full and 128 px strips: `/tmp/movie-corrections-a/contact/<slug>-full.jpg` and `<slug>-128.jpg`

Accepted temp GIFs: `/tmp/movie-corrections-a/gifs/`.

Accepted project masters were copied to `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/`. No manifest or production alignment file was edited.


