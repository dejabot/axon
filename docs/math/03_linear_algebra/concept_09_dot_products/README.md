# Concept 09: Dot Products, Projections & Alignment

> **▶ Interactive Demo: [Dot Product & Projection Visualizer](demo.html)**
>
> Open the interactive demo below to rotate two vector arrows and see their dot product, angle $\theta$, and projected shadow update live.

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

## 2. Solving It in Code: The Dot Product
To compute how aligned two vectors are, we multiply matching components and add them up:

```python
def dot_product(v1, v2):
    """Computes the dot product of two vectors."""
    return v1[0] * v2[0] + v1[1] * v2[1]

# Path direction and actual robot velocity
path_dir = [1.0, 0.0]
robot_vel = [2.0, 1.5]

# Calculate forward progress along path
forward_progress = dot_product(path_dir, robot_vel)

print(f"Forward progress along path: {forward_progress:.2f} m/s")  # 2.00 m/s
```

---

> 💡 **Math Sidebar: The Dot Product Formula**
>
> In linear algebra, the dot product between vectors `u` and `v` is written as:
>
> ```
>    u · v = u_x · v_x + u_y · v_y = ||u|| · ||v|| · cos(θ)
> ```
>
> **How to interpret the result:**
> * **`u · v > 0` (Positive):** The vectors point generally in the same direction (`θ < 90°`).
> * **`u · v = 0` (Zero):** The vectors are strictly **perpendicular / orthogonal** (`θ = 90°`). Zero progress is made along `u`!
> * **`u · v < 0` (Negative):** The vectors point in opposite directions (`θ > 90°`). The robot is driving backward relative to the path.

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
  <div><a href="../concept_08_vectors_scaling/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 08: Vectors & Scaling</a></div>
  <div><a href="../README.md" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 3 Overview</a></div>
  <div><a href="../concept_10_matrices_transforms/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 10: Matrix Transformations →</a></div>
</div>
