from pathlib import Path

from energy_lab.cli import wet_reference_snapshot
from energy_lab.labops import parse_run_id, validate_repository


def test_run_id_parser():
    assert parse_run_id("R073") == 73


def test_repository_contract_is_valid():
    assert validate_repository(Path(".")) == []


def test_wet_snapshot_preserves_r073_gate_and_phase_region():
    snap = wet_reference_snapshot()
    assert 108_000 < snap["gate_re_g_per_v_w_m3_k"] < 109_000
    central = next(
        row for row in snap["grid"]
        if row["hydraulic_radius_mm"] == 0.25 and row["frequency_hz"] == 5.0
    )
    assert -18.0 < central["thermal_phase_deg"] < -14.0
    assert -16.0 < central["mass_phase_deg"] < -12.0
