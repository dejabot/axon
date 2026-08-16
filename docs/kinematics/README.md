# Axon 05: Kinematics & Motion Planning

Welcome to the **Kinematics & Motion Planning Axon**. This track develops the mathematical models that translate high-level autonomous trajectory curves into real-time wheel speeds and steering angles.

---

## Modules in this Axon

### 1. Chassis Speeds & Forward/Inverse Kinematics
* *The Real-World Problem:* How does a robot translate high-level desired forward, strafe, and rotational speeds into individual wheel commands?
* *Key Concepts:* ChassisSpeeds `[vx, vy, omega]`, Differential drive kinematics, wheel velocity saturation, and desaturation algorithms.

---

### 2. Swerve Kinematics & 2nd-Order Twist Correction
* *The Real-World Problem:* Why do omnidirectional swerve robots drift in curved arcs during combined translation and rotation?
* *Key Concepts:* 4-module vector decomposition, azimuth angle optimization (180° speed flips), Lie group twist discretization, and continuous curvature compensation.

---

### 3. Motion Profiling (Trapezoidal & S-Curves)
* *The Real-World Problem:* How do we command mechanisms to move as fast as possible without exceeding physical motor velocity, acceleration, or jerk limits?
* *Key Concepts:* Trapezoidal profiles, constant jerk 7-segment S-curves, profile generation in time, and real-time state following.

---

### 4. Holonomic Trajectory Tracking
* *The Real-World Problem:* How does an autonomous robot follow a pre-computed spline trajectory across the carpet while compensating for wheel slip and defense?
* *Key Concepts:* Cubic and Quintic Hermite splines, HolonomicDriveController feedback, PathPlanner/Choreo trajectory execution, and dynamic obstacle repulsion.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../physics/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Previous Axon: Physics & Actuation</a></div>
  <div><a href="../README.md" style="color: var(--muted, #94a3b8); text-decoration: none;">Curriculum Home</a></div>
  <div><a href="../localization/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Next Axon: Localization & State Estimation →</a></div>
</div>
