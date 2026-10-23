#!/usr/bin/env python3
"""Command-Line Interface for running F1 Propulsion simulations."""

import argparse
from f1_propulsion_sim.solvers.monza_solver import F1MultiPhysicsSolver
from f1_propulsion_sim.visualization.telemetry_plots import generate_dual_comparison_graphics


def main():
    parser = argparse.ArgumentParser(description="F1 Propulsion & Sub-Atomic Material Simulator")
    parser.add_argument(
        "--mode",
        choices=["FIA_REGULATED_STRICT", "SUBATOMIC_UNRESTRICTED_ULTRA", "DUAL"],
        default="DUAL",
        help="Compliance execution mode"
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="Generate high-resolution telemetry graphic PNG"
    )

    args = parser.parse_args()

    if args.mode == "DUAL":
        s1 = F1MultiPhysicsSolver("FIA_REGULATED_STRICT").solve()
        s2 = F1MultiPhysicsSolver("SUBATOMIC_UNRESTRICTED_ULTRA").solve()
        print(f"[FIA REGULATED] Lap Time: {s1['optimized_lap_time']} | Mass: {s1['vehicle_mass_kg']} kg")
        print(f"[UNRESTRICTED]  Lap Time: {s2['optimized_lap_time']} | Mass: {s2['vehicle_mass_kg']} kg")
    else:
        s = F1MultiPhysicsSolver(args.mode).solve()
        print(f"[{args.mode}] Lap Time: {s['optimized_lap_time']} | Mass: {s['vehicle_mass_kg']} kg")

    if args.plot:
        generate_dual_comparison_graphics("f1_v4_monza_telemetry_simulation.png")


if __name__ == "__main__":
    main()
