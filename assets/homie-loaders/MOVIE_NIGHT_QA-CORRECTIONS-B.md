# Correction Batch B — Generation and QA

## Method

- Researched the real-world silhouettes and mechanics before prompting: side-to-side tilted gold-pan handling, American-football center stance/snap path, escalator step travel, surgeon/scalpel posture, U-shackle realtor lockbox construction, straight-jab mechanics, treadmill gait phases, mop sweep arc, and classic tuxedo/cuff/martini poise.
- Used built-in image generation exactly once per asset. No CLI/API fallback and no generation retries.
- Used the supplied Homie references as identity/style anchors; the lockboxing asset also used the supplied lockbox photo as a shape-only reference, and running comps used the existing stress-test sheet as a motion/perspective reference.
- Removed the generated chroma background with the installed image-generation helper, then normalized all four cells with one per-asset scale and baseline.
- Reasserted exact `#00ff00` outer edges, corners, and both two-pixel central axes.
- One isolated 5×44 px escalator sliver was found during connected-component/full-size inspection and mechanically cleared before the final master and GIF were rebuilt.

## Visual action checks

| Asset | Full-size and 128 px result |
|---|---|
| `panning-for-gold-crm` | PASS — wide left/level/right pan tilt; gold visibly traverses the black ridged pan; two connected hands throughout |
| `diamonding-in-rough-crm` | PASS — diamond starts half-buried, clears the rubble and torso, then finishes high at arm's length to viewer-right |
| `down-payment-hike-offers` | PASS — helmet, facemask, pads, jersey, pants, socks, cleats and gloves read immediately; deep center stance; single cash bag moves backward between the legs |
| `escrow-lating-offers` | PASS — same escalator silhouette in all phases; character and crow visibly advance from bottom step to top region; stray source sliver removed |
| `operating-on-file-reports` | PASS — teal scrubs, surgical cap, face mask and gloves read at 128 px; fixed coral file/table; scalpel progresses across seam |
| `lockboxing-offers` | PASS — male boxer, robe/trunks/boots/gloves, one connected straight jab, recognizable unbranded U-shackle lockbox bag and clear bag pivot |
| `running-comps-cma` | PASS — large left/right knee alternation, connected gait and counter-swing; treadmill and house-card belt remain consistent |
| `deslop-reports` | PASS — bowl/table/bin composition remains registered; one cohesive blob follows a visible spoon-to-bin arc |
| `moptimizing-crm` | PASS — one bucket, one floor patch, mop remains on floor and sweeps continuously left-to-right without returning to bucket |
| `james-bonding-manager` | PASS — tuxedo/bow tie, cuff adjustment and low martini glass read at 128 px; no actor likeness, gun, logo or scenery |

## Machine checks

- All ten source masters: exact 1254×1254, RGB, regular 2×2, four distinct authored cells.
- All ten source masters: exact `#00ff00` edge/corner/axis contract.
- Minimum per-cell clearance: 60–70 px.
- All ten temporary GIFs: 256×256, transparent, six frames, four unique visual phases, loop forever.
- Playback: `0,1,2,3,2,1` with `210,140,140,210,140,140` ms durations.
- GIF sizes: 48,863–77,021 bytes, below the 750 KB production ceiling.
- Exact hashes and measurements: `/tmp/movie-corrections-b/qa.json`.
- Assembly config: `/tmp/movie-corrections-b/alignment.json`.
- Reproducible normalization: `/tmp/movie-corrections-b/process.py`; isolated-fragment cleanup: `/tmp/movie-corrections-b/clear_escrow.py`.

## Review artifacts

- Full-size four-cell contact: `/tmp/movie-corrections-b/contact/full-size-contact.jpg`
- 128 px six-frame contact: `/tmp/movie-corrections-b/contact/gif-128-contact.jpg`
- Temporary transparent GIFs: `/tmp/movie-corrections-b/gifs/`
- Accepted temp masters: `/tmp/movie-corrections-b/final/`
- Exact prompt ledger: `/tmp/movie-corrections-b/prompts.md`

No manifest, production alignment, production GIF, gallery, deployment or deletion changes were made.


