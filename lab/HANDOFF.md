# Energy Research Lab — Handoff

Latest published run: **R081**
Next publishable run: **R082**. `R078` is explicitly abandoned and must not be reused.

## What R081 changed

The one-run EVOSM audit is complete. Compact 10 W / 2 L EVOSM is now LOW PRIORITY. At measured 0.66 W/m² large-area output, 10 W requires 15.15 m² membrane; with ~100 µm reported membrane thickness, the membrane solid is ~1.515 L. The absolute 2 L average repeat pitch is 132 µm, leaving only 32 µm total beyond the membrane for channels/electrodes/spacers. A 0.5 mm pitch requires 2.5 W/m² (3.79× measured); 1 mm requires 5 W/m² (7.58×).

External source accounting remains explicit: favorable natural-evaporation modelling gives an ideal >=0.953 m² source footprint for 10 W, and the 25°C/50% RH reversible water-vapor exergy bound implies >=0.377 kg/h ideal evaporation. A 50-bar ideal PRO route needs ~7.2 kg/h for 10 W before losses, so direct ion-selective conversion has a potential water-throughput advantage but is not proven source-to-electric efficient at scale.

Authoritative artifacts:
- `src/energy_lab/evosm.py`
- `tests/test_evosm.py`
- `lab/branches/EVOSM-01/R081-SCALING-AUDIT.md`
- `lab/runs/2026-08-22/R081-EVOSM-SCALING-AUDIT.md`

## Next task

There is intentionally **no ready desk research task**. On the next wakeup, reconstruct truth and stop without inventing work unless new evidence/data creates an eligible task.

## Reopen triggers

- WET: real calibrated EXP-WET-001 data.
- TO: matched 4-stage module data.
- EVOSM: matched ≥1000 cm² regeneration/crossover/auxiliary data or a substantially thinner membrane/module preserving large-area output.

## Known traps

- Do not extrapolate the 1 cm² 8.5 W/m² EVOSM record to module scale.
- Do not treat the 10.49 W/m² natural evaporation model as measured Joule input.
- Do not invent matched evaporation mass flow or salt crossover values absent from accessible evidence.
- Do not create a new task merely because the queue is empty.
