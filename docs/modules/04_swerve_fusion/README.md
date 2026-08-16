# Module 4: Swerve Kinematics & Sensor Fusion

Module 4 covers the omnidirectional kinematics and state estimation algorithms that enable agile mobile robot navigation on the competition field.

---

## Module Overview

1. **4-Wheel Swerve Kinematics & Vector Decomposition:** Translating high-level chassis speeds `[vx, vy, ω]ᵀ` into individual wheel module speeds and steering angles.
2. **Module Optimization & 2nd-Order Skew Correction:** Minimizing azimuth steering rotation angles and applying matrix exponential twist discretization to eliminate curved trajectory drift.
3. **Computer Vision & AprilTag Perspective-n-Point (PnP):** Pinhole camera models, camera intrinsic calibration matrices, and solving 3D spatial robot pose from planar fiducial tags.
4. **Extended Kalman Filter (EKF) Sensor Fusion:** Fusing high-rate (250 Hz) noisy wheel odometry with low-rate (30 Hz) camera pose observations.

---

## Concepts & Modules

* **Concept 13: 4-Wheel Swerve Kinematics & Vector Decomposition**
* **Concept 14: Module Optimization & 2nd-Order Skew Correction**
* **Concept 15: Computer Vision & AprilTag Perspective-n-Point (PnP)**
* **Concept 16: Extended Kalman Filter (EKF) Sensor Fusion**
