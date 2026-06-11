# Activation Policy

Frozen on: 2026-06-11

## Effective Date

The Claude/Fable architect loop must not be used for active serious builds until
2026-06-23.

## Before 2026-06-23

Allowed:

- Prepare repo docs.
- Prepare prompt templates.
- Prepare handoff templates.
- Run Codex-only implementation work when Dan asks.
- Manually review the workflow design.

Forbidden:

- Paid Claude/Fable architect sessions for production decisions.
- Automated Claude/Fable architect runs.
- Cron jobs that invoke the architect loop.
- Treating Claude/Fable output as a required gate for merges.

## On Or After 2026-06-23

Allowed:

- Use Claude/Fable as architect and judge for serious builds.
- Use Codex as builder.
- Use reviewer agents as evidence gates.
- Use `docs/HANDOFF.md` and `docs/contracts/` as repo memory.

## Reason

Fable is included in the Claude Max plan until 2026-06-23. The paid architect
workflow should start only after that date so the system is ready without
wasting paid API spend early.

