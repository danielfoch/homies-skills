# Tier-A Movie Night C2 — accepted prompt ledger

Execution mode: built-in `image_gen`, one successful call per accepted raw. Every successful call used the named Homie reference as an identity/style reference. The source masters were built temp-first from those accepted raws; no production manifest, alignment file, or GIF was touched.

## Pose/costume reference research

- `supermanning-marketing`: researched the classic one-fist-forward horizontal flight silhouette; the important readable cues were a straight leading arm, trailing legs, and a cape flowing opposite travel.
- `spider-manning-crm`: researched the classic full-body inverted single-line pose; the important cues were a fixed top attachment, white eye lenses, red/blue suit division, black web pattern, and lateral pendulum swing.
- `wolverine-ing-research`: researched the classic yellow/blue pointed-cowl silhouette; the important cues were two forward fists and exactly three parallel metal claws emerging from each fist.
- `joker-ing-content`: researched purple-suit/green-hair/white-makeup card flourishes; the selected loop uses exactly one blank card and alternating strong head tilts.
- `beetlejuicing-listings`: researched the black/white vertically striped suit and wild pale hair; the selected loop emphasizes elbows-out alternating shoulder compression.

## Accepted generations

### `supermanning-marketing`

- Identity/style reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/marketing.png`
- Accepted built-in raw: `/tmp/movie-c2/raw/supermanning-marketing.png`
- Successful prompt:

> Create a four-pose 2x2 sprite sheet using the exact male Marketing Homie from Image 1, preserving his recognizable face, beard, proportions, thin ink linework, and soft hand-painted editorial finish. Redress him as an original retro sky-rescue courier in a plain cobalt-blue fitted flight suit, plain red boots, a single flowing red back-cape, and a tiny plain gold diamond-shaped chest patch containing absolutely no letter, symbol, icon, or logo. In every quadrant he is fully airborne in an unmistakable horizontal one-fist-forward flying posture: leading fist extended ahead, torso angled forward, other arm trailing, exactly two connected arms and exactly two connected legs, red cape streaming behind. Four readable phases in reading order: low level flight; rising flight with cape lifted; highest flight with stronger upward pitch; descending return with cape curling. Keep identity, suit, anatomy, and all garments identical across the four poses; make movement large enough to read at 128px. One square canvas, four equal quadrants with no borders or dividers, one complete full-body figure per quadrant, at least 14% empty padding around every figure, nothing cropped. Entire canvas is one perfectly flat uniform solid #00ff00 background including all corners, outer edges, centre axes, and spaces. No floor, no shadows, no gradient, no texture, no glow, no text, no letters, no logo, no watermark, no extra props, no extra limbs, no detached body parts, no motion blur, no photorealism, no 3D.

- Deterministic build: one accepted canonical flight plate, rotated through `2°, -2.5°, -7°, -2°` and vertically offset `+28, +4, -30, +10` source pixels. This removes pose-to-pose anatomy/cape drift while preserving a large flight bob.

### `spider-manning-crm`

- Identity/style reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/crm.png`
- Accepted built-in raw: `/tmp/movie-c2/raw/spider-manning-crm.png`
- Successful prompt:

> Create a clean four-pose 2x2 character sprite sheet using the exact CRM Homie identity from Image 1, preserving his recognizable face, body proportions, warm hand-drawn ink-and-watercolor rendering, and clear simple anatomy. Dress him in an original circus gymnastics rehearsal outfit: one consistent plain fitted medium-gray long-sleeve unitard, matching soft shoes, and a smooth plain gray fabric hood that leaves only two simple white oval eye openings; no pattern, no emblem, no text, no logo. In every quadrant show the full body upright and fully visible with feet together and both arms straight overhead, hands joined, like a rhythmic-gymnastics reach pose. Four clear body-lean phases in reading order while feet and anatomy remain connected: strong lean left; mild lean left; strong lean right; mild lean right. Exactly one person, one head, two attached arms, two attached legs, and two hands in each pose. Identity, suit, hood, scale and anatomy identical; large body lean readable at 128px. Square canvas, conceptual 2x2 arrangement of four equal quadrants, no borders or dividers, one complete full-body figure per quadrant, generous padding, nothing cropped, all points at least 14% within the quadrant. Entire canvas perfectly flat uniform solid #00ff00 green including edges, corners, centre axes and gaps. No floor, no prop, no rope, no shadow, no glow, no gradient, no texture, no motion blur, no extra limbs, no detached pieces, no watermark, no 3D, no photorealism.

- Deterministic build: the accepted rigid acrobat plate was recoloured into red/blue fabric, clipped black web linework was added, the plate was inverted, then swung about one fixed top attachment at `-18°, -7°, +18°, +7°`. One single outlined white web line is constant in every frame. This local construction avoids line/anatomy morphing and keeps the complete body rigid.

### `wolverine-ing-research`

- Identity/style reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/research.png`
- Accepted built-in raw: `/tmp/movie-c2/raw/wolverine-ing-research.png`
- Successful prompt:

> Create a four-pose 2x2 loading-animation sprite master using the exact female Research Homie identity from Image 1, preserving her recognizable face shape, natural curls where visible, body proportions, thin dark ink linework and soft hand-painted editorial finish. Redress her as an original bold yellow-and-navy comic rescue hero: bright yellow fitted suit, navy gloves, navy boots, navy side panels, and a yellow-and-navy fabric cowl with two tall outward-pointing side fins. No letter, no chest emblem, no logo. Both forearms are held clearly forward and apart at waist-to-chest height with two tightly clenched navy-gloved fists fully visible, knuckles facing outward, wrists straight and connected. Absolutely no claws, blades, spikes, weapons, or metal objects in the generated art; leave clean green space immediately beyond both fists for later animation effects. Four consistent readable stances in reading order with only mild breathing/fist emphasis: neutral crouch; fists pushed slightly forward; deeper crouch with fists forward; return stance. Exactly one person, one head, two attached arms, two attached legs, and two fists in each pose; identity, mask, outfit, anatomy and fist locations remain consistent. Composition: one square 2x2 sprite sheet, four equal quadrants without panel borders or dividers, one complete full-body figure per quadrant, generous padding, nothing cropped, all hair, mask fins, boots and fists at least 14% inside each quadrant edge. Entire background perfectly flat uniform solid #00ff00 including outer edges, corners, centre axes and gaps. No floor, no shadow, no glow, no gradient, no texture, no motion blur, no text, no watermark, no extra limbs, no detached parts, no photorealism, no 3D.

- Deterministic build: one stable fists-forward plate is reused. Exactly three silver blades are drawn from each connected fist at source lengths `20, 40, 64, 82` pixels, giving a clean extend/retract loop with no body drift.

### `joker-ing-content`

- Identity/style reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/content.png`
- Accepted built-in raw: `/tmp/movie-c2/raw/joker-ing-content.png`
- Successful prompt:

> Create a four-pose 2x2 sprite sheet using the exact Content Homie from Image 1, preserving his recognizable East Asian face, slim build, black-hair silhouette beneath styling, body proportions, and the same warm hand-drawn editorial ink-and-watercolor finish. Costume him as an original eccentric stage-card magician: tailored violet suit, lime-green waistcoat, cream shirt, dark bow tie, swept bright-green theatrical wig, and neat white mime-style face paint with a tiny muted-red curved smile. Friendly playful expression, no menace, no logos. He holds exactly one blank ivory rectangular card total, pinched in his right hand. That card contains no rank, suit, letter, number, picture, text, or symbol. His empty left hand makes a broad theatrical flourish. Four clear phases in reading order: upright head/card low; head strongly tilted toward one shoulder/card raised; head strongly tilted toward opposite shoulder/empty hand flourishes wide; upright return/card at chest. Head-angle and hand motion are obvious at 128px, while feet and torso remain stable. Exactly one person, one head, two attached arms, two attached legs, two hands, and one card in every pose; consistent anatomy and outfit. Square canvas, conceptual 2x2 arrangement of four equal quadrants, no borders or divider lines, one complete full-body figure centred in each, generous padding, nothing cropped, all hair, hands, shoes and card at least 14% inside quadrant edges. Entire background perfectly flat uniform solid #00ff00 green including all outer edges, corners, centre axes and gaps. No floor, shadow, gradient, texture, glow or motion blur. No extra cards, no extra limbs, no detached pieces, no text, no watermark, no 3D, no photorealism, no generic standing sequence.

- Deterministic build: all four authored head/card phases were normalized to one foot anchor and one global scale. Intended hair/waistcoat greens were shifted to an olive-green chroma-safe range so they remain visibly green after the production matte/despill helper.

### `beetlejuicing-listings`

- Identity/style reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/listings.png`
- Accepted built-in raw: `/tmp/movie-c2/raw/beetlejuicing-listings.png`
- Successful prompt:

> Create a four-frame 2x2 loading-animation sprite master using the exact Listings Homie from Image 1, preserving his recognizable glasses, face, slim proportions, thin hand-inked contours and soft editorial painted texture. Redress him as a mischievous monochrome ghost-party showman: bold black-and-white vertical striped suit jacket and matching trousers, plain white shirt, narrow black tie, wild high-volume pale silver-white hair, subtle pale face makeup and dark eye accents. No logos. Perform an emphatic shoulder shimmy with both elbows held visibly out away from the torso and forearms bent, hands open. Four clearly distinct phases in reading order: left shoulder high/right low; shoulders level with elbows wide; right shoulder high/left low; deeper opposite shimmy return. The torso compresses and rebounds while both feet stay anchored; elbows remain connected and wide. Motion must read instantly at 128px. Exactly one person, one head, two attached arms, two attached legs, two hands in every pose; outfit stripe direction, hair shape, glasses and anatomy consistent. Composition: square sheet with a conceptual clean 2x2 grid, four equal quadrants, no panel borders or dividers, one complete full-body figure per quadrant, generous padding, nothing cropped, hair, elbows, fingertips and shoes at least 14% inside each quadrant edge. Entire canvas perfectly flat uniform solid #00ff00 green including all outer edges, corners, centre axes and gaps. No floor, no shadow, no gradient, no texture, no glow, no motion blur. Style: exact Image 1 refined hand-drawn editorial illustration, thin dark linework and softly painted fabric, no 3D, no photorealism. Constraints: four meaningful shoulder poses; elbows visibly out; persistent anatomy; no extra limbs; no detached pieces; no text; no watermark; no generic standing; no crop.

- Deterministic build: all four authored shimmy phases were normalized to one foot anchor and one global scale, keeping the feet stable while the shoulder/elbow action remains large.

## Moderation trace

Three concepts had output-stage moderation rejections before the successful prompts above (`supermanning`, `spider-manning`, and `joker-ing`). Rejected attempts produced no image file and are not part of the accepted source provenance. Each accepted source uses exactly one successful built-in generation raw.

