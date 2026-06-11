# Handoff

## Current Goal

Set up the Homies skills repo as the home for reusable build workflows.

## Frozen Contracts

| Contract | File | Frozen At | Owner | Notes |
| --- | --- | --- | --- | --- |
| Architect/builder operating rules | `docs/contracts/architect-builder-loop.md` | 2026-06-11 | Dan/Clyde | Initial repo contract |
| Activation policy | `docs/contracts/activation-policy.md` | 2026-06-11 | Dan/Clyde | Claude/Fable architect usage starts 2026-06-23 |

## Last Work Block

| Date | Slice | Commit/PR | Tests | Result |
| --- | --- | --- | --- | --- |
| 2026-06-11 | Seed architect/builder repo loop | `0e8cb74` | Docs only | Pushed to GitHub |

## What Was Built

| Item | File(s) | Evidence |
| --- | --- | --- |
| Repo README | `README.md` | File added |
| Handoff template | `docs/HANDOFF.md` | File added |
| Frozen loop contract | `docs/contracts/architect-builder-loop.md` | File added |
| Architect prompt | `prompts/architect.md` | File added |
| Builder goal prompt | `prompts/builder-goal.md` | File added |
| Reviewer prompt | `prompts/reviewer.md` | File added |
| OpenClaw skill | `skills/architect-builder-repo-loop/SKILL.md` | File added |
| Activation policy | `docs/contracts/activation-policy.md` | File added |

## Decisions

| Decision | Why | Decider | Date |
| --- | --- | --- | --- |
| Make a dedicated `homies-skills` repo | The named repo did not exist and the existing `homies` repo did not look like a skills library | Clyde | 2026-06-11 |
| Store workflow memory in repo docs | Keeps state portable across Claude, Codex, OpenClaw, and future agents | Dan/Clyde | 2026-06-11 |
| Delay active Claude/Fable architect usage until 2026-06-23 | Fable is included in Claude Max plan until then; build the system now but avoid active paid architect usage early | Dan | 2026-06-11 |

## Open Disagreements

| ID | Builder Position | Evidence | Architect Ruling | Status |
| --- | --- | --- | --- | --- |
| D-001 | Dedicated repo is cleaner than adding this to existing `homies` repo | `danielfoch/homies-skills` did not exist; `danielfoch/homies` appears to be a small Follow Up Boss CLI package | Pending | Open |

## Raw Verification

| Command/Check | Result | Evidence |
| --- | --- | --- |
| `gh repo view danielfoch/homies-skills` | Repo did not exist before setup | GitHub CLI returned repository not found |
| `gh repo list --limit 200` | Found `homies` and `homies-onboarding`, not `homies-skills` | GitHub CLI repo list |
| `gh repo create danielfoch/homies-skills --public --source=. --remote=origin --push` | Repo created and `main` pushed | `https://github.com/danielfoch/homies-skills` |
| `gh repo view danielfoch/homies-skills --json name,url,defaultBranchRef,description,visibility` | Repo verified | Public repo, default branch `main` |
| User activation instruction | Start using Claude/Fable loop June 23, 2026 | Telegram message 7956 |

## Next Slice Candidates

| Slice | Why Now | Risk | Size |
| --- | --- | --- | --- |
| Add a CLI/bootstrap script | Make the loop easy to install into Realist.ca and Homies repos | Low | Small |
| Add sample first Homies build spec | Prove the workflow on a real product slice | Medium | Medium |
