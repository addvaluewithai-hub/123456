# Energy Research Lab

A persistent invention/research operating system for exploring physically defensible energy architectures.

## Start here

Every scheduled research agent starts at [`lab/RUNNER.md`](lab/RUNNER.md). Do not reconstruct the lab from chat memory.

## Two-layer memory model

- **GitHub = operational and executable source of truth.** Queue, claims, roles, branch state, decisions, models, code, experiment manifests, run logs, and handoffs live here.
- **Google Sheet = append-only scientific ledger + human dashboard.** `Sheet1` is the immutable R001… research record. It is not the task queue.

Google Sheet: https://docs.google.com/spreadsheets/d/1WaDyqw91D8Ol8bgeX1NJ1e0nW7h1tFShoWW-BLR4sCQ/edit

## Current frontier

Latest published research run: **R074** (`PROMISING`). R074 correctly pivoted desk research from the hardware-blocked wet phase-change branch to **TO-01 thermo-osmotic hydraulic conversion** and found materially stronger 2025 evidence for resistance-reduced multi-stage TOEC.

The next computational question is whether the reported/modelled membrane-level performance survives a complete stage-by-stage heat-recovery and packaging model strongly enough to support ~10 W DC in <=2 L.

The wet phase-change branch remains preserved as a leading hardware candidate, not discarded: its decisive next evidence is the phase-calibrated 0.25 mm / 5 Hz / 10 bar coupon.

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
