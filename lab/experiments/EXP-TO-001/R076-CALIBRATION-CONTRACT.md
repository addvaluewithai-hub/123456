# R076 — 4-stage TOEC calibration contract

Evidence state: **PROPOSED experiment + analytical inversion + existing R075 SIMULATED envelope**
Branch: TO-01
Task: T-TOEC-MODULE-CALIBRATION

## Decision this experiment must make

R075 leaves a ~3× package-volume disagreement at 80/40°C: ~1.40 L optimistic vs ~4.29 L conservative around N=16. This contract is intentionally a **4-stage calibration module**, not a 16/38-stage product. It measures the variables that dominate that gap and feeds them into the frozen R075 4->16 screening law.

Primary decision metric: the 95% uncertainty interval of the calibrated N=16 projection for 10 W DC / 2 L, together with electric fraction of Carnot. No BENCH-MEASURED label is allowed until physical data exist.

## Exact bench topology

Build four thermally cascaded, hydraulically separable TOEC cassettes, each with **100 cm² active membrane area** (0.01 m²; 0.04 m² total). Each cassette has a hot/evaporation chamber, hydrophobic nanoporous membrane, pressurized condensation/permeate chamber, and an independently pressure-controlled permeate outlet. The four cassettes are connected thermally S1 -> S2 -> S3 -> S4 so the total source span is used once, nominally 80°C -> 40°C. Keep each high-pressure outlet independently metered before a common collection/accumulator point so stage transport and header loss are identifiable rather than hidden in one manifold number.

Use degassed working water and the same membrane/thermal-network concept intended for scale-up. The calibration module may use removable interstage heat-transfer blocks so their mass/volume and conductance are measured directly. It must not borrow pump work as output: any circulation/conditioning power is logged separately and excluded from hydraulic generation.

### Test matrix

1. Baseline blank/impermeable insert at 80/40°C to measure conductive + environmental heat leak.
2. Open-load / near-zero hydraulic backpressure to establish thermal/mass transport baseline.
3. Loaded sweep at nominal permeate backpressure: 1, 2, 3, 4, then 5 MPa **only within the membrane/module qualified pressure rating**.
4. Repeat the best loaded point three independent times after full depressurization/restart.
5. Optional 60/20°C repeat only after the 80/40°C calibration closes; it is not required for the first decision.

At 0.04 m² total area, the R075 N=4 screen spans roughly 0.58 W gross hydraulic (conservative 14.55 W/m²) to 0.90 W (optimistic 22.52 W/m²). At 5 MPa this corresponds to order 0.42–0.65 L/h water flow, while source heat is order 23–25 W. These signals are comfortably measurable without pretending they are already observed.

## Measurement map

### Thermal/source ledger

- T_H,in and T_H,out on the external hot-source loop.
- Hot-loop mass flow for Q_hot = m_dot cp DeltaT.
- T_C,in and T_C,out plus cold-loop mass flow for independent sink calorimetry.
- For every stage i=1..4: evaporation-side inlet/outlet/wall temperature and condensation-side wall/outlet temperature.
- Three interstage heat-transfer links instrumented with either calibrated heat-flux sensors or a separately calibrated conductance plus boundary temperatures; compute Q_rec,i and epsilon_rec,i.
- Insulated blank run establishes environmental/conductive loss correction.

Target hot/cold calorimetry uncertainty: <=2.5% (1 sigma) at steady state. Choose loop flow so the measured water-side DeltaT is ~3–5 K; with ~0.05 K calibrated temperature channels, DeltaT error does not dominate.

### Hydraulic ledger

For each stage:

- pressure immediately at the pressurized membrane chamber;
- pressure immediately after the stage outlet/restriction;
- individual permeate mass/volume flow;
- common-manifold pressure after combining flows.

Compute stage gross hydraulic power P_i = DeltaP_mem,i * Vdot_i and header/manifold loss P_header = sum(P_i) - P_common. The scale metric is **gross loaded hydraulic W/m² before header loss plus measured header-loss fraction**; do not infer power from open-circuit pressure alone.

Target pressure channel: 0–6 MPa class, calibrated uncertainty <=0.25% full scale or <=0.3% of a 5 MPa operating point. Target flow uncertainty <=0.5% reading (Coriolis/positive-displacement) or gravimetric collection with <=0.2% interval uncertainty. Combined hydraulic-power uncertainty target is ~0.6% (1 sigma).

### Geometry/package ledger

Measure rather than assume:

- active membrane area and membrane-core envelope volume -> rho_A [m²/L];
- actual heat-transfer network volume and steady source duty -> q_V [W/L];
- stage-specific dead/separator/header volume [L/stage];
- header pressure loss fraction;
- insulation/housing allowance separately.

The bench pressure-control hardware is not automatically counted as final-product PTO volume. The final projection must use an explicit PTO efficiency/volume assumption and show sensitivity.

## Data acquisition and identifiability

All pressure, flow and temperature channels share one clock. Log pressure/flow at >=10 Hz and thermal channels at >=1 Hz. A loaded point is valid only after temperatures and source/sink heat flows are statistically steady; use >=10 min steady averaging. Store raw CSV plus calibration coefficients and uncertainty metadata. Do not smooth away stage-to-stage imbalance.

Required energy checks:

1. source heat vs sink heat + hydraulic output + quantified environmental loss closes within <=5%;
2. sum of stage hydraulic powers vs common-manifold hydraulic power + measured header loss closes within <=3%;
3. replicate loaded power density and hydraulic efficiency within <=5% relative across three restarts.

## R075 model inversion — exact compactness boundary

The conservative N=16 R075 case has membrane area 0.8681 m², source heat 528.7 W, and fixed stage+PTO+housing volume 0.9537 L. Only **1.0463 L** remains for membrane core + thermal network under a 2 L cap. Therefore the packaging-only boundary is:

`0.8681 / rho_A + 528.7 / q_V <= 1.0463 L`

where rho_A is m²/L and q_V is W/L.

Consequences:

- even with zero thermal-network volume, rho_A must be >=0.830 m²/L;
- even with zero membrane-core volume, q_V must be >=505 W/L;
- at rho_A=1.10 m²/L, q_V must be >=~2056 W/L;
- at q_V=1000 W/L, rho_A must be >=~1.68 m²/L;
- at rho_A=2.00 m²/L, q_V must be >=~863 W/L.

This is a decisive correction: **optimistic membrane packing alone does not rescue conservative transport/thermal duty**. Transport efficiency, hydraulic power density, fixed stage volume, or thermal-network duty density must also improve.

Reusable calculator: `src/energy_lab/toec_calibration.py`.
Threshold table: `artifacts/r076-toec-calibration-thresholds.csv`.

## 4-stage -> 16-stage calibration bridge

The first projection uses the already frozen R075 interpolation only; it does not fit a new favorable law from the new data. For the optimistic interpolation, the predeclared 4->16 multipliers are about **1.163× for hydraulic efficiency** and **1.259× for gross hydraulic W/m²**. Measured 4-stage values, measured packaging, measured header loss and explicit PTO assumptions are inserted into the calculator.

The scale-law extrapolation receives a separate >=15–20% uncertainty/sensitivity band because it is not measured by a 4-stage rig. Sensor precision must not be used to make the scale law look certain.

## Predeclared decision rule

**PROMOTION CANDIDATE / remain active:** after calibration, the N=16 projection must have a 95% upper bound on total volume <=2.0 L, a 95% lower bound on electric performance >=15% of Carnot preferred (10% floor only with clear volume margin), heat/source closure <=5%, hydraulic closure <=3%, and no parameter that requires combining unmatched literature anchors.

**INCONCLUSIVE / hardware-blocked:** nominal projection is <=2 L but its 95% interval crosses 2 L, or the 4->16 scale-law uncertainty dominates despite good metrology. Do not manufacture more stage-count algebra; next evidence must be a larger measured stage count or better validated stage law.

**DOWNGRADE TO-01:** measured 4-stage transport/heat recovery/package values map to the conservative ~4.2 L envelope or worse, or getting under 2 L requires >~3× improvement in the measured combined membrane+thermal compactness with no demonstrated mechanism. A failure due only to one local engineering term may seed one targeted mutation, not a fresh broad branch.

## Safety boundary

This is a high-pressure hot-water apparatus. Pressure vessels, tubing, fittings, windows/sensors and membranes must be rated for the maximum working pressure and temperature with an independent relief path, guarded/remote operation, and a documented pressure-proof procedure. The experiment contract does not authorize operating above component ratings.

## Evidence used

- Straub et al., Nature Energy 2016: direct experimental thermo-osmotic operation against hydraulic pressure up to 13 bar and 3.53±0.29 W/m² at 60/20°C. DOI: https://doi.org/10.1038/nenergy.2016.90
- Li et al., ACS Applied Materials & Interfaces 2021: pump-free multistage experiment, 1.39±0.25 W/m² at 80°C; 30-stage 2.72% / 14 W/m² remains theoretical. DOI: https://doi.org/10.1021/acsami.1c03395
- Zhang et al., Applied Energy 2025: resistance reduction, experimental single-stage 56.69 L/m²/h; 38-stage 4.72% / 34.05 W/m² remains theoretical at 80/40°C. DOI: https://doi.org/10.1016/j.apenergy.2025.125740

These sources establish plausibility and scale anchors; none supplies the missing matched 4-stage measurements specified here.
