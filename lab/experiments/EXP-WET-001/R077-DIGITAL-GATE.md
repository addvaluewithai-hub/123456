# R077 — Deterministic phase-aware metrology gate

Evidence state: **ANALYTICAL / COMPUTATIONAL METROLOGY DESIGN**. No bench data are claimed.

## Mission

Freeze the R073 WET-01 decision rule in reproducible code before any hardware data are observed, preserving the primary `r_h=0.25 mm`, `f=5 Hz`, `P_mean≈10 bar` geometry and the 0.30 mm comparison only.

## Implemented contract

- model/gate: `src/energy_lab/wet_metrology.py`
- regression tests: `tests/test_wet_metrology.py`
- summary schema: `contracts/measurement-summary.schema.json`
- deterministic reference: `reference/R077-metrology-gate.json`
- CLI: `energy-lab wet-metrology-snapshot` and `energy-lab wet-classify`

The classifier propagates independent 1-sigma amplitude, phase and geometry uncertainty into

`Re{G*}/V = (|G*|/V) cos(phi)`

using first-order delta propagation, then applies two-sided 95% intervals. A clean PASS requires the lower confidence bound on in-phase conductance to exceed the conductance gate and the upper confidence bounds on absolute phase and wet loss to remain below their gates. A crossing interval is INCONCLUSIVE rather than PASS.

## Frozen benchmark reproduced

At 5 Hz:

- 0.25 mm: thermal factor Re≈0.90606, phase≈-16.2195°; mass factor Re≈0.93046, phase≈-13.9122°.
- 0.30 mm: thermal factor Re≈0.82670, phase≈-22.2540°; mass factor Re≈0.86793, phase≈-19.3252°.

These are intrinsic diffusion screens only; wall/contact/wet-film/interface effects remain unmeasured.

## New metrology guardband result

For an illustrative achievable analysis uncertainty of:

- sigma(Re)/Re = 5%;
- phase sigma = 2°;
- wet-loss sigma = 0.2 W;

clean 95%-bound PASS requires nominal values of approximately:

- `Re{G*}/V >= 119.734 kW m^-3 K^-1`;
- `|phase| <= 26.080°`;
- `wet loss <= 1.908 W`.

This is more stringent than the raw physics thresholds `108 kW m^-3 K^-1`, `30°`, and `2.3 W`, and prevents threshold-hugging measurements from being promoted.

## Validation

Key scientific regression assertions were independently executed against the fetched implementation logic during R077 recovery and passed: frozen 0.25/0.30 mm benchmark values, zero-phase sensitivity limit, near-threshold INCONCLUSIVE behavior, clear PASS, definite FAIL, bad-energy-closure INCONCLUSIVE behavior, and the guardband calculation above.

The GitHub Actions workflow was also updated so pushes run the full repository `pytest -q`, durable-state validation, and deterministic R077 snapshot generation. The workflow completion status was not observable through the available connector in this shift, so no CI PASS is claimed here.

## Energy/source ledger

No new energy-conversion claim is made. The eventual device source remains the real ~293→333 K thermal gradient. The servo/piston excitation in the identification experiment is experimental forcing only and must never be credited as useful generated energy. Promotion still requires measured hot/cold/acoustic closure and full cycle accounting.

## Falsification / promotion gate

Hardware data may only produce a clean PASS when all are satisfied:

1. 95% lower `Re{G*}/V >= 108 kW m^-3 K^-1`;
2. 95% upper `|phase| <= 30°`;
3. 95% upper wet loss `<=2.3 W`;
4. p-U versus `f∮p dV` disagreement `<=5%`;
5. energy closure `<=5%`;
6. repeatability `<=5%`.

Any interval crossing a physics gate or any failed measurement-quality gate is INCONCLUSIVE/NEEDS DATA.

## Decision

The digital/metrology uncertainty is closed. WET-01 remains **NEEDS DATA**, because the decisive unknown is now physical wet-interface performance. The next desk task is the buildable hardware/instrumentation packet; after that WET-01 should wait for bench data rather than reopen geometry optimization.
