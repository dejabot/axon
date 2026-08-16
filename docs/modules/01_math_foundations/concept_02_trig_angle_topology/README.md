# Concept 02: Trigonometry, atan2 & Continuous Angle Topology

```
       Module 1: Math Foundations  ➔  Concept 02: Trigonometry & atan2
```

---

## 1. Intuitive Mental Model

Imagine measuring distance along a straight highway versus tracking time on a circular clock face.

On a straight highway (the standard real number line `ℝ¹`), moving 10 miles forward and 10 miles backward always puts you at distinct positions. If point A is at mile marker 1 and point B is at mile marker 359, the shortest distance between them is undeniably `359 - 1 = 358` miles.

```
   Linear Space (ℝ¹):
   [0]─────────────[1]─────────────────────────────────[359]───►
                     ◄──────────────── 358 units ────────►
```

Now look at a 12-hour circular clock. If the minute hand is at 1 minute past the hour (`+6°`) and you want it to point to 59 minutes past the hour (`+354°` or `-6°`), how far does the hand have to turn? 

```
                    Circular Topology (S¹):
                            0° / 360°
                               ▲
                       59m     │     1m
                      (354°)   │    (6°)
                          \    │    /
                           \   │   /
                            \  │  /
                      ───────┼─┼─┼───────
                             │ │ │
                             │ │ │
                             ▼ │ ▼
                   Shortest turn is only 12°!
```

If your control software blindly computes `354° - 6° = +348°`, your motor will frantically spin nearly a full circle clockwise to travel a distance that was only 12 degrees counter-clockwise.

This fundamental topological difference—between a straight Euclidean line `ℝ¹` and the closed circle manifold **S¹**—is the root of the most frequent and destructive bugs in autonomous robotics and spatial machine learning. Angles do not live on a flat line; they wrap continuously. 

---

## 2. Mathematical & Physical Derivations

### The Unit Circle & Coordinate Projections
A point `P` on a unit circle (radius `r = 1`) at counter-clockwise angle `θ` from the positive x-axis has coordinates:

```
   x = cos(θ)
   y = sin(θ)
```

For any arbitrary vector `v = [x, y]ᵀ` with magnitude `r = ||v|| = √(x² + y²)`:

```
   x = r · cos(θ)
   y = r · sin(θ)
```

```
           y
           ▲
           │          P = (x, y) = (r·cos θ, r·sin θ)
           │         /│
           │      r / │
           │       /  │ y = r·sin θ
           │      / θ │
           └─────┴────┴────────► x
                   x = r·cos θ
```

The tangent function is the ratio of opposite to adjacent sides:

```
   tan(θ) = y / x = sin(θ) / cos(θ)
```

### Why Naive `atan(y/x)` Fails: The 4-Quadrant Ambiguity
The standard inverse tangent function `arctan(z)` accepts a single real scalar `z = y / x`. By mathematical definition, the range of `arctan` is restricted strictly to two quadrants:

```
   arctan(y / x) ∈ (-π/2, +π/2)   or   (-90°, +90°)
```

Because `arctan` receives only the quotient `y/x`, the individual signs of `x` and `y` are lost. Consider two distinct physical vectors:
1. `v₁ = [+1, +1]ᵀ` (Quadrant I, pointing North-East, `θ = +45°` or `+π/4 rad`)
2. `v₂ = [-1, -1]ᵀ` (Quadrant III, pointing South-West, `θ = -135°` or `-3π/4 rad`)

Evaluating naive `arctan`:
- `v₁ ➔ arctan(+1 / +1) = arctan(+1.0) = +45°`
- `v₂ ➔ arctan(-1 / -1) = arctan(+1.0) = +45°`

```
   Quadrant II (-x, +y)        │   Quadrant I (+x, +y)
   θ = +135°                   │   θ = +45°
   atan(1 / -1) = -45° [WRONG] │   atan(1 / 1) = +45° [CORRECT]
   ────────────────────────────┼────────────────────────────
   Quadrant III (-x, -y)       │   Quadrant IV (+x, -y)
   θ = -135°                   │   θ = -45°
   atan(-1 / -1) = +45°[WRONG] │   atan(-1 / 1) = -45°[CORRECT]
```

Naive `arctan` outputs `+45°` for vector `v₂`, commanding your robot to drive in the exact opposite direction of its goal. Furthermore, if `x = 0` (a purely vertical motion), `y/x` causes a fatal division-by-zero crash.

### Step-by-Step Derivation of `atan2(y, x)`
The 4-quadrant inverse tangent `atan2(y, x)` inspects the individual signs of both `y` and `x`, mapping uniquely to the full circular interval `(-π, +π]`:

```
                  ┌  arctan(y / x)            if x > 0
                  │  arctan(y / x) + π        if x < 0 and y ≥ 0
   atan2(y, x) = ┼  arctan(y / x) - π        if x < 0 and y < 0
                  │  +π / 2                   if x = 0 and y > 0
                  │  -π / 2                   if x = 0 and y < 0
                  └  undefined (or 0)         if x = 0 and y = 0
```

`atan2(y, x)` handles vertical lines without division-by-zero and preserves quadrant polarity across all 360 degrees.

### Angle Wrapping & Shortest Angular Distance
Given a current robot angle `θ_curr` and a target angle `θ_target`, the naive error is `e_naive = θ_target - θ_curr`.

Because angle space wraps every `2π` radians (360°), the true physical error `Δθ` must lie in the range `[-π, +π]`.

#### Derivation via Complex Phasor Projection
Represent both angles as 2D unit vectors on the complex plane:
- `z_curr = cos(θ_curr) + i·sin(θ_curr)`
- `z_target = cos(θ_target) + i·sin(θ_target)`

The relative rotation required to bring `z_curr` into `z_target` is given by the quotient `z_rel = z_target / z_curr = z_target · z_curr*`:

```
   z_rel = (cos θ_target + i·sin θ_target) · (cos θ_curr - i·sin θ_curr)
         = [cos(θ_target)·cos(θ_curr) + sin(θ_target)·sin(θ_curr)] 
           + i · [sin(θ_target)·cos(θ_curr) - cos(θ_target)·sin(θ_curr)]
```

Using trigonometric angle subtraction identities:
- `cos(θ_target - θ_curr) = cos(θ_target)·cos(θ_curr) + sin(θ_target)·sin(θ_curr)`
- `sin(θ_target - θ_curr) = sin(θ_target)·cos(θ_curr) - cos(θ_target)·sin(θ_curr)`

Therefore, extracting the continuous shortest angle error using `atan2`:

```
   Δθ = atan2( sin(θ_target - θ_curr), cos(θ_target - θ_curr) )
```

This single, elegant formula automatically maps any arbitrary angular difference onto `[-π, +π]` without conditional branching.

### Swerve Module Optimization (Azimuth Inversion)
A swerve drive wheel is bidirectional: spinning the drive motor forward at angle `θ` produces the exact same linear ground thrust as spinning the drive motor backward at angle `θ + π` (180° opposite).

```
   State A: [ v = +3.0 m/s , θ = 0°   ]
   State B: [ v = -3.0 m/s , θ = 180° ]
   ==> Both states produce identical physical traction forces!
```

To steer a swerve module from `θ_curr` to `θ_target`:
1. Compute the shortest angular error: `Δθ = wrap_to_pi(θ_target - θ_curr)`.
2. If `|Δθ| > π / 2` (greater than 90°):
   - Rather than rotating the wheel module through a large angle, rotate by `Δθ - sign(Δθ)·π` (which is `<= 90°`).
   - Invert the drive wheel velocity: `v_target = -v_target`.

```
   Optimized Angle Rule:
   If |Δθ| > 90°:
       θ_optimal = θ_curr + (Δθ - sign(Δθ)·π)
       v_optimal = -v_target
   Else:
       θ_optimal = θ_curr + Δθ
       v_optimal = +v_target
```

---

## 3. Dual Grounding: FRC Robotics & Modern ML

### FRC Autonomous Robotics: Swerve Azimuth Steering & Arm Gravity Feedforward

#### Swerve Azimuth Tracking
In FRC swerve drivetrains, the azimuth steering motor uses a high-frequency PID controller (running at 1 kHz in hardware motor controllers like Spark Max or Talon FX). 

If the robot is currently heading at `+175°` and the autonomous path planner requests `-175°`:
- **Naive controller:** Computes `error = -175° - 175° = -350°`. The azimuth motor violently slews 350 degrees around. During this 250ms turn, the chassis pulls off its autonomous trajectory.
- **Topologically-aware controller:** Computes `Δθ = wrap_to_pi(-350°) = +10°`. The module turns only 10 degrees, reaching target alignment in 20 milliseconds.

#### Single-Joint Pivot Arm Gravity Feedforward
For a robotic arm pivoting about a horizontal axle, gravity exerts a torque proportional to the horizontal distance from the pivot to the center of mass:

```
   τ_gravity(θ) = m · g · L_com · cos(θ)
```

Where `θ = 0` is the horizontal position. Using correct trigonometric projection `cos(θ)` allows feedforward voltage `V_ff = kG · cos(θ)` to perfectly balance the arm at every angle against gravity without relying on integral PID accumulation.

```
                  Pivot
                   (O)══════════════════● Center of Mass (m)
                    │ \ θ               │
                    │  \                │
                    │   \               ▼ F_g = m·g
                    ▼    \
                   Arm at angle θ: Torque = m·g·L·cos(θ)
```

### Machine Learning: Positional Encodings & Directional Losses

#### Cyclic Feature Encoding
If you feed raw angles `θ ∈ [0°, 360°)` as a scalar input into a neural network, the network sees a massive numerical discontinuity between `359.9°` and `0.0°`. The network believes those two adjacent physical states are 360 units apart.

To preserve circular topology in neural networks, angles are decomposed into continuous orthogonal trigonometric components:

```
   x_encoded = [ cos(θ), sin(θ) ]ᵀ
```

In Transformer models, **Rotary Positional Embeddings (RoPE)** apply 2D rotation matrices to query and key vectors based on token positions `m`:

```
   q_m = R(m · θ) · W_q · x_m
```

#### Cosine Directional Loss for 3D Bounding Boxes
When training object detection networks to predict autonomous vehicle headings, using Mean Squared Error `(θ_pred - θ_true)²` severely penalizes a prediction of `+179°` when the ground truth is `-179°` (error `358² = 128,164`).

Instead, the network is trained using **Cosine Proximity Loss**:

```
   L_angle = 1 - cos(θ_pred - θ_true) = 1 - (u_pred · u_true)
```

---

## 4. Classic Failure Mode & Python Engine

### The Classic Failure Mode: The 340-Degree Swerve Spin
In autonomous match routines, the robot must execute rapid maneuvers (e.g., scoring a game piece and instantly darting across the field to intake another).

**The Catastrophe:** If the swerve module code neglects continuous angle wrapping and azimuth inversion:
1. When steering transitions from `+170°` to `-170°`, the module rotates 340 degrees.
2. The azimuth motor draws peak stall current (80+ Amps), dropping the main battery voltage below 7.0 Volts (causing a **RoboRIO brownout**).
3. The violent 340° spin twists and eventually snaps the CAN bus wires and encoder cables inside the swerve module assembly.

### From-Scratch Python Implementation

```python
#!/usr/bin/env python3
"""
axon - Concept 02: Trigonometry, atan2 & Continuous Angle Topology
From-scratch implementation of circular angle math and swerve optimization.
"""
import math
from typing import Tuple


def wrap_to_pi(angle_rad: float) -> float:
    """
    Wrap an arbitrary angle in radians to the continuous interval [-π, +π).
    Uses atan2 phasor projection to eliminate branching and modulo edge-cases.
    """
    return math.atan2(math.sin(angle_rad), math.cos(angle_rad))


def wrap_to_degrees(angle_deg: float) -> float:
    """Wrap an angle in degrees to [-180, +180)."""
    rad = math.radians(angle_deg)
    return math.degrees(wrap_to_pi(rad))


class SwerveModuleState:
    def __init__(self, speed_mps: float, angle_rad: float):
        self.speed = float(speed_mps)
        self.angle = wrap_to_pi(angle_rad)

    def __repr__(self) -> str:
        return f"SwerveState(speed={self.speed:+.2f} m/s, angle={math.degrees(self.angle):+.1f}°)"


class SwerveOptimizer:
    @staticmethod
    def optimize(desired: SwerveModuleState, current_angle_rad: float) -> SwerveModuleState:
        """
        Optimize swerve target to turn no more than 90 degrees.
        If delta > 90°, inverts speed and rotates to the opposite angle (delta - 180°).
        """
        delta_angle = wrap_to_pi(desired.angle - current_angle_rad)

        if abs(delta_angle) > (math.PI / 2.0):
            optimized_speed = -desired.speed
            if delta_angle > 0:
                optimized_angle = current_angle_rad + (delta_angle - math.PI)
            else:
                optimized_angle = current_angle_rad + (delta_angle + math.PI)
        else:
            optimized_speed = desired.speed
            optimized_angle = current_angle_rad + delta_angle

        return SwerveModuleState(optimized_speed, optimized_angle)


def simulate_swerve_transition(current_deg: float, target_deg: float, target_speed: float):
    current_rad = math.radians(current_deg)
    target_rad = math.radians(target_deg)
    desired = SwerveModuleState(target_speed, target_rad)

    naive_turn_deg = target_deg - current_deg
    wrapped_delta_rad = wrap_to_pi(target_rad - current_rad)
    wrapped_turn_deg = math.degrees(wrapped_delta_rad)

    optimized = SwerveOptimizer.optimize(desired, current_rad)
    opt_turn_deg = math.degrees(wrap_to_pi(optimized.angle - current_rad))

    print(f"Current Angle : {current_deg:+.1f}° | Desired: {target_deg:+.1f}° @ {target_speed:+.1f} m/s")
    print(f"  [Naive Controller]     Turn: {naive_turn_deg:+.1f}° | Speed: {target_speed:+.1f} m/s")
    print(f"  [Wrapped Controller]   Turn: {wrapped_turn_deg:+.1f}° | Speed: {target_speed:+.1f} m/s")
    print(f"  [Optimized Azimuth]    Turn: {opt_turn_deg:+.1f}° | Speed: {optimized.speed:+.1f} m/s")
    print("-" * 65)


if __name__ == "__main__":
    print("=" * 65)
    print("SWERVE MODULE ANGLE TOPOLOGY BENCHMARK")
    print("=" * 65)
    simulate_swerve_transition(current_deg=170.0, target_deg=-170.0, target_speed=3.0)
    simulate_swerve_transition(current_deg=0.0, target_deg=160.0, target_speed=4.0)

    vx, vy = -2.0, -2.0
    computed_angle = math.atan2(vy, vx)
    naive_angle = math.atan(vy / vx)
    print(f"Vector [-2, -2]ᵀ:")
    print(f"  atan2(y, x) = {math.degrees(computed_angle):+.1f}° (Correct Quad III)")
    print(f"  atan(y / x) = {math.degrees(naive_angle):+.1f}° (FAIL: Wrong Quad I)")
```

---

## 5. Review Checkpoints & Deep-Dive Prompts

### Review Checkpoints

#### Checkpoint 1: Shortest Angular Difference Calculation
**Question:** A robot turret is tracking a vision target. The turret's current gyro heading is `θ_curr = +165°`. The computer vision camera detects a target at field heading `θ_target = -150°`.
1. What is the naive angular error?
2. What is the true shortest angular turn `Δθ`?
3. In which physical direction (clockwise or counter-clockwise) should the motor spin?

**Solution:**
1. **Naive Error:**
   ```
   e_naive = θ_target - θ_curr = -150° - 165° = -315°
   ```
2. **Shortest Angular Turn:**
   Convert to radians or apply modulo 360 wrapping:
   ```
   Δθ = wrap_to_degrees(-315°) = -315° + 360° = +45°
   ```
   Or via formula: `atan2(sin(-315°), cos(-315°)) = atan2(+0.7071, +0.7071) = +45°`.
3. **Physical Direction:** Since `Δθ = +45°` is positive, the turret must rotate **45 degrees counter-clockwise**, rather than spinning 315 degrees clockwise.

#### Checkpoint 2: Swerve Module Optimization Under 135° Commanded Slew
**Question:** A swerve module is currently rolling straight forward at `θ = 0°` with velocity `v = +3.5 m/s`. The driver suddenly shifts the translation joystick to `θ_target = +135°` at `v = +3.5 m/s`.
Determine the optimal steering angle `θ_opt` and motor velocity `v_opt` commanded by an optimized swerve controller.

**Solution:**
1. Compute shortest angular error: `Δθ = 135° - 0° = +135°`.
2. Check optimization condition: `|Δθ| = 135° > 90°`.
3. Apply swerve inversion rules:
   ```
   θ_opt = θ_curr + (Δθ - 180°) = 0° + (135° - 180°) = -45°
   v_opt = -v_target = -3.5 m/s
   ```
4. **Result:** The azimuth steering motor only needs to turn **45° clockwise** (instead of 135° counter-clockwise), and the drive motor runs in reverse at **-3.5 m/s**.

---

### Deep-Dive Exploration Prompts

1. **Quaternions & 3D Orientation Topology (SO(3)):** While 2D orientation lives on the circle `S¹`, 3D orientation lives on the special orthogonal group `SO(3)`. Why do Euler angles (roll, pitch, yaw) suffer from "Gimbal Lock", and how do unit quaternions `q = w + xi + yj + zk` on the 3-sphere `S³` eliminate topological singularities?
2. **Continuous Angular Filters in Kalman Estimation:** When an Extended Kalman Filter (EKF) fuses wheel odometry with a vision AprilTag measurement, the innovation step computes `y = z_meas - h(x)`. Why will an un-wrapped subtraction in the Kalman innovation calculation completely corrupt the covariance matrix `P` whenever the robot faces near `±180°`?

---

### Curriculum Linkages

* **Backward Link:** Concept 01 (Vectors, dot products, and 2D rotation matrices).
* **Forward Links:**
  * **Concept 10 (Modern Feedforward Modeling):** Gravity torque compensation `kG · cos(θ)` for robotic arms.
  * **Concept 13 (Swerve Kinematics):** Resolving wheel azimuth steering angles with `atan2(vy, vx)`.
  * **Concept 16 (Extended Kalman Filters):** Heading angle wrapping in sensor fusion innovation steps.
