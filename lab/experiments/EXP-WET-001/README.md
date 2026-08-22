# EXP-WET-001 — Phase-aware wet coupon identification

Status: **PROPOSED**
Branch: WET-01
Origin: R069–R073

## Question

At the frozen compact design point, does the real wet thermal/mass-transfer element have enough in-phase conductance and low enough dissipation to support a ~10 W DC / <=2 L converter?

## Frozen primary geometry

- hydraulic radius: ~0.25 mm primary
- comparison: 0.30 mm only
- frequency: 5 Hz primary; calibration checks around 1/3/5/7/10 Hz
- mean pressure: ~10 bar
- acoustic pressure amplitude: ~20 then 40 kPa
- thermal span: ~293 to 333 K nominal
- test order: DRY then WET under matched geometry/forcing

Earlier design lineage used an active coupon around 0.225 L, ~75 cm² gas-flow area and ~30 mm active length; exact build dimensions must remain linked to the final CAD/manufacturing tolerance record.

## Measured channels

- mean pressure separately from dynamic pressure;
- synchronized dynamic pressure across/within coupon;
- piston displacement (derive flow by harmonic fit, not noisy differentiation);
- hot/cold liquid-loop calorimetry;
- dynamically calibrated wall/gas temperature or heat-flux phase channel;
- optional H2O concentration/phase measurement if practical;
- water inventory / flooding-dryout observations.

All dynamic channels share a clock and have a measured complex transfer function around the operating frequency.

## Predeclared gate

Clean PASS only when calibrated uncertainty supports:

- 95% lower bound `Re{G*}/V >= 108 kW m^-3 K^-1`;
- total physical phase preferably `<30°`;
- 95% upper bound wet dissipative acoustic loss `<2.3 W`;
- p-U and `f∮p dV` acoustic-work estimates agree to approximately 5% or better;
- hot/cold/acoustic energy closure is within the declared measurement budget.

Near-threshold intervals are **INCONCLUSIVE / NEEDS DATA**, not PASS.

## R073 metrology targets

- calibrated phase uncertainty around 5 Hz: <=2–3°
- conductance/heat-rate amplitude uncertainty: ~5% target
- geometry uncertainty: ~1–2% target
- combined decision uncertainty: order 6–8% target
- 0.25 mm intrinsic thermal phase is already ~16°, leaving only single-digit-millisecond extra lag budget for wall/contact/wet-film/interface dynamics.

## Safety boundary

10 bar pressure hardware requires pressure-rated components, relief strategy, shielding/remote operation as appropriate, and competent physical review. The scheduled agent designs/analyzes; it must not claim physical operation occurred without actual bench evidence.

## Data contract

Future measurement summaries should be stored under `lab/experiments/EXP-WET-001/data/` with provenance, calibration ID, timestamps, units, raw-data hash/location, and an analysis manifest naming the Git commit and code version used.
