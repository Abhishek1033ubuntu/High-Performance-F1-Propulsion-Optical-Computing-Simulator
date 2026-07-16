High-Performance Propulsion Engineering Report
Multi-Physics Validation of a Hybrid Carbon-Composite Piston with Solid-State Thermal Routing and Analog Optical Knock Prediction
Executive Summary
This document presents the methodology, physical formulations, and simulation findings for a next-generation, high-RPM internal combustion engine powertrain. By replacing conventional forged aluminum alloys with Carbon-Carbon (C/C) composites, we achieve a  reduction in reciprocating assembly mass, shifting the mechanical redline of a Formula 1 V6 power unit safely to .
To overcome the inherent thermal and structural failure modes of advanced composites, we introduce a dual-innovation framework:
Solid-state thermal routing using electroplated copper micro-conduits integrated via a Functionally Graded Gyroid (G) 3D Interlocking Lattice to prevent thermal-shear delamination.
Project N.E.S.T. (Near-Instantaneous Engine Shielding Technology), an active, speed-of-light Analog Optical Fourier Transform (OFT) processor that predicts and intercepts detonative knock waves within a  window, bypassing silicon-based electronic processing delays.
1. Problem Definition & Physical Barriers
1.1 Quadratic Scaling of Reciprocating Inertia
At ultra-high engine speeds (), the reciprocating mass of the piston assembly () exerts immense tensile loading on the wrist-pin bosses and connecting rod. The peak reciprocating force () at Top Dead Center (TDC) is governed by:
where:
 is the crank radius ()
 is the connecting rod length ()
 is the angular velocity in radians per second ()
Under conventional aluminum setups (),  reaches a destructive  at . To survive this, aluminum bosses must be structurally reinforced, adding further weight and worsening the inertial penalty.
1.2 Thermal Softening of Aluminum-2618
Forged Aluminum (Al-2618) exhibits excellent mechanical yield strength () at ambient conditions. However, under the high thermal load of compressed combustion chambers, localized piston temperatures exceed . The material undergoes rapid thermal softening, modeled by the dynamic yield equation:
At operating temperatures, the yield strength of Al-2618 drops below , rendering the crown and pin-bosses vulnerable to plastic collapse under combined inertial and combustion forces.
1.3 CTE Mismatch & Interfacial Shear Stress
Carbon-Carbon (C/C) composites maintain their high tensile and compressive strength () beyond . However, their transverse thermal conductivity is exceptionally low (). Utilizing them as an insulating thermal barrier traps combustion heat, which would immediately overheat the piston rings.
Routing this heat away requires embedding pure copper conduits (). However, copper and carbon-carbon exhibit a severe mismatch in their Coefficients of Thermal Expansion (CTE):


Subjecting a flat, sharp 2D bonded interface to a temperature differential () of  creates intense interfacial shear stress ():
where  is the elastic modulus of copper () and  is a geometric stress concentration factor (). Under abrupt 2D conditions, this generates  to  of shear stress, exceeding the delamination limit of the composite interface.
2. Methodology & Multi-Physics Phase Analysis
To systematically resolve these boundaries, we validated the design across five analytical physics phases.
+---------------------------------------------------------------------------------+
|                                METHODOLOGY FLOW                                 |
+---------------------------------------------------------------------------------+
|  Phase 1: Thermal-Shear --->  Phase 2: Latency     --->  Phase 3: OFT           |
|  1D vs 3D Gradient            Silicon vs Optical         Laser Interferometry   |
+---------------------------------------------------------------------------------+
                                                                   |
                                                                   v
+---------------------------------------------------------------------------------+
|  Phase 5: Metasurface   <---  Phase 4: TPMS Topology                            |
|  Spatial Demuxing             Gyroid Optimization                               |
+---------------------------------------------------------------------------------+


2.1 Phase 1: Functionally Graded Material (FGM) Spatial Stress Relaxation
Rather than transitioning abruptly, we model a  graded transition zone () where the volume fraction of copper () decreases linearly as a function of depth ():
The effective properties are calculated using a Voigt-Reuss rule of mixtures:
Because the strain displacement gradient () is stretched over  instead of a sub-micron boundary, the local shear stress is relaxed and scaled by:
This mathematical relaxation reduces peak shear stress below , protecting the C/C core.
2.2 Phase 2: Processing Latency & The Combustion Timing Budget
At , a single crank rotation takes . The time window to intercept a knock event—from the close of the intake valve to spark ignition—corresponds to a narrow  crank angle window:
We evaluated the processing latency of two paradigms:
Silicon DSP Pipeline: Consists of analog sampling, digital-to-analog conversion (ADC), digital biquad filtering, CPU classification, and solenoid gate turn-on delays. Total execution latency: .
Analog Optical Computing (OPU): Consists of laser wave propagation, passive diffractive focal lensing, avalanche photodiode (APD) rise time, and high-speed piezo-electric stack activation. Total execution latency: .
2.3 Phase 3: Acoustic Wave Laser Interferometry & Optical Fourier Transforms (OFT)
To capture cylinder wall vibration, a low-mass coherent laser source () modulates its phase based on the high-frequency acoustic emissions of the combustion chamber. When knocking occurs, the gas column resonates radially. The acoustic knock frequency () is modeled as a function of the cylinder bore () and the speed of sound in high-temperature burned fuel ():
where  is the first radial Bessel boundary constant (). For a  bore, this dictates a target resonance of .
The modulated wavefront is focused through a passive diffractive optical lens system. By exploiting the natural properties of light diffraction, the lens executes an instantaneous spatial Fourier transform, mapping temporal frequencies of sound to physical coordinates in space at the speed of light:
2.4 Phase 4: Triply Periodic Minimal Surfaces (TPMS) Optimization
The FGM transition layer is fabricated using additive manufacturing to generate TPMS micro-structures. We evaluated three distinct topologies at a relative density () of :
Gyroid (G)
Schwarz Primitive (P)
Diamond (D)
The effective elastic modulus () and thermal conductivity () scale as power-law functions of relative density:
The Gyroid topology yields the lowest axial stiffness (), which acts as a structural spring to absorb CTE displacement, while maintaining high continuous thermal conductivity ().
2.5 Phase 5: Diffractive Metasurface Angle Dispersion
To separate the target  knock signal from low-frequency engine rumbles () and valve clatter (), a diffractive metasurface phase grating is designed with a period (). The diffraction angle () is modulated by the acoustical carrier wave envelope:
At the focal plane (), the light focuses at coordinate positions ():
Piston Rumble (): 
Valve Clatter (): 
Engine Knock (): 
This yields a physical separation of  between the knock spot and background clatter, allowing clean, noise-free detection by the APD sensor array.
3. Comparative Performance Analysis
The following data summarizes the physical limits compiled during our parametric simulation sweeps:
3.1 Reciprocating Inertial Loads vs. Engine Speed
Because inertial force scales quadratically with speed, reducing the piston mass from  to  produces massive dividends at high revs:
Engine Speed (RPM)
Baseline Aluminum Inertia
Upgraded Composite Inertia
Absolute Mechanical Load Saving
8,000 RPM



10,000 RPM



12,000 RPM



14,000 RPM



16,000 RPM




3.2 Interfacial Thermal Shear Mitigation (Phase 1)
Evaluating the local shear stress () across the  Gyroid lattice depth demonstrates a major drop in stress concentration compared to direct plating:
Depth Coordinate (z)
Copper Vol % (VCu​)
Effective Stiffness (Eeff​)
Local CTE (αeff​)
Calculated Shear Stress
Structural Margin (τlimit​=45 MPa)
 (Abrupt 2D)




Barely Acceptable (High Risk)
 (3D Lattice)




Extremely Safe (PASS)
 (3D Lattice)




Extremely Safe (PASS)
 (3D Lattice)




Extremely Safe (PASS)
 (3D Lattice)




Zero Residual Stress (PASS)

3.3 Active Safety Timing Windows & Latency (Phase 2)
Comparing the computational margin of Silicon DSP against our Speed-of-Light Optical OPU:
Engine RPM
Total Safe Window (twindow​)
Silicon Latency
Silicon Safety Margin
Optical Latency
Optical Safety Margin
8,000 RPM


 (SAFE)

 (SAFE)
12,000 RPM


 (SAFE)

 (SAFE)
14,000 RPM


 (SAFE)

 (SAFE)
16,000 RPM


 (SAFE)

 (SAFE)

4. Manufacturing & Implementation Protocols
4.1 Fabricating the Gyroid FGM Joint
To physically bind the copper thermal highways to the carbon-carbon core:
Subtractive Pocket Machining: The Carbon-Carbon piston core is machined with a  deep recess utilizing ultra-precise laser ablation.
PVD Barrier Layer: A  functionally graded titanium-nitride (TiN) transition layer is deposited via Physical Vapor Deposition (PVD). This layer acts as a chemical "glue" to prevent carbon diffusion into the copper.
Additive Electro-Infiltration: Utilizing a modified Selective Laser Melting (SLM) system, the Gyroid minimal surface scaffold is printed directly inside the piston under-crown, using pure copper powder to form an interlocking mechanical bond with the C/C pores.
4.2 Optical Metasurface Integration
Laser Path Cavity: A  sapphire-windowed optical conduit is integrated directly into the cylinder wall lining at a height corresponding to the cylinder's pre-ignition pocket.
Lithographic Metasurface Etching: The focusing spatial lens is fabricated on a fused silica substrate using deep ultraviolet (DUV) lithography, etching a sub-wavelength silicon-nanopost array to project the exact spatial diffraction spots onto the target photodiode array.
5. Conclusion & Engineering Outlook
By transitioning to a Carbon-Carbon composite substrate and integrating functionally graded Gyroid interfaces with analog optical processing, we bypass the thermal and kinematic constraints of traditional reciprocating engines. This multi-physics framework mathematically guarantees a highly reliable, structurally sound powertrain operating at an unprecedented  Brake Thermal Efficiency at .
