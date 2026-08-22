# Energy Lab Operating System

## Runtime model

Git is durable shared operational memory. The Google Sheet is the append-only scientific ledger and human dashboard. The hourly scheduler is only a wake-up mechanism.

Every scheduled execution starts at `lab/RUNNER.md`, reconciles Git with the last Sheet row, claims exactly one eligible task, performs one deep shift, persists artifacts/code/results, appends exactly one research row when substantive work completes, updates state/handoff, releases the claim, and stops.

This deliberately borrows the strongest pattern from the Alamaar content-ops system—single authoritative runner, durable Git state, queue claims, one deep shift, explicit handoff—but adapts it for research by adding run-number reservation, scientific evidence states, energy ledgers, model validation, experiment gates, and Sheet synchronization.

## Source-of-truth precedence

When records disagree, use this order:

1. `lab/CHARTER.md` for mission/non-negotiables.
2. Accepted decisions in `lab/decisions/DECISIONS.md` for durable scientific/operational decisions.
3. `lab/registry/queue.json` + `run-counter.json` for current work ownership and run reservation.
4. Branch/task/experiment workspaces for exact current mission and measured/model data.
5. `lab/STATE.md` and `lab/HANDOFF.md` as concise projections of current truth.
6. `Sheet1` as the immutable published research ledger; reconcile any missing Git projection from it, but never silently rewrite historical Sheet rows.
7. Old run logs explain history but never override newer accepted state.

## Work hierarchy

**Portfolio → Branch → Task → Research Run → Artifact/Experiment.**

A branch may survive many runs. A task should represent one uncertainty-reducing mission. One scheduler wakeup performs at most one task/shift.

## Portfolio discipline

Maintain multiple independent branches so the lab does not spend hundreds of runs on a dead local optimum. Current portfolio is in `lab/registry/branches.json` and `lab/portfolio/PORTFOLIO.md`.

Every 24th published research row is a synthesis/portfolio run unless a safety-critical or decisive experiment result should take precedence. Synthesis may reprioritize branches and queue new work; it is still exactly one task.

## Computational funnel

Use the cheapest trustworthy model first:

`closed-form / scaling -> low-order numerical model -> parameter sweep / uncertainty -> higher-fidelity model -> FEA/CFD only where decisive -> bench measurement -> replication`.

Do not spend high-fidelity compute on a design that fails a cheaper invariant or energy ledger. Conversely, do not treat a toy model as proof against a specific geometry when the neglected degree of freedom is the hypothesis.

## Hardware boundary

The repo can design, simulate, identify uncertainties, and analyze measurements. It cannot turn a simulation into a bench result. A branch whose decisive unknown is hardware-only must become `NEEDS DATA` and either wait on an explicit experiment task or yield desk-research priority to another branch.

## Completion definition

A successful shift materially reduces uncertainty and leaves enough durable truth that a different agent with no chat history can safely continue. Producing prose is not itself progress.
