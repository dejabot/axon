# Axon 06: Localization & State Estimation

Welcome to the **Localization & State Estimation Axon**. This track covers how an autonomous robot continuously knows its exact millimeter position, velocity, and orientation on the field by fusing wheel encoders, high-speed IMU gyros, and AprilTag computer vision.

---

## Modules in this Axon

### [1. Wheel Odometry & Gyro Integration](01_wheel_odometry/README.md)
* *The Real-World Problem:* How does a robot track where it is on the carpet by accumulating wheel rotations and IMU heading angles?
* *Concepts:* Forward kinematics integration, twist accumulation, wheel slip modeling, and systematic odometry drift over time.

---

### [2. AprilTag Computer Vision & PnP Pose](02_vision_pose/README.md)
* *The Real-World Problem:* How does a camera turn a 2D image of a planar AprilTag into a full 3D robot coordinate `(x, y, z, roll, pitch, yaw)` on the field?
* *Concepts:* Pinhole camera model, intrinsic matrix $K$, Perspective-n-Point (PnP) solvers, camera-to-robot coordinate transforms, and latency timestamp compensation.

---

### [3. Extended Kalman Filter (EKF) State Estimation](03_kalman_filters/README.md)
* *The Real-World Problem:* How do we combine continuous 100 Hz wheel odometry with intermittent, noisy 30 Hz AprilTag vision measurements into a single rock-solid global pose estimate?
* *Concepts:* State vector $x = [x, y, \theta]^T$, covariance matrix $P$, process noise $Q$, measurement noise $R$, observation model $h(x)$, and standard WPILib SwerveDrivePoseEstimator integration.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../kinematics/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Previous Axon: Kinematics & Motion</a></div>
  <div><a href="../README.md" style="color: var(--muted, #94a3b8); text-decoration: none;">Curriculum Home</a></div>
  <div><a href="../reinforcement_learning/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Next Axon: Reinforcement Learning →</a></div>
</div>
