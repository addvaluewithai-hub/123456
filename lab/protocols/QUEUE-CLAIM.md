# Queue Claim Protocol

Queue: `lab/registry/queue.json`
Run allocator: `lab/registry/run-counter.json`

## Eligible task

A task is eligible when it is `ready`, every dependency is `done`, and no live claim conflicts.

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

Default lease is 120 minutes. A live lease protects that task only; another worker may select another eligible task if parallel operation is intentionally available. Never steal a live lease.

## Release

After successful Sheet publication, clear `claim`, set the final task state, write `last_completed_run`, and remove the reservation from `active_reservations`. Update `last_published_run`/time only after the Sheet row exists.

If the task needs another shift, either set the same task back to `ready` with a narrowed next mission or create a clearly separate dependent task. Avoid immortal tasks with vague missions.
