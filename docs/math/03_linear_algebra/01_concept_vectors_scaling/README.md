# Concept 01: Vectors, Displacements & Scalar Scaling

> **▶ Interactive Demo: [Vector Addition & Scaling Sandbox](demo.html)**
>
> Open the interactive demo below to drag vector arrows **A** and **B**, adjust the scalar multiplier slider, and see head-to-tail vector addition live.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Combining Robot Moves
Suppose an autonomous robot performs two sequential driving steps:
1. **Move A:** Drive 2 meters East and 1 meter North (`[2.0, 1.0]`).
2. **Move B:** Drive 1 meter East and 2 meters North (`[1.0, 2.0]`).

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="170" viewBox="0 0 300 170" style="max-width: 100%; height: auto;">
    <!-- Vector A -->
    <line x1="30" y1="140" x2="150" y2="100" stroke="#38bdf8" stroke-width="3" />
    <circle cx="150" cy="100" r="4" fill="#38bdf8" />
    <text x="80" y="115" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="11">Move A [2, 1]</text>
    
    <!-- Vector B -->
    <line x1="150" y1="100" x2="210" y2="20" stroke="#4ade80" stroke-width="3" />
    <circle cx="210" cy="20" r="4" fill="#4ade80" />
    <text x="185" y="65" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="11">Move B [1, 2]</text>
    
    <!-- Sum Vector C -->
    <line x1="30" y1="140" x2="210" y2="20" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="4,4" />
    <text x="100" y="60" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="12">Total [3, 3]</text>
  </svg>
</div>

Where does the robot end up overall? 
You simply place the tail of Move B at the tip of Move A (**Head-to-Tail addition**). The net result is:
* Total X = `2.0 + 1.0 = 3.0 meters`
* Total Y = `1.0 + 2.0 = 3.0 meters`

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java
Vector addition and scalar scaling:

```java
// Robot starting velocity vector (vx, vy)
double v1x = 2.0;
double v1y = 1.0;

// Acceleration boost vector
double ax = 1.5;
double ay = 2.0;
double dt = 0.5; // half second

// v_new = v1 + a * dt
double vNewX = v1x + ax * dt; // 2.0 + 0.75 = 2.75 m/s
double vNewY = v1y + ay * dt; // 1.0 + 1.00 = 2.00 m/s

System.out.printf("New Velocity: (%.2f, %.2f) m/s%n", vNewX, vNewY);
```

### Production WPILib Equivalent
In WPILib, `Translation2d` supports vector arithmetic:

```java
import edu.wpi.first.math.geometry.Translation2d;

Translation2d velocity = new Translation2d(2.0, 1.0);
Translation2d acceleration = new Translation2d(1.5, 2.0);

Translation2d newVelocity = velocity.plus(acceleration.times(0.5));
```

---

## 3. Bridge to Machine Learning: Word Embeddings
In natural language processing AI (like Word2Vec and ChatGPT):
* Every word is represented as a list of numbers (a vector in 1536-dimensional space).
* Because concepts are vectors, the AI can perform vector arithmetic on meanings:
  ```
  Vector("King") - Vector("Man") + Vector("Woman") ≈ Vector("Queen")
  ```

---

## 4. Review Checkpoints
### Checkpoint 1
You have vector `A = [4.0, -2.0]` and vector `B = [-1.0, 5.0]`.
Compute `A + B`.

**Solution:**
`[4.0 + (-1.0), -2.0 + 5.0] = [3.0, 3.0]`.

---

### Checkpoint 2
A robot's velocity vector is `v = [2.0, 4.0]` m/s. The driver hits the "Turbo" button, scaling velocity by `1.5x`. What is the new velocity vector?

**Solution:**
`v_turbo = [2.0 · 1.5, 4.0 · 1.5] = [3.0, 6.0] m/s`.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../../02_trigonometry/06_concept_3d_rotations_quaternions/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 07: 3D Quaternions</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 3 Overview</a></div>
  <div><a href="../02_concept_dot_products/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 09: Dot Products & Projections →</a></div>
</div>
