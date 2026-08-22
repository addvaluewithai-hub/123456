# Queue Claim Protocol

Queue: `lab/registry/queue.json`
Run allocator: `lab/registry/run-counter.json`

## Eligible task

A task is eligible when it is `ready`, every dependency is `done`, and no live claim conflicts.

## Research-run serialization guard

Until Sheet1 reconciliation is upgraded to identify the maximum published R-number independently of row order, **research publication is serialized**. If `active_reservations` contains any live lower-number reservation owned by another shift, do not reserve a higher R-number or perform a second publishable research task. Leave the live lease untouched and stop after any necessary reconciliation/maintenance.

Reason: Sheet1 currently treats the latest non-empty row as the published frontier. Publishing R078 before a live R077 would make a later R077 append look like the frontier moved backwards and can corrupt `last_published_run`/handoff projections.

Parallel non-publishing maintenance may be performed only when it cannot alter scientific task/branch conclusions. A future protocol may relax this guard after Sheet synchronization is made order-independent.

## Claim fields

On claim set:

- `status: claimed`
- `claim.shift_id`
- `claim.worker_id` (stable descriptive value if available, otherwise `scheduled-agent`)
- `claim.claimed_at`
- `claim.lease_expires_at`
- `claim.reserved_run_id`
- increment `attempts`
- queue `updated_at`

Reserve the current `next_research_run` from `run-counter.json` as `RNNN`, then increment the counter. Add the reservation to `active_reservations`.

Claim and run reservation should be committed atomically when practical. Git SHA conflict is the concurrency lock; reread and retry on conflict. Never force another worker's state away.

## Lease

Default lease is 120 minutes. A live lease protects that task. Under the current Sheet serialization guard, another worker must not reserve/publish a later research R-number while a lower live reservation exists.

## Release

After successful Sheet publication, clear `claim`, set the final task state, write `last_completed_run`, and remove the reservation from `active_reservations`. Update `last_published_run`/time only after the Sheet row exists.

If a reservation must be abandoned before publication, record it explicitly in `abandoned_reservations` with task, shift, timestamp and reason; never silently reuse that R-number for unrelated work.

If the task needs another shift, either set the same task back to `ready` with a narrowed next mission or create a clearly separate dependent task. Avoid immortal tasks with vague missions.
