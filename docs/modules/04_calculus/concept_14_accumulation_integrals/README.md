# Concept 14: Accumulation, Area & Numerical Integration

> **▶ Interactive Demo: [Numerical Integration Visualizer](demo.html)**
>
> Open the interactive demo below to compare Euler rectangles vs. Trapezoidal slices and see how Trapezoidal integration drastically cuts odometry drift.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Where Did the Robot Go?
During the 15-second autonomous period, your robot's wheel encoders measure velocity every 20 milliseconds (`dt = 0.02s`).

How does the robot calculate its total distance traveled from a sequence of velocity readings?

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="150" viewBox="0 0 300 150" style="max-width: 100%; height: auto;">
    <!-- Slices -->
    <rect x="50" y="80" width="30" height="40" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="1.5" />
    <polygon points="120,120 120,70 150,40 150,120" fill="rgba(74, 222, 128, 0.25)" stroke="#4ade80" stroke-width="1.5" />
    <!-- Velocity Curve -->
    <path d="M 30 110 Q 150 20 270 110" fill="none" stroke="#38bdf8" stroke-width="3" />
    
    <text x="40" y="70" fill="#f43f5e" font-family="sans-serif" font-size="10">Euler: Rectangles</text>
    <text x="120" y="30" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="10">Trapezoid: Exact</text>
    <line x1="20" y1="120" x2="280" y2="120" stroke="#334155" stroke-width="1.5" />
  </svg>
</div>

Distance is the **Accumulation of Speed over Time**:
* In each small slice `dt`, distance traveled is `speed · dt`.
* Total distance is the **Area Under the Velocity Curve**!

---

## 2. Solving It in Code: Euler vs. Trapezoid
### 1. Forward Euler (Naive)
Assumes speed is constant across the entire 20ms slice:
```python
x = x + v * dt
```
* Underestimates position whenever the robot is accelerating.

### 2. Trapezoidal Integration (Smart)
Averages the speed at the start and end of the slice:
```python
x = x + 0.5 * (v_start + v_end) * dt
```

```python
def compare_integrators(acceleration=2.0, total_time=1.0, dt=0.05):
    """
    Compares Euler vs Trapezoidal integration against exact calculus.
    """
    steps = int(total_time / dt)
    
    # 1. Exact Calculus: x = 0.5 * a * t^2
    true_x = 0.5 * acceleration * (total_time ** 2)
    
    # 2. Forward Euler
    x_euler, v_euler = 0.0, 0.0
    for _ in range(steps):
        x_euler += v_euler * dt
        v_euler += acceleration * dt
        
    # 3. Trapezoidal (Heun's method)
    x_trap, v_trap = 0.0, 0.0
    for _ in range(steps):
        v_next = v_trap + acceleration * dt
        x_trap += 0.5 * (v_trap + v_next) * dt
        v_trap = v_next
        
    print(f"True Distance (Calculus) : {true_x:.3f} m")
    print(f"Euler Distance (Naive)   : {x_euler:.3f} m (Error: {abs(true_x - x_euler)*1000:.1f} mm)")
    print(f"Trapezoid Distance       : {x_trap:.3f} m (Error: {abs(true_x - x_trap)*1000:.1f} mm)")

compare_integrators(acceleration=2.0, total_time=1.0, dt=0.05)
```

---

> 💡 **Math Sidebar: Definite Integration**
>
> In calculus, accumulating continuous slices is written with the integral symbol `∫` (a stretched-out "S" for Sum):
>
> ```
>    x(t) = ∫ v(τ) dτ
> ```
>
> **How to read this equation out loud:**
> *"Distance is the sum of all tiny velocity slices `v(t)·dt` accumulated from time 0 to time t."*
> Integration and Differentiation are exact inverses (The Fundamental Theorem of Calculus).

---

## 3. Review Checkpoints
### Checkpoint 1
A robot drives at a constant speed of `2.5 m/s` for `3.0` seconds. What is the area under its velocity curve?

**Solution:**
Since speed is constant, the area is a simple rectangle: `Area = width · height = (3.0 s) · (2.5 m/s) = 7.5 meters`.

---

### Checkpoint 2
Why does Trapezoidal integration produce zero error under constant acceleration?

**Solution:**
Because under constant acceleration, velocity is a straight line ($v = a\cdot t$). The area under a straight line is an exact trapezoid, which the trapezoid formula calculates perfectly!
