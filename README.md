# Homies Skills

Reusable operating skills and repo-native playbooks for building Homies with
agentic workflows.

## Current Skills

- `architect-builder-repo-loop`: Claude acts as architect and judge, Codex acts
  as builder, the repo stores state, and reviewer gates block unverified work.

## Activation Policy

The architect/builder loop is built now, but Claude/Fable architect usage starts
on **2026-06-23**. Until then, this repo is for docs, prompts, contract
templates, and dry-run preparation only.

Before 2026-06-23:

- Do not run paid Claude/Fable architect sessions.
- Do not wire this into recurring production build loops.
- Do not treat Claude/Fable rulings as an active project dependency.

On or after 2026-06-23:

- Use Claude/Fable only for architect judgment, arbitration, and next-slice
  specs.
- Keep Codex as the builder.
- Keep repo docs as the memory.

## Repo Memory

Serious work should use repo-owned memory:

- `docs/HANDOFF.md` for current state and raw verification results
- `docs/contracts/` for frozen schemas, interfaces, API formats, and acceptance
  gates
- `docs/architecture-decisions/` for lightweight decisions that should survive
  the chat window

Rule: if it is not in the repo docs, it did not happen.
