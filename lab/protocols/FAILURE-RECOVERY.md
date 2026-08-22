# Failure Recovery

## Core rule

Never repair inconsistency by inventing a result, duplicating an R-number, rewriting historical Sheet rows, or force-overwriting another worker's live state.

## Expired claim with no Sheet row

Inspect the task workspace, run log, commits/CI, and reservation. If substantive work is incomplete, release/requeue with the same reserved R-number only when safe; otherwise abandon the reservation explicitly and record why before allocating a new number. Do not silently reuse a number for unrelated work.

## Sheet row exists but Git release is missing

Treat the Sheet row as published evidence. Reconstruct the matching Git state from the durable artifacts/run log, mark `last_published_run`, clear the stale claim, and do not append a duplicate row.

## Git artifacts exist but Sheet append failed

Verify the reserved R-number is absent from Sheet1. Retry publication only if the Git artifacts clearly identify one completed research result and the row content can be reconstructed exactly. Otherwise mark blocked for human reconciliation.

## CI/model failure

A failing test or workflow is evidence. Fix it within the claimed task only when it is directly required for that task. Never mark a model result valid because the failure “looks unrelated” without checking.

## Connector outage

Persist a precise blocker if possible. Do not claim an external write succeeded when the connector response is unavailable.
