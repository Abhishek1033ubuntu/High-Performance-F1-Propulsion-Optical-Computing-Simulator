"""Kinetic Energy & Turn 1 Braking Contraction Engine."""

class BrakingDynamicsEngine:
    @staticmethod
    def calculate_stop_distance(v_entry_kmh: float, v_exit_kmh: float, decel_g: float) -> float:
        v1 = v_entry_kmh / 3.6
        v2 = v_exit_kmh / 3.6
        a = abs(decel_g) * 9.81
        return (v1**2 - v2**2) / (2 * a)
