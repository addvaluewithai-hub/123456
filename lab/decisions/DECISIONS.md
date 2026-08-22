# Accepted Decisions

## D001 — Two-layer lab memory

Accepted 2026-08-22. GitHub is operational/executable truth; the Google Sheet is the append-only published research ledger and human dashboard. Scheduler prompts stay small and point to `lab/RUNNER.md`.

## D002 — One task per scheduler wakeup

Accepted 2026-08-22. Claims/leases and run-number reservations prevent duplicate work and allow future scaling to multiple workers without relying on chat memory.

## D003 — Freeze WET-01 geometry before hardware

Accepted from R072–R073. Primary point is about 0.25 mm hydraulic radius, 5 Hz, 10 bar; 0.30 mm is the only comparison. No new pore-geometry churn unless new evidence invalidates the freeze.

## D004 — Phase-aware pass gate

Accepted from R070–R073. Scalar UA is insufficient. Promotion requires phase-aware `Re{G*}/V`, calibrated wet-loss accounting, and uncertainty bounds; simulated/proposed values are not bench evidence.

## D005 — Portfolio fallback

Accepted from R072. When WET-01 is genuinely hardware-only, desk research moves to thermo-osmotic conversion rather than manufacturing additional wet-regenerator ideas to keep the scheduler busy.

## D006 — R074 activates TO-01 for desk research

Accepted 2026-08-22 from the published R074 row. Newer resistance-reduced TOEC evidence justifies a complete multi-stage heat-recovery/package model. TO-01 becomes portfolio rank 1 for desk work while WET-01 remains preserved at NEEDS DATA awaiting physical evidence. Promotion requires full source-to-electric and package accounting, not membrane-level/modelled literature numbers alone.

## D007 — Separate TOEC transport anchors and calibrate small before scaling

Accepted from R075. The measured 56.69 L m^-2 h^-1 **single-stage** flux and the separate **modelled 38-stage** 34.05 W/m² / 4.72% result must never be treated as one loaded operating point without matched conditions and normalization. The R075 audit shows an optimistic 80/40°C package can clear 2 L around N≈16, while a conservative envelope remains ~4.2 L; therefore the next decisive step is a measured 2–4 stage calibration module. Do not optimize or build 38 stages until loaded transport, heat recovery, header loss and thermal-network compactness collapse that uncertainty band.

## D008 — Freeze TOEC desk scaling at the 4-stage hardware gate

Accepted from R076. The matched four-stage calibration contract is now the authoritative next TO-01 evidence step. The conservative package boundary is `0.8681/rho_A + 528.7/q_V <= 1.0463 L`; optimistic membrane packing alone cannot rescue conservative transport/thermal duty. TO-01 becomes waiting-hardware. Do not create more stage-count variants until matched module data arrive. Desk priority returns to the highest-value non-hardware task, currently WET-01 metrology code.
