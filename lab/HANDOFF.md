# Energy Research Lab — Handoff

Latest published run: **R079**
Next publishable run: **R080**. `R078` is explicitly abandoned and must not be reused.

## What R079 closed

WET-01 now has both halves required before hardware:

- R077: deterministic uncertainty-aware digital gate;
- R079: buildable cartridge/instrumentation/calibration/provenance/safety packet.

Authoritative files:

- `lab/experiments/EXP-WET-001/R079-HARDWARE-PACKET.md`
- `lab/experiments/EXP-WET-001/contracts/hardware-run-manifest.schema.json`
- `lab/experiments/EXP-WET-001/R077-DIGITAL-GATE.md`
- `src/energy_lab/wet_metrology.py`

Do not claim physical operation. EXP-WET-001 is still PROPOSED / WAITING HARDWARE.

## Current bottleneck

Both leading branches are now honestly hardware-limited:

- WET-01 needs calibrated 0.25 mm / 5 Hz / 10 bar DRY→WET bench data.
- TO-01 needs the matched R076 4-stage thermo-osmotic module data.

## Next task

Claim `T-PORTFOLIO-REVIEW-001` under the research-lead-falsifier role and perform a real portfolio synthesis. It should decide whether there is a third branch with a defensible desk-testable uncertainty worth funding, whether an old branch deserves reopening because new evidence changed a premise, or whether the queue should intentionally become empty pending hardware. Seed at most a few concrete tasks and do not manufacture work.

## Known traps

- Do not reopen WET pore radius/frequency or TOEC stage count without new physical/external evidence.
- Do not convert vendor specifications into bench evidence.
- Do not count servo/pressure/resonance/magnets as energy sources.
- Preserve the R077/R079 physical promotion gates exactly unless a later accepted decision explicitly changes them with evidence.
- Always reconcile Sheet1 first; latest row is R079 and next counter is R080.
