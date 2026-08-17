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

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java: Trapezoidal Integration (Dead Reckoning)
```java
// Accumulate robot distance over time steps
double totalPosition = 0.0;
double dt = 0.020; // 20ms control loop

double[] velocityStream = {0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 2.0, 1.0, 0.0};

for (int i = 1; i < velocityStream.length; i++) {
    double vPrev = velocityStream[i - 1];
    double vCur = velocityStream[i];
    
    // Trapezoidal rule: Area = 0.5 * (vPrev + vCur) * dt
    double stepDistance = 0.5 * (vPrev + vCur) * dt;
    totalPosition += stepDistance;
}

System.out.printf("Integrated Odometer Distance: %.4f meters%n", totalPosition);
```

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
Because under constant acceleration, velocity is a straight line (v = a * t). The area under a straight line is an exact trapezoid, which the trapezoid formula calculates perfectly!

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_13_acceleration_jerk/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 13: Acceleration & Jerk</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 4 Overview</a></div>
  <div><a href="../concept_15_gradients_multivariable/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 15: Gradients & Optimization →</a></div>
</div>
