# Concept 01: Rates of Change & Derivatives

> **▶ Interactive Demo: [Rate of Change & Derivative Visualizer](demo.html)**
>
> Open the interactive demo below to shrink the time step dt and watch the average speed converge into the exact instantaneous tangent slope.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: How Fast Are We Moving?
A robot's wheel encoder does not measure velocity directly. It only reports how many rotations (or meters) the wheel has turned.

Every 20 milliseconds (`dt = 0.02s`), the robot's control loop reads the position:
* At `t = 1.00s`: Position `x₁ = 2.00 meters`.
* At `t = 1.02s`: Position `x₂ = 2.08 meters`.

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="160" viewBox="0 0 300 160" style="max-width: 100%; height: auto;">
    <!-- Curve -->
    <path d="M 30 130 Q 150 120 270 30" fill="none" stroke="#38bdf8" stroke-width="3" />
    <!-- Secant Line -->
    <line x1="100" y1="120" x2="200" y2="75" stroke="#fbbf24" stroke-width="2.5" />
    <circle cx="100" cy="120" r="4" fill="#fbbf24" />
    <circle cx="200" cy="75" r="4" fill="#fbbf24" />
    <text x="110" y="140" fill="#94a3b8" font-family="sans-serif" font-size="11">Δt = 0.02s</text>
    <text x="210" y="80" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="11">Slope = Δx / Δt</text>
  </svg>
</div>

To find the robot's speed, we calculate the **rate of change**:

```
   Speed = (Distance Traveled) / (Time Taken) = (2.08 - 2.00) / 0.02 = 4.0 meters per second
```

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java: Numerical Derivative
```java
// Sensor position readings (meters) at two timestamps
double x1 = 3.00, t1 = 1.00;
double x2 = 3.42, t2 = 1.05;

// Finite difference derivative: v = dx / dt
double dt = t2 - t1; // 0.05 seconds
double velocity = (x2 - x1) / dt; // 0.42 / 0.05 = 8.40 m/s

System.out.printf("Instantaneous Velocity: %.2f m/s%n", velocity);
```

---

## 3. Bridge to Machine Learning: The Loss Slope
In machine learning:
* When training a model, we measure how much the prediction error changes when a weight `w` is tweaked slightly:
  ```
  Slope = dLoss / dw
  ```
* If the derivative is positive, increasing `w` increases error (bad!). If the derivative is negative, increasing `w` decreases error (good!).

---

## 4. Review Checkpoints
### Checkpoint 1
An encoder reports `x = 5.0m` at `t = 2.0s`, and `x = 5.15m` at `t = 2.05s`.
What is the average velocity over this interval?

**Solution:**
`v = Δx / Δt = (5.15 - 5.0) / (2.05 - 2.0) = 0.15 / 0.05 = 3.0 m/s`.

---

### Checkpoint 2
If a robot's position curve is flat (horizontal line, `x(t) = 3.0m` constant), what is its velocity derivative `dx/dt`?

**Solution:**
Because position is not changing (`dx = 0`), the slope is zero: `v = dx/dt = 0 m/s` (The robot is stationary).

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../../03_linear_algebra/04_concept_determinants_inverses/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 11: Determinants & Inverses</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 4 Overview</a></div>
  <div><a href="../02_concept_acceleration_jerk/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 13: Acceleration & Jerk →</a></div>
</div>
