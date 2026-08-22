# Current Lab State

Updated: 2026-08-22 11:30 Africa/Cairo (infrastructure bootstrap)

## Published frontier

- Latest Sheet1 research run: **R073**
- Verdict: **NEEDS DATA**
- Lead branch: **WET-01 — wet phase-change liquid-piston / wet thermoacoustic core + direct linear alternator**
- Portfolio backup: **TO-01 — thermo-osmotic hydraulic conversion**
- Magnetic/vibration shaping: **LOW PRIORITY** as a general energy architecture; retain for niche impedance/frequency shaping.

## Frozen WET-01 point

- hydraulic radius: ~0.25 mm primary; 0.30 mm comparison
- frequency: ~5 Hz
- mean pressure: ~10 bar
- acoustic pressure cases: ~20 and 40 kPa
- sequence: DRY → WET
- source span: roughly 293 K → 333 K

## Promotion gate

Require calibrated evidence supporting all of:

- `Re{G*}/V >= 108 kW m^-3 K^-1` (95% lower bound preferred for final pass)
- total physical thermal/mass-transfer phase preferably `<30°`
- wet dissipative acoustic loss `<2.3 W` (95% upper bound for final pass)
- acoustic work cross-check by p-U and p-V methods
- heat-flow/energy closure within experiment uncertainty
- complete converter projection near 10 W DC in <=2 L with a credible Carnot fraction

## Current bottleneck

R073 showed the experiment is decision-capable only with dynamic phase calibration. The remaining decisive unknown is real wet interface/wall/contact behavior at 5 Hz/10 bar; no bench dataset for our exact coupon exists in the repo.

## Next task

`T-WET-METROLOGY-CODE`: turn the R073 measurement logic into reproducible repo code/configs, uncertainty propagation, and a machine-readable experiment contract. This is the last high-value desk/model implementation before hardware data or a deliberate portfolio switch.
