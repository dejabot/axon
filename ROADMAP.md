# Axon Curriculum Map

The living plan: seven axons, each a stack of modules, each module a sequence of concepts.

**Status key:** `[deep]` meets the REVIEWER_SPEC bar · `[thin]` exists but under-derived, needs a pass · `[new]` proposed, not yet written · `[stub]` axon has only a README

---

## Design Rules

Three rules govern the whole map. Every structural decision below follows from them.

1. **Strict prerequisite ordering.** A concept may only use tools already taught. This is the rule that reshaped Module 1 — geometry could not teach coordinate frames because frames need rotation, and rotation needs trigonometry, which comes later. When a concept needs an unavailable tool, either move the concept or move the tool. Never forward-reference and hope.
2. **Language follows the domain.** Robotics concepts are Java plus WPILib. Machine learning and LLM concepts are from-scratch Python plus PyTorch. Math concepts take the language of whichever consumer they serve. See CURRICULUM_SPEC rule 3.
3. **Derive, never assert.** 1,800–2,800 words, every formula traced back to something the reader already believes, "Math!" sidebars for notation, two checkpoints and two deep dives. See REVIEWER_SPEC.

---

## Axon 1: Mathematical Foundations

### Module 1: Geometry for Robotics — one concept outstanding
Deliberately trigonometry-free, so it can be built from arithmetic alone.

1. Coordinates, Poses & Pythagorean Distance `[deep]`
2. Lines, Segments & Intersections `[deep]`
3. Linear Interpolation, Lookup Tables & Blending `[new]`
4. Bounding Boxes, Overlap & Collision `[deep]`
5. Polygons, Areas & Field Zones `[deep]`

### Module 2: Trigonometry & Angles — next up
1. Right Triangles & the Unit Circle `[thin]` — must teach SOH-CAH-TOA explicitly, plus radians and arc length
2. Rotating a Vector & the 2D Rotation Matrix `[deep]`
3. Coordinate Frames (Field, Robot, Camera) `[thin]` — correctness patched, still needs full rigid-transform and inverse-transform derivation
4. Inverse Trig & 4-Quadrant Heading with atan2 `[thin]`
5. Angle Wrapping & Shortest Angular Distance `[thin]`
6. Law of Cosines & Two-Link Arm Geometry `[new]` — triangulation and arm reach; the missing tool for jointed mechanisms
7. 3D Rotations, Gimbal Lock & Quaternions `[thin]`

### Module 3: Linear Algebra & Transformations
1. Vectors, Scaling & Basis Spaces `[thin]`
2. Dot Products, Projections & Alignment `[thin]` — geometry Concept 02 already owes this a formal treatment
3. Matrices as Coordinate Transformers `[thin]`
4. Matrix Multiplication & Composition `[new]` — currently assumed by the rotation concept but never derived
5. Determinants, Inverses & Singularity `[thin]`
6. Solving Linear Systems & Least Squares `[new]` — the tool behind system identification and every regression fit
7. Eigenvectors & Eigenvalues `[new]` — prerequisite for covariance, PCA and the Kalman filter

### Module 4: Calculus, Motion & Optimization
1. Rates of Change & Derivatives `[thin]`
2. Derivative Rules & the Chain Rule `[new]` — backpropagation is the chain rule; it cannot stay implicit
3. Acceleration, Jerk & S-Curves `[thin]`
4. Accumulation, Area & Numerical Integration `[thin]`
5. Partial Derivatives & Gradients `[thin]`
6. Optimization, Critical Points & Saddle Points `[new]` — why loss landscapes are hard

### Module 5: Probability & Uncertainty
1. Random Variables, Sensor Noise & the Normal Distribution `[thin]`
2. Variance, Covariance & Correlation `[new]` — the covariance matrix the EKF runs on
3. Bayes' Rule & 1D Sensor Fusion `[thin]`
4. Discrete Distributions & Softmax `[thin]`
5. Maximum Likelihood Estimation `[new]` — why least squares and cross-entropy are the losses they are, rather than arbitrary choices
6. Expected Value & Decision Making `[thin]`

---

## Axon 2: Machine Learning & Vision

Python throughout: from-scratch with no NumPy, then PyTorch.

### Module 1: Loss Functions & Optimization
1. Measuring Errors with Loss Functions (MSE & MAE) `[deep]`
2. Cross-Entropy & Classification Loss `[thin]`
3. Gradient Descent & Learning Rates `[thin]`
4. Momentum, RMSProp & Adam `[new]` — currently named in the spec but never taught

### Module 2: Neural Layers & Activations
1. Linear Layers (Weights, Biases & Dot Products) `[thin]`
2. Non-Linear Activation Functions `[thin]`
3. Why Depth Without Non-Linearity Collapses `[new]` — the proof that stacked linear layers are one linear layer

### Module 3: Backpropagation
1. Computational Graphs & the Vector Chain Rule `[thin]`
2. Building an Autograd Engine in Pure Python `[thin]`
3. Training Loop, Batching & Overfitting `[new]`

### Module 4: Computer Vision & Detection
1. 2D Spatial Convolutions & Feature Maps `[thin]`
2. Pooling, Stride & Receptive Fields `[new]`
3. Object Detection, Anchor Boxes & IoU `[thin]`

### Module 5: Frameworks in Practice `[new module]`
Re-implements concepts already derived from scratch, so the framework reads as a payoff rather than a detour.
1. Tensors, Shapes & Broadcasting
2. Autograd in PyTorch — the same engine from Module 3, industrial strength
3. `nn.Module`, Optimizers & a Complete Training Loop
4. Deploying a Model to a Robot Coprocessor
5. Appendix: The Same Model in Keras/TensorFlow

---

## Axon 3: Large Language Models

Python throughout. Currently all Java — every concept needs relanguaging as well as deepening.

### Module 1: Embeddings
1. Tokenization & Byte-Pair Encoding `[thin]`
2. Vector Embeddings & Semantic Distance `[thin]`

### Module 2: Attention
1. Scaled Dot-Product Attention `[thin]`
2. Multi-Head Attention `[thin]`
3. Causal Masking & Why Order Matters `[new]`

### Module 3: The Transformer Block
1. Residual Connections & Layer Normalization `[thin]`
2. Feedforward Blocks `[thin]`
3. Assembling a Working Transformer `[new]`

### Module 4: Generation & Sampling
1. Rotary Position Embeddings (RoPE) `[thin]`
2. Temperature, Top-k & Top-p Sampling `[thin]`
3. The KV Cache & Why Inference Is Cheap `[new]`

---

## Axon 4: Physics, Dynamics & Actuation

Java and WPILib.

### Module 1: Motors & Electromechanics
1. Motor Curves & Back-EMF `[thin]`
2. Gearboxes & Reflected Inertia `[thin]`

### Module 2: Ballistics & Trajectories
1. 2D Kinematic Ballistics `[thin]`
2. Drag, Spin & Shooting on the Move `[thin]`

### Module 3: Dynamics & Energy
1. Newton's Laws & Friction `[thin]`
2. Work, Energy & Momentum `[thin]`

### Module 4: Control
1. Voltage Feedforward Models (kS, kV, kA, kG) `[thin]`
2. Closed-Loop PID & Tuning `[thin]`
3. Anti-Windup & Derivative Kick `[new]`

---

## Axon 5: Kinematics & Motion Planning `[stub]`

Proposed from scratch. Depends on Math Modules 2 and 3.

### Module 1: Chassis Kinematics
1. Differential Drive Kinematics
2. Swerve Module States & Inverse Kinematics
3. Forward Kinematics & Odometry from Wheels

### Module 2: Swerve in Practice
1. Module Optimization & the Shortest-Path Flip
2. Second-Order Twist & Skew Correction

### Module 3: Motion Profiling
1. Trapezoidal Profiles
2. S-Curve and Jerk-Limited Profiles
3. Path Following & Pure Pursuit

---

## Axon 6: Localization & Estimation `[stub]`

Proposed from scratch. Depends on Math Module 5 and Axon 5.

### Module 1: Odometry
1. Wheel Odometry & Dead Reckoning
2. Drift, Slip & Why Odometry Alone Fails

### Module 2: Vision & AprilTags
1. Pinhole Cameras, Intrinsics & Calibration — focal length, the principal point, lens distortion, and why an uncalibrated camera gives confidently wrong distances
2. AprilTags as Fiducial Markers — the detection pipeline (threshold, segment, quad fit, decode), tag families, and the Hamming distance that makes a misread tag ID nearly impossible
3. From Tag Corners to Pose (Homography & PnP) — four known 3D points, four measured 2D pixels, solve for the camera's pose
4. Pose Ambiguity & Why Tags Flip — the two-solution problem for planar targets, why it worsens as the tag gets small or face-on, and the standard mitigations
5. Tag Pose to Robot Pose — chaining camera→robot→field against the field layout. Directly consumes the frame transforms from Math Module 2.

### Module 3: Fusion
1. The 1D Kalman Filter, Derived
2. The Extended Kalman Filter
3. Fusing Vision with Odometry — measurement latency and timestamp alignment, per-measurement standard deviations, and rejecting an implausible pose rather than believing it

---

## Axon 7: Reinforcement Learning & Agents `[stub]`

Proposed from scratch. Python. Depends on Axon 2.

### Module 1: Foundations
1. Markov Decision Processes
2. Value Functions & the Bellman Equation
3. Tabular Q-Learning

### Module 2: Deep RL
1. Deep Q-Networks
2. Policy Gradients & REINFORCE
3. Actor-Critic & PPO

### Module 3: Agents in the Real World
1. Reward Shaping & Reward Hacking
2. Sim-to-Real & Domain Randomization
3. Behavior Trees & Hierarchical Control

---

## Totals

```
   existing and deep      6 concepts
   existing but thin     41 concepts
   proposed new          31 concepts
   ----------------------------------
   full curriculum       78 concepts
```

## Build Order

Math first, because everything depends on it, and within Math in module order because of the prerequisite rule. Then Axon 2 (ML) and Axon 4 (Physics) in parallel — they share no dependencies. Then Axon 3 (LLM) after ML, Axon 5 (Kinematics) after Math Module 3, Axon 6 (Localization) after Axon 5 and Math Module 5, and Axon 7 (RL) last.
