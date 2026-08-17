# Axon Curriculum Map

The living plan: seven axons, each a stack of modules, each module a sequence of concepts.

**Status key:** `[deep]` meets the REVIEWER_SPEC bar · `[thin]` exists but under-derived, needs a pass · `[new]` proposed and specified, not yet written · `[todo]` agreed in principle but not yet specified · `[stub]` axon has only a README

---

## Design Rules

Three rules govern the whole map. Every structural decision below follows from them.

1. **Strict prerequisite ordering.** A concept may only use tools already taught. This is the rule that reshaped Math Module 1 — geometry could not teach coordinate frames, because frames need rotation and rotation needs trigonometry, which comes later. It binds across axons too: Localization needs frames from Math Module 2, matrices from Module 3 and covariance from Module 5. When a concept needs an unavailable tool, move the concept or move the tool. Never forward-reference and hope.
2. **Language follows the domain.** Robotics concepts are Java plus WPILib. Machine learning and LLM concepts are from-scratch Python plus PyTorch. Math concepts take the language of whichever consumer they serve, and both where they genuinely serve both.
3. **Derive, never assert — and never pad.** Every result traced to something the reader already believes, "Math!" sidebars for notation, two checkpoints and two deep dives. Length follows the topic rather than a quota: most concepts run 30–45 minutes, some honestly run shorter, and inflating a small topic is as serious a failure as hand-waving a large one.
4. **Ground honestly.** Every concept connects to a named real system. Dual robotics/ML grounding wherever it is genuine — and nowhere it is not, since a manufactured connection is worse than a single honest one.

The full standard is **REVIEWER_SPEC.md**, which applies identically to all seven axons.

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

### Module 4: Feedback Control — built from the ground up

Each term earns its place by fixing a specific failure of the one before it. No concept introduces a gain the reader has not first watched a simpler controller fail without.

1. **Bang-Bang Control & Why It Oscillates** `[new]` — the simplest closed loop there is: below the setpoint, full power; at or above it, none. Introduces setpoint, error, actuator saturation and the limit cycle. Not a strawman — bang-bang genuinely outperforms PID on a flywheel recovering after a shot, and knowing *why* is the point.
2. **Proportional Control & Steady-State Error** `[new]` — push harder the further you are. Derives why a P-only arm holding against gravity always settles *below* its target, since zero error would mean zero output and nothing holding it up. Raising the gain shrinks the offset and starts oscillation, which motivates the next two terms.
3. **Integral Control & Windup** `[new]` — accumulated past error drives steady-state offset to zero. Then the failure it creates: while the mechanism is saturated or blocked, the integral keeps growing, and the stored error has to be paid back as overshoot. Anti-windup clamping and integral zones.
4. **Derivative Control, Damping & Noise** `[new]` — reacting to the rate of change adds damping. Then its two failure modes: derivative kick when the setpoint steps (fixed by differentiating the measurement, not the error), and amplification of encoder noise, since differentiating noise is the worst thing you can do to it.
5. **Proportional Feedforward: the F Term** `[new]` — the first controller that stops reacting and starts predicting. Output proportional to the *setpoint* rather than to the error: `output = kF · setpoint`. This is the `F` in the PIDF gains on a Talon or Spark, and on a flywheel it does almost all the work while P merely trims the remainder. Derives why kF is roughly the reciprocal of the mechanism's free speed, and why feeding a target forward beats waiting for error to appear. Then its limits: it assumes output is proportional to setpoint, which holds for a flywheel at steady speed and fails for anything fighting gravity or accelerating — which is exactly what motivates the next concept.
6. **Physical Feedforward Models (kS, kV, kA, kG)** `[thin]` — replacing the single kF with a model of the actual physics: static friction, velocity, acceleration and gravity, each a term that exists because a specific effect broke the simpler model. Why modern robot code lets feedforward carry the load and leaves PID correcting only the residual.
7. **Tuning in Practice** `[thin]` — what each gain does to a step response, a practical tuning order, what Ziegler-Nichols is and why teams rarely use it as written, and reading a real response curve to decide which term to reach for.

### Module 5: State-Space & Optimal Control `[todo]`

Not yet specified in detail — revisit once Math Module 3 exists, since this needs matrices and eigenvalues.

1. State-Space Representation `[todo]` — a mechanism as `x_dot = Ax + Bu`, and what the eigenvalues of `A` say about stability
2. LQR & Optimal Control `[todo]` — choosing gains by declaring what you care about via the Q and R cost matrices, rather than by hand-tuning. WPILib's `LinearSystem` and `LinearQuadraticRegulator`.

**Prerequisite note.** The I term is integration and the D term is differentiation, so this module must follow Math Module 4 (Calculus). Concepts 3 and 4 should cite the accumulation and rate-of-change concepts directly rather than re-deriving them.

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
   existing and deep      7 concepts
   existing but thin     41 concepts
   proposed new          39 concepts
   agreed, not specified  2 concepts
   ----------------------------------
   full curriculum       89 concepts
```

## Build Order

Math first, because everything depends on it, and within Math in module order because of the prerequisite rule. Then Axon 2 (ML) and Axon 4 (Physics) in parallel — they share no dependencies. Then Axon 3 (LLM) after ML, Axon 5 (Kinematics) after Math Module 3, Axon 6 (Localization) after Axon 5 and Math Module 5, and Axon 7 (RL) last.
