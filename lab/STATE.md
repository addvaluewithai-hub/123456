# Current Lab State

Updated: 2026-08-22 13:18 Africa/Cairo

## Published frontier

- Latest Sheet1 research run: **R076**
- Verdict: **NEEDS DATA**
- Active desk branch: **WET-01 — wet phase-change liquid-piston / wet thermoacoustic core + direct linear alternator**
- Hardware-waiting branch: **TO-01 — thermo-osmotic hydraulic conversion**

## What R076 changed

R076 converted the R075 TOEC optimistic-vs-conservative uncertainty into one buildable **4-stage calibration contract** instead of another stage-count sweep. The proposed rig uses 100 cm² active membrane per stage, 80→40°C thermal cascade, separate stage pressure/flow metering, hot/cold calorimetry, interstage heat accounting, blank/open-load controls and a loaded 1–5 MPa sweep within qualified hardware ratings.

The conservative N=16 package inversion is now explicit:

`0.8681/rho_A + 528.7/q_V <= 1.0463 L`

for the membrane + thermal network under the current conservative fixed-volume charges. Therefore rho_A must be at least 0.830 m²/L even if thermal-network volume vanished, and q_V at least 505 W/L even if membrane volume vanished. At rho_A=1.10 m²/L, q_V must be ~2056 W/L; at q_V=1000 W/L, rho_A must be ~1.68 m²/L. Optimistic membrane packing alone does not rescue conservative transport/thermal duty.

The proposed metrology budget is ~0.6% 1σ on hydraulic power and ~2.7% on hydraulic efficiency, much smaller than the ~3× package gap. The remaining important uncertainty is the unmeasured 4→16 stage scaling law, which must retain a separate ~15–20% sensitivity band.

## TO-01 state

TO-01 remains physically plausible but is now **waiting-hardware / NEEDS DATA**. Do not create more 16/38-stage variants. Promotion requires the matched 4-stage experiment in `lab/experiments/EXP-TO-001/R076-CALIBRATION-CONTRACT.md` to support a 95% upper projected volume <=2 L and 95% lower electric performance >=15% Carnot preferred.

## Current next task

`T-WET-METROLOGY-CODE` — implement the frozen WET-01 phase-aware coupon digital experiment and uncertainty gate. This is genuine remaining desk work and must not change the 0.25 mm / 5 Hz / 10 bar hardware point.
