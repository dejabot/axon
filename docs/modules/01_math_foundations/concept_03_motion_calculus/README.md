# Concept 03: Single-Variable Motion Calculus & Jerk

```
       Module 1: Math Foundations  ➔  Concept 03: Motion Calculus & Jerk
```

> **▶ Interactive Demo: [Single-Variable Motion Calculus & Jerk Visualizer](demo.html)**
>
> Open the visualizer in your browser or explore the embedded frame below to observe higher-order derivatives of motion and compare S-Curve smoothing against destructive step profiles.

<iframe src="demo.html" width="100%" height="560" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--code-bg, #0a0d14);"></iframe>

---

## 1. Intuitive Mental Model: The Elevator & The Cup of Coffee

Imagine you are standing inside an elevator holding a full cup of hot coffee filled to the very brim.

1. **Position `x` (Where you are):** The elevator is on the 1st floor (`x = 0m`) or the 5th floor (`x = 15m`).
2. **Velocity `v` (How fast position is changing):** If the elevator travels upward at a steady speed of 5 meters per second, the coffee remains completely calm and flat. Velocity alone creates no extra forces on your body.
3. **Acceleration `a` (How fast velocity is changing):** When the elevator speeds up from rest, your knees feel heavier. The coffee level pushes down into the cup with extra force `F = m·a`. As long as the acceleration is steady, the liquid surface stays level.
4. **Jerk `j` (How fast acceleration is changing):** What happens if the motor instantly snaps from 0 to full acceleration in zero milliseconds? The elevator violently jerks your body. The sudden, instantaneous leap in force splashes boiling coffee all over your hand!

<div style="text-align: center; margin: 20px 0;">
  <svg width="320" height="150" viewBox="0 0 320 150" style="max-width: 100%; height: auto;">
    <!-- S-Curve (Smooth) -->
    <path d="M 30 110 C 60 110 70 40 110 40 L 130 40" fill="none" stroke="#4ade80" stroke-width="3" />
    <text x="30" y="25" fill="#4ade80" font-family="monospace" font-weight="bold" font-size="11">Smooth S-Curve (Bounded Jerk)</text>
    <text x="30" y="135" fill="#94a3b8" font-family="monospace" font-size="10">Gentle force buildup</text>
    
    <!-- Step (Infinite Jerk) -->
    <path d="M 190 110 L 190 40 L 290 40" fill="none" stroke="#f43f5e" stroke-width="3" />
    <text x="190" y="25" fill="#f43f5e" font-family="monospace" font-weight="bold" font-size="11">Instant Step (Infinite Jerk)</text>
    <text x="190" y="135" fill="#f43f5e" font-family="monospace" font-size="10">Impulse shock: snaps chains!</text>
  </svg>
</div>

---

## 2. The Chain of Derivatives

Calculus is simply the mathematics of measuring these continuous rates of change:

```
   Position:     x(t)          (meters)
   Velocity:     v(t) = dx/dt  (meters per second)
   Acceleration: a(t) = dv/dt  (meters per second squared)
   Jerk:         j(t) = da/dt  (meters per second cubed)
```

### Why "Infinite Jerk" Destroys Hardware
By Newton's second law, `Force = mass · acceleration` (`F = m·a`).

* If acceleration jumps from `0` to `+a_max` in zero seconds (`Δt = 0`), the rate of change of force is infinite:
  ```
  jerk = Δa / Δt = a_max / 0 = ∞
  ```
* In the real physical world, applying an instantaneous torque step stretches timing belts, strips aluminum gearbox teeth, and causes robot elevator masts to oscillate violently.

### S-Curve Profiles: The Engineering Fix
Instead of jumping acceleration instantly, an **S-Curve Profile** ramps acceleration up and down smoothly at a constant jerk limit `j_max`. The velocity curve forms a smooth "S" shape, eliminating mechanical shock.

---

## 3. Discrete Numerical Integration in Robot Control Loops

A robot's onboard microcontroller (e.g. roboRIO) runs a control loop once every `dt = 0.020` seconds (20 milliseconds, 50 Hz). 

How do we calculate where the robot is from sensor acceleration and velocity measurements?

### 1. Forward Euler Integration (Naive)
Assumes velocity stays constant during the 20ms step:
```python
x = x + v * dt
v = v + a * dt
```
* **Flaw:** During acceleration, it underestimates the distance traveled because it uses the old velocity from the beginning of the step.

### 2. Trapezoidal Integration (Accurate)
Averages the velocity at the start and end of the time step:
```python
v_next = v + a * dt
x = x + 0.5 * (v + v_next) * dt
v = v_next
```
* **Benefit:** Captures quadratic motion curves exactly, drastically reducing numerical drift in odometry!

---

## 4. Python Implementation

Here is a side-by-side comparison of Forward Euler vs. Trapezoidal integration in pure Python:

```python
def simulate_motion(accel, duration, dt=0.02):
    """
    Compares Forward Euler vs Trapezoidal integration
    for a robot accelerating at a constant rate.
    """
    steps = int(duration / dt)
    
    # 1. Exact Ground Truth (Analytical calculus: x = 0.5 * a * t^2)
    x_true = 0.5 * accel * (duration ** 2)
    
    # 2. Forward Euler Integration
    x_euler, v_euler = 0.0, 0.0
    for _ in range(steps):
        x_euler += v_euler * dt
        v_euler += accel * dt
        
    # 3. Trapezoidal Integration
    x_trap, v_trap = 0.0, 0.0
    for _ in range(steps):
        v_next = v_trap + accel * dt
        x_trap += 0.5 * (v_trap + v_next) * dt
        v_trap = v_next
        
    print(f"True Position (Calculus) : {x_true:.4f} m")
    print(f"Euler Position (dt=20ms) : {x_euler:.4f} m  (Error: {abs(x_true - x_euler)*1000:.1f} mm)")
    print(f"Trapezoid Position       : {x_trap:.4f} m  (Error: {abs(x_true - x_trap)*1000:.1f} mm)")

# Run simulation: Accelerate at 3 m/s² for 1.0 second
simulate_motion(accel=3.0, duration=1.0)
```

---

## 5. Review Questions

### Question 1
A robot elevator is commanded to move with constant acceleration `a = 4.0 m/s²` for `2.0` seconds.
1. What is the final velocity `v` after 2.0 seconds?
2. What is the total distance `x` traveled?

**Answer:**
1. `v = a · t = 4.0 · 2.0 = 8.0 m/s`
2. `x = (1/2) · a · t² = 0.5 · 4.0 · (2.0)² = 0.5 · 4.0 · 4.0 = 8.0 meters`.

---

### Question 2
Why does Forward Euler integration always lag behind the true position during acceleration?

**Answer:**
Because Forward Euler computes displacement using the velocity at the **start** of the interval (`x_new = x + v_start · dt`), ignoring the fact that the robot was speeding up throughout the interval. Trapezoidal integration fixes this by averaging `(v_start + v_end) / 2`.
