"""
High-Performance F1 Propulsion & Optical Computing Simulator Package
Version: 4.0.0
Author: Abhishek Singh
Copyright (c) 2026 Abhishek Singh
"""

__version__ = "4.0.0"
__author__ = "Abhishek Singh"
__license__ = "Apache-2.0"

from .solvers.monza_solver import F1MultiPhysicsSolver
from .materials.bom_parser import F1BOMParser

__all__ = ["F1MultiPhysicsSolver", "F1BOMParser"]
