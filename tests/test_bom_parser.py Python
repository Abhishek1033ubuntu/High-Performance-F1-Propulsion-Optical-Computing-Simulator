import pytest
from f1_propulsion_sim.materials.bom_parser import F1BOMParser

YAML_SAMPLE = """
chassis_assembly:
  subassemblies:
    - id: "SUB-01"
      components:
        - baseline_mass_g: 1000.0
          optimized_mass_g: 800.0
"""

def test_mass_savings_calculation():
    parser = F1BOMParser(YAML_SAMPLE)
    assert parser.extract_mass_savings() == pytest.approx(0.2)
