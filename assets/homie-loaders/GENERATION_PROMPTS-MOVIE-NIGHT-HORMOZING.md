# Generation prompt and provenance — Movie Night: Hormozing

Date: 2026-07-14  
Loader: `hormozing-manager`  
Collection: Movie Night  
Status: candidate provenance record; this file does not assert QA approval or production promotion.

## Reference roles

- `references/manager.png` is the canonical identity, face, body-proportion,
  linework, and watercolour-style authority. SHA-256:
  `9bdcf4363fb403917761987da581f4cbfe746f1fe564ad64480c582877d8fc55`.
- `sources/wildcard/gary-veeing-crm.png` is a secondary reference for the
  established Homies rendering language only. It is not an identity reference.
  SHA-256:
  `72abdf6a37492c47cc93172e311a3ec7c37f23cc7dfaa5298c832f5d796413aa`.
- The likeness cues are deliberately brand-free: backward royal-blue cap,
  clear-lens glasses, white nasal strip, thick salt-and-pepper beard, muscular
  upper arms, white sleeveless shirt, charcoal trousers, and silver watch.

## Exact generation prompt

The following text is copied verbatim from
`qa/strict-repairs/hormozing-manager/candidates/imagegen-prompt.txt`:

```text
Create a single square 2x2 contact sheet on a perfectly flat, solid #00ff00 chroma-key background. Every panel must show the same locked donor pose and identical crop so one panel can be used as an immutable animation plate.

Use the attached Manager Homie illustration as the canonical visual-language reference and the attached Gary Vee Homie source only as a secondary reference for the established Homies line-and-watercolour rendering style. Draw one adult male Manager Homie, waist-up, centred with generous transparent-safe margins. Keep the established Homies proportions, clean black ink contours, lightly textured watercolour fills, friendly expressive face, and anatomically correct connected arms and hands.

Make the character a recognizable but brand-free Alex Hormozi homage: muscular upper arms, thick dark salt-and-pepper beard, dark hair beneath a backwards royal-blue baseball cap, clear-lens black glasses, a small white nasal strip across the bridge of his nose, white sleeveless training shirt, charcoal trousers, and one chunky silver watch. He smiles confidently at the viewer.

He holds exactly one large blank upright navy hardback business book against his chest with one hand while the other hand forms one anatomically correct index-finger pointing gesture toward the blank cover. The book must have a stable rectangular geometry, dark navy cover, and a narrow muted-coral page edge. Leave a large clean blank area on the book for deterministic lettering and value graphics to be added later. Exactly two arms, two attached hands, five fingers per hand where visible. No moving pose variants between panels.

No logos, no brand marks, no generated lettering, no symbols, no numbers, no money, no extra props, no extra hands or fingers, no overlapping duplicate character, no detached limbs, no background objects, no shadows cast onto the green, no white or off-white background. The entire background must be uniform #00ff00 all the way to every edge.
```

No targeted image-edit prompt was used.

## Candidate provenance

The built-in image-generation tool produced the candidate recorded at
`qa/strict-repairs/hormozing-manager/candidates/raw-chroma.png` with SHA-256
`a80c23284d9a2fe9147b765b6ee5be486a408a68694713c2b52a1ecd47692fd2`.
Panel `0` is the selected immutable donor.

The chroma candidate was processed by the image-generation skill's
`remove_chroma_key.py` helper using border auto-keying, soft matte, transparency
threshold `12`, opacity threshold `220`, and despill. The detected key was
`#03f904`. The resulting candidate alpha is
`qa/strict-repairs/hormozing-manager/candidates/raw-alpha.png` with SHA-256
`cf51ec239bff8407868cb4f735911fa75747ce77ee5e306b99ad24d4028ddb0a`.

## Deterministic animation contract

The candidate builder must keep the selected character, face, cap, glasses,
nasal strip, beard, body, arms, hands, book geometry, crop, scale, and anchor
pixel-locked in all four authored phases. It may add the fixed `$100M` title
and animate only three value bars plus a final small gold glint inside the book
effect mask. No generated text, whole-character movement, independent redraw,
camera motion, or changes outside that mask are allowed.

The intended reversible playback is `[0, 1, 2, 3, 2, 1]` with durations
`[210, 140, 140, 210, 140, 140]` milliseconds. Release approval remains
conditional on the separate root and independent visual QA gates.
