# Sub-Atomic Materials API Integration Guide

To query material profiles directly from `subatomic-materials-suite`:

```python
from f1_propulsion_sim.materials.material_suite import MaterialSuiteBridge

bridge = MaterialSuiteBridge()
spec = bridge.fetch_material_spec("MAT-ALLI-MMC-GYROID-01")
print(spec)
---

### Standalone Examples & Unit Tests (`examples/` & `tests/`)

#### `examples/monza_stint_simulation.py`
```python
#!/usr/bin/env python3
"""Standalone example script to execute Monza stint simulation."""

from f1_propulsion_sim.solvers.monza_solver import F1MultiPhysicsSolver

if __name__ == "__main__":
    solver = F1MultiPhysicsSolver("SUBATOMIC_UNRESTRICTED_ULTRA")
    results = solver.solve()
    print("=== MONZA STINT SIMULATION RESULTS ===")
    for key, val in results.items():
        print(f"{key}: {val}")
