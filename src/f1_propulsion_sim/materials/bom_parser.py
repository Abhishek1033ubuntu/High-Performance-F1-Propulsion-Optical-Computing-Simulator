"""YAML and JSON Schema Parser for Chassis & Engine Block BOMs."""

import yaml

class F1BOMParser:
    def __init__(self, yaml_content: str):
        self.data = yaml.safe_load(yaml_content)["chassis_assembly"]

    def extract_mass_savings(self) -> float:
        total_baseline, total_optimized = 0.0, 0.0
        for sub in self.data["subassemblies"]:
            for cmp in sub["components"]:
                qty = cmp.get("quantity", 1)
                b = cmp["baseline_mass_g"]
                opt = cmp.get("optimized_mass_g", b)
                total_baseline += b
                total_optimized += opt
        return (total_baseline - total_optimized) / 1000.0
