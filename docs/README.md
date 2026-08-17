# Axon Curriculum

Axon is an educational curriculum designed from first principles to bridge high-school mathematics and physics into university-level applied mathematics, physical dynamics, autonomous robotics (FIRST Robotics Competition / FRC), machine learning, large language models, and agentic decision systems.

---

## Pedagogical Philosophy

* **FRC & Everyday Intuition First:** We start with real robot scenarios (scoring targets, joystick steering, sensor jitter, elevator chains, shooter ballistics, obstacle avoidance) before presenting formal equations.
* **Code-First Explanations (Java & WPILib):** Every concept is solved in clean, boilerplate-free Java with descriptive variable names, paired with the official production WPILib class equivalent.
* **"Math!" Translation Sidebars:** Formal mathematical symbols, equations, and pronunciation guides are introduced as friendly translations of the code.
* **Bridge to Machine Learning & Modern Robotics:** Every concept explicitly connects to its role in modern deep learning (embeddings, transformer position encoding, dense layers, diffusion models, backpropagation) and physical robotic autonomy.
* **Clean Interactive Visualizers:** Concepts include companion interactive HTML5/Canvas demos with dark/light theming.

---

## The 7 Axon Tracks

```
                        ┌───────────────────────────────┐
                        │   1. Mathematical Foundations │
                        └───────────────┬───────────────┘
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             ▼                                                     ▼
┌───────────────────────────────┐               ┌─────────────────────────────────────┐
│ 2. Machine Learning & Vision  │               │   4. Physics, Dynamics & Actuation  │
└────────────┬──────────────────┘               └──────────────────┬──────────────────┘
             │                                                     │
             ▼                                                     ▼
┌───────────────────────────────┐               ┌─────────────────────────────────────┐
│ 3. Large Language Models      │               │   5. Kinematics & Motion Planning   │
└────────────┬──────────────────┘               └──────────────────┬──────────────────┘
             │                                                     │
             └──────────────────────────┬──────────────────────────┘
                                        ▼
                        ┌───────────────────────────────┐
                        │ 6. Localization & Estimation  │
                        └───────────────┬───────────────┘
                                        │
                                        ▼
                        ┌───────────────────────────────┐
                        │ 7. Reinforcement Learning     │
                        └───────────────────────────────┘
```

---

### [Axon 01: Mathematical Foundations](math/)
* **[Geometry for Robotics](math/01_geometry/)**: Coordinates, Poses, Frame Transforms, 2D AABB Bounding Boxes.
* **[Trigonometry & Angles](math/02_trigonometry/)**: Unit Circle, `atan2`, Angle Wrapping, 180° Swerve Speed Flips, 3D Quaternions.
* **[Linear Algebra & Matrix Transformations](math/03_linear_algebra/)**: Vectors, Dot Products, Matrices, Determinants, Matrix Inverses.
* **[Calculus, Motion & Optimization](math/04_calculus/)**: Rates of Change, S-Curves & Jerk, Numerical Integrals, Multivariable Gradients.
* **[Probability & Uncertainty](math/05_probability/)**: Sensor Noise & Bell Curves, Bayes' Rule 1D Fusion, Softmax, Expected Value & Monte Carlo.

---

### [Axon 02: Machine Learning & Vision](machine_learning/)
* **[Loss Functions & Optimization](machine_learning/01_loss_optimization/)**: MSE, MAE, Cross-Entropy, Gradient Descent, Learning Rates.
* **[Neural Layers & Activation Functions](machine_learning/02_neural_layers/)**: Dense weights `y = W @ x + b`, non-linear activations (ReLU, GELU, Sigmoid).
* **[Vector Backpropagation Engine](machine_learning/03_backpropagation/)**: Computational DAG graphs, multivariate Chain Rule, micro-autograd engine.
* **[Computer Vision & Object Detection](machine_learning/04_computer_vision/)**: 2D Spatial Convolutions, Sobel edge filters, YOLO bounding boxes, IoU, Non-Maximum Suppression (NMS).

---

### [Axon 03: Large Language Models & Transformers](large_language_models/)
* **[Tokenization & Vector Embeddings](large_language_models/01_embeddings/)**: BPE subword tokenization, vocabulary lookup spaces, high-dimensional semantic vectors, cosine similarity.
* **[Scaled Dot-Product & Self-Attention](large_language_models/02_attention_heads/)**: Query, Key, Value (Q, K, V) projections, attention heatmaps, Multi-Head Attention feature subspaces.
* **[The Transformer Architecture](large_language_models/03_transformers/)**: Pre-RMSNorm normalization, residual skip connections (gradient highway), SwiGLU Feed-Forward Blocks.
* **[Generation, RoPE & Sampling](large_language_models/04_generation_sampling/)**: Rotary Position Embeddings (RoPE), 2D coordinate rotations, Temperature scaling, Top-k, Top-p (Nucleus) sampling, KV-Caching.

---

### [Axon 04: Physics, Dynamics & Actuation](physics/)
* **[DC Motors & Electromechanics](physics/01_motors_electromechanics/)**: Brushless motor curves, Back-EMF, `K_t` and `K_v` constants, planetary reductions, reflected load inertia (`J / G²`).
* **[Projectile Ballistics & Trajectories](physics/02_ballistics_trajectories/)**: 2D parabolic kinematic arcs, air drag deceleration, Magnus backspin lift, shooting on the move vector compensation.
* **[Dynamics, Friction & Energy](physics/03_dynamics_energy/)**: Coulomb friction circles (`F_max = μ_s · N`), static vs kinetic slip cliffs, kinetic energy (`½ m v²`), elevator constant-force spring counterbalancing.
* **[Control Physics & Voltage Models](physics/04_control_physics/)**: Physics feedforward (`kS`, `kV`, `kA`, `kG`), `SimpleMotorFeedforward`, `ElevatorFeedforward`, `ArmFeedforward`, closed-loop PID tuning and stability.

---

### [Axon 05: Kinematics & Motion Planning](kinematics/)
* **Chassis Speeds & Kinematics**: Forward/Inverse kinematics, wheel velocity desaturation.
* **Swerve Kinematics & 2nd-Order Twist**: 4-wheel decomposition, azimuth optimization, Lie group twist discretization.
* **Motion Profiling**: Trapezoidal and 7-segment S-Curve velocity profiles.
* **Holonomic Trajectory Tracking**: Hermite splines, HolonomicDriveController, dynamic obstacle potential fields.

---

### [Axon 06: Localization & State Estimation](localization/)
* **Wheel Odometry & Gyro Integration**: Twist dead reckoning, encoder tick accumulation, IMU heading integration.
* **AprilTag Computer Vision & PnP Pose**: Pinhole camera matrix K, Perspective-n-Point solvers, camera latency compensation.
* **Extended Kalman Filter (EKF)**: Multi-state sensor fusion combining high-frequency odometry with low-frequency vision.

---

### [Axon 07: Reinforcement Learning & Agentic Decision Systems](reinforcement_learning/)
* **Markov Decision Processes**: States, actions, reward shaping, discount factors.
* **Value Functions & Deep Q-Learning**: Bellman optimality, Deep Q-Networks (DQN), experience replay.
* **Policy Gradients & Actor-Critic**: Continuous action spaces, REINFORCE, PPO.
* **Monte Carlo Tree Search**: UCT tree search, AlphaZero search, real-time match strategists.
