# Thrillering claw-step candidate — independent strict audit

## Verdict

**PASS** — `/tmp/thrillering-marketing-claw` clears the requested low, wide Thriller claw-step action and the strict loader-artifact gate.

## Reference/action match

- The red, black-trimmed Thriller-style jacket, black trousers, white socks, and black loafers read immediately at 128px.
- Every authored pose remains in a deep, wide crouch with visibly bent knees and lowered hips. This is materially different from an upright shoulder-pop loop.
- Frames 0 and 2 alternate a lateral torso/weight pitch while the elbows stay out and the wrists/fingers hang in loose zombie claws. Frames 1 and 3 are distinct low transition poses, so the action reads as a left-to-right crouched claw-step rather than a static costume with an effect pasted over it.
- The 128px source and decoded-GIF contacts preserve the pose and action readability.

## Full-size four-cell inspection

- All four 627px cells were inspected individually.
- Anatomy remains coherent: one head, two attached arms, two attached hands, two legs, and two grounded feet in every cell; no extra/detached limbs or merged hand remnants.
- The hand silhouettes retain limp wrists and separated claw fingers without a three-hand/extra-finger read.
- Face, beard, hair, jacket construction, black trim, trousers, socks, and shoes remain recognizably continuous across the four redraws.
- No trash, chroma-green residue, floating fragments, detached pixels, or accidental extra props were found. Each cell has one significant connected foreground component and zero green-dominant opaque pixels.
- Crop is clear. The minimum authored-cell margin is 60px; no hair, hands, elbows, knees, or shoes touch the canvas edge.

## GIF/loop inspection

- Canonical GIF: 256×256, six frames, loop 0.
- Exact decoded sequence is `[0, 1, 2, 3, 2, 1]`, producing a reversible left-centre-right-centre loop with no hard D→A teleport.
- Durations are `[210, 140, 140, 210, 140, 140]` ms.
- GIF margins remain safe: at least 22px horizontally, 25px below, and 44px above.
- The decoded GIF retains the authored action and contains no crop, disposal trail, colour-key fringe, ghost limb, or frame residue.

## Registration judgment

The structural checker flags large silhouette/XOR changes because the arms, torso, and stance deliberately traverse between four distinct dance poses. Visual inspection shows coherent, directional weight travel rather than random whole-character redraw jitter: the low stance, identity, outfit, floor relationship, and anatomical construction remain consistent while the alternating claw pose changes. The warning is therefore expected motion, not a release blocker.

## Exact candidate hashes

- Source: `68d6b6a7e2e7c9e4529957692bff5c6b7bc17ae4a95b3a2aa6b4d854ed1536ec`
- GIF: `cef86e9c98145bec9060b8664509f0c480053ad059f1e34a3f9e6405a4904ada`

