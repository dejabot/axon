# Module 2: Trigonometry & Angles

Welcome to **Module 2: Trigonometry & Angles**. [Module 1](../01_geometry/) built everything reachable without angles. This module supplies the missing tool and immediately spends it: right-triangle ratios and the unit circle, then rotation matrices, then the coordinate-frame transforms that field-oriented drive and every vision pipeline depend on, and finally 4-quadrant headings, circle topology and 3D quaternions.

---

## Concepts in this Module

* **[Concept 01: The Unit Circle & Trigonometric Ratios](01_concept_unit_circle_ratios/)**
  * *The Everyday Problem:* How does pushing a gamepad joystick decompose into forward and sideways wheel power?
  * *Code & Math:* SOH-CAH-TOA, unit circle projections, `cos` as horizontal shadow, `sin` as vertical height, radians versus degrees.
  * *Visualizer:* [Joystick unit circle](01_concept_unit_circle_ratios/demo.html)

* **[Concept 02: Rotating a Vector & the 2D Rotation Matrix](02_concept_rotating_vectors/)**
  * *The Everyday Problem:* The driver pushes "away from me" but the robot is turned 40 degrees. How does that command become wheel speeds?
  * *Code & Math:* Rotation derived by tracking the basis vectors, the rotation matrix, proof that rotation preserves length, why the inverse is the transpose, and composition as angle addition.
  * *Visualizer:* [Rotation & field-oriented drive](02_concept_rotating_vectors/demo.html)

* **[Concept 03: Coordinate Frames (Field, Robot & Camera)](03_concept_coordinate_frames/)**
  * *The Everyday Problem:* The camera sees a game piece 1.5 metres ahead. Where is it on the field?
  * *Code & Math:* Rigid transforms combining rotation and translation, chaining field to robot to camera, and inverting a transform.
  * *Visualizer:* [Frame transformation](03_concept_coordinate_frames/demo.html)

* **[Concept 04: 4-Quadrant Heading with atan2](04_concept_atan2_heading/)**
  * *The Everyday Problem:* Why does standard `tan⁻¹(y/x)` confuse aiming North-East with South-West?
  * *Code & Math:* The 4 quadrants, negative sign cancellations, and the robust `atan2(y, x)` function.
  * *Visualizer:* [atan2 heading](04_concept_atan2_heading/demo.html)

* **[Concept 05: Angle Wrapping & Swerve 180° Speed Flip](05_concept_angle_wrapping_swerve/)**
  * *The Everyday Problem:* Why does a naive angle subtraction make a robot spin 340° instead of turning 20°?
  * *Code & Math:* Modular angle difference on a circle, shortest path wrapping, and swerve drive direction inversion.
  * *Visualizer:* [Angle wrapping](05_concept_angle_wrapping_swerve/demo.html)

* **[Concept 06: 3D Rotations & Quaternions](06_concept_3d_rotations_quaternions/)**
  * *The Everyday Problem:* Why do 3-axis Euler angles lock up and crash IMU gyros when pitching straight up (Gimbal Lock)?
  * *Code & Math:* Roll/Pitch/Yaw limitations and unit Quaternions `(w, x, y, z)` on the 4D sphere.
  * *Visualizer:* [Quaternions](06_concept_3d_rotations_quaternions/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_geometry/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1: Geometry</a></div>
  <div><a href="./" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="01_concept_unit_circle_ratios/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: Unit Circle & Ratios →</a></div>
</div>
