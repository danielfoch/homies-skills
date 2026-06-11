# Architect Builder Repo Loop

Use this skill when Dan wants a serious software build run through a split
architect/builder loop: Claude or another strong reasoning model provides
judgment and specs, Codex executes, the repo stores state, and a reviewer gate
blocks unverified work.

## Principle

The loop is simple:

1. Architect thinks and judges.
2. Builder implements and verifies.
3. Repo remembers.
4. Human decides continue, kill, modify, or ship.

This is for serious builds only: Realist.ca, Homies, production workflows,
schema/API changes, multi-module work, or any task where architecture mistakes
are expensive.

## Definition Of Done

A work block is done only when:

- The slice has a paste-ready architect spec.
- The builder has stated disagreements before coding.
- Shared contracts are frozen in docs before implementation.
- Implementation has raw verification evidence.
- A reviewer that did not write feature code returns APPROVE or numbered
  defects.
- The repo handoff is updated with facts, tables, numbers, and open
  disagreements.
- The human/architect gets a crisp verdict request: continue, kill, modify, or
  ship.

## One-Time Repo Setup

For each serious repo, create:

- `docs/HANDOFF.md`
- `docs/contracts/`
- `docs/architecture-decisions/`

Rule: if it is not in `docs/HANDOFF.md` or frozen docs, it did not happen.

## Operating Rules

- Disagreement is mandatory before coding.
- Verify APIs, SDKs, payloads, routes, auth, and file formats against current
  reality before coding.
- Freeze success criteria before results exist.
- Never edit frozen contracts after implementation starts unless the architect
  reopens them.
- Keep slices small enough for one PR.
- Do not let lane agents work on modules that import each other.
- Reviewer agents cannot write feature code.
- Builder never grades its own work.
- Update `docs/HANDOFF.md` after each work block.

## Prompts

Use the repo prompt templates:

- `prompts/architect.md`
- `prompts/builder-goal.md`
- `prompts/reviewer.md`

## Cost Guardrails

- Default to Codex for build work.
- Use Claude only after repo state is compressed into `docs/HANDOFF.md` and
  relevant frozen docs.
- Prefer one architect session per work block.
- Ask Dan before running long paid architect loops.
- If the Anthropic key is missing or unfunded, run the same architecture prompt
  manually in the Claude app until API funding is ready.

## Final Report To Dan

Keep it short:

- Slice completed or blocked.
- PR/commit link if available.
- Reviewer verdict.
- Tests/checks run.
- Open disagreements needing architect/human ruling.
- Next recommended slice.

