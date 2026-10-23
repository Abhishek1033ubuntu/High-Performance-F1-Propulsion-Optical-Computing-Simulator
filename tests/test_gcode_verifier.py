from f1_propulsion_sim.cam.gcode_parser import GCodeToolpathVerifier

def test_surface_finish():
    verifier = GCodeToolpathVerifier()
    assert verifier.verify_surface_finish() <= 0.018
