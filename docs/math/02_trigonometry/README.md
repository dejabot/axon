# Module 2: Trigonometry & Angles

Welcome to **Module 2: Trigonometry & Angles**. [Module 1](../01_geometry/) built everything reachable without angles. This module supplies the missing tool and immediately spends it: right-triangle ratios and the unit circle, then rotation matrices, then the coordinate-frame transforms that field-oriented drive and every vision pipeline depend on, and finally 4-quadrant headings, circle topology and 3D quaternions.

---

## Concepts in this Module

* **[Concept 01: The Unit Circle & Trigonometric Ratios](01_concept_unit_circle_ratios/)**
  * *The Everyday Problem:* A wheel is pointed 30° off down-field, moving at 4.0 m/s. How much of that carries the robot down-field, and how much sideways?
  * *Code & Math:* Why the ratios depend on the angle alone, SOH-CAH-TOA, the hypotenuse-1 collapse onto the unit circle, signs across all four quadrants, radians as arc length, and `sin² + cos² = 1` as Pythagoras.

* **[Concept 02: Rotating a Vector](02_concept_rotating_vectors/)**
  * *The Everyday Problem:* The driver pushes "away from me" but the robot is turned 40 degrees. How does that command become wheel speeds?
  * *Code & Math:* Rotation derived by tracking where `î` and `ĵ` land, proof that rotation preserves length, undoing a rotation by flipping one sign, and composition deriving the angle-addition identities.

* **[Concept 03: Coordinate Frames (Field, Robot & Camera)](03_concept_coordinate_frames/)**
  * *The Everyday Problem:* The camera sees a game piece 1.5 metres ahead. Where is it on the field?
  * *Code & Math:* Rigid transforms combining rotation and translation, chaining field to robot to camera, and inverting a transform.

* **[Concept 04: Inverse Trig & 4-Quadrant Heading with atan2](04_concept_atan2_heading/)**
  * *The Everyday Problem:* You know the two components. How do you get the angle back — without confusing North-East for South-West?
  * *Code & Math:* Why each inverse trig function needs a restricted range, how `tan⁻¹(y/x)` collapses two quadrants into one, and how `atan2(y, x)` recovers the sign information that the division destroyed.

* **[Concept 05: Angle Wrapping & Shortest Angular Distance](05_concept_angle_wrapping_swerve/)**
  * *The Everyday Problem:* A wheel at 350° is told to go to 10°. Why does it spin 340° the wrong way for a 20° move?
  * *Code & Math:* Angles live on a circle rather than a line, folding a difference into ±180°, why interpolating angles needs the wrap first, and the 90° threshold behind the swerve 180° flip.

* **[Concept 06: Law of Sines, Law of Cosines & Two-Link Arms](06_concept_law_of_cosines/)**
  * *The Everyday Problem:* A jointed arm forms a triangle with no right angle in it. Everything so far assumed one.
  * *Code & Math:* The law of cosines derived as a generalization of Pythagoras, solving a triangle from three sides, two-link inverse kinematics, reachability limits, and the elbow-up/elbow-down ambiguity.

* **[Concept 07: 3D Rotations, Gimbal Lock & Quaternions](07_concept_3d_rotations_quaternions/)**
  * *The Everyday Problem:* Yaw alone describes a robot on flat carpet. A robot on a ramp, or an arm on two axes, needs more.
  * *Code & Math:* Why 3D rotations depend on order, gimbal lock as a lost degree of freedom, Euler's rotation theorem, and quaternions as an axis-angle encoding.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_geometry/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1: Geometry</a></div>
  <div><a href="./" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="01_concept_unit_circle_ratios/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: Unit Circle & Ratios →</a></div>
</div>
