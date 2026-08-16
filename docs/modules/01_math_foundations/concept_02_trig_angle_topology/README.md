# Concept 02: Trigonometry, atan2, Angle Topology & Quaternions

```
       Module 1: Math Foundations  ➔  Concept 02: Angle Topology & Quaternions
```

<iframe src="demo.html" width="100%" height="560" style="border: 1px solid var(--card-border, #232b3b); border-radius: 12px; margin: 16px 0; background: #0a0d14;"></iframe>

---

## 1. Intuitive Mental Model

Imagine measuring distance along a straight highway versus tracking time on a circular clock face.

On a straight highway (the real number line `ℝ¹`), moving 10 miles forward and 10 miles backward always puts you at distinct positions. If point A is at mile marker 1 and point B is at mile marker 359, the distance between them is undeniably `359 - 1 = 358` miles.

Now look at a 12-hour circular clock. If the minute hand points to 1 minute past the hour (`+6°`) and you want it to point to 59 minutes past the hour (`+354°` or `-6°`), how far does the hand have to turn?

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="200" viewBox="0 0 340 200" style="max-width: 100%; height: auto;">
    <defs>
      <marker id="arrow-green2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#4ade80" />
      </marker>
      <marker id="arrow-red2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#f43f5e" />
      </marker>
    </defs>
    <!-- Clock circle -->
    <circle cx="170" cy="100" r="70" fill="none" stroke="#334155" stroke-width="2" />
    <!-- 0 deg / 12 o'clock -->
    <line x1="170" y1="20" x2="170" y2="40" stroke="#94a3b8" stroke-width="1.5" />
    <text x="160" y="18" fill="#94a3b8" font-family="monospace" font-size="11">0° / 360°</text>
    <!-- 1m hand (6 deg) -->
    <line x1="170" y1="100" x2="182" y2="35" stroke="#38bdf8" stroke-width="2.5" />
    <text x="190" y="45" fill="#38bdf8" font-family="monospace" font-size="11">+6°</text>
    <!-- 59m hand (354 deg) -->
    <line x1="170" y1="100" x2="158" y2="35" stroke="#fbbf24" stroke-width="2.5" />
    <text x="110" y="45" fill="#fbbf24" font-family="monospace" font-size="11">354° (-6°)</text>
    <!-- Shortest turn arc (Green) -->
    <path d="M 178 50 A 50 50 0 0 0 162 50" fill="none" stroke="#4ade80" stroke-width="3.5" marker-end="url(#arrow-green2)" />
    <text x="135" y="75" fill="#4ade80" font-family="monospace" font-weight="bold" font-size="11">Shortest: 12°</text>
    <!-- Naive spin arc (Red) -->
    <path d="M 185 65 A 60 60 0 1 1 155 65" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#arrow-red2)" />
    <text x="120" y="185" fill="#f43f5e" font-family="monospace" font-size="10">Naive linear: 348° spin!</text>
  </svg>
</div>

If your control software blindly computes `354° - 6° = +348°`, your motor will spin nearly a full circle clockwise to travel a distance that was only 12 degrees counter-clockwise.

This fundamental topological difference—between a straight Euclidean line `ℝ¹` and the closed circle manifold **S¹**—is the root of frequent bugs in robotics.

When we move to **3D space**, rotations become even more subtle. Describing 3D orientations with three sequential angles—Roll, Pitch, and Yaw (Euler Angles)—inevitably leads to **Gimbal Lock**, where two rotation axes align and collapse a full degree of freedom. 

To overcome this, modern autonomous robotics and aerospace guidance use **Quaternions**: four-dimensional hypercomplex numbers that navigate the 3-sphere manifold **S³**, guaranteeing smooth, singularity-free 3D spatial rotations.

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

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="180" viewBox="0 0 300 180" style="max-width: 100%; height: auto;">
    <circle cx="100" cy="90" r="60" fill="none" stroke="#334155" stroke-width="1.5" />
    <line x1="20" y1="90" x2="180" y2="90" stroke="#64748b" stroke-width="1" />
    <line x1="100" y1="10" x2="100" y2="170" stroke="#64748b" stroke-width="1" />
    <!-- Radius Vector -->
    <line x1="100" y1="90" x2="145" y2="48" stroke="#38bdf8" stroke-width="2.5" />
    <line x1="145" y1="90" x2="145" y2="48" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="2,2" />
    <text x="150" y="70" fill="#4ade80" font-family="monospace" font-size="11">y = r·sin θ</text>
    <text x="105" y="105" fill="#fbbf24" font-family="monospace" font-size="11">x = r·cos θ</text>
    <text x="150" y="45" fill="#38bdf8" font-family="monospace" font-weight="bold" font-size="11">P(x, y)</text>
  </svg>
</div>

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
1. `v₁ = [+1, +1]ᵀ` (Quadrant I, pointing North-East, `θ = +45°`)
2. `v₂ = [-1, -1]ᵀ` (Quadrant III, pointing South-West, `θ = -135°`)

Evaluating naive `arctan`:
- `v₁ ➔ arctan(+1 / +1) = arctan(+1.0) = +45°`
- `v₂ ➔ arctan(-1 / -1) = arctan(+1.0) = +45°`

Naive `arctan` outputs `+45°` for vector `v₂`, commanding your robot to drive in the exact opposite direction. Furthermore, if `x = 0` (a purely vertical motion), `y/x` causes a division-by-zero crash.

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

### Continuous Angle Wrapping via Phasor Projection
To find the shortest signed angular difference between current heading `θ_curr` and target heading `θ_target`:

```
   Δθ = atan2( sin(θ_target - θ_curr), cos(θ_target - θ_curr) )
```

This single formula automatically maps any arbitrary angular difference onto `[-π, +π]` without conditional branches.

---

### 3D Rotations & The Geometry of Quaternions

In three-dimensional space, the set of all valid rotation matrices forms the Special Orthogonal Lie Group **SO(3)**.

#### Why Euler Angles Suffer from Gimbal Lock
Euler angles represent orientation as three sequential single-axis rotations: `R_z(yaw) · R_y(pitch) · R_x(roll)`.

When pitch reaches `±90°` (`±π/2 rad`), `cos(pitch) = 0`. Multiplying the three matrices reveals that the resulting rotation matrix depends only on the combined sum or difference `(yaw ± roll)`. 

**Gimbal Lock:** The first rotation axis (Yaw / Z) and the third rotation axis (Roll / X) align in 3D space, collapsing 3 degrees of freedom down to 2. Angular rates become mathematically singular, causing physical gyro tracking loops to violently destabilize.

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="180" viewBox="0 0 340 180" style="max-width: 100%; height: auto;">
    <!-- Normal 3-Axis Gimbal -->
    <ellipse cx="90" cy="90" rx="60" ry="60" fill="none" stroke="#38bdf8" stroke-width="2" />
    <ellipse cx="90" cy="90" rx="45" ry="30" fill="none" stroke="#4ade80" stroke-width="2" />
    <ellipse cx="90" cy="90" rx="30" ry="10" fill="none" stroke="#f43f5e" stroke-width="2" />
    <text x="35" y="165" fill="#38bdf8" font-family="monospace" font-size="11">Normal: 3 Independent Axes</text>
    
    <!-- Locked Gimbal -->
    <ellipse cx="250" cy="90" rx="60" ry="60" fill="none" stroke="#38bdf8" stroke-width="2" />
    <ellipse cx="250" cy="90" rx="45" ry="5" fill="none" stroke="#4ade80" stroke-width="2" />
    <ellipse cx="250" cy="90" rx="30" ry="58" fill="none" stroke="#f43f5e" stroke-width="2" />
    <text x="195" y="165" fill="#f43f5e" font-family="monospace" font-weight="bold" font-size="11">Gimbal Lock: Pitch=90°</text>
  </svg>
</div>

#### Unit Quaternions (Euler-Rodrigues Axis-Angle Representation)
A quaternion `q` is a 4-dimensional hypercomplex number:

```
   q = w + x·i + y·j + z·k = [ w , v ]
```

Where `w` is the scalar real component, `v = [x, y, z]ᵀ` is the imaginary vector component, and the basis elements satisfy **Hamilton's Fundamental Rules**:

```
   i² = j² = k² = i · j · k = -1
   i · j = k  = -j · i
   j · k = i  = -k · j
   k · i = j  = -i · k
```

To represent a 3D spatial rotation of angle `θ` around a unit axis `û = [ux, uy, uz]ᵀ` (`||û|| = 1`):

```
   w = cos(θ / 2)
   x = ux · sin(θ / 2)
   y = uy · sin(θ / 2)
   z = uz · sin(θ / 2)
   
   ||q|| = √(w² + x² + y² + z²) = 1   (Unit Quaternion on S³)
```

#### Quaternion Multiplication (Hamilton Product)
The composition of two rotations `q₁` followed by `q₂` is given by the non-commutative Hamilton product `q_total = q₂ ⊗ q₁`:

```
   q₁ ⊗ q₂ = [ w₁·w₂ - (v₁ · v₂) ,  w₁·v₂ + w₂·v₁ + (v₁ × v₂) ]
```

In scalar component form:

```
   w_res = w₁·w₂ - x₁·x₂ - y₁·y₂ - z₁·z₂
   x_res = w₁·x₂ + x₁·w₂ + y₁·z₂ - z₁·y₂
   y_res = w₁·y₂ - x₁·z₂ + y₁·w₂ + z₁·x₂
   z_res = w₁·z₂ + x₁·y₂ - y₁·x₂ + z₁·w₂
```

#### Rotating a 3D Vector with Quaternions
To rotate a 3D point or vector `p = [px, py, pz]ᵀ`, we represent `p` as a pure quaternion with zero real component `p_quat = [0, px, py, pz]`.

The rotated vector `p'` is computed by sandwiching `p_quat` between unit quaternion `q` and its **conjugate** `q* = [w, -x, -y, -z]`:

```
   p'_quat = q ⊗ p_quat ⊗ q*
```

This operation rotates vector `p` by exactly angle `θ` around axis `û` with zero trigonometric evaluations and zero gimbal singularities.

#### Spherical Linear Interpolation (SLERP)
To smoothly blend between two 3D orientations `q₁` and `q₂` with parameter `t ∈ [0, 1]`:

```
   slerp(q₁, q₂, t) = ( sin((1 - t)·Ω) / sin(Ω) ) · q₁ + ( sin(t·Ω) / sin(Ω) ) · q₂
```

Where `cos(Ω) = q₁ · q₂ = w₁·w₂ + x₁·x₂ + y₁·y₂ + z₁·z₂` is the 4D dot product. If `cos(Ω) < 0`, negate `q₂` to take the shortest path across the 3-sphere (since `q` and `-q` represent the exact same 3D spatial rotation).

---

## 3. Dual Grounding: FRC Robotics & Modern ML

### FRC Autonomous Robotics: Swerve Azimuth Optimization & 3D Gyro IMU Fusion

#### Swerve Module 90° Inversion Optimization
A swerve drive wheel is bidirectional: spinning forward at angle `θ` produces identical ground traction to spinning backward at angle `θ + π` (180° opposite).

```
   If |Δθ| > 90°:
       θ_optimal = θ_curr + (Δθ - sign(Δθ)·π)
       v_optimal = -v_target
   Else:
       θ_optimal = θ_curr + Δθ
       v_optimal = +v_target
```

#### 3D Gyro / IMU Quaternion Integration
High-performance FRC robots equipped with 6-DOF IMUs (such as NavX2 or Pigeon 2.0) measure 3-axis angular velocity `ω = [ωx, ωy, ωz]ᵀ` at 250–1000 Hz.

The robot software updates its 3D orientation quaternion via the kinematic differential equation:

```
   dq / dt = (1 / 2) · q ⊗ [0, ωx, ωy, ωz]
   q[k+1]  = normalize( q[k] + (dq / dt) · dt )
```

Because this update operates in quaternion space, the robot tracks pitch, roll, and yaw accurately even when tipping onto charging station ramps or negotiating aggressive field defense without gimbal lock.

### Machine Learning: Rotary Embeddings & 3D Quaternion Pose Regression

#### Rotary Positional Embeddings (RoPE)
In modern Transformer language models (LLaMA, Mistral, Gemma), cyclic 2D rotation operators encode token distance:

```
   q_m = R(m · θ) · W_q · x_m
```

The relative inner product `⟨q_m, k_n⟩` depends purely on the relative distance `(m - n)` through continuous angle rotation.

#### 3D Bounding Box Orientation in Autonomous Driving
In autonomous vehicle perception (e.g. Waymo or Tesla FSD), neural networks predict the 3D bounding box orientation of surrounding vehicles as unit quaternions `q = [w, x, y, z]`. 

Using quaternion loss `L_rot = 1 - |q_pred · q_true|` avoids the discontinuous wrapping penalties of Euler angles and ensures stable gradient propagation.

---

## 4. Classic Failure Mode & Python Engine

### The Classic Failure Mode: The 340-Degree Spin Trap & Euler Gimbal Lock

1. **2D Swerve Spin:** When steering transitions from `+170°` to `-170°`, an un-wrapped controller commands a 340° rotation, drawing 80+ Amps, browning out the robot battery, and snapping internal CAN encoder wiring.
2. **3D Gimbal Lock:** An autonomous drone or balancing robot tracking pitch with Euler angles pitches up to `+90°`. The yaw and roll axes collapse, making `d(roll)/dt` undefined (`NaN`), causing the flight controller to issue infinite torque commands and flip uncontrollably.

### From-Scratch Python Implementation

```python
#!/usr/bin/env python3
"""
axon - Concept 02: Trigonometry, atan2 & 3D Quaternions
From-scratch implementation of continuous angle wrapping and 3D Quaternions.
"""
import math
from typing import Tuple


def wrap_to_pi(angle_rad: float) -> float:
    """Wrap angle in radians to [-π, +π) via phasor projection."""
    return math.atan2(math.sin(angle_rad), math.cos(angle_rad))


class Quaternion:
    def __init__(self, w: float, x: float, y: float, z: float):
        self.w = float(w)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @classmethod
    def from_axis_angle(cls, axis: Tuple[float, float, float], angle_rad: float) -> 'Quaternion':
        """Construct unit quaternion from 3D axis and rotation angle."""
        ax, ay, az = axis
        norm = math.sqrt(ax**2 + ay**2 + az**2)
        if norm < 1e-9:
            return cls(1.0, 0.0, 0.0, 0.0)
        ux, uy, uz = ax / norm, ay / norm, az / norm
        half_angle = angle_rad / 2.0
        s = math.sin(half_angle)
        return cls(math.cos(half_angle), ux * s, uy * s, uz * s)

    def magnitude(self) -> float:
        return math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    def normalized(self) -> 'Quaternion':
        m = self.magnitude()
        if m < 1e-9:
            return Quaternion(1.0, 0.0, 0.0, 0.0)
        return Quaternion(self.w / m, self.x / m, self.y / m, self.z / m)

    def conjugate(self) -> 'Quaternion':
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def multiply(self, other: 'Quaternion') -> 'Quaternion':
        """Hamilton Product: q_res = self ⊗ other"""
        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        return Quaternion(w, x, y, z)

    def rotate_vector(self, v: Tuple[float, float, float]) -> Tuple[float, float, float]:
        """Rotate a 3D vector v via sandwich product: v' = q ⊗ [0, v] ⊗ q*"""
        p = Quaternion(0.0, v[0], v[1], v[2])
        q_unit = self.normalized()
        p_rot = q_unit.multiply(p).multiply(q_unit.conjugate())
        return (p_rot.x, p_rot.y, p_rot.z)

    def __repr__(self) -> str:
        return f"Quat(w={self.w:.4f}, x={self.x:.4f}, y={self.y:.4f}, z={self.z:.4f})"


def demonstrate_quaternion_rotations():
    print("=" * 65)
    print("1. 3D QUATERNION ROTATION (90° about Z-axis)")
    print("=" * 65)
    v_orig = (1.0, 0.0, 0.0)
    q_rot = Quaternion.from_axis_angle(axis=(0.0, 0.0, 1.0), angle_rad=math.radians(90))
    v_rot = q_rot.rotate_vector(v_orig)
    print(f"Original Vector  : {v_orig}")
    print(f"Rotation Quat    : {q_rot}")
    print(f"Rotated Vector   : ({v_rot[0]:.4f}, {v_rot[1]:.4f}, {v_rot[2]:.4f})")

    print("\n" + "=" * 65)
    print("2. 2D CONTINUOUS SWERVE ANGLE OPTIMIZATION")
    print("=" * 65)
    curr_deg, target_deg = 170.0, -170.0
    delta_deg = math.degrees(wrap_to_pi(math.radians(target_deg - curr_deg)))
    print(f"Current: {curr_deg}° | Target: {target_deg}°")
    print(f"Naive Difference : {target_deg - curr_deg:+.1f}° (Destructive 340° spin!)")
    print(f"Continuous Wrap  : {delta_deg:+.1f}° (Safe shortest turn)")


if __name__ == "__main__":
    demonstrate_quaternion_rotations()
```

---

## 5. Review Checkpoints & Deep-Dive Prompts

### Review Checkpoints

#### Checkpoint 1: Shortest Angular Difference Calculation
**Question:** A robot turret's gyro heading is `θ_curr = +165°`. Computer vision detects a target at field heading `θ_target = -150°`. Compute the shortest angular turn `Δθ` and physical direction.

**Solution:**
1. Apply continuous wrapping formula:
   ```
   Δθ = wrap_to_degrees(-150° - 165°) = wrap_to_degrees(-315°) = +45°
   ```
2. **Physical Direction:** Positive sign means the turret turns **45 degrees counter-clockwise** in 30ms, rather than spinning 315 degrees clockwise.

#### Checkpoint 2: Quaternion 3D Vector Rotation
**Question:** Let unit quaternion `q = [cos(45°), 0, 0, sin(45°)] = [1/√2, 0, 0, 1/√2]`. Compute the rotated result of vector `v = [1, 0, 0]ᵀ`.

**Solution:**
1. `q` represents a rotation of `2 × 45° = 90°` around the Z-axis `[0, 0, 1]ᵀ`.
2. Evaluating `v' = q ⊗ [0, 1, 0, 0] ⊗ q*`:
   ```
   v' = [0, 1, 0]ᵀ
   ```
3. **Physical Meaning:** The vector pointing East along the X-axis rotates 90° counter-clockwise to point North along the Y-axis.

---

### Deep-Dive Exploration Prompts

1. **Dual Quaternions in Spatial Kinematics:** Standard quaternions represent pure 3D rotations. **Dual Quaternions** `q_hat = q_rot + ε · q_trans` combine both 3D rotation and 3D translation into a single 8-parameter algebra. How do dual quaternions eliminate screw axis singularities in 6-DOF robotic arm forward kinematics?
2. **Quaternion Normalization Drift in IMUs:** At 500 Hz, discrete numerical integration causes floating-point roundoff to degrade unit length `||q|| ≠ 1.0`. What fast first-order Taylor expansion `q_norm ≈ q · (1.5 - 0.5 · ||q||²)` is used in embedded firmware to renormalize quaternions without computing expensive square roots?
