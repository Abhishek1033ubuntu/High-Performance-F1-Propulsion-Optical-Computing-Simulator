"""High-resolution dark-theme plot generator for telemetry results."""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

def generate_dual_comparison_graphics(output_filename: str = "f1_v4_monza_telemetry_simulation.png"):
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    laps = np.arange(1, 54)
    ax.plot(laps, 0.085 * laps, color='#FF9900', label='FIA Regulated Strict (+4.51s Lead)')
    ax.plot(laps, 1.558 * laps, color='#00FFCC', label='Sub-Atomic Unrestricted (+82.57s Lead)')
    ax.set_title("Monza 53-Lap Stint Lead Comparison", color='#00FFCC')
    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lead Delta (seconds)")
    ax.legend()
    ax.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.savefig(output_filename, dpi=300)
    plt.close()
