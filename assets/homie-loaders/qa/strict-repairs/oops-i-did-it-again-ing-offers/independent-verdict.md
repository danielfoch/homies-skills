# Oops chest-reach v4 — independent strict audit

## Verdict

**PASS** — `/tmp/oops-chest-reach-v4` satisfies the supplied Oops references, the exact pose/outfit contract, and both authored-source and decoded-GIF invariance gates.

## Reference/action match

- The outfit reads as one uninterrupted, glossy, saturated-red high-neck spandex catsuit from neck through the red footwear. There is no black belt, contrasting trouser panel, jacket, or casual-clothing read.
- One arm is straight and horizontal at shoulder height; the opposite open palm remains flat across the chest.
- The legs remain distinctly crossed in every phase.
- The pose remains legible in both source-128 and decoded-GIF-128 contacts.

## Four-cell source inspection

- All four 627px cells were inspected individually. Their pixels are byte-for-byte identical to the already inspected v3 source cells; only the GIF encoding changed in v4.
- Anatomy is coherent in every cell: one head, two attached arms/hands, two legs, and two feet; no doubled hand, detached finger, extra limb, or merged redraw remnant.
- The reaching palm changes orientation/height subtly while staying connected to a continuous horizontal arm. The opposite chest palm remains fully stable.
- The foreground bounding box is identical in all four cells: `(154, 65)–(473, 562)`. Minimum authored-cell margin is 65px.
- Each cell has one connected foreground component. No green/chroma residue, floating fragment, trash, seam, or crop was found.

## Exact no-jiggle proof

- In the authored 627px cells, every changed pixel is confined to the extended forearm/hand area; head, chest hand, torso, hips, crossed legs, and feet have zero changed pixels.
- In the four unique decoded GIF phases, every RGBA pixel at `x < 132` is **exactly identical**, including transparency and colour. The only decoded differences are at `x142–192`, `y59–75`, inside the reaching forearm/hand.
- This independently confirms that v4's shared palette removed fixed-body colour shimmer as well as positional jiggle.
- The decoded foreground bounding box is identical in all six GIF frames: `(63, 27)–(193, 229)`.

## Motion visibility and GIF

- Consecutive motion is confined to the intended reach extremity. Relative to phase 0, phases 1–3 change 408, 499, and 554 decoded pixels respectively in that arm region, so the hand/forearm motion remains visible while the body stays locked.
- Canonical GIF is 256×256, transparent, six frames, infinite loop.
- Exact decoded sequence is `[0, 1, 2, 3, 2, 1]` with durations `[210, 140, 140, 210, 140, 140]` ms, giving a reversible eased loop without a D→A jump.
- GIF margins are safe: 63px left/right, 27px above, and 27px below.
- No disposal trail, palette debris, chroma fringe, ghost anatomy, crop, or source/GIF semantic mismatch was found.

## Exact v4 hashes

- Source: `bf7f632f6f869210f99e33dedf9805182a44765fd1b201af57bd8da4a29b799b`
- GIF: `268893b78d9de5affae5392311f915433e14333400c725cde6d6eaef15350e6d`

