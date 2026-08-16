# Axon Curriculum

Axon is an educational curriculum designed from first principles to bridge high-school mathematics and physics into university-level applied mathematics, physical dynamics, autonomous robotics (FIRST Robotics Competition / FRC), machine learning, large language models, and agentic decision systems.

---

## Pedagogical Philosophy

* **FRC & Everyday Intuition First:** We start with real robot scenarios (scoring targets, joystick steering, sensor jitter, elevator chains, shooter ballistics, obstacle avoidance) before presenting formal equations.
* **Code-First Explanations:** Every concept is solved in 5–15 lines of clean, readable Python with descriptive variable names.
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

### [Axon 01: Mathematical Foundations](math/README.md)
* **[Geometry for Robotics](math/01_geometry/README.md)**: Coordinates, Poses, Frame Transforms, 2D AABB Bounding Boxes.
* **[Trigonometry & Angles](math/02_trigonometry/README.md)**: Unit Circle, `atan2`, Angle Wrapping, 180° Swerve Speed Flips, 3D Quaternions.
* **[Linear Algebra & Matrix Transformations](math/03_linear_algebra/README.md)**: Vectors, Dot Products, Matrices, Determinants, Matrix Inverses.
* **[Calculus, Motion & Optimization](math/04_calculus/README.md)**: Rates of Change, S-Curves & Jerk, Numerical Integrals, Multivariable Gradients.
* **[Probability & Uncertainty](math/05_probability/README.md)**: Sensor Noise & Bell Curves, Bayes' Rule 1D Fusion, Softmax, Expected Value & Monte Carlo.

---

### [Axon 02: Machine Learning & Vision](machine_learning/README.md)
* **Loss Functions & Optimization**: MSE, Cross-Entropy, Gradient Descent, Learning Rates, Adam Optimizer.
* **Neural Layers & Activation Functions**: Dense weights, biases, non-linear activations (ReLU, GELU, Sigmoid).
* **Vector Backpropagation Engine**: Computational DAG graphs, multivariate Chain Rule, autograd.
* **Computer Vision & Object Detection**: 2D Spatial Convolutions, YOLO single-shot architectures, bounding box IoU.

---

### [Axon 03: Large Language Models & Transformers](large_language_models/README.md)
* **Tokenization & Vector Embeddings**: BPE tokenization, vector lookup spaces, semantic similarity.
* **Scaled Dot-Product & Self-Attention**: Query, Key, Value ($Q, K, V$) projections.
* **The Transformer Architecture**: Multi-Head Attention, residual skip connections, RMSNorm.
* **Generation, RoPE & Sampling**: Rotary Position Embeddings, Temperature, Top-$p$ sampling.

---

### [Axon 04: Physics, Dynamics & Actuation](physics/README.md)
* **DC Motor Electromechanics**: Brushless motor curves, Back-EMF, $K_t$ and $K_v$ constants.
* **Gearboxes & Reflected Inertia**: Planetary reductions, torque multiplication, reflected load inertia ($J/G^2$).
* **Projectile Ballistics & Shooter Trajectories**: 2D parabolic arcs, air drag, Magnus spin, shooter flywheel RPM, shooting on the move.
* **Physics Feedforward & Closed-Loop PID**: Voltage models ($kS, kV, kA, kG$), velocity feedforward, PID closed-loop control.

---

### [Axon 05: Kinematics & Motion Planning](kinematics/README.md)
* **Chassis Speeds & Kinematics**: Forward/Inverse kinematics, wheel velocity desaturation.
* **Swerve Kinematics & 2nd-Order Twist**: 4-wheel decomposition, azimuth optimization, Lie group twist discretization.
* **Motion Profiling**: Trapezoidal and 7-segment S-Curve velocity profiles.
* **Holonomic Trajectory Tracking**: Hermite splines, HolonomicDriveController, dynamic obstacle potential fields.

---

### [Axon 06: Localization & State Estimation](localization/README.md)
* **Wheel Odometry & Gyro Integration**: Twist dead reckoning, encoder tick accumulation, IMU heading integration.
* **AprilTag Computer Vision & PnP Pose**: Pinhole camera matrix $K$, Perspective-n-Point solvers, camera latency compensation.
* **Extended Kalman Filter (EKF)**: Multi-state sensor fusion combining high-frequency odometry with low-frequency vision.

---

### [Axon 07: Reinforcement Learning & Agentic Decision Systems](reinforcement_learning/README.md)
* **Markov Decision Processes**: States, actions, reward shaping, discount factors.
* **Value Functions & Deep Q-Learning**: Bellman optimality, Deep Q-Networks (DQN), experience replay.
* **Policy Gradients & Actor-Critic**: Continuous action spaces, REINFORCE, PPO.
* **Monte Carlo Tree Search**: UCT tree search, AlphaZero search, real-time match strategists.
