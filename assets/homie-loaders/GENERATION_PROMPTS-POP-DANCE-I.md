# Pop & Dance batch I — reference correction prompt ledger

Date: 2026-07-14  
Scope: eight retained-loader rebuilds and four new loaders

Every loader in this batch starts from one accepted, SHA-locked generated
character plate. No animation frame was generated independently. The release
builders extract connected limbs or props from that plate, use one union crop,
one scale, one bottom anchor, one reversible sequence, and one shared GIF
palette.

## Shared generation contract

```text
Use case: precise illustration rebuild for a four-phase chat loading animation.
Identity: preserve the exact role-canonical Homie face, hair, body proportions,
ink outline, soft watercolour shading, and editorial illustration finish from
the supplied Homie reference.
Composition: one uncropped full-body character on a perfectly flat exact
#00ff00 chroma field, with generous clearance on every side. Keep the moving
limbs and props separated enough to isolate as connected pieces.
Continuity: one character, exactly two arms and two legs, natural hands and
feet, one consistent outfit and prop design, fixed camera and scale.
Avoid: sprite grid, extra people, duplicate anatomy, detached body parts,
overlapping character copies, scenery, floor, shadow, text, logo, watermark,
gradient, texture, green clothing, and satellite debris.
```

## Rebuilt retained loaders

### `disco-inferno-ing-reports`

- Character anchor: `references/reports.png`
- Locked plate: `qa/strict-repairs/raw/disco-inferno-ing-reports-locked-v2.png`
- Builder: `scripts/repair_pop_dance_hand_cleanup.py`

```text
Dress Reports Homie in one clean white disco suit over a warm gold blouse.
Pose her upright with one complete arm pointing high overhead, one clear index
finger, and the other forearm resting across the waist. Keep both feet planted
and leave clearance around the raised hand so that arm alone can travel down
and back up without moving or scaling the body.
```

### `rickrolling-manager`

- Character anchor: `references/manager.png`
- Locked plate: `qa/strict-repairs/raw/rickrolling-manager-locked-v2.png`
- Builder: `scripts/repair_pop_dance_hand_cleanup.py`

```text
Dress Manager Homie in a camel trench over a black-and-white striped knit,
dark trousers, and black shoes. Use one complete outward pointing arm and keep
the second hand in the coat pocket. Exactly one character and one face; leave
the pointing arm isolated for a small reversible finger-point groove.
```

### `ymca-ing-cma`

- Character anchor: `references/cma.png`
- Locked plate: `qa/strict-repairs/raw/ymca-ing-cma-locked-v2.png`
- Builder: `scripts/repair_pop_dance_hand_cleanup.py`

```text
Dress CMA Homie in warm retro dance-floor clothing with a mustard jacket,
burgundy shirt, flared dark trousers, and light boots. Pose the complete arms
high and clearly separated from the head and torso so one connected two-arm
rig can form four readable Y, M, C, and A silhouettes. Keep the core and legs
fixed and preserve one natural hand at the end of each arm.
```

### `wednesday-ing-offers`

- Character anchor: `references/offers.png`
- Locked plate: `qa/strict-repairs/raw/wednesday-ing-offers-locked-v2.png`
- Builder: `scripts/repair_pop_dance_hand_cleanup.py`

```text
Dress Offers Homie in a long black dress with white collar, black tights,
black shoes, and two neat braids. Use one stiff raised forearm with a single
flat hand and one second forearm held horizontally across the waist. Keep the
raised hand isolated so it can move without leaving a persistent ghost hand.
```

### `cha-cha-sliding-marketing`

- Character anchor: `references/marketing.png`
- Wardrobe/action anchor: user-supplied Cha Cha Slide cover
- Locked plate: `qa/strict-repairs/raw/cha-cha-sliding-marketing-canonical-v2.png`
- Builder: `scripts/repair_pop_dance_reference_four.py`

```text
Use the supplied gold-jacket cover literally: shiny gold jacket held open over
a plain black shirt, long silver chain, baggy black trousers, and gold work
boots. Cross the feet in the recognizable slide stance; keep the upper body
fixed and leave both boots clear for a small crossed-step opening and return.
```

### `harlem-shaking-listings`

- Character anchor: `references/listings.png`
- Wardrobe/action anchors: user-supplied tutorial and original meme stills
- Locked plate: `qa/strict-repairs/raw/harlem-shaking-listings-canonical-v2.png`
- Builder: `scripts/repair_pop_dance_reference_four.py`

```text
Put Listings Homie in the unmistakable bright-pink full-body meme suit with
hood, while retaining his face, brown hair, and black glasses. Use a bent-knee,
leaning stance with both fists held low and separated so the complete arms can
counter-swing through a quick shake without moving the torso or camera.
```

### `umbrella-ing-manager`

- Character anchor: `references/manager.png`
- Locked plate: `qa/strict-repairs/raw/umbrella-ing-manager-canonical-v2.png`
- Builder: `scripts/repair_pop_dance_reference_four.py`

```text
Show Manager Homie clearly and physically holding one large transparent dome
umbrella: visible canopy, ribs, centre shaft, hooked handle, and a natural hand
wrapped around the shaft. Keep the umbrella fully inside frame and do not mime
an absent prop.
```

### `dougie-ing-content`

- Character anchor: `references/content.png`
- Choreography anchor: user-supplied three-pose Dougie diagram
- Locked plate: `qa/strict-repairs/raw/dougie-ing-content-canonical-v3.png`
- Builder: `scripts/repair_pop_dance_reference_four.py`

```text
Dress Content Homie in a plain white T-shirt, black joggers, white socks, and
black sneakers. Use the supplied Dougie reference: bent knees and side lean,
one complete forearm brushing horizontally across the upper chest/shoulder,
the other complete arm low beside the hip. Keep both arms away from the face
and cleanly separated so a small shoulder-brush sweep cannot create overlaps.
```

## New loaders

### `david-blaining-manager`

- Character anchor: `references/manager.png`
- Locked plate: `qa/strict-repairs/raw/david-blaining-manager-generated.png`
- Builder: `scripts/add_pop_dance_david_crank.py`

```text
Dress a male Manager Homie in a simple all-black street-magician suit, black
shirt, trousers, and shoes. Put a deck in one natural hand and six clearly
separated playing cards in a rising arc above the open opposite hand. Keep the
outer card isolated so it can travel through the arc while the body, deck, and
remaining cards stay fixed.
```

### `cranking-that-marketing`

- Character anchor: `references/marketing.png`
- Pose anchor: user-supplied Superman move diagram
- Wardrobe anchor: user-supplied white-graffiti-jacket music-video still
- Locked plate: `qa/strict-repairs/raw/cranking-that-marketing-generated.png`
- Builder: `scripts/add_pop_dance_david_crank.py`

```text
Dress a male Marketing Homie in the literal reference wardrobe: oversized
white graffiti/paint jacket, long red shirt, sideways white cap, white
wraparound sunglasses, baggy black trousers with yellow panels, and yellow-
black sneakers. Hold the recognizable Superman phase with both complete arms
spread wide, torso leaning, one rear leg lifted, and generous limb clearance.
```

### `cranking-the-step-marketing`

- Character anchor: `references/marketing.png`
- Pose anchor: user-supplied Crank That steps 1–3 diagram
- Wardrobe anchor: user-supplied white-graffiti-jacket music-video still
- Locked plate: `qa/strict-repairs/raw/cranking-the-step-marketing-generated.png`
- Builder: `scripts/add_pop_dance_david_crank.py`

```text
Use the same white graffiti jacket, long red shirt, sideways cap, white shades,
black-and-yellow trousers, and matching shoes. Hold the crossed-foot small-hop
phase with both fists separated near shoulder height so they can counter-pump
without changing the body, face, lifted leg, crop, or scale.
```

### `cranking-the-motorbike-marketing`

- Character anchor: `references/marketing.png`
- Pose anchor: user-supplied Crank That steps 4–7 diagram
- Wardrobe anchor: user-supplied white-graffiti-jacket music-video still
- Locked plate: `qa/strict-repairs/raw/cranking-the-motorbike-marketing-generated.png`
- Builder: `scripts/add_pop_dance_david_crank.py`

```text
Use the same requested Crank That wardrobe. Hold a low bent-knee, side-leaning
motorbike-rev phase with both complete fists forward like imaginary handlebars.
Leave both arms separated from the jacket core so they can counter-rev while
the head, torso, trousers, shoes, camera, and scale remain fixed.
```

## Runtime grammar

- Source master: exact 2×2 grid, 1254×1254 pixels.
- GIF: 256×256, binary-transparent canvas, infinite loop.
- Authored phases: `0,1,2,3`; runtime sequence: `0,1,2,3,2,1`.
- Durations: `210,140,140,210,140,140ms`.
- Registration: one union crop, fixed scale and bottom anchor per loader.
- Palette: one shared palette per GIF; no frame-by-frame quantization shimmer.
