# Accepted image-generation prompts — scooby-dooing-manager

Built-in image generation was used. Image 1 was the user-supplied pose/concept reference; Image 2 was `references/manager.png`, the canonical Manager identity/style reference.

## Accepted base generation prompt

```text
Use case: stylized-concept
Asset type: original immutable character plate for a small animated web loader
Primary request: Draw an original comic scene with exactly two subjects: one adult male Manager character carrying one oversized goofy brown spotted dog. Both are startled and trembling together in a tight, funny huddle. The dog must be a new generic design, not a reproduction of any named or existing media character.
Input images: Image 1 supplies only the broad physical idea of a frightened man carrying a frightened large dog; change the dog design, colors, markings, face, and accessories into an original generic animal. Image 2 supplies the canonical Homies Manager identity and ink-and-watercolour illustration language. Preserve Image 2's adult male Manager face language, proportions, hand-drawn dark contour, restrained watercolor wash, warm paper-like coloring, and editorial character finish.
Scene/backdrop: one perfectly uniform flat solid #00ff00 chroma-key field. No floor plane.
Subject: exactly one adult male and exactly one large dog. The man supports the dog safely using exactly two clear human arms and two hands. The dog has one head, one body, exactly four legs/paws, and one tail; floppy ears, medium-brown coat, several irregular dark spots, no collar and no tag. Both face generally forward with wide comic alarmed eyes and tense posture. Entire connected pair visible.
Style/medium: canonical Homies hand-drawn ink-and-watercolour 2D illustration; natural slightly imperfect line, soft restrained wash; not 3D, not clay, not photorealistic, not anime, not flat vector art.
Composition/framing: centered full-body combined pair, generous even empty padding on every side, no crop, no detached elements, one cohesive silhouette.
Constraints: exactly two subjects total; no extra people or animals; no extra heads, faces, arms, hands, fingers, legs, paws, or tails; crisp clean outline; no use of #00ff00 in the subjects; no cast shadow, contact shadow, reflection, gradient, texture, background lighting variation, or green spill.
Avoid: any existing franchise-specific dog likeness, logos, brand marks, text, letters, numbers, glyphs, watermarks, emblems, signs, debris, particles, motion marks, duplicate props, furniture, scenery, borders, halos.
```

## Targeted edit 1 — remove stray motion marks

```text
Use case: precise-object-edit
Asset type: corrected immutable chroma character plate for an animated web loader
Primary request: Remove only every small black tremble squiggle or motion mark floating around the man and dog. Replace those removed marks with the exact same perfectly flat solid #00ff00 chroma color as the surrounding background.
Input image: Image 1 is the edit target and accepted subject design.
Invariants: Keep the adult male Manager and the single large brown spotted dog unchanged in identity, facial expressions, pose, anatomy, hands, paws, tail, clothing, colors, textures, outlines, scale, crop, anchor, and composition. Keep exactly one man and one dog. Keep the entire connected pair visible with the same padding. Do not redraw or restyle the subjects. Do not add anything.
Background: perfectly uniform flat #00ff00 with no shadows, gradients, floor plane, texture, halos, spill, or lighting variation.
Constraints: exactly two subjects; no motion marks, squiggles, debris, particles, text, letters, numbers, glyphs, logos, brand marks, watermark, border, shadow, or reflection.
```

## Targeted edit 2 — add recognizable blank collar/tag cue

```text
Use case: precise-object-edit
Asset type: final immutable chroma character plate for an animated web loader
Primary request: Add only one simple bright teal-blue collar around the large brown spotted dog's neck and one small plain green diamond-shaped tag hanging at the center of that collar. The tag must be blank: no letter, number, logo, mark, engraving, or glyph.
Input image: Image 1 is the edit target and accepted composition.
Invariants: Keep every other visible element unchanged: exactly one adult male Manager and exactly one large brown spotted dog; their identities, faces, frightened expressions, eye directions, pose, anatomy, human hands, dog paws, tail, embrace, clothing, colors, textures, outlines, scale, crop, anchor, and composition. Keep the flat chroma background unchanged. Do not alter or add any other accessory. Do not redraw or restyle the subjects.
Background: perfectly uniform flat solid #00ff00 with no shadows, gradients, floor plane, texture, halos, spill, or lighting variation.
Constraints: exactly two subjects total; exactly one collar and exactly one small blank diamond tag; no motion marks, squiggles, debris, particles, text, letters, numbers, glyphs, logos, brand marks, watermark, border, shadow, or reflection.
```

Accepted chroma SHA-256: `f1974fd98e5240af0a8527bbf3548209885fc304a4884dbf65325115dfdfb2dc`

Accepted alpha SHA-256: `c29f3a2e02ca6f01405df62535cc3d41f8503d28bf10aaeb386b585c74555d55`
