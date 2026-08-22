# Google Sheet Synchronization

Spreadsheet: https://docs.google.com/spreadsheets/d/1WaDyqw91D8Ol8bgeX1NJ1e0nW7h1tFShoWW-BLR4sCQ/edit
Timezone: Africa/Cairo

## Roles of the tabs

- `Sheet1`: immutable published research ledger. Append-only.
- `Dashboard`: human-readable control panel/projection.
- `Branches`: portfolio projection; may be updated when branch state changes.
- `Experiments`: experiment registry projection; may be updated when experiment state changes.

Operational queue/claims/run locks live in Git, not in Sheets.

## Sheet1 schema — exactly 15 columns A:O

1. Run ID
2. Timestamp (Cairo)
3. Lead Research Role
4. Research Question / Angle
5. Previous Findings Used
6. Hypothesis / Concept
7. External Energy Source / Gradient
8. Mechanism
9. Quantitative Estimate
10. Evidence / Papers / Experiments
11. Critical Falsification Check
12. Verdict
13. Next Experiment / Question
14. Sources (URLs)
15. Confidence

Allowed verdicts: `HIGH PRIORITY`, `PROMISING`, `NEEDS DATA`, `LOW PRIORITY`, `REJECTED`, `SYNTHESIS`.
Allowed confidence: `Low`, `Medium-Low`, `Medium`, `Medium-High`, `High`.

## Publication transaction

1. Reserve R-number in Git claim.
2. Persist substantive Git artifacts.
3. Re-read latest Sheet row immediately before append.
4. Verify reserved R-number is not already present.
5. Append exactly one row.
6. Re-read the appended row to verify values.
7. Only then release the Git claim and advance `last_published_run`.

If step 5 or 6 fails, do not mark the research run published. Recovery must inspect both systems.
