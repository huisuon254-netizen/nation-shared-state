# NATION 1.2 Shared State

This repo is the single source of truth for all 7 NATION nodes.

## Structure
- `tasks/` — task queue and results
- `artifacts/` — all generated files (content-addressed)
- `state/` — node registry, heartbeat, settings
- `packages/` — versioned deliverables

## How it works
1. Orchestrator writes a task to `tasks/queue/`
2. Any node picks up the task, executes, writes result to `tasks/done/`
3. Artifacts are stored in `artifacts/` with sha256 names
4. Packages are assembled in `packages/`

All nodes `git pull` before dispatch and `git push` after completion.
