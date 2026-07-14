# Character-assignment correction batch

Accepted 2026-07-13. Each loader uses one SHA-locked canonical plate and a
deterministic local-motion rig from `scripts/repair_character_assignment_batch.py`.
No final animation frame was independently redrawn.

## `barbie-ing-listings`

- Identity/style reference: `references/reports.png`
- Costume/action reference: prior `sources/wildcard/barbie-ing-listings.png`
- Accepted raw: `qa/strict-repairs/raw/barbie-ing-listings-female-canonical-v2.png`
- Raw SHA-256: `d92ad128433f92dc39618c915f84fe124d7bfe2317b4a002eba2d811c92980e2`

```text
Create one single full-body canonical Homies AI plate, not a sprite sheet.
Image 1 is the authoritative adult female identity and ink/watercolour style
reference. Image 2 supplies pink costume/action inspiration only and must not
supply its male face or body. Depict one clearly female Homie in a coordinated
bright-pink tailored blazer and knee-length skirt, pink heels, heart-shaped pink
sunglasses and a blonde high ponytail. One hand rests on her hip; the opposite
connected distal forearm points into clear space. Keep the connected ponytail
tail clear for rigging. Exactly one woman, two arms and two hands. Exact solid
#00ff00 background, generous clearance, no text, logos, scenery, shadow, extra
parts, clay, 3D, vector mascot or photorealism.
```

Rig: only the connected pointing forearm and ponytail tail counter-move around
fixed joints. Face, sunglasses, hair cap, torso, planted hand, skirt, legs and
heels remain fixed.

## `pulp-fictioning-manager`

- Identity/style reference: `references/manager.png`
- Pose-only reference: superseded female `pulp-fictioning-reports` source
- Accepted raw: `qa/strict-repairs/raw/pulp-fictioning-manager-canonical-v1.png`
- Raw SHA-256: `0c31fa822b4fbc02f48eed1cc93d6da94aeb7d06c4bcc89e2ac175bb788671e2`

```text
Create one single full-body canonical Homies AI plate, not a sprite sheet.
Preserve the clearly adult male Manager Homie identity, male proportions and
fine ink-and-watercolour style. Use the prior source only for the bent-knee
twist pose and black-suit contrast; replace its woman entirely. Dress the man
in a black tailored suit, white shirt, slim bolo-style tie, black shoes and dark
slicked-back shoulder-length hair. Both connected distal forearms occupy clean
separate space for counter-rotation around visible fixed elbows. Exactly one
man, two arms and two hands. Exact solid #00ff00 background, no cigarette,
props, text, shadow, scenery, extra anatomy, clay, 3D or photorealism.
```

Rig: both connected distal forearms counter-swing while the male head, hair,
bolo tie, torso, pelvis, legs and shoes remain fixed. The old
`pulp-fictioning-reports` production asset is retired.

## `michael-burrying-manager`

- Identity/style reference: `references/manager.png`
- Composition reference: user-provided desk-drumming still
- Rejected raw v1: `qa/strict-repairs/raw/michael-burrying-manager-canonical-v1.png`
- Accepted raw v2: `qa/strict-repairs/raw/michael-burrying-manager-canonical-v2.png`
- Raw v2 SHA-256: `c55e7eca21c8cc53353274932aa827899739ebd3c994ce7faef60838c7be8c10`

```text
Create one single canonical male Manager Homie plate seated behind one fixed
office desk, wearing a faded slate-blue logo-free pocket T-shirt and visibly
connected wired earbuds. He holds exactly two wooden drumsticks in exactly two
hands. Both visible elbows remain fixed; each connected distal forearm, hand
and entire stick occupies clear space for independent rotation. Lower the desk
to the bottom fifth and keep both stick tips clear of it in the canonical plate.
One chair and one neat blank paper stack may remain fixed. Exclude bottles,
keyboard, monitor, wall art, other people, text, logos, notes, debris and extra
anatomy. Exact solid #00ff00 background and canonical ink/watercolour style;
no clay, 3D, vector mascot or photorealism.
```

Rig: the two connected forearm-hand-stick units alternate strokes. Head, hair,
earbud wires, shirt core, chair, papers and desk remain fixed.

## `harvey-spectering-manager`

- Identity/style reference: `references/manager.png`
- Accepted raw: `qa/strict-repairs/raw/harvey-spectering-manager-canonical-v1.png`
- Raw SHA-256: `8da32e0fc4997570f0ff484a860250b5710f628a1cd05c047b6365ff91063e5f`

```text
Create one single full-body canonical adult male Manager Homie plate as a
razor-sharp television closer-lawyer archetype: charcoal tailored suit, crisp
white shirt, deep navy tie, black shoes, confident side part and calm half
smile. One fixed hand holds a blank manila case folder low at the hip. The
opposite connected distal forearm and hand sit in open space for a compact
cuff/lapel adjustment around a visible fixed elbow. Exactly one man, two arms,
two hands and one folder. Exact solid #00ff00 background, generous clearance,
no office scenery, text, logos, gavel, scales, shadow, extra anatomy, clay, 3D,
vector mascot or photorealism.
```

Rig: only the cuff/lapel forearm moves. Male face, hair, tie, suit core, folder,
other arm, legs and shoes remain fixed.

## Export and QA contract

- Source: 1254×1254 RGB, exact 2×2 cells of 627×627.
- One union crop, scale and bottom anchor; 60 px minimum source clearance.
- GIF: 256×256 transparent, shared 95-colour palette, disposal 2.
- Phase sequence: `[0,1,2,3,2,1]`.
- Durations: `[210,140,140,210,140,140]` ms.
- Strict report: `qa/strict-repairs/character-assignment-batch/report-final/strict-qa.md`.
