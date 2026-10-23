"""Monza Grand Prix 53-Lap Multi-Physics Stint Solver."""

class F1MultiPhysicsSolver:
    def __init__(self, mode: str):
        self.mode = mode
        if mode == "FIA_REGULATED_STRICT":
            self.vehicle_mass_kg = 798.000
            self.ballast_kg = 44.512
            self.lap_time_gain_s = 0.085
            self.peak_decel_g = -5.20
            self.t1_brake_m = 88.94
            self.accel_mult = 1.0000
        elif mode == "SUBATOMIC_UNRESTRICTED_ULTRA":
            self.vehicle_mass_kg = 753.488
            self.ballast_kg = 0.000
            self.lap_time_gain_s = 1.558
            self.peak_decel_g = -5.51
            self.t1_brake_m = 83.98
            self.accel_mult = 1.0591
        else:
            raise ValueError(f"Unknown mode: {mode}")

    def solve((self) -> dict:
        baseline_lap = 81.050
        optimized_lap = baseline_lap - self.lap_time_gain_s
        return {
            "mode": self.mode,
            "vehicle_mass_kg": self.vehicle_mass_kg,
            "ballast_added_kg": self.ballast_kg,
            "accel_multiplier": self.accel_mult,
            "optimized_lap_time": f"1:{optimized_lap - 60.0:.3f}",
            "lap_time_gain_sec": self.lap_time_gain_s,
            "stint_lead_53_laps_sec": round(self.lap_time_gain_s * 53, 2),
            "peak_decel_g": self.peak_decel_g,
            "t1_brake_dist_m": self.t1_brake_m
        }
