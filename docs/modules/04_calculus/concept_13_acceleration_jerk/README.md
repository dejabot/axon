# Concept 13: Acceleration, Jerk & S-Curves

```
       Module 4: Calculus  ➔  Concept 13: Acceleration & Jerk
```

> **▶ Interactive Demo: [Elevator Motion & Jerk Visualizer](demo.html)**
>
> Open the interactive demo below to compare an instant acceleration step against a smooth S-Curve profile and watch the sloshing coffee / carriage forces in real time.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Coffee-Spill Elevator

Imagine you are standing inside an elevator holding a full cup of hot coffee filled to the very brim:

1. **Position `x` (Where you are):** Which floor you are on.
2. **Velocity `v` (How fast you move):** At a steady cruising speed of 3 m/s, the coffee stays completely flat. Velocity creates no extra force.
3. **Acceleration `a` (Rate of speed change):** When the elevator speeds up, your knees feel heavier. The coffee presses down into the cup with force `F = m·a`. Steady acceleration keeps the surface level.
4. **Jerk `j` (Rate of acceleration change):** If the motor instantly slams full voltage in 0 milliseconds, the floor violently jerks upward. The sudden jump in force sloshes boiling coffee all over your hand!

<div style="text-align: center; margin: 20px 0;">
  <svg width="320" height="150" viewBox="0 0 320 150" style="max-width: 100%; height: auto;">
    <!-- S-Curve -->
    <path d="M 30 110 C 60 110 70 40 110 40 L 130 40" fill="none" stroke="#4ade80" stroke-width="3" />
    <text x="30" y="25" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="11">Smooth S-Curve (Bounded Jerk)</text>
    
    <!-- Instant Step -->
    <path d="M 190 110 L 190 40 L 290 40" fill="none" stroke="#f43f5e" stroke-width="3" />
    <text x="190" y="25" fill="#f43f5e" font-family="sans-serif" font-weight="bold" font-size="11">Instant Step (Infinite Jerk)</text>
    <text x="190" y="135" fill="#f43f5e" font-family="sans-serif" font-size="10">Snaps chains & strips gears!</text>
  </svg>
</div>

---

## 2. Solving It in Code: S-Curve Smoothing

To protect mechanical chains and gearboxes, software bounds the maximum **Jerk** (`j_max`), producing a smooth "S-shaped" velocity curve:

```python
def generate_scurve_step(t, total_time, distance):
    """
    Smoothly ramps position, velocity, and acceleration using a bounded jerk curve.
    """
    p = min(1.0, max(0.0, t / total_time))
    
    # 5th-order smooth polynomial (zero jerk at endpoints)
    smooth_fraction = 10*(p**3) - 15*(p**4) + 6*(p**5)
    
    current_position = distance * smooth_fraction
    return current_position

# Calculate elevator position at 0.5 seconds into a 2.0-second move
x = generate_scurve_step(t=0.5, total_time=2.0, distance=2.0)
print(f"Elevator height at 0.5s: {x:.3f} meters")  # 0.206m (gentle start)
```

---

> 💡 **Math Sidebar: The Hierarchy of Motion Derivatives**
>
> In physics and calculus, each concept is the derivative (rate of change) of the previous one:
>
> ```
>    Position:     x(t)          (meters)
>    Velocity:     v(t) = dx/dt  (meters per second)
>    Acceleration: a(t) = dv/dt  (meters per second squared)
>    Jerk:         j(t) = da/dt  (meters per second cubed)
> ```
>
> **Why Infinite Jerk Breaks Mechanisms:**
> By Newton's second law, `Force = mass · acceleration` (`F = m·a`). An instantaneous step in acceleration requires an instantaneous change in mechanical force, producing shockwaves that shear gear teeth.

---

## 3. Review Checkpoints

### Checkpoint 1
A robot elevator's velocity is given by `v(t) = 3·t²`.
What is the acceleration `a(t)` at `t = 2.0` seconds?

**Solution:**
1. Differentiate velocity: `a(t) = dv/dt = 6·t`.
2. Evaluate at `t = 2.0`: `a(2.0) = 6(2.0) = 12.0 m/s²`.

---

### Checkpoint 2
Why do modern FRC elevator feedforward controllers include `kA · a`?

**Solution:**
Because accelerating a heavy mechanism requires extra motor voltage (`F = m·a`). Providing voltage proportionally to target acceleration (`kA · a`) cancels out inertia and eliminates lag.
