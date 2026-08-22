from __future__ import annotations

import argparse
import json
from pathlib import Path

from .labops import validate_repository
from .wet_core import (
    WetCorePoint,
    complex_diffusion_factor,
    penetration_depth,
    phase_deg,
    required_effective_conductance_density,
)


def wet_reference_snapshot() -> dict:
    base = WetCorePoint()
    gate = required_effective_conductance_density(
        p_dc_w=10.0,
        carnot_fraction=0.15,
        tc_k=base.tc_k,
        th_k=base.th_k,
        total_hx_volume_m3=1.025e-3,
        local_delta_t_k=10.0,
        hx_count=2,
    )
    grid = []
    for radius_mm in (0.20, 0.25, 0.30):
        for frequency_hz in (3.0, 5.0, 7.0):
            radius_m = radius_mm * 1e-3
            dth = penetration_depth(base.alpha_m2_s, frequency_hz)
            dm = penetration_depth(base.vapor_diffusivity_m2_s, frequency_hz)
            fth = complex_diffusion_factor(radius_m, dth)
            fm = complex_diffusion_factor(radius_m, dm)
            grid.append(
                {
                    "hydraulic_radius_mm": radius_mm,
                    "frequency_hz": frequency_hz,
                    "thermal_factor_real": fth.real,
                    "thermal_phase_deg": phase_deg(fth),
                    "mass_factor_real": fm.real,
                    "mass_phase_deg": phase_deg(fm),
                }
            )
    return {
        "evidence_state": "SIMULATED_SCREEN",
        "branch": "WET-01",
        "experiment": "EXP-WET-001",
        "gate_re_g_per_v_w_m3_k": gate,
        "gate_total_phase_deg_preferred_max": 30.0,
        "gate_wet_dissipative_loss_w_max": 2.3,
        "grid": grid,
        "warning": "Diffusion screen only; wall/contact/wet-film/interface lag and bench data are not supplied by this model.",
    }


def cmd_validate_repo(args: argparse.Namespace) -> int:
    errors = validate_repository(Path(args.root))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Energy Lab repository state: OK")
    return 0


def cmd_wet_snapshot(args: argparse.Namespace) -> int:
    payload = wet_reference_snapshot()
    text = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
        print(path)
    else:
        print(text)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="energy-lab")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate-repo")
    validate.add_argument("--root", default=".")
    validate.set_defaults(func=cmd_validate_repo)

    snapshot = sub.add_parser("wet-snapshot")
    snapshot.add_argument("--output")
    snapshot.set_defaults(func=cmd_wet_snapshot)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
