# Current Lab State

Updated: 2026-08-22 17:16 Africa/Cairo

## Published frontier

- Latest Sheet1 research run: **R077**
- Verdict: **NEEDS DATA**
- Active desk branch: **WET-01 — wet phase-change liquid-piston / wet thermoacoustic core + direct linear alternator**
- Hardware-waiting branch: **TO-01 — thermo-osmotic hydraulic conversion**
- Next publishable R-number: **R079** (`R078` is explicitly abandoned and must not be reused)

## What R077 changed

R077 recovered an expired but unpublished reservation safely, validated the existing WET metrology implementation, and froze the R073 decision rule into deterministic code before any hardware measurements are observed.

The repo now has:

- `src/energy_lab/wet_metrology.py` for uncertainty propagation and PASS/INCONCLUSIVE/FAIL classification;
- `tests/test_wet_metrology.py` scientific regressions;
- `lab/experiments/EXP-WET-001/contracts/measurement-summary.schema.json` for calibrated summary input;
- `lab/experiments/EXP-WET-001/reference/R077-metrology-gate.json` deterministic reference;
- CLI commands `wet-metrology-snapshot` and `wet-classify`;
- CI configured to run repository tests and generate the deterministic R077 reference on push.

No CI pass is claimed because the available connector did not expose the completed push workflow status during the shift. Key regression assertions were independently executed in the tool environment and passed.

## R077 quantitative guardband

The frozen 5 Hz diffusion screen still reproduces the accepted 0.25 mm point: thermal phase ~-16.22° and mass phase ~-13.91°. The 0.30 mm comparison remains materially slower (~-22.25° thermal, ~-19.33° mass).

If the final fitted in-phase conductance has ~5% 1-sigma relative uncertainty, phase sigma is 2°, and wet-loss sigma is 0.2 W, a **clean 95%-bound PASS** requires nominal approximately:

- `Re{G*}/V >= 119.73 kW m^-3 K^-1`;
- `|phase| <= 26.08°`;
- `wet loss <= 1.908 W`.

A nominal result near 110–115 kW/m³K is therefore still inconclusive at that uncertainty even though it exceeds the raw 108 kW/m³K threshold.

## WET-01 state

WET-01 remains **NEEDS DATA**. The digital decision layer is closed; one desk task remains to freeze the exact buildable hardware/instrumentation/calibration/safety packet. After that the branch should become waiting-hardware rather than reopen geometry optimization.

## TO-01 state

TO-01 remains **waiting-hardware / NEEDS DATA** at the R076 4-stage matched calibration boundary. Do not create more stage-count variants without new physical module evidence.

## Current next task

`T-WET-HARDWARE-PACKET` — freeze exact pressure-rated coupon dimensions/tolerances, instrumentation, dynamic transfer-function calibration, DRY→WET procedure, data provenance, BOM-level measurement contract and safety boundaries without claiming physical operation.
