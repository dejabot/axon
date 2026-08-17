# Concept 03: Angle Wrapping & Swerve 180° Speed Flip

> **▶ Interactive Demo: [Swerve Angle Wrapping Visualizer](demo.html)**
>
> Open the interactive demo below to drag the Current and Target angles and observe the shortest-path turn vs. the 180° swerve speed flip in action.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The 340° Spin Trap
Imagine your robot is currently facing **North-West at `+170°`**. 

During autonomous, the trajectory planner commands the robot to turn to **South-West at `-170°`**.

<div style="text-align: center; margin: 20px 0;">
  <svg width="280" height="160" viewBox="0 0 280 160" style="max-width: 100%; height: auto;">
    <circle cx="140" cy="80" r="60" fill="none" stroke="#334155" stroke-width="1.5" />
    <!-- Current -->
    <line x1="140" y1="80" x2="85" y2="65" stroke="#38bdf8" stroke-width="2.5" />
    <circle cx="85" cy="65" r="4" fill="#38bdf8" />
    <text x="25" y="60" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="11">+170°</text>
    
    <!-- Target -->
    <line x1="140" y1="80" x2="85" y2="95" stroke="#fbbf24" stroke-width="2.5" />
    <circle cx="85" cy="95" r="4" fill="#fbbf24" />
    <text x="25" y="110" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="11">-170°</text>
    
    <!-- Short Arc -->
    <path d="M 85 65 A 60 60 0 0 0 85 95" fill="none" stroke="#4ade80" stroke-width="3.5" />
    <text x="160" y="85" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="12">Turn 20°</text>
  </svg>
</div>

* **Naive Math:** `Error = Target - Current = -170° - 170° = -340°`
* If you feed `-340°` into your steering motor PID loop, the robot will violently spin almost a full 360-degree circle across the field!
* **Physical Reality:** The robot is only **`20°` away**!

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java: Shortest Angle Path
```java
public static double shortestAngleDiff(double targetDeg, double currentDeg) {
    double diff = (targetDeg - currentDeg) % 360.0;
    if (diff > 180.0) diff -= 360.0;
    if (diff < -180.0) diff += 360.0;
    return diff;
}
```

### Production WPILib Equivalent
WPILib provides built-in utilities in `MathUtil` and `SwerveModuleState`:

```java
import edu.wpi.first.math.MathUtil;
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.math.kinematics.SwerveModuleState;

// 1. Angle modulus wrapping [-pi, +pi]
double wrappedAngle = MathUtil.angleModulus(rawAngleRadians);

// 2. Swerve 180-degree module optimization (reversing speed instead of spinning 180°)
SwerveModuleState desiredState = new SwerveModuleState(3.5, Rotation2d.fromDegrees(170.0));
Rotation2d currentAzimuth = Rotation2d.fromDegrees(0.0);

SwerveModuleState optimized = SwerveModuleState.optimize(desiredState, currentAzimuth);
// Automatically inverts speed to -3.5 m/s and targets -10.0°!
```

---

## 3. The Swerve Drive 180° Speed Flip
In an autonomous swerve drive robot, every wheel module has two motors:
1. An **Azimuth Steering Motor** that rotates the wheel pod angle.
2. A **Drive Motor** that spins the wheel forward or backward.

Suppose a wheel is currently aimed at `0°` (straight ahead) and needs to drive at `175°` (almost completely backward):
* If you rotate the steering pod by `175°`, it takes precious milliseconds to slew the pod around.
* **The Swerve Trick:** Rotate the wheel pod by only `-5°` (to `180°`), and run the drive motor in **reverse (`speed = -1.0`)**!

```python
def optimize_swerve_module(target_angle, target_speed, current_angle):
    """
    Optimizes swerve module to never steer more than 90 degrees.
    """
    error = shortest_angle_error(target_angle, current_angle)
    
    # If required turn is greater than 90 degrees, flip direction!
    if abs(error) > 90.0:
        error = error - 180.0 if error > 0 else error + 180.0
        target_speed = -target_speed
        
    return current_angle + error, target_speed
```

---

> 💡 **Math Sidebar: Circle Topology & Modulo**
>
> On a standard line, numbers go from `-∞` to `+∞`. 
> But angles live on a circle (written mathematically as **`S¹`**). On a circle, `+180°` and `-180°` are the **exact same physical point**.
>
> The modulo operator `% 360` wraps numbers so that `370°` becomes `10°`, ensuring our controller always takes the shortest geometric arc.

---

## 4. Review Checkpoints
### Checkpoint 1
Your robot heading is `-175°`. The autonomous command requests a heading of `+175°`.
What is the shortest turn required?

**Solution:**
1. `raw_error = 175 - (-175) = +350°`.
2. Wrapped: `(350 + 180) % 360 - 180 = 530 % 360 - 180 = 170 - 180 = -10.0°`.
3. The robot turns **`10°` clockwise** instead of `350°`.

---

### Checkpoint 2
Why does the swerve module 180° speed flip make a robot faster and reduce wheel wear?

**Solution:**
Because the steering motor never has to rotate more than `90°` to achieve any desired drive vector. Reducing steering slew from `180°` down to `0°` eliminates delay and prevents tire scrubbing on the carpet.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../04_concept_atan2_heading/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 04: 4-Quadrant atan2</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../06_concept_3d_rotations_quaternions/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 06: 3D Quaternions →</a></div>
</div>
