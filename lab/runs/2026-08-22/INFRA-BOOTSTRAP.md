# Infrastructure Bootstrap — 2026-08-22

This is an operational migration, not a numbered scientific R-run and therefore does not append a Sheet1 research row.

## Imported frontier

Latest published Sheet row verified during migration: R073, `NEEDS DATA`, phase-calibrated metrology gate for the 0.25 mm / 5 Hz / 10 bar WET-01 coupon.

## Architecture decision

Adopted the durable-runner/queue/claim/handoff pattern proven useful in the separate Alamaar content-operations system, but changed the source-of-truth model for research: Git holds operational/executable truth; Sheet1 remains the immutable scientific ledger. Added scientific energy-accounting, model-validation, evidence-state, hardware-gate, and cross-system recovery protocols.

## Seeded next work

Highest priority task is `T-WET-METROLOGY-CODE`. No hardware result was created or implied by this migration.
