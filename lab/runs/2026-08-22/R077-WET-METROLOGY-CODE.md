# R077 — WET phase-aware metrology code

- Reserved run: `R077`
- Operational shift: `shift-20260822-1707-r077`
- Recovered from expired shift: `run-20260822-1411-r077`
- Task: `T-WET-METROLOGY-CODE`
- Branch: `WET-01`
- Role: `computational-modeler`
- Cairo date: 2026-08-22
- State before: WET-01 active / NEEDS DATA; R077 code artifacts existed under an expired un-published reservation
- State after: WET digital gate complete; hardware packet is next; branch remains NEEDS DATA

## Principal mission

Turn the frozen R073 phase-calibrated WET coupon decision rule into a deterministic uncertainty-aware computational gate and machine-readable contract without changing the 0.25 mm / 5 Hz / 10 bar point or inventing measurements.

## Success / falsification test

A fresh implementation must reproduce the frozen diffusion benchmark, propagate uncertainty into `Re{G*}/V`, force near-threshold confidence intervals to INCONCLUSIVE, support PASS/FAIL limiting cases, expose a stable JSON contract, and leave no ambiguity that only bench evidence can promote the branch.

## Reconciliation / recovery

At shift start Sheet1 ended at R076. Git contained a stale R077 claim whose lease expired at 16:11 Cairo, while `src/energy_lab/wet_metrology.py`, its regression tests, JSON schema and deterministic reference artifact already existed. Per failure recovery, the same R077 reservation was transferred to this recovery shift rather than abandoned or duplicated. R078 remains explicitly abandoned/unpublished.

## Bottleneck

The remaining desk uncertainty was not heat-engine physics or geometry; it was whether the future measured conductance/phase/loss values could be classified reproducibly without post-hoc threshold changes.

## Hypothesis

Freezing 95%-bound classification before hardware will materially reduce decision bias and show how far nominal measurements must sit inside the raw physical gate for a clean promotion.

## Counter-hypothesis

The raw R073 thresholds may be too close to realistic measurement uncertainty, leaving most plausible measurements inconclusive even when nominally favorable.

## Work performed

1. Reconciled Sheet frontier R076 against expired R077 Git state.
2. Reviewed existing `wet_metrology.py`, regression tests and committed reference artifact.
3. Independently executed the key regression equations/assertions in the tool environment; the frozen 0.25/0.30 mm diffusion values and PASS/INCONCLUSIVE/FAIL behavior matched the committed tests.
4. Added CLI support for deterministic R077 reference generation and future calibrated-summary classification.
5. Froze the calibrated measurement-summary JSON schema and embedded the predeclared gate metadata.
6. Updated CI to execute repository tests and generate the R077 metrology artifact on pushes.
7. Updated EXP-WET-001 documentation and added the durable R077 result artifact.

## Quantitative result

Frozen 5 Hz intrinsic diffusion screen:

- 0.25 mm thermal: Re=0.9060636563, phase=-16.21951592°
- 0.25 mm mass: Re=0.9304622368, phase=-13.91223196°
- 0.30 mm thermal: Re=0.8267011735, phase=-22.25402788°
- 0.30 mm mass: Re=0.8679306227, phase=-19.32516939°

For sigma(Re)/Re=5%, phase sigma=2°, wet-loss sigma=0.2 W, the nominal clean-PASS guardbands are:

- `Re{G*}/V >= 119.7337 kW m^-3 K^-1`
- `|phase| <= 26.0801°`
- `wet loss <= 1.9080 W`

Thus a nominal result at 110–115 kW/m³K cannot be called a clean pass at this uncertainty level even though it exceeds the raw 108 kW/m³K threshold.

## Energy/source/reset ledger

No bench generation is claimed. The eventual converter source remains the real low-grade thermal gradient. Experimental piston/servo forcing is identification energy only. Reset remains evaporation/condensation plus liquid replenishment in the eventual cyclic engine. The R077 task changes only the measurement decision layer, not the thermodynamic source balance.

## Validation evidence

Evidence state: **ANALYTICAL / COMPUTATIONAL METROLOGY DESIGN**.

Independent regression execution during the shift passed the key scientific cases. Push-triggered GitHub Actions was configured to run `pytest -q`, repository-state validation and deterministic metrology snapshot generation. The connector did not expose a completed workflow result for the push, so CI success is not claimed.

## Adversarial review

- Delta-method propagation assumes approximately independent, locally linear uncertainties; strongly non-Gaussian fitted covariance should later be propagated by bootstrap/Monte Carlo from the real identification fit.
- The code consumes a calibrated summary, not raw traces. Raw calibration/provenance is still mandatory for scientific promotion.
- The intrinsic diffusion screen omits wall/contact/wet-film/interface kinetics; favorable reference values therefore cannot promote the branch.
- A failed energy-closure/repeatability gate yields INCONCLUSIVE, not a false physics PASS or FAIL.

## Verdict

`NEEDS DATA`.

The metrology-code uncertainty is closed, but the branch still depends on physical wet-coupon data.

## Handoff

Next task: `T-WET-HARDWARE-PACKET` under `experimentalist-metrologist`. Freeze exact pressure-rated coupon geometry/instrumentation/calibration/BOM-level measurement contract and then mark WET-01 waiting-hardware if no further desk uncertainty remains. Do not reopen pore/frequency optimization.
