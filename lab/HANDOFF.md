# Handoff

## Read first

1. `lab/STATE.md`
2. `lab/registry/queue.json`
3. `lab/experiments/EXP-WET-001/README.md`
4. `lab/experiments/EXP-WET-001/R077-DIGITAL-GATE.md`
5. `lab/experiments/EXP-WET-001/contracts/measurement-summary.schema.json`
6. `src/energy_lab/wet_metrology.py`
7. `lab/protocols/EXPERIMENT-GATES.md`

## Current bottleneck

R077 closed the remaining WET-01 digital/metrology ambiguity. The PASS/INCONCLUSIVE/FAIL rule and uncertainty propagation are frozen before hardware data. The remaining actionable desk bottleneck is now physical experiment specification: exact pressure-rated geometry/tolerances, sensor choices/locations, transfer-function calibration, calorimetry, DRY→WET procedure, data provenance and safety packet.

TO-01 remains waiting-hardware at its R076 matched 4-stage calibration boundary.

## Next recommended role

`experimentalist-metrologist`.

## Exact next mission

Execute `T-WET-HARDWARE-PACKET`. Preserve the frozen `r_h≈0.25 mm`, 5 Hz, ~10 bar, p-hat≈20/40 kPa point and 0.30 mm comparison only. Convert EXP-WET-001 into a buildable measurement packet with exact channels, bandwidth/phase calibration around 1/3/5/7/10 Hz, mechanical/pressure tolerances, hot/cold calorimetry, synchronized clock requirements, raw-data/provenance manifest, controls, repeatability, and pressure/thermal safety boundaries. Do not claim any hardware has been run.

## R077 guardband to preserve

With illustrative sigma(Re)/Re=5%, phase sigma=2° and wet-loss sigma=0.2 W, clean 95%-bound PASS needs nominal roughly `119.73 kW m^-3 K^-1`, `|phase|<=26.08°`, and `wet loss<=1.908 W`. The raw physical gates remain 108 kW/m³K, 30° and 2.3 W with <=5% work/energy/repeatability quality checks.

## Run-number warning

`R078` was explicitly abandoned unpublished during an earlier concurrency recovery and must never be reused. `run-counter.json` therefore sets the next publishable research number to **R079**.

## Hard rules

- Do not reopen WET pore/frequency optimization.
- Do not generate more TOEC stage-count cases without matched module evidence.
- Keep PROPOSED/SIMULATED/BENCH-MEASURED labels separate.
- A calibrated summary JSON is not enough for promotion without raw/calibration provenance.
- Do not claim GitHub Actions passed unless the workflow result is actually observed.

## Stop condition

Once the hardware packet is precise enough that a competent builder/metrologist could execute the coupon test without inventing missing measurement logic, set WET-01 to waiting-hardware. If no other desk branch has an uncertainty-reducing task, portfolio review may then seed the next independent invention branch instead of polishing WET geometry.
