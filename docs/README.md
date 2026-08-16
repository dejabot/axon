# Axon Curriculum Documentation

Axon is an educational curriculum designed from first principles to bridge high-school mathematics (algebra, geometry, trigonometry, single-variable calculus) into university-level applied mathematics for autonomous robotics (FIRST Robotics Competition / FRC) and machine learning (grounded in [*Mathematics for Machine Learning*](https://mml-book.github.io/book/mml-book.pdf) by Deisenroth, Faisal, and Ong).

---

## Pedagogical Philosophy

* **High-School On-Ramp:** We take zero university-level math for granted. Every concept starts with simple, intuitive analogies (graph paper steps, clock hands, elevator forces, blindfolded hiking).
* **First Principles (No Black Boxes):** Every formula is derived step-by-step with clean text and zero hand-waving.
* **Dual Grounding:** Every mathematical concept is directly connected to a real robot mechanism (e.g., swerve kinematics, elevator feedforward, gyro odometry, quaternion 3D poses) and a core Machine Learning component (e.g., dense layers, loss optimization, backpropagation, rotary embeddings).
* **Interactive Visualizers:** Every concept includes a standalone HTML5/Canvas interactive demo with a shared Dark Mode / Light Mode theme toggle.

---

## Curriculum Outline

### [Module 1: Math Foundations](modules/01_math_foundations/README.md)
Foundational linear algebra, continuous angle topology, single-variable motion calculus, and multivariable gradient calculus bridging high-school math to MML Part I.
* [Concept 01: Vectors, Basis Spaces & Matrix Transformations](modules/01_math_foundations/concept_01_vectors_matrices/README.md) — [Interactive Visualizer](modules/01_math_foundations/concept_01_vectors_matrices/demo.html)
* [Concept 02: Trigonometry, atan2, Continuous Angle Topology & Quaternions](modules/01_math_foundations/concept_02_trig_angle_topology/README.md) — [Interactive Visualizer](modules/01_math_foundations/concept_02_trig_angle_topology/demo.html)
* [Concept 03: Single-Variable Motion Calculus & Jerk](modules/01_math_foundations/concept_03_motion_calculus/README.md) — [Interactive Visualizer](modules/01_math_foundations/concept_03_motion_calculus/demo.html)
* [Concept 04: Multivariable Calculus, Gradients & The Chain Rule](modules/01_math_foundations/concept_04_multivariable_gradients/README.md) — [Interactive Visualizer](modules/01_math_foundations/concept_04_multivariable_gradients/demo.html)

---

### [Module 2: Machine Learning](modules/02_machine_learning/README.md)
5. Loss Landscapes & Optimization Algorithms (MSE, Cross-Entropy, Adam)
6. Dense Layers & Non-Linear Activation Functions (ReLU, Sigmoid, GELU)
7. Vector Calculus Backpropagation & Computation Graphs
8. In-Browser 2D Neural Classifier Sandbox

---

### [Module 3: Control & Physics](modules/03_control_physics/README.md)
9. DC Motor Electromechanics & Torque-Speed Curves
10. Modern Feedforward Modeling (kS, kV, kA, kG)
11. Feedback PID Control & Anti-Windup
12. State-Space Representation & LQR Optimal Control

---

### [Module 4: Swerve & Sensor Fusion](modules/04_swerve_fusion/README.md)
13. 4-Wheel Swerve Kinematics & Vector Decomposition
14. Module Optimization & 2nd-Order Skew Correction
15. Computer Vision & AprilTag Perspective-n-Point (PnP)
16. Extended Kalman Filter (EKF) Sensor Fusion

---

### [Module 5: Reinforcement Learning & Agents](modules/05_rl_agents/README.md)
17. Markov Decision Processes (MDPs) & Q-Learning
18. Policy Gradients & Deep RL (PPO)
19. Reward Engineering & Sim-to-Real Domain Randomization
20. Hierarchical Control Architecture & Behavior Trees
21. Dynamic Obstacle Avoidance & Path Planning
22. Agentic LLM Tool-Calling & Autonomous Diagnostics
23. Full Autonomous Match Simulator Lab
24. System Identification & Real-World Calibration
25. Capstone Architecture & Complete Repository Index
