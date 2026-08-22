# R075 — TOEC multi-stage package audit

- Shift: `shift-20260822-1210-r75`
- Task: `T-TOEC-SCALING-MODEL`
- Role: computational-modeler
- Branch: `TO-01`
- State before: PROMISING / active desk research after R074
- Principal mission: test whether the 2025 38-stage TOEC promise survives non-double-counted temperature staging, source heat, PTO, headers and a complete <=2 L package screen.
- Success test: reproducible 60/20 and 80/40°C model for N=1/4/8/16/38 with conservative + optimistic screens, energy/Carnot tests, explicit evidence labels, and a binary 10 W / 2 L gate.

## Bottleneck

R074 had a strong literature-modelled membrane result but no package-level proof, and it risked informally combining a measured single-stage flux with a separate 38-stage model point.

## Work performed

Created `src/energy_lab/toec.py`, `tests/test_toec.py`, and deterministic reference artifact `artifacts/r075-toec-sweep.csv`. The stage temperature audit partitions the source temperature span exactly once. Modelled literature anchors, experimental anchors, and our free package assumptions are kept separate.

External evidence checked:
- Zhang et al., Applied Energy 389 (2025) 125740, DOI 10.1016/j.apenergy.2025.125740: measured 56.69 L m^-2 h^-1 single-stage flux; theoretical 38-stage 80/40°C peak 4.72% and 34.05 W/m².
- Li et al., ACS Applied Materials & Interfaces 13 (2021) 21371–21378, DOI 10.1021/acsami.1c03395: experimental pump-free multistage 1.39±0.25 W/m²; theoretical 30-stage 2.72% and 14.0 W/m².
- Straub & Elimelech, Environmental Science & Technology 51 (2017) 12925–12937, DOI 10.1021/acs.est.7b02213: optimized 60/20°C model up to 4.1% (~34% Carnot) with finite-HX/high-power-density penalties.
- Liu et al., Water Research 256 (2024) 121586, DOI 10.1016/j.watres.2024.121586: experimental neighboring hollow-fiber in-situ latent heat recovery, used only as architecture motivation.

## Quantitative result

Optimistic-but-defensible 80/40°C screen:
- N=16: ~10 W DC, ~0.445 m² membrane, ~304 W source heat, ~1.40 L total, ~3.29% electric efficiency = ~29.0% Carnot.
- N=38: ~0.371 m², ~268 W source heat, ~1.45 L. Added stage overhead makes it slightly less compact than N=16 despite better conversion.

Conservative 80/40°C screen:
- N=16: ~4.29 L, ~529 W source heat.
- N=38: ~4.18 L, ~455 W source heat.
- Efficiency can clear the 10–15%-of-Carnot gate, but package compactness does not. For N=16, membrane-core + thermal-network volume must improve by about 3.2× relative to the conservative assumptions to fit 2 L.

Optimistic 60/20°C is borderline: N=16 ~1.99 L; N=38 ~1.95 L. Conservative 60/20°C remains ~6–10 L.

## Adversarial anchor check

Naively combining the published single-stage 56.69 L m^-2 h^-1 flux with the separate 38-stage 34.05 W/m² / 4.72% benchmark implies ~37.1 kW/m² latent transport but only ~0.721 kW/m² source heat, or ~98.06% apparent latent-heat recovery. A simple ideal 38-effect recycle gives 97.37%. Therefore those anchors cannot be treated as one loaded operating point; the mismatch is a normalization/operating-condition warning, not an anomalous energy gain.

## Validation

Private recomputation reproduced all 20 reference cases and the anchor diagnostic. Regression tests encode: source temperature span used once, energy efficiency below Carnot, preservation of the published 38-stage model anchor before BOM losses, and explicit failure of the conservative compactness case. GitHub status API returned no completed status context yet after the commits, so this run does **not** claim CI passed.

## Verdict

**NEEDS DATA.** TO-01 remains physically interesting, but R075 shows the pass/fail boundary is dominated by module-level compactness and by how loaded multi-stage transport normalizes relative to the published single-stage flux. The optimistic envelope passes; the conservative envelope misses by >2× volume.

## Next decisive task

Build/freeze an instrumented 2–4 stage TOEC module contract and a calibration model that measures source heat, per-stage temperatures, loaded flux/pressure, hydraulic output, heat recovery and header pressure loss. Use those measurements to collapse the optimistic-vs-conservative package envelope before any 16/38-stage design.
