# Architect Builder Loop Contract

Frozen on: 2026-06-11

## Roles

| Role | Allowed | Forbidden |
| --- | --- | --- |
| Architect | Judge evidence, arbitrate disagreements, define next slice, reject scope creep | Implementation code, self-grading, vague acceptance criteria |
| Builder | Implement the architect spec, verify APIs, run tests, update repo memory | Silent compliance, silent scope additions, editing frozen contracts after coding starts |
| Reviewer | Check changed files against spec, tests, and frozen contracts | Feature code, praise, interpretation without evidence |
| Human | Continue, kill, modify, ship | Acting as the repo memory |

## Required Loop

1. Architect reads `docs/HANDOFF.md` and frozen docs.
2. Architect rules on open disagreements.
3. Architect writes one small slice spec with acceptance criteria and
   out-of-scope items.
4. Builder responds with a plan and mandatory disagreements before coding.
5. Builder freezes shared contracts in `docs/contracts/`.
6. Builder implements only the slice.
7. Reviewer returns `APPROVE` or numbered defects.
8. Builder updates `docs/HANDOFF.md` with raw results only.
9. Architect/human decides the next move.

## Hard Rules

- Repo docs are the memory. If it is not in `docs/HANDOFF.md` or frozen docs, it
  did not happen.
- Success criteria freeze before results exist.
- The builder never grades its own work.
- Disagreement is mandatory before implementation.
- Architect time is for judgment. Builder time is for execution.
- Nothing merges without reviewer approval.
- Frozen contracts are read-only during a slice unless the architect explicitly
  reopens them.

## Scope Gate

Use this loop for serious work only:

- production Homies features
- Realist.ca feature slices
- CRM/lead routing workflows
- billing, auth, data models, schemas, APIs
- multi-module refactors
- sophisticated OpenClaw skills

Do not use it for trivial docs, one-off scripts, or quick copy fixes.

