# Concept 02: Trigonometry, atan2, Angle Topology & Quaternions

```
       Module 1: Math Foundations  ➔  Concept 02: Angle Topology & Quaternions
```

> **▶ Interactive Demo: [2D Angle Topology & 3D Quaternion Sandbox](demo.html)**
>
> Open the visualizer in your browser or explore the embedded frame below to experiment with 2D angle wrapping, 4-quadrant atan2, and 3D Quaternion rotations without Gimbal Lock.

<iframe src="demo.html" width="100%" height="560" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--code-bg, #0a0d14);"></iframe>

---

## 1. Intuitive Mental Model: The Geometry of Angles

### Part A: The Unit Circle & Vector Projections
Imagine a clock hand of length 1 pinned at the center `(0, 0)`. As the hand sweeps around counter-clockwise by an angle `θ`:

* The **x-coordinate** (horizontal shadow) is `cos(θ)`.
* The **y-coordinate** (vertical height) is `sin(θ)`.

<div style="text-align: center; margin: 20px 0;">
  <svg width="280" height="200" viewBox="0 0 280 200" style="max-width: 100%; height: auto;">
    <circle cx="140" cy="100" r="70" fill="none" stroke="#334155" stroke-width="1.5" />
    <line x1="40" y1="100" x2="240" y2="100" stroke="#475569" stroke-width="1" />
    <line x1="140" y1="20" x2="140" y2="180" stroke="#475569" stroke-width="1" />
    <!-- Radius line -->
    <line x1="140" y1="100" x2="189" y2="51" stroke="#fbbf24" stroke-width="2.5" />
    <!-- Triangle drops -->
    <line x1="140" y1="100" x2="189" y2="100" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="2" />
    <line x1="189" y1="100" x2="189" y2="51" stroke="#4ade80" stroke-dasharray="3,3" stroke-width="2" />
    <circle cx="189" cy="51" r="4" fill="#fbbf24" />
    <text x="150" y="118" fill="#38bdf8" font-family="monospace" font-size="11">cos(θ)</text>
    <text x="195" y="80" fill="#4ade80" font-family="monospace" font-size="11">sin(θ)</text>
    <text x="160" y="70" fill="#fbbf24" font-family="monospace" font-size="11">r=1</text>
  </svg>
</div>

By the Pythagorean theorem:
```
   cos²(θ) + sin²(θ) = 1
```

---

### Part B: Why We Need `atan2(y, x)` Instead of `atan(y / x)`
Suppose a sensor gives you `(x, y)` coordinates and you want to calculate the heading angle `θ`.

If you use high-school `tan⁻¹(y / x)`:
* Point A: `(x = +1, y = +1)` ➔ `y/x = +1/1 = +1` ➔ `tan⁻¹(1) = 45°` (Quadrant I)
* Point B: `(x = -1, y = -1)` ➔ `y/x = -1/-1 = +1` ➔ `tan⁻¹(1) = 45°` (Quadrant III!)

Because the negative signs cancel out (`-1 / -1 = +1`), standard `tan⁻¹` is blind to the difference between pointing North-East (`+45°`) and South-West (`-135°`).

**The Solution:** The function **`atan2(y, x)`** takes `y` and `x` as two separate arguments. It inspects the signs of both numbers and correctly returns angles across all 4 quadrants, from `-180°` to `+180°` (`-π` to `+π`).

---

### Part C: Continuous Angle Topology & The Wrap-Around Trap
Numbers on a standard number line go on forever: `... -2, -1, 0, 1, 2 ...`
Angles, however, live on a circle. **`+180°` is the exact same physical heading as `-180°`.**

<div style="text-align: center; margin: 20px 0;">
  <svg width="280" height="150" viewBox="0 0 280 150" style="max-width: 100%; height: auto;">
    <circle cx="140" cy="75" r="55" fill="none" stroke="#334155" stroke-width="1.5" />
    <line x1="140" y1="75" x2="90" y2="60" stroke="#38bdf8" stroke-width="2.5" />
    <circle cx="90" cy="60" r="4" fill="#38bdf8" />
    <text x="30" y="55" fill="#38bdf8" font-family="monospace" font-size="11">θ₁ = +170°</text>
    
    <line x1="140" y1="75" x2="90" y2="90" stroke="#fbbf24" stroke-width="2.5" />
    <circle cx="90" cy="90" r="4" fill="#fbbf24" />
    <text x="30" y="105" fill="#fbbf24" font-family="monospace" font-size="11">θ₂ = -170°</text>
    
    <!-- Short Arc -->
    <path d="M 90 60 A 55 55 0 0 0 90 90" fill="none" stroke="#4ade80" stroke-width="3" />
    <text x="155" y="80" fill="#4ade80" font-family="monospace" font-size="11">Shortest: 20°</text>
  </svg>
</div>

Suppose a robot is currently facing `+170°` and you command it to turn to `-170°`:
* **Naive subtraction:** `error = Target - Current = -170° - 170° = -340°`
* If you feed this `-340°` error into a motor controller, the robot will violently spin almost a full 360-degree circle!
* **Reality:** The robot is only **`20°` away**!

**Angle Normalization Formula:**
To find the shortest turn, wrap the difference into the range `[-180°, +180°]`:

```
   wrapped_error = ((error + 180°) % 360°) - 180°
```

---

### Part D: Swerve Module 180° Speed Inversion
In an autonomous swerve drive robot, each wheel module can both steer (rotate angle) and drive (spin wheel).

Suppose the wheel is currently facing `0°` and needs to drive at `170°`:
* If you rotate the steering azimuth motor by `170°`, it takes time to slew around.
* **The Clever Shortcut:** Rotate the wheel by only `-10°` (to `180°`), and run the drive motor **backward (reverse speed)**!

> **Rule:** If the angular error is greater than `90°`, flip the target angle by `180°` and invert the wheel speed: `speed = -speed`. The wheel never has to turn more than `90°`.

---

### Part E: Moving to 3D: Why Quaternions?

In 3D space, describing rotations with 3 angles (Roll, Pitch, Yaw) causes a fatal mathematical flaw known as **Gimbal Lock**:
* When the pitch angle reaches `±90°` (pointing straight up or down), the Roll axis and the Yaw axis align into the exact same plane.
* You lose a complete degree of freedom, and the math divides by zero.

**What is a Quaternion?**
A unit quaternion uses **4 numbers** `q = (w, x, y, z)` to describe a 3D rotation:
1. `w` represents the **rotation angle**: `w = cos(θ / 2)`
2. `(x, y, z)` represents the **3D axis** around which you rotate: `(u_x, u_y, u_z) · sin(θ / 2)`

Because quaternions represent rotations smoothly without trigonometric singularities, all modern 3D game engines, robotics IMU gyros (e.g., Pigeon 2.0, NavX), and spacecraft flight software use quaternions for 3D orientation.

---

## 2. Python Implementation

Here is how you compute 4-quadrant heading, wrap angle errors, and optimize swerve steering in pure Python:

```python
import math

def compute_heading(x, y):
    """Returns the continuous angle θ in degrees from (x, y) coordinates."""
    return math.degrees(math.atan2(y, x))

def shortest_angle_diff(target_deg, current_deg):
    """Calculates the shortest angular error wrapped to [-180, +180]."""
    diff = target_deg - current_deg
    return (diff + 180.0) % 360.0 - 180.0

def optimize_swerve_module(target_angle_deg, target_speed, current_angle_deg):
    """
    Optimizes swerve module to never turn more than 90 degrees
    by inverting motor direction if necessary.
    """
    error = shortest_angle_diff(target_angle_deg, current_angle_deg)
    
    if abs(error) > 90.0:
        # Flip direction and reverse drive speed
        error = error - 180.0 if error > 0 else error + 180.0
        target_speed = -target_speed
        
    optimized_angle = current_angle_deg + error
    return optimized_angle, target_speed

# Example 1: 340° Spin Trap Prevention
current = 170.0   # Facing North-West
target = -170.0   # Facing South-West

naive_error = target - current
smart_error = shortest_angle_diff(target, current)

print(f"Naive Error : {naive_error:+.1f}° (Dangerous 340° spin!)")
print(f"Smart Error : {smart_error:+.1f}° (Clean 20° turn)")

# Example 2: Swerve 180° Flip
opt_angle, opt_speed = optimize_swerve_module(target_angle_deg=175.0, target_speed=1.0, current_angle_deg=0.0)
print(f"Swerve Module Angle: {opt_angle:.1f}°, Speed: {opt_speed:+.1f}x")
```

---

## 3. Review Questions

### Question 1
A vision camera detects a target at position `x = -3.0` meters, `y = +3.0` meters.
1. Which quadrant is the target located in?
2. What angle does `atan2(y, x)` return in degrees?

**Answer:**
1. Since `x < 0` and `y > 0`, the target is in **Quadrant II**.
2. `atan2(3.0, -3.0) = +135.0°` (or `3π/4` radians).

---

### Question 2
A robot's gyro reads a heading of `-175°`. The autonomous trajectory commands a heading of `+175°`.
If the robot's control loop uses `shortest_angle_diff(175, -175)`, what is the commanded turn angle?

**Answer:**
`diff = 175 - (-175) = +350°`.
Wrapping into `[-180, +180]`: `(350 + 180) % 360 - 180 = 530 % 360 - 180 = 170 - 180 = -10.0°`.
The robot makes a smooth **`10°` clockwise turn** instead of a `350°` spin.
