# Energy Research Lab Runner

This file is the single authoritative entrypoint for every scheduled Energy Research Lab agent.

**Do not start from remembered conversation context. Reconstruct current truth from Git and the Sheet on every run.**

## 0. Fixed resources

Repository: `addvaluewithai-hub/123456`
Default branch: `main`
Google Sheet: `https://docs.google.com/spreadsheets/d/1WaDyqw91D8Ol8bgeX1NJ1e0nW7h1tFShoWW-BLR4sCQ/edit`
Timezone: `Africa/Cairo`

Use the branch containing this runner unless a claimed task explicitly names a working branch.

## 1. Bootstrap read

Read, in order:

1. `lab/config.json`
2. `lab/CHARTER.md`
3. `lab/OPERATING-SYSTEM.md`
4. `lab/protocols/SHIFT-CONTRACT.md`
5. `lab/protocols/QUEUE-CLAIM.md`
6. `lab/protocols/SHEET-SYNC.md`
7. `lab/protocols/ENERGY-ACCOUNTING.md`
8. `lab/protocols/EVIDENCE.md`
9. `lab/protocols/MODEL-VALIDATION.md`
10. `lab/protocols/EXPERIMENT-GATES.md`
11. `lab/protocols/FAILURE-RECOVERY.md`
12. `lab/registry/run-counter.json`
13. `lab/registry/queue.json`
14. `lab/registry/branches.json`
15. `lab/STATE.md`
16. `lab/HANDOFF.md`

Read the role catalog only after selecting a task. Read only the minimum historical run logs needed to resolve contradictions.

## 2. Reconcile Git and Sheet before new work

Read the Sheet header and the latest non-empty `Sheet1` research row. Compare its R-number, verdict, next question, and timestamp with `run-counter.json`, `STATE.md`, and the active task/branch.

Rules:

- `Sheet1` historical rows are append-only; never rewrite an old row merely to make Git agree.
- If Sheet contains a completed R-number missing from Git state, repair the Git projection before selecting new work.
- If Git reserved an R-number but no Sheet row exists and the claim is expired, follow `FAILURE-RECOVERY.md` rather than skipping or duplicating the number.
- Never create two different research results with the same R-number.

## 3. Recover stale claims

Inspect claimed tasks. Never steal a live claim. Recover only objectively expired leases according to `QUEUE-CLAIM.md` and `FAILURE-RECOVERY.md`.

Reconciliation/recovery is maintenance, not a second research task.

## 4. Select exactly one eligible task

Select in this order:

1. `status == ready`;
2. all `depends_on` tasks are `done`;
3. no live claim conflict;
4. highest numeric `priority`;
5. oldest `created_at` on ties;
6. prefer the task that most reduces the current decisive uncertainty.

Do not work blocked/done/cancelled tasks. If no task is eligible after reconciliation, stop without inventing work.

## 5. Claim and reserve the research-run number

Before deep work:

1. create a unique operational shift ID `shift-YYYYMMDD-HHMM-<suffix>`;
2. claim the selected queue task;
3. reserve the current `next_research_run` from `run-counter.json` as its `reserved_run_id`;
4. increment `next_research_run`;
5. write claim + counter reservation atomically when possible.

The Git SHA conflict mechanism is the lock. On conflict, reread state and retry; never force-push over another worker.

## 6. Reconstruct task truth

Read the task workspace, its branch entry, exact files named in `read_first`, relevant accepted decisions, and only the evidence/models required for the mission. If the task touches code, inspect the relevant implementation and tests before changing it.

Do not replay the whole research history by default.

## 7. Choose the working role

Read `lab/roles/ROLE-CATALOG.md`. Treat `recommended_role` as a strong suggestion, not a blind command. Override only if another role clearly attacks the actual bottleneck better; record why in the run log.

## 8. Execute one deep research shift

Follow `SHIFT-CONTRACT.md`.

The shift must include:

- one principal mission;
- one explicit success/falsification test;
- quantitative work, not commentary about future work;
- a full energy/source/reset ledger where relevant;
- current targeted external research when evidence is needed;
- code/simulation when it can materially reduce uncertainty;
- adversarial self-review;
- one of the allowed verdicts;
- a precise next task/question.

If code is changed, run or trigger the available validation path and inspect the result when accessible. Never claim CI, simulation, FEA, or hardware passed unless it actually ran and the evidence is available.

If the decisive missing evidence is physical hardware data and no new data exist, do not invent pseudo-measurements. Complete only a genuinely useful remaining modeling/metrology task; otherwise hold that branch and work the next eligible branch task.

## 9. Persist durable outputs

Before Sheet publication, persist the substantive work in Git. Depending on task type, this may include:

- model/code/tests;
- parameter/config files;
- `lab/experiments/...` manifest or analysis;
- branch/task artifacts;
- accepted decisions;
- evidence registry updates;
- one append-only run log under `lab/runs/YYYY-MM-DD/`.

Important findings must not live only in the run log.

## 10. Publish exactly one Sheet1 research row

For every successfully completed substantive research shift, append exactly one 15-column row to `Sheet1` using the reserved R-number and `SHEET-SYNC.md` schema.

Do not overwrite historical rows. Do not append a row for a pure no-op/recovery-only scheduler wakeup.

If the Sheet cannot be read or appended, do not pretend publication succeeded. Leave enough Git state for recovery and report the failure.

## 11. Update human dashboard tabs

After successful Sheet1 append, update `Branches` and/or `Experiments` only when their summarized state actually changed. `Dashboard` may be formula-driven. These tabs are projections; `Sheet1` remains the published run ledger and Git remains operational truth.

## 12. Release the task and update handoff

Update the same queue item:

- clear claim;
- set final task status (`done`, `ready`, `blocked`, or `cancelled`);
- set `last_completed_run` to the published R-number when substantive work completed;
- record next actionable task or exact blocker;
- preserve unrelated tasks.

Update `STATE.md`, `HANDOFF.md`, `branches.json`, and `run-counter.json.last_published_run` to match the Sheet. Commit the release/projection updates.

If Sheet publication succeeded but the final Git update conflicts/fails, the next run must reconcile from the Sheet rather than duplicate the research row.

## 13. Stop

Execute exactly one research task per scheduled wakeup. Do not immediately claim a second task even if time remains.

A successful run ends with Git + Sheet containing enough durable truth for a fresh agent to continue without conversation history.
