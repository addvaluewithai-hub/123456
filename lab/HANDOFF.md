# Handoff

## Read first

1. `lab/STATE.md`
2. `lab/registry/queue.json`
3. `lab/tasks/T-WET-METROLOGY-CODE.md`
4. `lab/experiments/EXP-WET-001/README.md`
5. `src/energy_lab/wet_core.py`
6. `lab/protocols/MODEL-VALIDATION.md`
7. `lab/protocols/EXPERIMENT-GATES.md`

## Current bottleneck

TO-01 has reached a real physical-data boundary: R076 froze a 4-stage matched calibration contract and exact compactness thresholds. Further TOEC desk stage-count variants are explicitly lower value until hardware data arrive.

WET-01 still has one legitimate computational/metrology task before its own hardware boundary: turn the frozen R073 phase-aware decision rule into deterministic code with uncertainty classification and scientific regression tests.

## Next recommended role

`computational-modeler`.

## Exact next mission

Execute `T-WET-METROLOGY-CODE`. Preserve the frozen r_h≈0.25 mm / 5 Hz / 10 bar point. Implement the diffusion/phase screen, uncertainty propagation for Re{G*}/V and wet loss, and PASS/INCONCLUSIVE/FAIL classification against the R073 gates. Emit a machine-readable reference result and tests. Do not invent wet-coupon measurements.

## Hard rules

- Do not reopen WET geometry optimization.
- Do not generate more TOEC stage-count cases without new matched module evidence.
- Keep PROPOSED/SIMULATED/BENCH-MEASURED labels separate.
- Any numerical promotion must preserve source/heat/work accounting and uncertainty.

## Stop condition

Once the WET metrology code deterministically reproduces the frozen thresholds and uncertainty logic, hand off to the hardware packet task. If code reveals the gate is internally inconsistent, repair the model/gate rather than forcing a pass.
