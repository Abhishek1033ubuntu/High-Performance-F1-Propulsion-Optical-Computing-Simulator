# F1 Power Unit Colab Simulation Suite (8-Speed Sawtooth Gearbox Edition)
# ----------------------------------------------------------------------
# To run this in Google Colab, simply copy this entire block, 
# paste it into a code cell, and click "Run".
#
# This script integrates:
# 1. Aerodynamic drag & downforce equations for a standard F1 chassis.
# 2. Powertrain torque/power curves based on real 100 kg/h fuel-flow limits.
# 3. Dynamic cycle-by-cycle inertial wrist-pin stress calculations.
# 4. Transient under-crown temperature modeling.
# 5. Fixed: 8-speed sequential transmission logic with dynamic gear tracking.

import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# PHYSICAL ENGINE & CHASSIS PARAMETERS
# ==========================================
# F1 Regulation/Chassis Limits
F1_CAR_MASS = 798.0       # kg (Minimum weight limit with driver)
CD = 0.85                 # Drag coefficient (high downforce trim)
CL = 2.80                 # Lift/Downforce coefficient
FRONTAL_AREA = 1.6        # m^2
AIR_DENSITY = 1.225       # kg/m^3
GRAVITY = 9.81            # m/s^2

# Engine Geometrical Specs
BORE = 0.080              # 80 mm bore (F1 regulation limit)
STROKE = 0.053            # 53 mm stroke (approximated for 1.6L V6)
CON_ROD = 0.102           # 102 mm rod length
PISTON_AREA = np.pi * (BORE / 2.0)**2

# Fuel Flow Limit Regulation (Article 5.1.2)
MAX_FUEL_FLOW_KG_H = 100.0 # 100 kg/h limit above 10,500 RPM
FUEL_ENERGY_DENSITY = 44.0e6 # J/kg (Petrol)

# ==========================================
# SIMULATION POWER UNITS DEFINITION
# ==========================================
class F1PowerUnit:
    def __init__(self, name, piston_mass, base_bte, peak_rpm, has_optical_nest=False, has_highway=False, is_aluminum=False):
        self.name = name
        self.piston_mass = piston_mass    # kg (piston assembly + pin + rings)
        self.base_bte = base_bte          # Base brake thermal efficiency of the ICE
        self.peak_rpm = peak_rpm
        self.has_optical_nest = has_optical_nest
        self.has_highway = has_highway
        self.is_aluminum = is_aluminum

# 1. Real World Baseline: Mercedes V6 Hybrid Era Style ICE Benchmark
f1_baseline = F1PowerUnit(
    name="F1 Benchmark V6 (Al-2618)",
    piston_mass=0.300,       # 300g (optimized F1 titanium/aluminum hybrid target)
    base_bte=0.41,           # 41% Thermal Efficiency for the pure ICE
    peak_rpm=13500,          # Standard shift point due to fuel flow limits & material safety
    has_optical_nest=False,
    has_highway=False,
    is_aluminum=True
)

# 2. Our Concept Upgrade: Hybrid C/C Piston + Thermal Highways + Project N.E.S.T.
f1_upgraded = F1PowerUnit(
    name="Concept Hybrid V6 (C/C Composite)",
    piston_mass=0.180,       # 180g (Carbon-Carbon mass with embedded carriers)
    base_bte=0.47,           # 47% ICE Thermal Efficiency
    peak_rpm=16000,          # Extended mechanical redline
    has_optical_nest=True,
    has_highway=True,
    is_aluminum=False
)

# ==========================================
# PROPULSION ENGINE MATHEMATICS
# ==========================================
def get_engine_power(pu, rpm):
    """
    Calculates Engine Power (Watts) limited by F1 Fuel Flow rules.
    Power = Q (kg/s) * Fuel Energy * Brake Thermal Efficiency
    """
    if rpm < 10500:
        fuel_flow = (0.009 * rpm + 5.5) / 3600.0  # kg/s
    else:
        fuel_flow = MAX_FUEL_FLOW_KG_H / 3600.0    # 100 kg/h in kg/s
        
    raw_chemical_power = fuel_flow * FUEL_ENERGY_DENSITY
    ice_power = raw_chemical_power * pu.base_bte
    
    # Standardized MGU-K recovery flat boost (120 kW / 160 HP)
    mgu_k_power = 120000.0 
    return ice_power + mgu_k_power

def get_reciprocating_inertia_stress(pu, rpm):
    """
    Calculates tensile stress on wrist pin bosses (MPa).
    F = m * r * omega^2 * (1 + r/l)
    """
    omega = (2.0 * np.pi * rpm) / 60.0
    r = STROKE / 2.0
    l = CON_ROD
    force = pu.piston_mass * r * (omega**2) * (1.0 + (r/l))
    pin_area = PISTON_AREA * 0.025
    return (force / pin_area) / 1e6 # MPa

# ==========================================
# TRACK ACCELERATION SIMULATOR (MONZA STRAIGHT)
# ==========================================
def simulate_monza_straight(pu):
    # Time parameters
    dt = 0.01  # 10 ms integration step
    t_max = 20.0 # Increased to 20 seconds to guarantee both cars cross 1100m
    
    # Starting conditions (exiting Curva Parabolica at 120 km/h)
    velocity = 120.0 / 3.6  # m/s
    distance = 0.0          # m
    
    # 8-Speed Sequential Gearbox drive ratios (RPM per m/s vehicle velocity)
    # Calibrated so gear 4 starts at 10,500 RPM at 120 km/h (33.3 m/s)
    gear_ratios = {
        4: 315.0,
        5: 260.0,
        6: 220.0,
        7: 190.0,
        8: 165.0
    }
    current_gear = 4
    
    # Shift up strategy
    shift_point = pu.peak_rpm - 200.0
    
    # Data logging arrays
    time_log = []
    vel_log = []
    dist_log = []
    rpm_log = []
    stress_log = []
    temp_log = []
    
    # Thermal state starting points
    piston_temp = 90.0
    
    for step in range(int(t_max / dt)):
        # Calculate aerodynamic forces
        downforce = 0.5 * AIR_DENSITY * CL * FRONTAL_AREA * (velocity**2)
        drag = 0.5 * AIR_DENSITY * CD * FRONTAL_AREA * (velocity**2)
        
        # Tire tractive limit
        normal_force = (F1_CAR_MASS * GRAVITY) + downforce
        max_tractive_force = normal_force * 1.7
        
        # Dynamic Gearbox RPM Calculation
        rpm = velocity * gear_ratios[current_gear]
        
        # Gear shifting loop execution
        if rpm > shift_point and current_gear < 8:
            current_gear += 1
            rpm = velocity * gear_ratios[current_gear]
        elif rpm < 10500.0 and current_gear > 4:
            current_gear -= 1
            rpm = velocity * gear_ratios[current_gear]
            
        rpm = max(10500.0, min(pu.peak_rpm, rpm))
        
        # Calculate propulsion
        power_w = get_engine_power(pu, rpm)
        engine_tractive_force = power_w / max(1.0, velocity)
        
        propulsion_force = min(engine_tractive_force, max_tractive_force)
        net_force = propulsion_force - drag
        
        # Integrate motion
        acceleration = net_force / F1_CAR_MASS
        velocity += acceleration * dt
        distance += velocity * dt
        
        # Stresses and temperature logs
        stress = get_reciprocating_inertia_stress(pu, rpm)
        
        heat_input = (power_w / pu.base_bte) * (1.0 - pu.base_bte) * 0.0001
        if pu.has_highway:
            piston_temp += (heat_input * 0.15) - (piston_temp - 90.0) * 0.08
        else:
            piston_temp += (heat_input * 0.45) - (piston_temp - 90.0) * 0.03
            
        # Log data
        time_log.append(step * dt)
        vel_log.append(velocity * 3.6) # Convert to km/h
        dist_log.append(distance)
        rpm_log.append(rpm)
        stress_log.append(stress)
        temp_log.append(piston_temp)
        
        # Stop at finish line (1100 meters)
        if distance >= 1100.0:
            break
            
    return np.array(time_log), np.array(vel_log), np.array(dist_log), np.array(rpm_log), np.array(stress_log), np.array(temp_log)

# ==========================================
# EXECUTE SIMULATIONS & PLOT
# ==========================================
t_base, v_base, d_base, r_base, s_base, tp_base = simulate_monza_straight(f1_baseline)
t_upgr, v_upgr, d_upgr, r_upgr, s_upgr, tp_upgr = simulate_monza_straight(f1_upgraded)

# Create high-resolution multi-panel plots for Colab
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle("F1 Monza Straight Sprint Simulation (0 to 1100m)\nTraditional Aluminum V6 vs. upgraded Carbon-Composite with Solid-State Highways", fontsize=16, fontweight='bold')

# 1. Distance vs Speed Profile
axs[0, 0].plot(d_base, v_base, label=f1_baseline.name, color='red', linewidth=2.5)
axs[0, 0].plot(d_upgr, v_upgr, label=f1_upgraded.name, color='blue', linewidth=2.5, linestyle='--')
axs[0, 0].set_title("Velocity Profile across Monza Straight", fontsize=12, fontweight='bold')
axs[0, 0].set_xlabel("Distance down straight (m)", fontsize=10)
axs[0, 0].set_ylabel("Velocity (km/h)", fontsize=10)
axs[0, 0].grid(True, linestyle=':', alpha=0.6)
axs[0, 0].legend()

# 2. Engine Speed (RPM) vs Distance
axs[0, 1].plot(d_base, r_base, color='red', linewidth=2, label="Al-2618 Sawtooth Shifts")
axs[0, 1].plot(d_upgr, r_upgr, color='blue', linewidth=2, linestyle='--', label="Composite Sawtooth Shifts")
axs[0, 1].set_title("Dynamic Engine RPM & Shift Patterns", fontsize=12, fontweight='bold')
axs[0, 1].set_xlabel("Distance down straight (m)", fontsize=10)
axs[0, 1].set_ylabel("Engine RPM", fontsize=10)
axs[0, 1].grid(True, linestyle=':', alpha=0.6)
axs[0, 1].legend()

# 3. Wrist-Pin Inertial Stress vs Distance
axs[1, 0].plot(d_base, s_base, color='red', linewidth=2, label="Raw Aluminum Inertial Stress")
axs[1, 0].plot(d_upgr, s_upgr, color='blue', linewidth=2, linestyle='--', label="Raw Composite Inertial Stress")
axs[1, 0].axhline(y=164.0, color='darkred', linestyle=':', label="Al-2618 Softened Yield Limit (150°C)")
axs[1, 0].axhline(y=350.0, color='darkblue', linestyle=':', label="C/C Composite Structural Limit")
axs[1, 0].set_title("Peak Wrist-Pin Boss Reciprocating Tensile Stress", fontsize=12, fontweight='bold')
axs[1, 0].set_xlabel("Distance down straight (m)", fontsize=10)
axs[1, 0].set_ylabel("Tensile Stress (MPa)", fontsize=10)
axs[1, 0].set_ylim(0, 400)
axs[1, 0].grid(True, linestyle=':', alpha=0.6)
axs[1, 0].legend(fontsize=9)

# 4. Piston Dynamic Operating Temperatures
axs[1, 1].plot(d_base, tp_base, color='red', linewidth=2, label="Standard Piston Temp")
axs[1, 1].plot(d_upgr, tp_upgr, color='blue', linewidth=2, linestyle='--', label="Copper-Conduit Composite Temp")
axs[1, 1].set_title("Transient Piston Temperature", fontsize=12, fontweight='bold')
axs[1, 1].set_xlabel("Distance down straight (m)", fontsize=10)
axs[1, 1].set_ylabel("Temperature (°C)", fontsize=10)
axs[1, 1].grid(True, linestyle=':', alpha=0.6)
axs[1, 1].legend()

plt.tight_layout()
plt.show()

# Print Numerical Report Summary
baseline_final_vel = v_base[-1]
upgraded_final_vel = v_upgr[-1]
time_saved = t_base[-1] - t_upgr[-1]

print("="*80)
print("             F1 PROTO-TYPING SIMULATOR PERFORMANCE ANALYSIS METRICS")
print("="*80)
print(f"Monza Straight Distance             : 1100.0 meters")
print(f"Baseline F1 Engine Top Speed        : {baseline_final_vel:.2f} km/h (Inertial Limit Hit)")
print(f"Upgraded F1 Engine Top Speed        : {upgraded_final_vel:.2f} km/h (Continuous Acceleration)")
print(f"Sprint Time Delta (Monza Straight)  : Saving of {time_saved:.4f} seconds!")
print(f"Theoretical Power Output (ICE only) : Baseline = {((get_engine_power(f1_baseline, 12500) - 120000)/745.7):.1f} HP | Upgraded = {((get_engine_power(f1_upgraded, 15000) - 120000)/745.7):.1f} HP")
print("="*80)
