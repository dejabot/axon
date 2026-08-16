# Axon Curriculum Roadmap

A 25-sprint curriculum broken into 5 stages, calibrated for 20–30 minute study sessions.

---

### Stage 1: The Unified Math Engine
* **Concept 1: Vectors, Basis Spaces & Matrix Transformations**
  * *Files:* `docs/modules/01_math_foundations/concept_01_vectors_matrices/README.md` | `demo.html`
  * *Scope:* Basis vectors (`i-hat`, `j-hat`), linear transformations, determinants (area scaling & singularity), eigenvectors/eigenvalues, dot product projections.
  * *Forward Link:* Sprints 5 (Dense layers), 13 (Swerve kinematics), and 15 (Vision PnP).
* **Concept 2: Trigonometry, atan2 & Continuous Angle Topology**
  * *Files:* `docs/modules/01_math_foundations/concept_02_trig_angle_topology/README.md` | `demo.html`
  * *Scope:* Unit circle, 4-quadrant `atan2(y, x)` vs `atan(y/x)`, shortest angular distance wrapping across `[-π, +π]` to prevent the 340-degree swerve spin bug.
  * *Forward Link:* Sprints 10 (Arm feedforward), 13 (Swerve angle optimization), and 16 (EKF heading).
* **Concept 3: Single-Variable Motion Calculus & Rates of Change**
  * *Files:* `docs/modules/01_math_foundations/concept_03_motion_calculus/README.md` | `demo.html`
  * *Scope:* Derivatives of motion (Position ➔ Velocity ➔ Acceleration ➔ Jerk), why unbounded jerk causes mechanical shock, discrete 20ms Euler vs. Trapezoidal integration.
  * *Forward Link:* Sprints 5 (Loss landscapes), 10 (Acceleration feedforward), and 14 (2nd-order skew).
* **Concept 4: Multivariable Calculus, Gradients & The Chain Rule**
  * *Files:* `docs/modules/01_math_foundations/concept_04_multivariable_gradients/README.md` | `demo.html`
  * *Scope:* Partial derivatives (`∂f/∂x`), gradient vectors (`∇f`), directional derivatives, and the multivariable chain rule.
  * *Forward Link:* Sprints 5 (Gradient descent), 7 (Backpropagation), and 18 (Policy gradients).

---

### Stage 2: Machine Learning from First Principles
* **Sprint 5: Loss Landscapes & Optimization Algorithms**
  * *Files:* `modules/sprint_05.md` | `interactive/sprint_05_demo.html`
  * *Scope:* Objective functions (MSE, Cross-Entropy), learning rates (`α`), momentum (`β`), and Adam optimizer mechanics.
  * *Backward Link:* Sprint 4 (Gradients).
* **Sprint 6: Dense Layers & Non-Linear Activation Functions**
  * *Files:* `modules/sprint_06.md` | `interactive/sprint_06_demo.html`
  * *Scope:* Linear matrix mapping + non-linear activations (ReLU, Sigmoid, Tanh, GELU). Proof of why linear networks collapse without activations.
  * *Backward Link:* Sprint 1 (Matrix transformations).
* **Sprint 7: Vector Calculus Backpropagation & Computation Graphs**
  * *Files:* `modules/sprint_07.md` | `interactive/sprint_07_demo.html`
  * *Scope:* Mathematical derivation of error vectors (`δ^[l]`) and weight gradients (`∂L/∂W`). From-scratch Python backprop engine.
  * *Backward Link:* Sprints 1 (Matrices) and 4 (Chain rule).
* **Sprint 8: In-Browser 2D Neural Classifier Sandbox**
  * *Files:* `modules/sprint_08.md` | `interactive/sprint_08_demo.html`
  * *Scope:* Live in-browser MLP training in JavaScript; interactive decision boundary warping to separate non-linear clusters.
  * *Backward Link:* Sprints 5, 6, and 7.

---

### Stage 3: Actuator Physics & Control Theory
* **Sprint 9: DC Motor Electromechanics & Torque-Speed Curves**
  * *Files:* `modules/sprint_09.md` | `interactive/sprint_09_demo.html`
  * *Scope:* Back-EMF (`V = IR + ke·ω`), stall torque, free speed, peak power at 50% RPM, gear ratios (`G`), and reflected inertia (`J/G²`).
  * *Forward Link:* Sprint 10 (Feedforward).
* **Sprint 10: Modern Feedforward Modeling (kS, kV, kA, kG)**
  * *Files:* `modules/sprint_10.md` | `interactive/sprint_10_demo.html`
  * *Scope:* Predictive physical feedforward vs reactive feedback; stiction (`kS`), velocity (`kV`), acceleration (`kA`), gravity (`kG`) for elevators and pivot arms.
  * *Backward Link:* Sprints 2 (Cosine gravity) and 3 (Acceleration derivatives).
* **Sprint 11: Feedback PID Control & Anti-Windup**
  * *Files:* `modules/sprint_11.md` | `interactive/sprint_11_demo.html`
  * *Scope:* P, I, and D mechanics, eliminating derivative kick, anti-windup clamping, and disturbance rejection.
  * *Backward Link:* Sprint 3 (Integration & differentiation).
* **Sprint 12: State-Space Representation & LQR Optimal Control**
  * *Files:* `modules/sprint_12.md` | `interactive/sprint_12_demo.html`
  * *Scope:* Continuous/discrete state vectors (`x_dot = Ax + Bu`), Linear Quadratic Regulator cost function minimization (`J = ∫ (xᵀQx + uᵀRu) dt`), inverted arm stabilization.
  * *Backward Link:* Sprint 1 (State vectors and matrices).

---

### Stage 4: Swerve Kinematics & Sensor Fusion
* **Sprint 13: 4-Wheel Swerve Kinematics & Vector Decomposition**
  * *Files:* `modules/sprint_13.md` | `interactive/sprint_13_demo.html`
  * *Scope:* ChassisSpeeds `[vx, vy, ω]ᵀ` to 4-wheel module states `(vi, θi)` via wheel vector addition (`v_trans + ω × r_i`).
  * *Backward Link:* Sprints 1 (Vector addition) and 2 (`atan2` angle calculation).
* **Sprint 14: Module Optimization & 2nd-Order Skew Correction**
  * *Files:* `modules/sprint_14.md` | `interactive/sprint_14_demo.html`
  * *Scope:* Shortest-path angle turn (`< 90°`) with speed inversion; matrix exponential twist discretization (`v_corrected = R(-ω·dt/2)·v_desired`) to eliminate curved drift.
  * *Backward Link:* Sprints 1 (Rotation matrices) and 2 (Angle optimization).
* **Sprint 15: Computer Vision & AprilTag Perspective-n-Point (PnP)**
  * *Files:* `modules/sprint_15.md` | `interactive/sprint_15_demo.html`
  * *Scope:* Pinhole camera models, camera intrinsic matrix (`K`), planar homography, and solving 3D spatial robot pose from 2D pixel coordinates.
  * *Backward Link:* Sprint 1 (Homogeneous transformations).
* **Sprint 16: Extended Kalman Filter (EKF) Sensor Fusion**
  * *Files:* `modules/sprint_16.md` | `interactive/sprint_16_demo.html`
  * *Scope:* Fusing high-rate (250 Hz) wheel odometry with low-rate (30 Hz) noisy vision measurements. Covariance propagation and innovation updates.
  * *Backward Link:* Sprints 1 (Matrix algebra), 3 (Integration), and 12 (State estimation).

---

### Stage 5: Reinforcement Learning & Agentic Systems
* **Sprint 17: Markov Decision Processes (MDPs) & Q-Learning**
  * *Files:* `modules/sprint_17.md` | `interactive/sprint_17_demo.html`
  * *Scope:* States `S`, Actions `A`, Transition Dynamics `P`, Rewards `R`, Discount `γ`, Bellman Optimality Equation, tabular Q-learning gridworld.
* **Sprint 18: Policy Gradients & Deep RL (PPO)**
  * *Files:* `modules/sprint_18.md` | `interactive/sprint_18_demo.html`
  * *Scope:* Actor-Critic architectures, policy loss, and Proximal Policy Optimization (PPO) clipped surrogate objectives for continuous robot control.
  * *Backward Link:* Sprints 4 (Gradients) and 7 (Backpropagation).
* **Sprint 19: Reward Engineering & Sim-to-Real Domain Randomization**
  * *Files:* `modules/sprint_19.md` | `interactive/sprint_19_demo.html`
  * *Scope:* Reward shaping, avoiding reward hacking (wheel scrub vs speed), and parameter randomization (mass, friction, CAN latency) to bridge the sim-to-real gap.
* **Sprint 20: Hierarchical Control Architecture & Behavior Trees**
  * *Files:* `modules/sprint_20.md` | `interactive/sprint_20_demo.html`
  * *Scope:* Strategic Layer (1-5 Hz) vs Tactical Layer (20-50 Hz) vs Execution Layer (250-1000 Hz). Behavior Tree primitives (Sequence, Selector, Parallel).
* **Sprint 21: Dynamic Obstacle Avoidance & Path Planning**
  * *Files:* `modules/sprint_21.md` | `interactive/sprint_21_demo.html`
  * *Scope:* Potential fields, dynamic obstacle repulsion, and trajectory re-routing around roving defender robots.
  * *Backward Link:* Sprints 1 (Vectors) and 13 (Swerve execution).
* **Sprint 22: Agentic LLM Tool-Calling & Autonomous Diagnostics**
  * *Files:* `modules/sprint_22.md` | `interactive/sprint_22_demo.html`
  * *Scope:* Designing agentic feedback loops: LLM-driven match monitors with tool-calling capabilities to inspect subsystem telemetry, detect anomalies, and trigger recovery routines.
* **Sprint 23: Full Autonomous Match Simulator Lab**
  * *Files:* `modules/sprint_23.md` | `interactive/sprint_23_demo.html`
  * *Scope:* Integrating all layers: autonomous scoring, game piece intake arbitration, dynamic defender avoidance, and auto-alignment.
* **Sprint 24: System Identification & Real-World Calibration**
  * *Files:* `modules/sprint_24.md` | `interactive/sprint_24_demo.html`
  * *Scope:* Practical sys-id: deriving physical mechanism constants (`kS`, `kV`, `kA`, Moment of Inertia `J`) from real sensor telemetry logs using linear regression.
  * *Backward Link:* Sprints 4 (Optimization) and 9 (Motor physics).
* **Sprint 25: Capstone Architecture & Complete Repository Index**
  * *Files:* `modules/sprint_25.md` | `interactive/sprint_25_demo.html`
  * *Scope:* Comprehensive review, master synthesis of Math ➔ Physics ➔ ML ➔ Swerve ➔ RL ➔ Agentic Control, and final navigation index.
  