# Concept 11: Determinants, Inverses & Singularity

> **▶ Interactive Demo: [Determinant & Singularity Sandbox](demo.html)**
>
> Open the interactive demo below to squash the 2D plane down to a 1D line and observe when a matrix becomes singular (`det = 0`) and loses its inverse.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Running the Movie Backward
Suppose your robot's swerve drive kinematics software uses a matrix `A` to convert robot velocities `[vx, vy]` into wheel motor speeds:

```
   wheel_speeds = A · robot_velocity
```

During autonomous navigation, the problem is reversed:
> *"The wheel encoders tell us the 4 wheel speeds. How fast is the robot moving across the field?"*

To solve for `robot_velocity`, the software must compute the **Matrix Inverse** (`A⁻¹`):

```
   robot_velocity = A⁻¹ · wheel_speeds
```

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="150" viewBox="0 0 300 150" style="max-width: 100%; height: auto;">
    <!-- Non-singular 2D square -->
    <polygon points="30,110 80,110 110,60 60,60" fill="rgba(74, 222, 128, 0.2)" stroke="#4ade80" stroke-width="2" />
    <text x="35" y="130" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="11">det > 0 (Invertible 2D)</text>
    
    <!-- Singular 1D line -->
    <line x1="180" y1="110" x2="270" y2="60" stroke="#f43f5e" stroke-width="3" />
    <text x="180" y="130" fill="#f43f5e" font-family="sans-serif" font-weight="bold" font-size="11">det = 0 (Singular 1D Line)</text>
  </svg>
</div>

What happens if the matrix squashes 2D space down into a single 1D line? You lose information—it is impossible to reconstruct the original 2D speeds, and the software crashes with **Division by Zero**!

---

## 2. Solving It in Code
In Python, we compute the determinant `det` first to verify that the matrix is safe to invert:

```python
def invert_2x2_matrix(A):
    """
    Computes the inverse of a 2x2 matrix [[a, b], [c, d]].
    """
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    
    # 1. Calculate the Determinant (Area scaling factor)
    det = a * d - b * c
    
    # 2. Check for Singularity (Cannot invert if det is zero!)
    if abs(det) < 1e-6:
        raise ValueError("Matrix is Singular (det=0)! Inverse does not exist.")
        
    # 3. Swap diagonal, negate off-diagonal, and divide by det
    return [
        [ d / det, -b / det],
        [-c / det,  a / det]
    ]

# Example: Inverting a scaling matrix
matrix_A = [[2.0, 0.0], [0.0, 4.0]]
inv_A = invert_2x2_matrix(matrix_A)

print(f"Inverse Matrix: {inv_A}")  # [[0.5, 0.0], [0.0, 0.25]]
```

---

> 💡 **Math Sidebar: Determinant & Inverse**
>
> * **Determinant (`det A`):** Measures how much the matrix stretches or shrinks 2D areas:
>   ```
>      det(A) = a·d - b·c
>   ```
> * **The Inverse Matrix (`A⁻¹`):** The undo button that reverses the transformation:
>   ```
>      A⁻¹ = (1 / det(A)) · [  d   -b ]
>                           [ -c    a ]
>   ```
> * **Singular Matrix:** If `det(A) = 0`, `1 / det` divides by zero. The matrix has no inverse.

---

## 3. Bridge to Machine Learning: Linear Regression
In machine learning:
* When fitting a straight line through data points (Linear Regression), the AI solves the famous **Normal Equation**:
  ```
  weights = (Xᵀ · X)⁻¹ · Xᵀ · y
  ```
* If two features in the dataset are identical, `Xᵀ · X` becomes singular (`det = 0`). Machine learning libraries use **Pseudo-Inverses (SVD)** to gracefully handle these singular cases without crashing!

---

## 4. Review Checkpoints
### Checkpoint 1
Matrix `A = [[3, 1], [6, 2]]`.
1. Compute `det(A)`.
2. Can this matrix be inverted?

**Solution:**
1. `det(A) = (3)(2) - (1)(6) = 6 - 6 = 0.0`.
2. **No.** The determinant is zero (singular), so its inverse does not exist.

---

### Checkpoint 2
If a transformation matrix has `det(A) = -1.0`, what physical effect did it have on the coordinate grid?

**Solution:**
A negative determinant means the grid was **reflected** (flipped inside out, like looking into a mirror).

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_10_matrices_transforms/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 10: Matrix Transformations</a></div>
  <div><a href="../README.md" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 3 Overview</a></div>
  <div><a href="../04_calculus/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 4: Calculus →</a></div>
</div>
