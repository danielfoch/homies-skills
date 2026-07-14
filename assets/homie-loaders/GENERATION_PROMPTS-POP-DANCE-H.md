# Pop & Dance batch H — Checking the Backstreets prompt ledger

## `checking-the-backstreets-marketing`

- Character anchor: `references/marketing.png`
- Wardrobe and choreography anchor: user-supplied boy-band reference
- Accepted generated plate: `qa/strict-repairs/raw/checking-the-backstreets-marketing-generated.png`
- Deterministic release builder: `scripts/repair_checking_the_backstreets.py`
- Final source: `sources/wildcard/checking-the-backstreets-marketing.png`
- Final GIF: `gifs/wildcard/checking-the-backstreets-marketing.gif`

```text
Use case: precise illustration rebuild for a four-phase loading-animation sprite.
Identity: preserve the exact male Marketing Homie face, short dark hair, full beard,
ink-and-watercolor linework, proportions, and restrained editorial finish from the
Marketing reference.
Wardrobe: one consistent black wide-brim hat, dark aviator sunglasses, black bomber
jacket, long untucked white shirt, ripped black jeans, and black boots.
Action: use a wide bent-knee stance and perform sharp opposing open-hand boy-band arm
hits. One connected sleeve, forearm, and natural open hand sweeps upward as the other
complete connected arm sweeps downward, then they pass through centre and reverse.
The gesture must read clearly at 128px without moving the camera or redrawing the body.
Composition: one uncropped full-body Homie on a perfectly flat exact #00ff00 field,
with generous clearance. No scenery, floor line, shadow, text, logo, watermark,
extra limbs, detached pieces, or satellite debris.
Continuity: keep the hat, aviators, face, beard, jacket core, long white shirt, hips,
ripped jeans, legs, boots, scale, camera, and palette identical. Exactly two connected
arms and two natural hands remain attached at consistent shoulders in every phase.
```

The accepted generated plate supplies one canonical full-body pose. The release
builder SHA-locks that plate, extracts the two complete connected sleeve-forearm-hand
units, and rotates them in opposing phase pairs `(-8°, 8°)`, `(-2.5°, 2.5°)`,
`(2.5°, -2.5°)`, and `(8°, -8°)`. Fixed shoulder joint disks keep both arm seams
continuous. One union crop, scale, bottom anchor, reversible sequence, and shared GIF
palette prevent redraw wiggle, crop drift, and shimmer.
