# Current Lab State

Updated: 2026-08-22 12:18 Africa/Cairo

## Published frontier

- Latest Sheet1 research run: **R075**
- Verdict: **NEEDS DATA**
- Active branch: **TO-01 — thermo-osmotic hydraulic conversion**
- Hardware-waiting branch: **WET-01 — wet phase-change liquid-piston / wet thermoacoustic core + direct linear alternator**

## What R075 changed

R075 built a reproducible 20-case TOEC source-to-electric/package audit for 60/20°C and 80/40°C at N=1/4/8/16/38. The source temperature span is used exactly once and the model charges membrane area, source heat, header loss, PTO, parasitics, stage overhead, thermal-network volume and housing.

The optimistic-but-defensible 80/40°C screen clears 10 W / 2 L, with the smallest tested package near **N=16: ~1.40 L, ~0.445 m² membrane, ~304 W source heat, ~3.29% electric = ~29% Carnot**. N=38 is slightly larger (~1.45 L) because stage hardware begins to offset area/thermal savings. The conservative 80/40°C envelope is ~4.2 L; its N=16 membrane+thermal subsystem needs roughly **3.2× combined compactness improvement** to fit 2 L. Optimistic 60/20°C is only borderline (~1.95–1.99 L at N=16–38).

A key evidence correction is now durable: the measured **56.69 L m^-2 h^-1 single-stage flux** and the separate **38-stage modelled 34.05 W/m² / 4.72%** point cannot be treated as one loaded operating point. Doing so implies ~98.06% latent-heat recovery, above the simple ideal 38-effect ~97.37%, signaling a normalization/operating-condition mismatch rather than an energy anomaly.

## Current decisive question

Do measured 2–4 stage module values for loaded flux/pressure, heat recovery, header loss and thermal-network compactness land near the optimistic envelope or the conservative one?

## Next task

`T-TOEC-MODULE-CALIBRATION` — freeze the smallest instrumented 2–4 stage module and invert the R075 model into measured pass/fail thresholds before considering 16 or 38 stages.

## Preserved WET-01 gate

When hardware becomes available, WET-01 still requires the frozen 0.25 mm / 5 Hz / 10 bar DRY→WET coupon with phase-aware `Re{G*}/V`, wet loss and uncertainty bounds. Do not restart geometry churn.
