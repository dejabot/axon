# Axon Curriculum Roadmap

A 25-concept curriculum structured across 5 core modules:

---

### Module 1: Math Foundations
* **Concept 01: Vectors, Basis Spaces & Matrix Transformations**
  * *Files:* `docs/modules/01_math_foundations/concept_01_vectors_matrices/README.md` | `demo.html`
  * *Scope:* Basis vectors (`î`, `ĵ`), linear transformations, determinants (area scaling & singularity), eigenvectors/eigenvalues, dot product projections, embedded interactive visualizer & SVGs.
* **Concept 02: Trigonometry, atan2, Continuous Angle Topology & Quaternions**
  * *Files:* `docs/modules/01_math_foundations/concept_02_trig_angle_topology/README.md` | `demo.html`
  * *Scope:* Unit circle, 4-quadrant `atan2(y, x)` vs `atan(y/x)`, shortest angular distance wrapping across `[-π, +π]`, 3D rotation topology with unit quaternions (`SO(3)`), Hamilton product, Gimbal Lock prevention, and SLERP interpolation.
* **Concept 03: Single-Variable Motion Calculus & Jerk**
  * *Files:* `docs/modules/01_math_foundations/concept_03_motion_calculus/README.md` | `demo.html`
  * *Scope:* Derivatives of motion (Position ➔ Velocity ➔ Acceleration ➔ Jerk), why unbounded jerk causes mechanical shock, discrete 20ms Euler vs. Trapezoidal integration, embedded interactive visualizer & SVGs.
* **Concept 04: Multivariable Calculus, Gradients & The Chain Rule**
  * *Files:* `docs/modules/01_math_foundations/concept_04_multivariable_gradients/README.md` | `demo.html`
  * *Scope:* Partial derivatives (`∂f/∂x`), gradient vectors (`∇f`), directional derivatives, steepest ascent proof, level curve orthogonality, and the multivariable chain rule.

---

### Module 2: Machine Learning
* **Concept 05: Loss Landscapes & Optimization Algorithms**
  * *Files:* `docs/modules/02_machine_learning/concept_05_loss_optimization/README.md` | `demo.html`
  * *Scope:* Objective functions (MSE, Cross-Entropy), learning rates (`α`), momentum (`β`), and Adam optimizer mechanics.
* **Concept 06: Dense Layers & Non-Linear Activation Functions**
  * *Files:* `docs/modules/02_machine_learning/concept_06_dense_activations/README.md` | `demo.html`
  * *Scope:* Linear matrix mapping + non-linear activations (ReLU, Sigmoid, Tanh, GELU). Proof of why linear networks collapse without activations.
* **Concept 07: Vector Calculus Backpropagation & Computation Graphs**
  * *Files:* `docs/modules/02_machine_learning/concept_07_backprop_graphs/README.md` | `demo.html`
  * *Scope:* Mathematical derivation of error vectors (`δ^[l]`) and weight gradients (`∂L/∂W`). From-scratch Python backprop engine.
* **Concept 08: In-Browser 2D Neural Classifier Sandbox**
  * *Files:* `docs/modules/02_machine_learning/concept_08_neural_sandbox/README.md` | `demo.html`
  * *Scope:* Live in-browser MLP training in JavaScript; interactive decision boundary warping to separate non-linear clusters.

---

### Module 3: Control & Physics
* **Concept 09: DC Motor Electromechanics & Torque-Speed Curves**
  * *Files:* `docs/modules/03_control_physics/concept_09_dc_motors/README.md` | `demo.html`
  * *Scope:* Back-EMF (`V = IR + ke·ω`), stall torque, free speed, peak power at 50% RPM, gear ratios (`G`), and reflected inertia (`J/G²`).
* **Concept 10: Modern Feedforward Modeling (kS, kV, kA, kG)**
  * *Files:* `docs/modules/03_control_physics/concept_10_feedforward_models/README.md` | `demo.html`
  * *Scope:* Predictive physical feedforward vs reactive feedback; stiction (`kS`), velocity (`kV`), acceleration (`kA`), gravity (`kG`) for elevators and pivot arms.
* **Concept 11: Feedback PID Control & Anti-Windup**
  * *Files:* `docs/modules/03_control_physics/concept_11_pid_control/README.md` | `demo.html`
  * *Scope:* P, I, and D mechanics, eliminating derivative kick, anti-windup clamping, and disturbance rejection.
* **Concept 12: State-Space Representation & LQR Optimal Control**
  * *Files:* `docs/modules/03_control_physics/concept_12_state_space_lqr/README.md` | `demo.html`
  * *Scope:* Continuous/discrete state vectors (`x_dot = Ax + Bu`), Linear Quadratic Regulator cost function minimization (`J = ∫ (xᵀQx + uᵀRu) dt`), inverted arm stabilization.

---

### Module 4: Swerve & Sensor Fusion
* **Concept 13: 4-Wheel Swerve Kinematics & Vector Decomposition**
  * *Files:* `docs/modules/04_swerve_fusion/concept_13_swerve_kinematics/README.md` | `demo.html`
  * *Scope:* ChassisSpeeds `[vx, vy, ω]ᵀ` to 4-wheel module states `(vi, θi)` via wheel vector addition (`v_trans + ω × r_i`).
* **Concept 14: Module Optimization & 2nd-Order Skew Correction**
  * *Files:* `docs/modules/04_swerve_fusion/concept_14_swerve_optimization/README.md` | `demo.html`
  * *Scope:* Shortest-path angle turn (`< 90°`) with speed inversion; matrix exponential twist discretization (`v_corrected = R(-ω·dt/2)·v_desired`) to eliminate curved drift.
* **Concept 15: Computer Vision & AprilTag Perspective-n-Point (PnP)**
  * *Files:* `docs/modules/04_swerve_fusion/concept_15_vision_pnp/README.md` | `demo.html`
  * *Scope:* Pinhole camera models, camera intrinsic matrix (`K`), planar homography, and solving 3D spatial robot pose from 2D pixel coordinates.
* **Concept 16: Extended Kalman Filter (EKF) Sensor Fusion**
  * *Files:* `docs/modules/04_swerve_fusion/concept_16_ekf_sensor_fusion/README.md` | `demo.html`
  * *Scope:* Fusing high-rate (250 Hz) wheel odometry with low-rate (30 Hz) noisy vision measurements. Covariance propagation and innovation updates.

---

### Module 5: Reinforcement Learning & Agents
* **Concept 17: Markov Decision Processes (MDPs) & Q-Learning**
  * *Files:* `docs/modules/05_rl_agents/concept_17_mdp_q_learning/README.md` | `demo.html`
  * *Scope:* States `S`, Actions `A`, Transition Dynamics `P`, Rewards `R`, Discount `γ`, Bellman Optimality Equation, tabular Q-learning gridworld.
* **Concept 18: Policy Gradients & Deep RL (PPO)**
  * *Files:* `docs/modules/05_rl_agents/concept_18_policy_gradients_ppo/README.md` | `demo.html`
  * *Scope:* Actor-Critic architectures, policy loss, and Proximal Policy Optimization (PPO) clipped surrogate objectives for continuous robot control.
* **Concept 19: Reward Engineering & Sim-to-Real Domain Randomization**
  * *Files:* `docs/modules/05_rl_agents/concept_19_reward_engineering/README.md` | `demo.html`
  * *Scope:* Reward shaping, avoiding reward hacking (wheel scrub vs speed), and parameter randomization (mass, friction, CAN latency) to bridge the sim-to-real gap.
* **Concept 20: Hierarchical Control Architecture & Behavior Trees**
  * *Files:* `docs/modules/05_rl_agents/concept_20_behavior_trees/README.md` | `demo.html`
  * *Scope:* Strategic Layer (1-5 Hz) vs Tactical Layer (20-50 Hz) vs Execution Layer (250-1000 Hz). Behavior Tree primitives (Sequence, Selector, Parallel).
* **Concept 21: Dynamic Obstacle Avoidance & Path Planning**
  * *Files:* `docs/modules/05_rl_agents/concept_21_obstacle_avoidance/README.md` | `demo.html`
  * *Scope:* Potential fields, dynamic obstacle repulsion, and trajectory re-routing around roving defender robots.
* **Concept 22: Agentic LLM Tool-Calling & Autonomous Diagnostics**
  * *Files:* `docs/modules/05_rl_agents/concept_22_agentic_tool_calling/README.md` | `demo.html`
  * *Scope:* Designing agentic feedback loops: LLM-driven match monitors with tool-calling capabilities to inspect subsystem telemetry, detect anomalies, and trigger recovery routines.
* **Concept 23: Full Autonomous Match Simulator Lab**
  * *Files:* `docs/modules/05_rl_agents/concept_23_match_simulator_lab/README.md` | `demo.html`
  * *Scope:* Integrating all layers: autonomous scoring, game piece intake arbitration, dynamic defender avoidance, and auto-alignment.
* **Concept 24: System Identification & Real-World Calibration**
  * *Files:* `docs/modules/05_rl_agents/concept_24_sysid_calibration/README.md` | `demo.html`
  * *Scope:* Practical sys-id: deriving physical mechanism constants (`kS`, `kV`, `kA`, Moment of Inertia `J`) from real sensor telemetry logs using linear regression.
* **Concept 25: Capstone Architecture & Complete Repository Index**
  * *Files:* `docs/modules/05_rl_agents/concept_25_capstone_synthesis/README.md` | `demo.html`
  * *Scope:* Comprehensive review, master synthesis of Math ➔ Physics ➔ ML ➔ Swerve ➔ RL ➔ Agentic Control, and final navigation index.