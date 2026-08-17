# Module 2: Projectile Ballistics & Trajectories

Welcome to **Module 2: Projectile Ballistics & Trajectories**. In this module, we develop the physics models needed to calculate shooter flywheel launch speeds, release hood angles, aerodynamic drag deceleration, Magnus backspin lift, and vector compensation for shooting on the move.

---

## Concepts in this Module
* **[Concept 01: 2D Parabolic Projectile Motion & Launch Angles](01_concept_2d_kinematic_ballistics/)**
  * *The Everyday Problem:* How does a robot calculate the exact flywheel RPM and hood angle needed to score into a high target basket from any arbitrary distance on the field?
  * *Code & WPILib:* 2D kinematic trajectory equations: `x(t) = v₀ · cos(θ) · t`, `y(t) = y₀ + v₀ · sin(θ) · t - ½ · g · t²`, and solving for launch velocity `v₀`.

* **[Concept 02: Aerodynamic Drag, Magnus Spin & Shooting on the Move](02_concept_drag_spin_shooting_on_move/)**
  * *The Everyday Problem:* Foam game pieces slow down from air resistance and lift from backspin. How do you model drag and compensate when the robot is driving at 3.5 m/s while shooting?
  * *Code & WPILib:* Numerical drag integration `F_drag = -½ · ρ · C_d · A · v²`, Magnus lift, and vector velocity addition (`v_target = v_launch + v_robot`).

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_motors_electromechanics/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1: DC Motors</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Physics Axon Home</a></div>
  <div><a href="01_concept_2d_kinematic_ballistics/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: 2D Ballistics →</a></div>
</div>
