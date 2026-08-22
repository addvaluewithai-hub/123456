# EXP-TO-001 — Multi-stage thermo-osmotic calibration gate

Status: **PROPOSED / WAITING HARDWARE**
Branch: TO-01
Latest run: R076

## Current question

Can matched 4-stage measurements of loaded hydraulic power density, thermal-to-hydraulic efficiency, heat recovery, header loss and physical package density support a credible 10 W DC / <=2 L N≈16 scale path?

## Durable evidence

- Foundational thermo-osmotic pressure generation against hydraulic back-pressure is published experimental evidence.
- Li et al. 2021 published a pump-free multistage experiment at 1.39±0.25 W/m²; its 30-stage 2.72% / 14 W/m² point is theoretical.
- Zhang et al. 2025 published measured single-stage flux 56.69 L m^-2 h^-1; its 38-stage 4.72% / 34.05 W/m² point is theoretical and must not be fused with the single-stage flux as one loaded operating point.
- R075 is our SIMULATED package screen: ~1.40 L optimistic versus ~4.29 L conservative around N=16 at 80/40°C.
- R076 is a PROPOSED physical calibration contract plus analytical inversion; no bench data exist from our lab.

## Frozen R076 experiment

Authoritative contract: `lab/experiments/EXP-TO-001/R076-CALIBRATION-CONTRACT.md`
Reusable scale bridge: `src/energy_lab/toec_calibration.py`
Threshold table: `artifacts/r076-toec-calibration-thresholds.csv`

The rig is four thermally cascaded but hydraulically separable cassettes, 100 cm² active area each, with matched source/sink calorimetry, every-stage temperature, membrane/outlet pressure, individual permeate flow, common-manifold pressure and interstage heat accounting. Loaded sweep is 1–5 MPa only within qualified component ratings, with blank/open-load controls and three restart repeats at the best loaded point.

## Compactness gate

For the R075 conservative N=16 state, only 1.0463 L remains for membrane + thermal network under 2 L:

`0.8681/rho_A + 528.7/q_V <= 1.0463 L`

At rho_A=1.10 m²/L, q_V must be ~2056 W/L; at q_V=1000 W/L, rho_A must be ~1.68 m²/L. This shows membrane packing alone does not close the conservative package.

## Promotion rule

Do not promote from proposed instrumentation or from sensor precision. Promotion requires actual matched 4-stage data whose calibrated projection has 95% upper total volume <=2 L and 95% lower electric performance >=15% Carnot preferred, plus heat closure <=5%, hydraulic closure <=3%, and restart reproducibility <=5%. The unmeasured 4→16 scale law retains a separate ~15–20% sensitivity band.

Until those data exist, TO-01 is **waiting-hardware / NEEDS DATA** and further stage-count desk variants are not eligible progress.
