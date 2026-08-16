# Axon Curriculum Documentation

Axon is an educational curriculum designed from first principles to teach applied mathematics, physics, control theory, machine learning, and autonomous robotics for high-performance engineering (such as FIRST Robotics Competition / FRC and modern AI systems).

---

## Philosophy & Structure

* **First Principles (No Black Boxes):** Every formula is derived step-by-step with zero hand-waving.
* **Dual Grounding:** Every mathematical concept is directly connected to an FRC robotics mechanism (e.g., swerve kinematics, elevator feedforward, gyro odometry, quaternion 3D poses) and a core Machine Learning component (e.g., dense layers, loss optimization, backpropagation, rotary embeddings).
* **Interactive Visualizers:** Every concept includes a companion standalone HTML5/Canvas interactive demo with a shared Dark Mode / Light Mode theme toggle.

---

## Curriculum Outline

### [Module 1: Math Foundations](modules/01_math_foundations/README.md)
1. [Vectors, Basis Spaces & Matrix Transformations](modules/01_math_foundations/concept_01_vectors_matrices/README.md) — [Interactive Visualizer](modules/01_math_foundations/concept_01_vectors_matrices/demo.html)
2. [Trigonometry, atan2, Continuous Angle Topology & Quaternions](modules/01_math_foundations/concept_02_trig_angle_topology/README.md) — [Interactive Visualizer](modules/01_math_foundations/concept_02_trig_angle_topology/demo.html)
3. [Single-Variable Motion Calculus & Jerk](modules/01_math_foundations/concept_03_motion_calculus/README.md) — [Interactive Visualizer](modules/01_math_foundations/concept_03_motion_calculus/demo.html)
4. [Multivariable Calculus, Gradients & The Chain Rule](modules/01_math_foundations/concept_04_multivariable_gradients/README.md) — [Interactive Visualizer](modules/01_math_foundations/concept_04_multivariable_gradients/demo.html)

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
