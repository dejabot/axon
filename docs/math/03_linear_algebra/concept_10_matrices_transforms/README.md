# Concept 10: Matrices as Coordinate Transformers

> **▶ Interactive Demo: [2D Grid Transformation Visualizer](demo.html)**
>
> Open the interactive demo below to drag the landing spots of basis steps **î'** and **ĵ'** and see the entire coordinate grid transform in real time.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Field-Centric Robot Driving
In FRC autonomous and teleop driving, the driver pushes the joystick "Forward" relative to the field.

However, if the robot is currently rotated by heading angle `θ`:
* The robot's "Forward" is facing in direction `[cos(θ), sin(θ)]`.
* The robot's "Left" is facing in direction `[-sin(θ), cos(θ)]`.

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="170" viewBox="0 0 300 170" style="max-width: 100%; height: auto;">
    <!-- Field Grid Axes -->
    <line x1="30" y1="130" x2="270" y2="130" stroke="#334155" stroke-width="1.5" />
    <line x1="30" y1="130" x2="30" y2="20" stroke="#334155" stroke-width="1.5" />
    
    <!-- Rotated Basis î' and ĵ' -->
    <line x1="30" y1="130" x2="130" y2="90" stroke="#4ade80" stroke-width="3" />
    <text x="135" y="95" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="11">î' (New East)</text>
    
    <line x1="30" y1="130" x2="70" y2="30" stroke="#f43f5e" stroke-width="3" />
    <text x="75" y="35" fill="#f43f5e" font-family="sans-serif" font-weight="bold" font-size="11">ĵ' (New North)</text>
  </svg>
</div>

How does the chassis controller translate the driver's field command `[v_field_x, v_field_y]` into local wheel motor voltages?

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java: 2D Rotation Matrix
```java
// Point (x, y) = (2.0, 1.0)
double px = 2.0;
double py = 1.0;
double theta = Math.toRadians(90.0); // 90 degree rotation

// 2x2 Rotation Matrix Transformation:
// [ x_new ] = [ cos -sin ] [ px ]
// [ y_new ]   [ sin  cos ] [ py ]
double newX = Math.cos(theta) * px - Math.sin(theta) * py; // 0*2 - 1*1 = -1.0
double newY = Math.sin(theta) * px + Math.cos(theta) * py; // 1*2 + 0*1 =  2.0

System.out.printf("Rotated Vector: (%.2f, %.2f)%n", newX, newY);
```

### Production WPILib Equivalent
```java
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.math.geometry.Translation2d;

Translation2d point = new Translation2d(2.0, 1.0);
Translation2d rotated = point.rotateBy(Rotation2d.fromDegrees(90.0));
// Output: (-1.0, 2.0)
```

---

## 3. Bridge to Machine Learning: Dense Neural Layers
In deep neural networks (like ChatGPT or image classifiers):
* Every standard layer is a **Matrix Multiplication**:
  ```
  y = W · x + b
  ```
* The weight matrix `W` rotates and stretches the input numbers `x` into a new coordinate space where patterns (like cat ears or stop signs) become easy to classify!

---

## 4. Review Checkpoints
### Checkpoint 1
Suppose matrix `A` has columns `[2, 0]` and `[0, 3]`.
What is the result of `A · [1, 1]`?

**Solution:**
`[ 2(1) + 0(1), 0(1) + 3(1) ] = [2, 3]`.
The horizontal dimension was scaled by 2, and the vertical by 3.

---

### Checkpoint 2
What matrix leaves every vector completely unchanged?

**Solution:**
The **Identity Matrix `I`**:
`[ [1, 0], [0, 1] ]`. Where `î` lands at `[1, 0]` and `ĵ` lands at `[0, 1]`.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_09_dot_products/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 09: Dot Products & Projections</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 3 Overview</a></div>
  <div><a href="../concept_11_determinants_inverses/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 11: Determinants & Inverses →</a></div>
</div>
