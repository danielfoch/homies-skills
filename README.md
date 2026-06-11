# Homies Skills

Reusable operating skills and repo-native playbooks for building Homies with
agentic workflows.

## Current Skills

- `architect-builder-repo-loop`: Claude acts as architect and judge, Codex acts
  as builder, the repo stores state, and reviewer gates block unverified work.

## Repo Memory

Serious work should use repo-owned memory:

- `docs/HANDOFF.md` for current state and raw verification results
- `docs/contracts/` for frozen schemas, interfaces, API formats, and acceptance
  gates
- `docs/architecture-decisions/` for lightweight decisions that should survive
  the chat window

Rule: if it is not in the repo docs, it did not happen.

