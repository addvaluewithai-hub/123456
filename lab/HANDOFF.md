# Handoff

## Read first

1. `lab/STATE.md`
2. `lab/registry/queue.json`
3. `lab/tasks/T-WET-METROLOGY-CODE.md`
4. `lab/experiments/EXP-WET-001/README.md`
5. `src/energy_lab/wet_core.py`
6. `src/energy_lab/cli.py`

## Current bottleneck

The WET-01 branch is no longer waiting for another geometry idea. It is waiting for a reproducible phase-aware measurement/model pipeline and then real coupon data.

## Next recommended role

`computational-modeler` with metrology mindset.

## Exact next mission

Implement/verify the uncertainty-aware digital experiment around the frozen 0.25 mm / 5 Hz / 10 bar point, including 0.30 mm comparison, explicit phase-error propagation, pass/inconclusive/fail logic, and deterministic machine-readable output suitable for later ingesting hardware traces.

## Stop condition

Do not invent wet-interface measurements. When the repo model/measurement contract is closed and the decisive uncertainty is genuinely hardware-only, mark WET-01 `NEEDS DATA` and allow the next desk-research task to move to TO-01 rather than creating more pore geometry variants.
