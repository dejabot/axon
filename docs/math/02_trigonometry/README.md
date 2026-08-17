# Module 2: Trigonometry & Angles

Welcome to **Module 2: Trigonometry & Angles**. In this module, we build from everyday right triangles and the clock-hand unit circle up into 4-quadrant heading calculations, circle topology, swerve drive module speed flips, and 3D Quaternions.

---

## Concepts in this Module
* **[Concept 01: The Unit Circle & Trigonometric Ratios](01_concept_unit_circle_ratios/)**
  * *The Everyday Problem:* How does pushing a gamepad joystick decompose into forward and sideways wheel power?
  * *Code & Math:* SOH-CAH-TOA, unit circle projections, `cos` as horizontal shadow, `sin` as vertical height.
  * *Visualizer:* [01_concept_unit_circle_ratios/demo.html](01_concept_unit_circle_ratios/demo.html)

* **[Concept 02: 4-Quadrant Heading with atan2](02_concept_atan2_heading/)**
  * *The Everyday Problem:* Why does standard `tan⁻¹(y/x)` confuse aiming North-East with South-West?
  * *Code & Math:* The 4 quadrants, negative sign cancellations, and the robust `atan2(y, x)` function.
  * *Visualizer:* [02_concept_atan2_heading/demo.html](02_concept_atan2_heading/demo.html)

* **[Concept 03: Angle Wrapping & Swerve 180° Speed Flip](03_concept_angle_wrapping_swerve/)**
  * *The Everyday Problem:* Why does a naive angle subtraction make a robot spin 340° instead of turning 20°?
  * *Code & Math:* Modular angle difference on a circle, shortest path wrapping, and swerve drive direction inversion.
  * *Visualizer:* [03_concept_angle_wrapping_swerve/demo.html](03_concept_angle_wrapping_swerve/demo.html)

* **[Concept 04: 3D Rotations & Quaternions](04_concept_3d_rotations_quaternions/)**
  * *The Everyday Problem:* Why do 3-axis Euler angles lock up and crash IMU gyros when pitching straight up (Gimbal Lock)?
  * *Code & Math:* Roll/Pitch/Yaw limitations and unit Quaternions `(w, x, y, z)` on the 4D sphere.
  * *Visualizer:* [04_concept_3d_rotations_quaternions/demo.html](04_concept_3d_rotations_quaternions/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_geometry/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1: Geometry</a></div>
  <div><a href="./" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="01_concept_unit_circle_ratios/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 04: Unit Circle & Ratios →</a></div>
</div>
