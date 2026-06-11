# Builder Goal Prompt

```text
/goal: execute the architect spec.

Rules:

PHASE 0: Before any code, reply with your plan and every disagreement you have,
with reasons, citing real files in the repo. Silent compliance is failure.
Silent scope additions are failure.

PHASE 1: Freeze shared contracts first in docs. After freeze, they are read-only
for this slice unless the architect explicitly reopens them.

PHASE 2: Spawn max 3-4 lane agents only on modules that do not import each
other. Spawn one reviewer agent that never writes feature code. The reviewer
checks every lane against the spec, tests, and frozen docs, then returns APPROVE
or a numbered defect list.

PHASE 3: Nothing merges without reviewer APPROVE. Commit and push each slice if
repo policy allows. Update docs/HANDOFF.md with raw results only: tables,
commands, numbers, file paths, open disagreements. No interpretation, no
promising. Verdicts belong to the architect and human.
```

