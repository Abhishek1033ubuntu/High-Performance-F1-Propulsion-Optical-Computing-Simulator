# Sub-Atomic Materials API Integration Guide

To query material profiles directly from `subatomic-materials-suite`:

```python
from f1_propulsion_sim.materials.material_suite import MaterialSuiteBridge

bridge = MaterialSuiteBridge()
spec = bridge.fetch_material_spec("MAT-ALLI-MMC-GYROID-01")
print(spec)
