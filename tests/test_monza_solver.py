from f1_propulsion_sim.solvers.monza_solver import F1MultiPhysicsSolver

def test_strict_mode_mass():
    solver = F1MultiPhysicsSolver("FIA_REGULATED_STRICT")
    res = solver.solve()
    assert res["vehicle_mass_kg"] == 798.0

def test_unrestricted_mode_mass():
    solver = F1MultiPhysicsSolver("SUBATOMIC_UNRESTRICTED_ULTRA")
    res = solver.solve()
    assert res["vehicle_mass_kg"] == 753.488
