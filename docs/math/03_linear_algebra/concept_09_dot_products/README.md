# Concept 09: Dot Products, Projections & Alignment

> **▶ Interactive Demo: [Dot Product & Projection Visualizer](demo.html)**
>
> Open the interactive demo below to rotate two vector arrows and see their dot product, angle \θ, and projected shadow update live.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Are We Driving on Path?
Imagine your robot is following an autonomous path pointing straight down the field:
* **Desired Path Direction:** `u = [1.0, 0.0]` (Straight East).
* **Actual Robot Velocity:** `v = [2.0, 1.5]` (Moving at an angle due to wheel slip).

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="170" viewBox="0 0 300 170" style="max-width: 100%; height: auto;">
    <!-- Desired Path u -->
    <line x1="30" y1="120" x2="220" y2="120" stroke="#38bdf8" stroke-width="3" />
    <text x="140" y="140" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="11">Desired Path u</text>
    
    <!-- Actual Velocity v -->
    <line x1="30" y1="120" x2="190" y2="40" stroke="#fbbf24" stroke-width="3" />
    <text x="110" y="70" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="11">Actual Velocity v</text>
    
    <!-- Shadow projection -->
    <line x1="190" y1="40" x2="190" y2="120" stroke="#4ade80" stroke-width="2" stroke-dasharray="3,3" />
    <line x1="30" y1="120" x2="190" y2="120" stroke="#4ade80" stroke-width="3" />
    <text x="50" y="105" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="11">Projected Progress</text>
  </svg>
</div>

The path-following software needs to know:
1. **How much speed is driving along the path?** (Forward progress).
2. **How much speed is pushing off-course?** (Cross-track error).

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java
Calculating dot product, magnitudes, and directional alignment:

```java
// Vector A: Robot Heading Vector (Facing 45 degrees)
double ax = 1.0, ay = 1.0;

// Vector B: Target Line-of-Sight Vector
double bx = 3.0, by = 1.0;

// 1. Compute Dot Product: A · B = ax*bx + ay*by
double dotProduct = ax * bx + ay * by; // 1*3 + 1*1 = 4.0

// 2. Compute Magnitudes
double magA = Math.hypot(ax, ay); // 1.414
double magB = Math.hypot(bx, by); // 3.162

// 3. Cosine of the angle between them: cos(θ) = (A · B) / (|A| * |B|)
double cosTheta = dotProduct / (magA * magB);
double angleDegrees = Math.toDegrees(Math.acos(cosTheta));

System.out.printf("Alignment Angle: %.1f degrees%n", angleDegrees);
```

### Production WPILib Equivalent
```java
import edu.wpi.first.math.geometry.Translation2d;

Translation2d heading = new Translation2d(1.0, 1.0);
Translation2d targetDir = new Translation2d(3.0, 1.0);

// Angle between vectors using WPILib Rotation2d
double angleDiff = heading.getAngle().minus(targetDir.getAngle()).getDegrees();
```

---

## 3. Bridge to Machine Learning: Cosine Similarity
In modern AI search engines and RAG (Retrieval-Augmented Generation):
* When you ask a question to an AI, the question is converted into a vector `q`.
* Every document in the database is stored as a vector `d`.
* The AI computes the **Cosine Similarity**:
  ```
  Similarity = (q · d) / (||q|| · ||d||)
  ```
* The document with the highest dot product is the most relevant answer!

---

## 4. Review Checkpoints
### Checkpoint 1
Vector `u = [3.0, 4.0]` and vector `v = [-4.0, 3.0]`.
Compute `u · v`. What is the angle between them?

**Solution:**
1. `u · v = (3.0)(-4.0) + (4.0)(3.0) = -12.0 + 12.0 = 0.0`.
2. Because the dot product is `0.0`, the angle between them is exactly **`90°` (Perpendicular)**.

---

### Checkpoint 2
A robot applies a force vector `F = [10.0, 0.0]` Newtons while driving along displacement vector `d = [5.0, 2.0]` meters. How much mechanical work was done?

**Solution:**
In physics, `Work = Force · displacement = (10.0)(5.0) + (0.0)(2.0) = 50.0 Joules`.
The vertical displacement `2.0m` did zero work because it was perpendicular to the force.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_08_vectors_scaling/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 08: Vectors & Scaling</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 3 Overview</a></div>
  <div><a href="../concept_10_matrices_transforms/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 10: Matrix Transformations →</a></div>
</div>
