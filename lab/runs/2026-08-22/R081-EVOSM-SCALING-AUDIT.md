# R081 run log — EVOSM scaling audit

- Reserved run: R081
- Shift: shift-20260822-1910-r081
- Task: T-EVOSM-SCALING-AUDIT
- Branch: EVOSM-01
- Role: computational-modeler + research-lead-falsifier
- State before: PROMISING / active-desk
- Mission: close the 10 W whole-system compactness/source envelope from measured large-area performance and compare fairly with R019 hydraulic PRO.
- Success/falsification test: downgrade compact EVOSM if the 2 L path requires heroic scaling/packing improvements; preserve distributed use only if the source-area ledger remains physically credible.

## Evidence read

- Sheet R019 and R080.
- Joule 2026, DOI 10.1016/j.joule.2026.102359: 8.5 W/m² at 1 cm²; 0.66 W/m² at 1000 cm²; typical NGO thickness ~100 µm in fabrication text.
- Nature Communications 2017, DOI 10.1038/s41467-017-00581-w: natural evaporation resource modelling up to 10.49 W/m² annual-average in favorable locations; work depends on evaporation rate and vapor chemical-potential drop.
- PRO reviews used only as qualitative baseline support for scale losses/concentration polarization; R019 supplies the specific hydraulic architecture being compared.

## Quantitative result

The decisive new bound is geometric: 10 W / 0.66 W/m² = 15.15 m². At 100 µm membrane thickness that is 1.515 L of membrane solid. A 2 L package therefore permits only 132 µm average stack pitch, leaving 32 µm total non-membrane pitch. A 0.5 mm pitch would require 2.5 W/m², 3.79× measured large-area performance; a 1 mm pitch requires 5 W/m², 7.58×.

External source stays real: 10 W / 10.49 W/m² >=0.953 m² ideal favorable evaporation footprint. At 25°C, 50% RH, reversible vapor exergy is ~95.38 kJ/kg and the ideal 10 W evaporation minimum is ~0.377 kg/h. A 50-bar ideal PRO output requires ~7.2 kg/h for 10 W, ~19.1× that thermodynamic minimum before losses.

## Adversarial review

The accessible Joule text did not expose a matched evaporation mass rate, salinity inventory, salt crossover, auxiliary pumping power, or complete source-to-electric efficiency for the 1000 cm² point. Those terms are therefore not invented. The natural-evaporation 10.49 W/m² value is an optimistic regional resource ceiling, not a measured input to the Joule solar-evaporation apparatus. The 0.5–1.0 mm stack pitches are explicit engineering scenarios, not reported module geometry.

## Verdict

LOW PRIORITY for compact 10 W / 2 L. Preserve distributed EVOSM as NEEDS DATA, not as a compact candidate.

## Next recommendation

Do not seed another compact EVOSM optimizer. Only reopen EVOSM desk work if new matched large-area evidence provides evaporation mass balance, salt crossover/retention, auxiliaries, or thinner high-performance membrane/module geometry. With WET-01 and TO-01 waiting hardware, allow the ready queue to go empty rather than invent work.
