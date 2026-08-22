# R076 — TOEC module calibration and compactness inversion

- Reserved run: R076
- Shift: shift-20260822-1307-r076
- Task: T-TOEC-MODULE-CALIBRATION
- Branch: TO-01
- Role: experimentalist-metrologist
- Timestamp: 2026-08-22 13:07–13:18 Africa/Cairo
- State before: R075 NEEDS DATA; optimistic 80/40 N16 ~1.40 L vs conservative ~4.29 L
- State after: R076 published NEEDS DATA; TO-01 waiting-hardware; WET-01 next desk branch
- Evidence state: ANALYTICAL + SIMULATED + PUBLISHED EXPERIMENTAL anchors; new apparatus remains PROPOSED

## Mission

Freeze the smallest decisive 2–4 stage measurement contract and invert the R075 package model into thresholds that can distinguish a credible <=2 L path from a conservative ~4.2 L outcome.

## Bottleneck

The dominant uncertainty is module-level transport/thermal/package compactness, not stage-count arithmetic: gross loaded hydraulic W/m², hydraulic efficiency, membrane packing density, thermal-network duty density, stage/header dead volume and header pressure loss are not jointly measured at matched conditions.

## Hypothesis / counter-hypothesis

Hypothesis: a resistance-reduced 4-stage module will measure close enough to the R075 optimistic transport and packaging envelope that N≈16 remains a credible <=2 L scale path.

Counter-hypothesis: once loaded pressure-flow, source heat, recovery and real module dead volume are measured simultaneously, the system will land near the conservative envelope and require >~3× combined compactness improvement.

## Work performed

1. Chose a 4-stage thermally cascaded, hydraulically separable rig with 100 cm² active membrane per stage. This gives ~0.58–0.90 W gross hydraulic signal across the current R075 conservative/optimistic N4 screen and order 23–25 W source heat, large enough for accurate calorimetry/flow measurement.
2. Defined source/sink/stage temperature, pressure, flow, interstage recovery and geometry measurements, controls, repeatability and safety boundaries.
3. Derived the conservative N16 packaging boundary exactly: `0.8681/rho_A + 528.7/q_V <= 1.0463 L`.
4. Implemented `src/energy_lab/toec_calibration.py` so a future measured N4 point can be projected through the frozen R075 4->16 law without fitting a new favorable stage curve.
5. Added regression tests requiring the N4->N16 bridge to reproduce both existing R075 optimistic and conservative envelopes.
6. Rechecked primary evidence: Nature Energy 2016 direct pressure-generation experiment; ACS AMI 2021 pump-free multistage experiment (1.39±0.25 W/m²); Applied Energy 2025 resistance-reduced single-stage flux plus separate theoretical 38-stage benchmark.

## Quantitative result

The conservative fixed stage/PTO/housing charge leaves only 1.0463 L for membrane + thermal network. Absolute packaging minima are rho_A>=0.830 m²/L and q_V>=505 W/L even if the other subsystem had zero volume. More realistically, at rho_A=1.10 m²/L, q_V must exceed ~2056 W/L; at q_V=1000 W/L, rho_A must exceed ~1.68 m²/L. Thus simply moving conservative membrane packing to the optimistic 1.10 m²/L while leaving thermal duty density near 300–600 W/L does not close the 2 L target.

A sensor budget around 0.3% pressure, 0.5% flow and <=2.5% calorimetry yields ~0.6% hydraulic-power and ~2.7% hydraulic-efficiency 1-sigma uncertainty. This is far smaller than the ~3× package-volume gap; the dominant uncertainty after the proposed rig is expected to be the 4->16 scale law, which should retain a separate >=15–20% sensitivity band.

## Energy/source/reset ledger

Source: external 80->40°C low-grade heat. Power stroke: thermo-osmotic vapour transport against hydraulic backpressure. Useful output: measured DeltaP*Vdot, later converted by explicit PTO efficiency. Reset: condensation, working-water return and thermal cascade. Costs: conductive/environmental heat leak, header pressure drop, thermal-network volume/resistance, circulation/conditioning power, PTO/parasitics and stage/housing volume. No output is credited to pressure storage or heat recovery itself.

## Adversarial review and validation

The proposed 4-stage rig cannot by itself prove the 16-stage interpolation. High sensor precision could create false confidence if stage-scaling error is omitted. Therefore the decision rule separates metrology uncertainty from a >=15–20% scale-law band, and nominal <=2 L with an interval crossing 2 L is INCONCLUSIVE rather than a pass.

A pre-close calculation caught a regression bug in the first calibration bridge: it used the optimistic eta stage law for both optimistic and conservative regression cases. The bridge was corrected to carry the R075 stage-law parameter explicitly. Direct recalculation after the fix reproduces the accepted N=16 package values: optimistic 1.40265 L / 304.18 W source heat and conservative 4.29427 L / 528.68 W. GitHub Actions status was not surfaced through the available connector during this run, so CI is not claimed as passed.

## Verdict

NEEDS DATA. The desk uncertainty is now sufficiently compressed that further stage-count variants are lower value than a physical 4-stage calibration. TO-01 is waiting-hardware.

## Next exact question

Run EXP-TO-001 as specified. If no hardware data are available, execute the next eligible non-hardware task: WET-01 phase-aware metrology/uncertainty code. Do not generate more TOEC package scenarios to fill runs.

## Sources

https://doi.org/10.1038/nenergy.2016.90
https://doi.org/10.1021/acsami.1c03395
https://doi.org/10.1016/j.apenergy.2025.125740
