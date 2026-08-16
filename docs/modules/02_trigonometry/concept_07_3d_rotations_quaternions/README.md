# Concept 07: 3D Rotations & Quaternions

```
       Module 2: Trigonometry  ➔  Concept 07: 3D Quaternions
```

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

## 2. The Solution: What is a Quaternion?

Instead of using 3 angles that can lock up, modern robotics software (like WPILib's `Rotation3d`) uses a **Quaternion**.

A unit quaternion packages a 3D rotation into **4 numbers**: `(w, x, y, z)`:
* **`w`:** Measures the **amount of rotation**: `w = cos(θ / 2)`.
* **`(x, y, z)`:** A 3D vector arrow pointing along the **axis of rotation**, scaled by `sin(θ / 2)`.

```python
import math

def euler_to_quaternion(roll_deg, pitch_deg, yaw_deg):
    """
    Converts Roll, Pitch, Yaw angles into a 4-component Unit Quaternion (w, x, y, z).
    """
    r = math.radians(roll_deg) / 2.0
    p = math.radians(pitch_deg) / 2.0
    y = math.radians(yaw_deg) / 2.0
    
    w = math.cos(r)*math.cos(p)*math.cos(y) + math.sin(r)*math.sin(p)*math.sin(y)
    x = math.sin(r)*math.cos(p)*math.cos(y) - math.cos(r)*math.sin(p)*math.sin(y)
    y_q = math.cos(r)*math.sin(p)*math.cos(y) + math.sin(r)*math.cos(p)*math.sin(y)
    z = math.cos(r)*math.cos(p)*math.sin(y) - math.sin(r)*math.sin(p)*math.cos(y)
    
    return [w, x, y_q, z]

# Example: A 90-degree pitch up
q = euler_to_quaternion(roll_deg=0.0, pitch_deg=90.0, yaw_deg=0.0)
print(f"Quaternion (w, x, y, z): [{q[0]:.3f}, {q[1]:.3f}, {q[2]:.3f}, {q[3]:.3f}]")
```

---

> 💡 **Math Sidebar: 4D Unit Sphere**
>
> A unit quaternion lives on a 4-dimensional sphere (written as **`S³`**).
>
> Its 4 components always satisfy:
> ```
>    w² + x² + y² + z² = 1
> ```
>
> Because there are no trigonometric denominators (`tan(θ)`), quaternions **never divide by zero** and can smoothly interpolate any 3D orientation without Gimbal Lock!

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
