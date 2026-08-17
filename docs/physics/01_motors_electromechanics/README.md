# Module 1: DC Motors & Electromechanics

Welcome to **Module 1: DC Motors & Electromechanics**. In this module, we explore how brushless DC motors (like the Kraken X60, Falcon 500, and NEO) convert electrical energy into mechanical torque, and how gearboxes multiply torque while scaling reflected load inertia.

---

## Concepts in this Module
* **[Concept 01: Brushless DC Motors, Back-EMF & Torque Curves](01_concept_motor_curves_back_emf/)**
  * *The Everyday Problem:* Why does a brushless motor draw 300+ Amps of current at a dead stop (stall), and why does output torque drop to zero when spinning freely at maximum RPM?
  * *Code & WPILib:* Modeling the fundamental electromechanical circuit: `V = I · R + ω / K_v`, torque `τ = K_t · I`, and `edu.wpi.first.math.system.plant.DCMotor`.
  * *Visualizer:* [01_concept_motor_curves_back_emf/demo.html](01_concept_motor_curves_back_emf/demo.html)

* **[Concept 02: Gear Ratios, Torque Multiplication & Reflected Inertia](02_concept_gearboxes_reflected_inertia/)**
  * *The Everyday Problem:* Why does a heavy 15 kg elevator feel like a lightweight feather to a motor when geared down 25:1? The physics of reflected load inertia scaling by `1 / G²`.
  * *Code & WPILib:* Torque multiplication `τ_out = G · τ_in · η` and reflected rotational inertia `J_reflected = J_load / G²`.
  * *Visualizer:* [02_concept_gearboxes_reflected_inertia/demo.html](02_concept_gearboxes_reflected_inertia/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Physics Axon Home</a></div>
  <div><a href="./" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="01_concept_motor_curves_back_emf/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: DC Motors & Back-EMF →</a></div>
</div>
