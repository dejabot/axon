# Module 1: Math Foundations

```
       Module 1: Math Foundations (Concepts 01 ➔ 04)
```

Welcome to **Module 1: Math Foundations**. This module serves as the intuitive, first-principles on-ramp from high-school mathematics (algebra, Cartesian geometry, trigonometry, and basic rates of change) into the foundational pillars of applied mathematics in autonomous robotics and university-level machine learning—specifically covering the mathematical foundations in [*Mathematics for Machine Learning* (MML)](https://mml-book.github.io/book/mml-book.pdf) (Chapters 2–5 and 7).

---

## Pedagogical On-Ramp: From High School to MML

Standard machine learning textbooks start with abstract vector spaces, inner product definitions, and differential manifolds that assume extensive mathematical maturity. 

In this module, every concept builds directly on high school intuition before ascending to advanced applications:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ High School Intuition           ➔  MML Foundation & Applied Robotics    │
├─────────────────────────────────────────────────────────────────────────┤
│ 1. Graph Paper & Grid Steps     ➔  Basis Spaces, Matrices & Transforms   │
│ 2. Clock-Hands & Unit Circle    ➔  4-Quadrant atan2 & 3D Quaternions    │
│ 3. Elevator Coffee Cup Forces   ➔  Motion Derivatives & Bounded Jerk    │
│ 4. Blindfolded Hiker in the Fog ➔  Gradients, Jacobians & Chain Rule    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Concept Guides & Interactive Visualizers

* **[Concept 01: Vectors, Basis Spaces & Matrix Transformations](concept_01_vectors_matrices/README.md)**
  * *High School Bridge:* Walking steps on a coordinate grid, scaling vectors with scalars.
  * *MML Alignment:* Chapter 2 (Linear Algebra: Vector spaces, basis, linear mappings) & Chapter 3 (Analytic Geometry: Determinants and dot product orthogonality).
  * *Study Guide:* [concept_01_vectors_matrices/README.md](concept_01_vectors_matrices/README.md)
  * *Interactive Visualizer:* [concept_01_vectors_matrices/demo.html](concept_01_vectors_matrices/demo.html)

* **[Concept 02: Trigonometry, atan2, Continuous Angle Topology & Quaternions](concept_02_trig_angle_topology/README.md)**
  * *High School Bridge:* Clock-hand projections, sin/cos ratios, angle measurements.
  * *MML Alignment:* Chapter 3 (Analytic Geometry: Angles, 2D rotation matrices, 3D Lie Group SO(3) rotations, and Unit Quaternions on S³).
  * *Study Guide:* [concept_02_trig_angle_topology/README.md](concept_02_trig_angle_topology/README.md)
  * *Interactive Visualizer:* [concept_02_trig_angle_topology/demo.html](concept_02_trig_angle_topology/demo.html)

* **[Concept 03: Single-Variable Motion Calculus & Jerk](concept_03_motion_calculus/README.md)**
  * *High School Bridge:* Speedometer readings, acceleration pedals, area under a curve.
  * *MML Alignment:* Chapter 5.1 (Vector Calculus: Univariate differentiation, Taylor approximations, and discrete Euler vs. Trapezoidal numerical integration).
  * *Study Guide:* [concept_03_motion_calculus/README.md](concept_03_motion_calculus/README.md)
  * *Interactive Visualizer:* [concept_03_motion_calculus/demo.html](concept_03_motion_calculus/demo.html)

* **[Concept 04: Multivariable Calculus, Gradients & The Chain Rule](concept_04_multivariable_gradients/README.md)**
  * *High School Bridge:* Slopes on a 3D hill, contour elevation lines.
  * *MML Alignment:* Chapter 5.2–5.6 (Vector Calculus: Partial derivatives, gradients, Jacobians, multivariable chain rule) & Chapter 7 (Continuous Optimization: Gradient Descent).
  * *Study Guide:* [concept_04_multivariable_gradients/README.md](concept_04_multivariable_gradients/README.md)
  * *Interactive Visualizer:* [concept_04_multivariable_gradients/demo.html](concept_04_multivariable_gradients/demo.html)
