# Concept 05: 4-Quadrant Heading with atan2

> **▶ Interactive Demo: [4-Quadrant atan2 vs atan Sandbox](demo.html)**
>
> Open the interactive demo below to drag the target into all 4 quadrants and see where high-school `atan(y/x)` fails and `atan2(y, x)` succeeds.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Minus-Sign Trap
Suppose your robot is at `(0, 0)` and wants to turn its turret to aim at a target.

Consider two completely different target locations:
* **Target A (North-East):** `dx = +2.0m, dy = +2.0m` (Ahead and to the Right)
* **Target B (South-West):** `dx = -2.0m, dy = -2.0m` (Behind and to the Left)

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="180" viewBox="0 0 300 180" style="max-width: 100%; height: auto;">
    <line x1="30" y1="90" x2="270" y2="90" stroke="#334155" stroke-width="1.5" />
    <line x1="150" y1="20" x2="150" y2="160" stroke="#334155" stroke-width="1.5" />
    
    <!-- Quad I Target A -->
    <circle cx="210" cy="40" r="6" fill="#38bdf8" />
    <line x1="150" y1="90" x2="210" y2="40" stroke="#38bdf8" stroke-width="2" />
    <text x="220" y="45" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="11">A (+2, +2) ➔ +45°</text>
    
    <!-- Quad III Target B -->
    <circle cx="90" cy="140" r="6" fill="#f43f5e" />
    <line x1="150" y1="90" x2="90" y2="140" stroke="#f43f5e" stroke-width="2" />
    <text x="10" y="145" fill="#f43f5e" font-family="sans-serif" font-weight="bold" font-size="11">B (-2, -2) ➔ -135°</text>
  </svg>
</div>

If you use high-school inverse tangent `tan⁻¹(dy / dx)`:
* Target A: `tan⁻¹(+2 / +2) = tan⁻¹(+1) = +45°` (Correct!)
* Target B: `tan⁻¹(-2 / -2) = tan⁻¹(+1) = +45°` (**CATASTROPHE!**)

Because the two negative signs cancel out (`-2 / -2 = +1`), regular `tan⁻¹` is blind to the fact that Target B is behind you. It aims the turret forward toward empty space!

---

## 2. Solving It in Code: The `atan2` Function
Programming languages solve this by providing **`math.atan2(y, x)`**, which takes `y` and `x` as **two separate parameters** rather than dividing them first:

```python
import math

def calculate_aim_angle(dx, dy):
    """
    Computes the true 4-quadrant heading angle in degrees.
    """
    angle_rad = math.atan2(dy, dx)  # Note: y comes first, then x!
    return math.degrees(angle_rad)

# Target A: North-East (+2m, +2m)
angle_A = calculate_aim_angle(dx=2.0, dy=2.0)
print(f"Target A Heading: {angle_A:+.1f}°")  # Output: +45.0° (Quad I)
# Target B: South-West (-2m, -2m)
angle_B = calculate_aim_angle(dx=-2.0, dy=-2.0)
print(f"Target B Heading: {angle_B:+.1f}°")  # Output: -135.0° (Quad III)
```

---

> 💡 **Math Sidebar: The 4 Quadrants**
>
> The 2D plane is divided into 4 quadrants based on the signs of `(x, y)`:
>
> | Quadrant | X Sign | Y Sign | Angle Range |
> |---|---|---|---|
> | **I (North-East)** | `+` | `+` | `0°` to `+90°` |
> | **II (North-West)** | `-` | `+` | `+90°` to `+180°` |
> | **III (South-West)** | `-` | `-` | `-180°` to `-90°` |
> | **IV (South-East)** | `+` | `-` | `-90°` to `0°` |
>
> `atan2(y, x)` automatically inspects the positive/negative signs of both inputs and returns the correct angle across all 4 quadrants from `-180°` to `+180°`.

---

## 3. Bridge to Machine Learning: Orientation Loss
In AI object detection (e.g. bounding boxes around cars or robot game pieces):
* The AI must predict the object's orientation angle `θ`.
* Predicting a single raw number can jump discontinuously. Instead, neural networks often predict `[cos(θ), sin(θ)]` as two separate output neurons, and the software reconstructs the true heading using `atan2(sin_pred, cos_pred)`.

---

## 4. Review Checkpoints
### Checkpoint 1
An AprilTag is at `dx = -4.0` meters, `dy = +4.0` meters.
1. Which quadrant is the target in?
2. What angle does `atan2(dy, dx)` return in degrees?

**Solution:**
1. Since `x < 0` and `y > 0`, it is in **Quadrant II (North-West)**.
2. `atan2(4.0, -4.0) = +135.0°` (or `3π/4` radians).

---

### Checkpoint 2
Why does `atan2` take arguments in the order `(y, x)` instead of `(x, y)`?

**Solution:**
Because the slope is defined as `Rise / Run = Δy / Δx`. In `tan(θ) = y / x`, `y` is in the numerator, so mathematical convention places `y` as the first argument in `atan2(y, x)`.
