# Generation prompts — Tarzaning

Date: 2026-07-14  
Loader: `tarzaning-manager`  
Collection: Movie Night  
Image workflow: built-in image-generation tool, local chroma-key removal, then deterministic fixed-pivot animation.

## Reference roles

- User reference `codex-clipboard-374d7e82-b89b-4c5f-a646-4fc80576c042.png`: classic adult male jungle-adventurer hair, brown waist wrap and barefoot wardrobe only.
- `references/manager.png`: exact canonical male Manager identity, face, proportions and Homies ink/watercolour style.

## Accepted character-plate prompt

> Use case: stylized-concept. Create one locked full-body character plate for a 128px transparent chat-interface loading GIF. Use the Manager reference as the exact identity and rendering-style anchor. Draw the same clearly adult male Manager Homie as a classic jungle adventurer in a joyful airborne action pose. His two hands meet directly above his head as though firmly holding a small unseen handle; both arms are raised, connected and anatomically correct. His body angles diagonally and both knees bend into a compact flying arc. Preserve the Manager face, friendly expression, skin tone, ink line quality and normal Homies proportions. Give him slightly longer tousled brown hair, a classic modest adult jungle-hero outfit, and bare feet. Full figure, both hands and both feet visible with generous padding. Exact editorial black ink, soft muted watercolour and light pencil texture. Perfectly flat uniform `#00ff00` chroma background. Exactly one adult male, two arms, two five-finger hands, two legs and two feet; no props, extra anatomy, crop, text, logo, shadow, floating fragments or debris.

## Accepted wardrobe edit

> Preserve the exact same canonical face, hair, hands, arms, body proportions, airborne pose, legs, feet, framing, scale and flat green background. Replace the upper tunic with a classic modest adult male jungle-hero costume: uncovered upper torso plus one opaque brown draped waist wrap over secure matching mid-thigh shorts. Keep the waist and upper legs fully covered, longer tousled hair and bare feet. Do not add any prop or alter anatomy.

## Accepted locked plates

| Artifact | SHA-256 |
|---|---|
| Accepted generated chroma plate | `9c4a364817c7690f18db8db58a4d04e5f5cf29719c5e013ddceaf493a2e19f08` |
| Transparent canonical plate | `33e4ea830ec94f4b0c2bf0f6d346b41eb42aaa2c405df5149eaf6b102e090228` |

The chroma plate was processed with border auto-keying, a soft matte,
thresholds `12/220`, and despill. The vine is deterministic artwork, not a
generated per-frame object: it is fused behind the accepted character once,
then the complete character-and-vine rig rotates through `-9°`, `-3°`, `3°`
and `9°` around one fixed overhead knot. No character or prop geometry redraws.

