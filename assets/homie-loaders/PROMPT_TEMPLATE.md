# Generation prompt set

The 371 sprite masters were created with the built-in image-generation tool.
Each base animation used the matching transparent character in `references/`
as the identity anchor and substituted the action-specific four-beat storyboard
represented by the animation label in `manifest.json`. Targeted source-
continuity repairs may use an additional precise-object edit pass.

```text
Use case: stylized-concept
Asset type: four-frame animation sprite sheet for a small chat-interface loading GIF
Input image: the transparent reference is the exact "{HOMIE_NAME}" character anchor
Primary request: create exactly four consecutive animation frames of {HOMIE_NAME}
performing this job action. {FRAME_1}. {FRAME_2}. {FRAME_3}. {FRAME_4}.
Scene/backdrop: every panel must use one perfectly flat, solid #00ff00 chroma-key
background for later removal
Subject: preserve the exact identity, face, hair, outfit, palette, and proportions
from the reference
Style/medium: exact same hand-drawn editorial ink outline with soft watercolor and
pencil shading; charming, restrained, slightly funny
Composition/framing: exact 2-by-2 grid of four equal square panels in reading
order; no gutters, borders, captions, or panel lines; one knee-up character per
panel, centered at identical scale and camera angle with generous padding;
oversized iconic props fully inside each panel
Lighting/mood: flat neutral illustration lighting
Constraints: preserve identity, proportions, outfit, palette, line weight, prop
design, framing, and camera across all four frames; only pose and prop positions
change; one character only in each panel; crisp silhouette; uniform #00ff00
background with no shadow, gradient, texture, floor, reflection, or lighting
variation; do not use #00ff00 in character or props; no readable letters or
numbers, no text, logos, watermark, extra people, or extra limbs
```

## Frame and loop grammar

- Top-left: setup pose.
- Top-right: wind-up or first movement.
- Bottom-left: peak action.
- Bottom-right: recovery toward setup.
- Runtime sequence: `TL → TR → BL → BR → BL → TR`.
- Live loading copy is stored in `manifest.json` and is never baked into the GIF.

Selected complex Reports actions use six authored poses instead. Lasso masters
use a 3-by-2 grid; snowboard, skateboard, and thread-pull masters use a 2-by-3
grid. Their output sequence is declared per asset in `scripts/alignment.json`,
while the six-frame GIF timing contract remains unchanged.

The 28 Teamwork, 89 Wildcard, 94 Movie Night, and 35 Pop & Dance masters use
four authored poses. Teamwork prompts attach the Manager reference plus one
specialist reference and require exactly two persistent characters in every
panel. The complete exact prompts for these additions are stored in the
`GENERATION_PROMPTS-TEAMWORK-*.md`, `GENERATION_PROMPTS-WILDCARD-*.md`,
`GENERATION_PROMPTS-MOVIE-NIGHT-*.md`, and
`GENERATION_PROMPTS-POP-DANCE-*.md` companion files.

## Identity anchors

- Manager: swept brown hair, camel double-breasted coat, charcoal scarf.
- CMA: close-cropped fade, navy/slate blazer, pale-blue shirt.
- CRM: bald head, olive bomber, white T-shirt, pale-blue jeans.
- Listings: tousled brown hair, black glasses, camel overshirt, cream T-shirt.
- Marketing: short dark hair, full beard, ivory hoodie, olive cargo trousers.
- Research: voluminous natural curls, hoop earrings, light-blue denim jacket.
- Content: neat black side-part, charcoal crewneck over a white collar.
- Offers: high messy bun, beige pinstripe utility jumpsuit.
- Reports: long wavy dark hair, cream suit, warm patterned neck scarf.

## Transparency

Every sprite master was processed with the image-generation skill's installed
`remove_chroma_key.py` helper using border auto-keying, a soft matte, and
despill. GIF edge pixels are matted to the live Homies AI canvas colour
`#FBF9F6`; the outer canvas remains transparent.

The four additional Listings masters use the same registration contract for
the shovel, binoculars, cinderblocks, and cornerstone scenes. `details-dig` is
the sole exception to the no-numerals rule: the shovel scoop intentionally
reveals a few small numeric details.

The three additional Marketing masters use the same registration contract for
the bow-and-target, artist-palette, and giant-hook grinder scenes. The target,
palette, and hook are persistent props; only the working arms, arrow, paint,
grinder wheel, and sparks advance across their four-beat storyboards.
`reel-storyboard` also received a precise-object edit pass so one fixed three-
slot board persists while only the house, camera, and key cards advance.

The additional Research master uses the same registration contract for one
fixed house-icon sale sign and a single phone that follows a clean low-to-chest
lifting path while the character performs the “Nosy neighbouring…” side-eye.

The Content guitar replacement and four additional Content masters use the same
registration contract for one acoustic guitar, a dense feather duster and fixed
file stack, a paper target with persistent puncture holes, a vintage projector
and film strip, and an oversized office presentation laser. The laser is styled
as a presentation/scanning prop rather than a weapon; only its red scan beam
advances toward the viewer.

The six additional Offers masters use the same registration contract for three
lowball juggling balls, a conditioner bottle and fixed paper, two dumbbells, one
safe with a hinged door and cash, a friendly shield-and-sword guard, and blank
papers organized on clip hangers. The lease, calculator, and amendment masters
also received full locked-base replacements so their desk props, calculator
body, paperwork, and stapler remain continuous frame to frame.

The ten additional Reports masters use the same identity lock for a cowboy-hat
lasso, dashboard snowboard and skateboard scenes, opaque number decanting,
chart pressure-washing, seated meditation, literal sweater unraveling, chain
breaking, cable plug-in, and rotary screen polishing. Lasso, snowboard, and
skateboard use six unique authored runtime poses. The decanter receives a
separate object-level registration pass so both the character and pedestal stay
fixed while the number stream advances.
