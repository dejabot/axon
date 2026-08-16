# Axon Curriculum Documentation

Welcome to the Axon educational curriculum. Axon is designed from first principles to teach applied mathematics, physics, control theory, machine learning, and autonomous robotics for high-performance engineering (such as FIRST Robotics Competition / FRC and modern AI systems).

---

## Purpose & Philosophy

Traditional curricula often treat mathematics, physical modeling, machine learning, and robot controls as disconnected subjects. Axon unifies them:
* **First Principles (No Black Boxes):** Every formula is derived step-by-step with zero hand-waving.
* **Dual Grounding:** Every mathematical concept is directly connected to a high-stakes FRC robotics mechanism (e.g., swerve kinematics, elevator feedforward, gyro odometry) and a core Machine Learning component (e.g., dense layers, loss optimization, backpropagation).
* **Interactive Visualizers:** Every concept includes a companion standalone HTML5/Canvas interactive demo with touch and slider controls.

---

## Curriculum Modules

### [Module 1: Math Foundations](modules/01_math_foundations/README.md)
Core linear algebra, continuous angle topology, single-variable motion calculus, and multivariable gradient calculus.
* [Concept 01: Vectors, Basis Spaces & Matrix Transformations](modules/01_math_foundations/concept_01_vectors_matrices/README.md) ([Demo](modules/01_math_foundations/concept_01_vectors_matrices/demo.html))
* [Concept 02: Trigonometry, atan2 & Continuous Angle Topology](modules/01_math_foundations/concept_02_trig_angle_topology/README.md) ([Demo](modules/01_math_foundations/concept_02_trig_angle_topology/demo.html))
* [Concept 03: Single-Variable Motion Calculus & Jerk](modules/01_math_foundations/concept_03_motion_calculus/README.md) ([Demo](modules/01_math_foundations/concept_03_motion_calculus/demo.html))
* [Concept 04: Multivariable Calculus, Gradients & The Chain Rule](modules/01_math_foundations/concept_04_multivariable_gradients/README.md) ([Demo](modules/01_math_foundations/concept_04_multivariable_gradients/demo.html))

---

### [Module 2: Machine Learning](modules/02_machine_learning/README.md)
Loss landscapes, dense neural network layers, activation functions, vector backpropagation, and in-browser classifier sandboxes.
* Concept 05: Loss Landscapes & Optimization Algorithms (MSE, Cross-Entropy, Adam)
* Concept 06: Dense Layers & Non-Linear Activation Functions (ReLU, Sigmoid, GELU)
* Concept 07: Vector Calculus Backpropagation & Computation Graphs
* Concept 08: In-Browser 2D Neural Classifier Sandbox

---

### [Module 3: Control & Physics](modules/03_control_physics/README.md)
DC motor electromechanics, predictive feedforward modeling (kS, kV, kA, kG), feedback PID control with anti-windup, and state-space LQR optimal control.
* Concept 09: DC Motor Electromechanics & Torque-Speed Curves
* Concept 10: Modern Feedforward Modeling (kS, kV, kA, kG)
* Concept 11: Feedback PID Control & Anti-Windup
* Concept 12: State-Space Representation & LQR Optimal Control

---

### [Module 4: Swerve & Sensor Fusion](modules/04_swerve_fusion/README.md)
4-wheel independent swerve vector decomposition, module azimuth optimization, 2nd-order matrix twist skew correction, AprilTag PnP vision, and Extended Kalman Filtering (EKF).
* Concept 13: 4-Wheel Swerve Kinematics & Vector Decomposition
* Concept 14: Module Optimization & 2nd-Order Skew Correction
* Concept 15: Computer Vision & AprilTag Perspective-n-Point (PnP)
* Concept 16: Extended Kalman Filter (EKF) Sensor Fusion

---

### [Module 5: Reinforcement Learning & Agents](modules/05_rl_agents/README.md)
Markov Decision Processes, deep policy gradients (PPO), sim-to-real domain randomization, hierarchical behavior trees, dynamic path planning, and autonomous diagnostics.
* Concept 17: Markov Decision Processes (MDPs) & Q-Learning
* Concept 18: Policy Gradients & Deep RL (PPO)
* Concept 19: Reward Engineering & Sim-to-Real Domain Randomization
* Concept 20: Hierarchical Control Architecture & Behavior Trees
* Concept 21: Dynamic Obstacle Avoidance & Path Planning
* Concept 22: Agentic LLM Tool-Calling & Autonomous Diagnostics
* Concept 23: Full Autonomous Match Simulator Lab
* Concept 24: System Identification & Real-World Calibration
* Concept 25: Capstone Architecture & Complete Repository Index
