# Energy Research Lab

A persistent invention/research operating system for exploring physically defensible energy architectures.

## Start here

Every scheduled research agent starts at [`lab/RUNNER.md`](lab/RUNNER.md). Do not reconstruct the lab from chat memory.

## Two-layer memory model

- **GitHub = operational and executable source of truth.** Queue, claims, roles, branch state, decisions, models, code, experiment manifests, run logs, and handoffs live here.
- **Google Sheet = append-only scientific ledger + human dashboard.** `Sheet1` is the immutable R001… research record. It is not the task queue.

Google Sheet: https://docs.google.com/spreadsheets/d/1WaDyqw91D8Ol8bgeX1NJ1e0nW7h1tFShoWW-BLR4sCQ/edit

## Current frontier

Latest published research run at infrastructure bootstrap: **R073** (`NEEDS DATA`). The leading branch is a wet phase-change liquid-piston / thermoacoustic core with direct linear alternator. The frozen first hardware point is approximately `r_h=0.25 mm`, `f=5 Hz`, `P_mean=10 bar`, with DRY→WET tests at about 20/40 kPa acoustic amplitude.

Promotion gate: `Re{G*}/V >= 108 kW m^-3 K^-1`, total physical phase preferably `<30°`, wet dissipative loss `<2.3 W`, with calibrated uncertainty and a complete package path to ~10 W DC in <=2 L.

## Repository map

- `lab/RUNNER.md` — authoritative scheduler entrypoint
- `lab/CHARTER.md` — mission and non-negotiables
- `lab/OPERATING-SYSTEM.md` — runtime/state architecture
- `lab/STATE.md` / `lab/HANDOFF.md` — concise current truth
- `lab/registry/queue.json` — claimable work queue
- `lab/registry/run-counter.json` — collision-safe research-run allocation
- `lab/registry/branches.json` — portfolio state
- `lab/protocols/` — scientific and operational contracts
- `lab/tasks/` — task workspaces
- `lab/experiments/` — experiment manifests and gates
- `lab/runs/` — append-only shift/run logs
- `src/energy_lab/` — executable models and validation utilities
- `tests/` — regression tests

The scheduler is only a wake-up mechanism. Durable truth must survive in Git and the Sheet so a fresh agent with no conversation history can continue safely.
