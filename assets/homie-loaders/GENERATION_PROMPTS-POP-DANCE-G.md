# Pop & Dance batch G — Smooth-Crimining prompt ledger

## `smooth-crimining-marketing`

- Character anchor: `references/marketing.png`
- User motion and wardrobe reference: `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-f7c6f481-7af2-42c9-b83d-240b876ca07f.png`
- Accepted generated plate: `qa/strict-repairs/raw/smooth-crimining-marketing-generated.png`
- Deterministic release builder: `scripts/repair_smooth_crimining_lean.py`
- Final source: `sources/wildcard/smooth-crimining-marketing.png`
- Final GIF: `gifs/wildcard/smooth-crimining-marketing.gif`

```text
Use case: precise illustration rebuild for a four-phase loading-animation sprite.
Identity: preserve the exact male Marketing Homie face, short dark hair, full beard,
ink-and-watercolor linework, proportions, and restrained editorial finish from the
Marketing reference.
Wardrobe: one consistent ivory-white pinstripe suit, slate-blue shirt, white fedora
with a black band, black upper-arm band, white socks, and black-and-white loafers.
Action: reproduce the supplied iconic gravity-defying forward lean. Start in a
strong lean, deepen through two connected full-body phases, reach the strongest
ankle-anchored lean, then return through the reversible runtime sequence. The body
must remain one continuous figure; both shoes and sole contacts stay fixed.
Composition: one uncropped full-body Homie on a perfectly flat exact #00ff00 field,
with generous clearance. No scenery, floor line, shadow, text, logo, watermark,
extra limbs, detached pieces, or satellite debris.
Continuity: keep the same face, hat, armband, suit construction, pinstripes, arms,
hands, legs, shoes, scale, camera, and palette. Motion must come from one locked
character plate, not independently redrawn characters.
```

The accepted generated plate supplies one canonical lean pose. The release
builder SHA-locks that plate and authors four deterministic phases using a
progressive ankle-anchored shear `(0.000, 0.040, 0.080, 0.120)`. Rows containing
the ankle cuffs, socks, shoes, soles, and floor-contact pixels are copied
byte-for-byte into every phase. One union crop, scale, bottom anchor, reversible
sequence, and shared GIF palette prevent redraw wiggle, crop drift, and shimmer.
