# Module 3: Linear Algebra & Matrix Transformations

Welcome to **Module 3: Linear Algebra & Matrix Transformations**. In this module, we start with simple lists of numbers and graph-paper arrows, build up to dot product directional alignments, discover matrices as coordinate grid transformers, and understand determinants and matrix inverses.

---

## Concepts in this Module
* **[Concept 08: Vectors, Displacements & Scalar Scaling](concept_08_vectors_scaling/README.md)**
  * *The Everyday Problem:* How does an autonomous robot combine driving forward 2 meters with strafing right 3 meters?
  * *Code & Math:* Vectors as lists/arrows, vector addition (head-to-tail), scalar multiplication, and basis steps.
  * *Visualizer:* [concept_08_vectors_scaling/demo.html](concept_08_vectors_scaling/demo.html)

* **[Concept 09: Dot Products, Projections & Alignment](concept_09_dot_products/README.md)**
  * *The Everyday Problem:* How much of our robot's velocity is pushing directly along the desired path vs. drifting off-track?
  * *Code & Math:* Dot product `u · v`, vector projection, perpendicular orthogonality check (`dot = 0`).
  * *Visualizer:* [concept_09_dot_products/demo.html](concept_09_dot_products/demo.html)

* **[Concept 10: Matrices as Coordinate Transformers](concept_10_matrices_transforms/README.md)**
  * *The Everyday Problem:* How do we convert driver joystick commands into wheel velocities when the robot is spun at an angle?
  * *Code & Math:* 2D rotation matrices, matrix-vector multiplication as tracking where unit steps land.
  * *Visualizer:* [concept_10_matrices_transforms/demo.html](concept_10_matrices_transforms/demo.html)

* **[Concept 11: Determinants, Inverses & Singularity](concept_11_determinants_inverses/README.md)**
  * *The Everyday Problem:* Why does a drive kinematics solver crash with `Division by Zero` when a robot loses traction or steering locks?
  * *Code & Math:* Determinant as area scaling, singular matrices (`det = 0`), and matrix inverses.
  * *Visualizer:* [concept_11_determinants_inverses/demo.html](concept_11_determinants_inverses/demo.html)
