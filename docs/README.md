# Axon Curriculum Documentation

Axon is an educational curriculum designed from first principles to bridge high-school mathematics (algebra, geometry, trigonometry, single-variable calculus, and probability) into university-level applied mathematics, physical dynamics, autonomous robotics (FIRST Robotics Competition / FRC), and machine learning (grounded in [*Mathematics for Machine Learning*](https://mml-book.github.io/book/mml-book.pdf) by Deisenroth, Faisal, and Ong).

---

## Pedagogical Philosophy

* **FRC & Everyday Intuition First:** We start with real robot scenarios (scoring targets, joystick steering, sensor jitter, elevator chains, obstacle avoidance) before presenting formal equations.
* **Code-First Explanations:** Every concept is solved in 5–15 lines of clean, readable Python with descriptive variable names.
* **"Math!" Translation Sidebars:** Formal mathematical symbols, equations, and pronunciation guides are introduced as friendly translations of the code.
* **Bridge to Machine Learning:** Every math concept explicitly connects to its role in modern deep learning (embeddings, transformer position encoding, dense layers, diffusion models, softmax sampling, backpropagation).
* **Clean Interactive Visualizers:** Every concept includes a companion interactive HTML5/Canvas demo with dark/light theming.

---

## Curriculum Outline

### [Module 1: Geometry for Robotics](modules/01_geometry/README.md)
* [Concept 01: Coordinates, Poses & Pythagorean Distance](modules/01_geometry/concept_01_coordinates_distance/README.md) — [Interactive Visualizer](modules/01_geometry/concept_01_coordinates_distance/demo.html)
* [Concept 02: Coordinate Frames (Field vs. Robot vs. Camera)](modules/01_geometry/concept_02_coordinate_frames/README.md) — [Interactive Visualizer](modules/01_geometry/concept_02_coordinate_frames/demo.html)
* [Concept 03: 2D Bounding Boxes & Collision Detection](modules/01_geometry/concept_03_bounding_boxes/README.md) — [Interactive Visualizer](modules/01_geometry/concept_03_bounding_boxes/demo.html)

---

### [Module 2: Trigonometry & Angles](modules/02_trigonometry/README.md)
* [Concept 04: The Unit Circle & Trigonometric Ratios](modules/02_trigonometry/concept_04_unit_circle_ratios/README.md) — [Interactive Visualizer](modules/02_trigonometry/concept_04_unit_circle_ratios/demo.html)
* [Concept 05: 4-Quadrant Heading with atan2](modules/02_trigonometry/concept_05_atan2_heading/README.md) — [Interactive Visualizer](modules/02_trigonometry/concept_05_atan2_heading/demo.html)
* [Concept 06: Angle Wrapping & Swerve 180° Speed Flip](modules/02_trigonometry/concept_06_angle_wrapping_swerve/README.md) — [Interactive Visualizer](modules/02_trigonometry/concept_06_angle_wrapping_swerve/demo.html)
* [Concept 07: 3D Rotations & Quaternions](modules/02_trigonometry/concept_07_3d_rotations_quaternions/README.md) — [Interactive Visualizer](modules/02_trigonometry/concept_07_3d_rotations_quaternions/demo.html)

---

### [Module 3: Linear Algebra & Matrix Transformations](modules/03_linear_algebra/README.md)
* [Concept 08: Vectors, Displacements & Scalar Scaling](modules/03_linear_algebra/concept_08_vectors_scaling/README.md) — [Interactive Visualizer](modules/03_linear_algebra/concept_08_vectors_scaling/demo.html)
* [Concept 09: Dot Products, Projections & Alignment](modules/03_linear_algebra/concept_09_dot_products/README.md) — [Interactive Visualizer](modules/03_linear_algebra/concept_09_dot_products/demo.html)
* [Concept 10: Matrices as Coordinate Transformers](modules/03_linear_algebra/concept_10_matrices_transforms/README.md) — [Interactive Visualizer](modules/03_linear_algebra/concept_10_matrices_transforms/demo.html)
* [Concept 11: Determinants, Inverses & Singularity](modules/03_linear_algebra/concept_11_determinants_inverses/README.md) — [Interactive Visualizer](modules/03_linear_algebra/concept_11_determinants_inverses/demo.html)

---

### [Module 4: Calculus, Motion & Optimization](modules/04_calculus/README.md)
* [Concept 12: Rates of Change & Derivatives](modules/04_calculus/concept_12_rates_of_change/README.md) — [Interactive Visualizer](modules/04_calculus/concept_12_rates_of_change/demo.html)
* [Concept 13: Acceleration, Jerk & S-Curves](modules/04_calculus/concept_13_acceleration_jerk/README.md) — [Interactive Visualizer](modules/04_calculus/concept_13_acceleration_jerk/demo.html)
* [Concept 14: Accumulation, Area & Numerical Integration](modules/04_calculus/concept_14_accumulation_integrals/README.md) — [Interactive Visualizer](modules/04_calculus/concept_14_accumulation_integrals/demo.html)
* [Concept 15: Multivariable Gradients & Hill Climbing](modules/04_calculus/concept_15_gradients_multivariable/README.md) — [Interactive Visualizer](modules/04_calculus/concept_15_gradients_multivariable/demo.html)

---

### [Module 5: Probability & Uncertainty](modules/05_probability/README.md)
* [Concept 16: Sensor Noise & Normal Distributions](modules/05_probability/concept_16_sensor_noise_normal/README.md) — [Interactive Visualizer](modules/05_probability/concept_16_sensor_noise_normal/demo.html)
* [Concept 17: Bayes' Rule & 1D Sensor Fusion](modules/05_probability/concept_17_bayes_sensor_fusion/README.md) — [Interactive Visualizer](modules/05_probability/concept_17_bayes_sensor_fusion/demo.html)
* [Concept 18: Discrete Distributions & Softmax](modules/05_probability/concept_18_discrete_softmax/README.md) — [Interactive Visualizer](modules/05_probability/concept_18_discrete_softmax/demo.html)
* [Concept 19: Expected Value & Decision Making](modules/05_probability/concept_19_expected_value_decision/README.md) — [Interactive Visualizer](modules/05_probability/concept_19_expected_value_decision/demo.html)

---

### [Module 6: Machine Learning Foundations](modules/06_machine_learning/README.md)
* Concept 20: Loss Landscapes & Optimization (MSE, Cross-Entropy)
* Concept 21: Dense Layers & Non-Linear Activation Functions (ReLU, GELU)
* Concept 22: Vector Calculus Backpropagation & Computation Graphs
* Concept 23: 2D Neural Classifier Sandbox
