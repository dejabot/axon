# Module 4: Control Physics & Voltage Models

Welcome to **Module 4: Control Physics & Voltage Models**. In this module, we bridge physical dynamics with modern autonomous control systems—showing why physics-based feedforward models (`kS`, `kV`, `kA`, `kG`) eliminate lag and how closed-loop PID controllers achieve tight, stable trajectory tracking.

---

## Concepts in this Module
* **[Concept 01: Physics Feedforward: kS, kV, kA, and kG Models](01_concept_voltage_feedforward_models/)**
  * *The Everyday Problem:* Why does a pure feedback PID controller lag behind fast motion profiles or droop under gravity? The physics of predicting required motor voltage from desired velocity and acceleration.
  * *Code & WPILib:* `SimpleMotorFeedforward`, `ElevatorFeedforward`, `ArmFeedforward`, and `V = kS · sgn(v) + kV · v + kA · a + kG`.
  * *Visualizer:* [01_concept_voltage_feedforward_models/demo.html](01_concept_voltage_feedforward_models/demo.html)

* **[Concept 02: Closed-Loop PID Tuning & Step-Response Stability](02_concept_closed_loop_pid_tuning/)**
  * *The Everyday Problem:* How do you tune a flywheel RPM velocity loop or an arm position servo without sluggish settling, violent overshoot, or dangerous oscillations?
  * *Code & WPILib:* Proportional stiffness (`kP`), Integral error accumulation (`kI`), Derivative damping (`kD`), and `edu.wpi.first.math.controller.PIDController`.
  * *Visualizer:* [02_concept_closed_loop_pid_tuning/demo.html](02_concept_closed_loop_pid_tuning/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../03_dynamics_energy/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 3: Dynamics</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Physics Axon Home</a></div>
  <div><a href="01_concept_voltage_feedforward_models/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: Voltage Feedforward →</a></div>
</div>
