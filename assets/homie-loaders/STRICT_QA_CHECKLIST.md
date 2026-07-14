# Homies strict loader QA checklist

This gate is deliberately stricter than the current production verifier. A technically valid GIF is not necessarily a good loader. Four distinct frames can still be a static costume pose, and large motion can still be unusable when the Homie or props redraw between frames.

## 1. Define the action contract before generation

- Record the exact loading line and a one-sentence observable signature action.
- Name the moving layer(s): hand, arm, prop, carriage, whole rigid plate, particles, etc.
- Name every element that must remain stationary: floor, table, machine, chair, sign, bucket, background prop, character torso, or camera.
- Decide whether whole-body motion is intentional. If it is not explicitly required, global subject/camera drift above 3 source pixels is a failure.
- Set a concept-specific minimum silhouette displacement. The default for a signature action is greater than 3 source pixels; stronger motions such as a jump, swing, lean, or mop stroke should require more.
- A recognizable costume is not the action. “Standing while dressed as Mario/Neo/etc.” does not satisfy “hopping,” “bullet-dodging,” or another signature verb.

## 2. Automated source-sheet gate

- Exact 1254×1254 RGB master unless the manifest explicitly declares another supported grid.
- Exact `#00ff00` on every outer-edge pixel and both pixels of every centre gutter/axis.
- Four non-empty, byte-distinct authored cells for the standard 2×2 grid.
- At least 60px content clearance in every direction of every cell.
- No foreground touches a cell boundary; no neighbouring-cell bleed.
- Report each cell's foreground area, bbox, centroid, connected-component counts, tiny fragments, and hash.
- Flag large foreground-area, bbox-size, and significant-component-count jumps. These are prop/anatomy continuity proxies and require visual adjudication.
- Preserve the audited source SHA-256. Any later source change invalidates the review and requires a complete rerun.

## 3. Motion and semantic-action gate

- Measure consecutive-cell mask XOR, silhouette displacement, centroid displacement, registration shift, and registered pixel residual.
- Fail a signature-action asset when its robust silhouette motion is at or below the policy threshold. The default threshold is intentionally above 3px.
- Fail a signature-action asset when the 128px review does not make the requested verb immediately recognizable, even if automated amplitude passes.
- Reject generic standing, scale pulsing, a tiny vertical bob, or motion ticks as a substitute for a requested jump, lean, dance, swing, handoff, tool operation, or other signature action.
- Distinguish intentional rigid motion from redraw: a translated/rotated canonical plate is acceptable; changing facial features, clothing seams, limb shapes, or prop construction is not.

## 4. Anatomy, prop, and stationary-layer gate

- Confirm exactly the intended number of hands, arms, legs, heads, tools, and props in every cell.
- Track hand-to-prop and body-to-prop contact across all cells. Grips, straps, handles, chains, cords, and hinges must not jump sides or detach.
- Confirm prop identity and geometry: the same bucket, machine, chair, sign, document, ball, vehicle, or instrument must persist unless its appearance/disappearance is the explicit action.
- Annotate stationary regions in the policy JSON. The script measures changed-pixel percentage inside each region and fails it above the declared limit.
- Treat upper-body correlation, component counts, and registered residual as proxies only. They can identify likely redraw but cannot certify anatomy.

## 5. Mandatory visual gate — every cell, both scales

No asset can pass without a completed review JSON.

For **each authored cell 0–3**:

- Open `cell-N-full.png` at its natural 627×627 size and mark `full_size_inspected: true`.
- Open `cell-N-128.png` at exactly 128×128 and mark `thumbnail_128_inspected: true`.
- Record explicit booleans for crop, anatomy, prop continuity, and unintended redraw wiggle.
- Any false or missing cell field is a hard failure.

For the **assembled loop**:

- Inspect the six-frame 128px contact in order and the actual animated GIF at 256px and 128px.
- Confirm the signature action is readable without relying on the filename/loading text.
- Confirm stationary elements do not drift and the loop looks intentional rather than like registration jitter.
- Confirm the reversible return does not create a pause, snap, extra limb, duplicated prop, or discontinuity.
- Record `signature_action_readable`, `stationary_elements_stable`, and `loop_motion_natural`. Any required false/missing verdict is a hard failure.

## 6. Production GIF contract and loop closure

- 256×256 GIF, six frames, exactly four unique visual phases.
- Equality pattern exactly `[0, 1, 2, 3, 2, 1]`.
- Durations exactly `[210, 140, 140, 210, 140, 140]` milliseconds unless a reviewed asset-specific exception exists.
- Forever loop, transparency present, all four corners fully transparent in every frame, no empty frame, and within the file-size ceiling.
- Frames 4 and 5 must be byte-equal after RGBA decoding to phases 2 and 1 respectively; this makes the final-to-first transition the reverse of the opening step.

## 7. Release lock

- Rerun strict QA after the final production assembly, not merely against a generator's temporary GIF.
- Compare final source and GIF hashes to the audited report.
- Reopen the final production GIF in the gallery at its real displayed size.
- Any post-QA replacement, alignment edit, recompression, or source change invalidates the previous pass.

## Tool usage

```sh
python3 /tmp/homie_strict_qa.py \
  sources/wildcard/example.png \
  --gif-root gifs \
  --alignment scripts/alignment.json \
  --policy /path/to/policy.json \
  --review /path/to/completed-review.json \
  --output /tmp/homie-strict-qa-example
```

First run without `--review` to generate `visual-review-template.json`, per-cell evidence, contacts, and proxy metrics. Inspect the evidence, complete the review file, then rerun. A missing visual review always fails.


