# Concept 04: 3D Rotations & Quaternions

> **▶ Interactive Demo: [3D Gimbal Lock & Quaternion Sandbox](demo.html)**
>
> Open the interactive demo below to pitch the 3D axis to `±90°` and see Euler Gimbal Lock occur, and observe how unit Quaternions represent 3D orientation smoothly.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: When 3D Angles Lock Up
On a flat 2D carpet, we only care about 1 angle: **Heading (Yaw)**.

But a real robot moves in 3D space:
1. **Roll:** Tilting side-to-side (e.g. over a bump).
2. **Pitch:** Tilting nose-up or nose-down (e.g. climbing a charging ramp).
3. **Yaw:** Rotating flat on the carpet (steering heading).

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="170" viewBox="0 0 300 170" style="max-width: 100%; height: auto;">
    <g transform="translate(150, 85)">
      <!-- 3D Axes -->
      <line x1="0" y1="0" x2="80" y2="40" stroke="#f43f5e" stroke-width="2.5" />
      <line x1="0" y1="0" x2="-70" y2="40" stroke="#4ade80" stroke-width="2.5" />
      <line x1="0" y1="0" x2="0" y2="-70" stroke="#38bdf8" stroke-width="2.5" />
      <text x="85" y="45" fill="#f43f5e" font-family="sans-serif" font-weight="bold" font-size="11">X (Roll)</text>
      <text x="-120" y="45" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="11">Y (Pitch)</text>
      <text x="-5" y="-75" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="11">Z (Yaw)</text>
    </g>
  </svg>
</div>

### The "Gimbal Lock" Catastrophe
If a robot's 3D gyro (like a Pigeon 2.0 or NavX) pitches straight up by `90°`:
* The Roll axis and the Yaw axis align into the exact same plane!
* Rotating around Roll and rotating around Yaw do the exact same thing.
* You lose a complete degree of freedom, and standard trigonometry divides by zero (`tan(90°) = ∞`).

---

## 2. Solving It in Code (Java & WPILib)

### Production WPILib Equivalent
WPILib contains full 3D rotation and quaternion support in `Rotation3d` and `Quaternion`:

```java
import edu.wpi.first.math.geometry.Rotation3d;
import edu.wpi.first.math.geometry.Quaternion;

// 1. Create a 3D rotation from Euler angles (Roll, Pitch, Yaw)
Rotation3d gyroRotation = new Rotation3d(
    Math.toRadians(2.0),  // Roll
    Math.toRadians(-5.0), // Pitch
    Math.toRadians(45.0)  // Yaw
);

// 2. Extract unit Quaternion (w, x, y, z) for gimbal-lock-free fusion
Quaternion q = gyroRotation.getQuaternion();
System.out.printf("Quaternion: (w: %.3f, x: %.3f, y: %.3f, z: %.3f)%n",
    q.getW(), q.getX(), q.getY(), q.getZ());
```

---

## 3. Review Checkpoints
### Checkpoint 1
What is the quaternion `(w, x, y, z)` for a robot that has zero rotation (identity orientation)?

**Solution:**
When `θ = 0°`:
* `w = cos(0°) = 1.0`
* `(x, y, z) = (0, 0, 0) · sin(0°) = (0.0, 0.0, 0.0)`
* The identity quaternion is **`[1.0, 0.0, 0.0, 0.0]`**.

---

### Checkpoint 2
Why do spacecraft, drones, and FRC vision libraries (PhotonVision / Limelight) always publish 3D poses as Quaternions instead of Euler angles?

**Solution:**
Because Euler angles (Roll, Pitch, Yaw) produce mathematical singularities at `pitch = ±90°` where software crashes from division by zero. Quaternions guarantee smooth, continuous calculations across all possible 3D orientations.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../03_concept_angle_wrapping_swerve/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 06: Angle Wrapping & Swerve</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../../03_linear_algebra/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 3: Linear Algebra →</a></div>
</div>
