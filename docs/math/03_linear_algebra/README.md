# Module 3: Linear Algebra & Matrix Transformations

Welcome to **Module 3: Linear Algebra & Matrix Transformations**. In this module, we start with simple lists of numbers and graph-paper arrows, build up to dot product directional alignments, discover matrices as coordinate grid transformers, and understand determinants and matrix inverses.

---

## Concepts in this Module
* **[Concept 01: Vectors, Displacements & Scalar Scaling](01_concept_vectors_scaling/)**
  * *The Everyday Problem:* How does an autonomous robot combine driving forward 2 meters with strafing right 3 meters?
  * *Code & Math:* Vectors as lists/arrows, vector addition (head-to-tail), scalar multiplication, and basis steps.

* **[Concept 02: Dot Products, Projections & Alignment](02_concept_dot_products/)**
  * *The Everyday Problem:* How much of our robot's velocity is pushing directly along the desired path vs. drifting off-track?
  * *Code & Math:* Dot product `u · v`, vector projection, perpendicular orthogonality check (`dot = 0`).

* **[Concept 03: Matrices as Coordinate Transformers](03_concept_matrices_transforms/)**
  * *The Everyday Problem:* How do we convert driver joystick commands into wheel velocities when the robot is spun at an angle?
  * *Code & Math:* 2D rotation matrices, matrix-vector multiplication as tracking where unit steps land.

* **[Concept 04: Determinants, Inverses & Singularity](04_concept_determinants_inverses/)**
  * *The Everyday Problem:* Why does a drive kinematics solver crash with `Division by Zero` when a robot loses traction or steering locks?
  * *Code & Math:* Determinant as area scaling, singular matrices (`det = 0`), and matrix inverses.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../02_trigonometry/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 2: Trigonometry</a></div>
  <div><a href="./" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 3 Overview</a></div>
  <div><a href="01_concept_vectors_scaling/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 08: Vectors & Scaling →</a></div>
</div>
