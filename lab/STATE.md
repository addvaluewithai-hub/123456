# Energy Research Lab — Current State

Updated: 2026-08-22 17:50 EEST
Latest published research run: **R079**
Next publishable research run: **R080** (`R078` is abandoned and must never be reused)

## Portfolio state

1. **WET-01 — NEEDS DATA / waiting-hardware.** R077 froze the deterministic phase-aware classifier. R079 froze the exact buildable experiment: 0.25 mm primary, 0.30 mm comparison only, 5 Hz, ~10 bar, p-hat 20/40 kPa, DRY→WET; simultaneous phase acquisition, dynamic FRF, calorimetry, provenance and safety gates are predeclared. No more WET desk variants are justified without bench data.
2. **TO-01 — NEEDS DATA / waiting-hardware.** R075 showed ~1.4 L optimistic versus ~4.2 L conservative 80/40°C packages; R076 froze the matched 4-stage calibration needed to decide which envelope is real. No more stage-count variants without hardware.
3. **MAG-01 — LOW PRIORITY / parked.** No fair equal-resource advantage over a strong multimodal linear baseline.

## WET-01 frozen physical gate

Clean promotion requires calibrated BENCH-MEASURED evidence with:

- 95% lower bound `Re{G*}/V >= 108 kW m^-3 K^-1`;
- 95% upper `|phase| <= 30°`;
- 95% upper wet dissipative loss `<=2.3 W`;
- p-U vs `f∮p dV` agreement <=5%;
- hot/cold/acoustic energy closure <=5%;
- repeatability <=5%;
- immutable raw/calibration provenance tied to analysis Git SHA.

R079 instrument audit says ADC/pressure bandwidth is not the limiting uncertainty; installed thermal-interface phase calibration is the narrowest measurement risk.

## Active desk work

No leading energy branch has an honest remaining desk-only task. The next eligible queue item is `T-PORTFOLIO-REVIEW-001`: re-rank the portfolio and seed only genuinely uncertainty-reducing non-hardware work. Do not invent another WET or TOEC parameter sweep to keep the scheduler busy.

## CI note

R079 changed experiment-design/provenance files, not physics code. The Git status connector returned no completed status checks for the substantive commit, so no CI PASS is claimed.
