from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ALLOWED_STATUSES = {"ready", "claimed", "blocked", "done", "cancelled"}
REQUIRED_PATHS = [
    "lab/RUNNER.md",
    "lab/CHARTER.md",
    "lab/OPERATING-SYSTEM.md",
    "lab/STATE.md",
    "lab/HANDOFF.md",
    "lab/registry/queue.json",
    "lab/registry/run-counter.json",
    "lab/registry/branches.json",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_run_id(run_id: str) -> int:
    if not isinstance(run_id, str) or not run_id.startswith("R") or not run_id[1:].isdigit():
        raise ValueError(f"invalid research run id: {run_id!r}")
    return int(run_id[1:])


def validate_queue(queue: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    tasks = queue.get("tasks")
    if not isinstance(tasks, list):
        return ["queue.tasks must be a list"]

    ids = [task.get("id") for task in tasks]
    if any(not task_id for task_id in ids):
        errors.append("every task needs a non-empty id")
    if len(ids) != len(set(ids)):
        errors.append("queue task ids must be unique")

    id_set = set(ids)
    for task in tasks:
        task_id = task.get("id", "<missing>")
        status = task.get("status")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{task_id}: invalid status {status!r}")
        for dep in task.get("depends_on", []):
            if dep not in id_set:
                errors.append(f"{task_id}: missing dependency {dep}")
        claim = task.get("claim")
        if status == "claimed":
            if not isinstance(claim, dict):
                errors.append(f"{task_id}: claimed task requires claim object")
            else:
                for key in ("shift_id", "worker_id", "claimed_at", "lease_expires_at", "reserved_run_id"):
                    if not claim.get(key):
                        errors.append(f"{task_id}: claim missing {key}")
        elif claim is not None:
            errors.append(f"{task_id}: non-claimed task must have claim=null")
    return errors


def validate_run_counter(counter: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    next_run = counter.get("next_research_run")
    last_run = counter.get("last_published_run")
    if not isinstance(next_run, int) or next_run <= 0:
        errors.append("next_research_run must be a positive integer")
    try:
        last_number = parse_run_id(last_run)
    except ValueError as exc:
        errors.append(str(exc))
        return errors
    if isinstance(next_run, int) and next_run <= last_number:
        errors.append("next_research_run must be greater than last_published_run")
    reservations = counter.get("active_reservations", [])
    if not isinstance(reservations, list):
        errors.append("active_reservations must be a list")
    return errors


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            errors.append(f"missing required path: {rel}")

    queue_path = root / "lab/registry/queue.json"
    counter_path = root / "lab/registry/run-counter.json"
    if queue_path.exists():
        errors.extend(validate_queue(load_json(queue_path)))
    if counter_path.exists():
        errors.extend(validate_run_counter(load_json(counter_path)))
    return errors
