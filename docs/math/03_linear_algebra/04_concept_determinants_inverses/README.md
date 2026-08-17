# Concept 04: Determinants, Inverses & Singularity

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

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java: 2x2 Matrix Inversion
```java
// Matrix M = [[a, b], [c, d]]
double a = 2.0, b = 1.0;
double c = 1.0, d = 3.0;

// 1. Calculate Determinant: det(M) = a*d - b*c
double det = a * d - b * c; // 2*3 - 1*1 = 5.0

if (Math.abs(det) < 1e-9) {
    throw new IllegalArgumentException("Matrix is singular (cannot be inverted)!");
}

// 2. Invert Matrix: M^(-1) = (1/det) * [[d, -b], [-c, a]]
double invA =  d / det;
double invB = -b / det;
double invC = -c / det;
double invD =  a / det;

System.out.printf("Inverse Matrix: [[%.2f, %.2f], [%.2f, %.2f]]%n", invA, invB, invC, invD);
```

### Production WPILib Matrix
```java
import edu.wpi.first.math.Matrix;
import edu.wpi.first.math.Nat;
import edu.wpi.first.math.numbers.*;

// WPILib Matrix types: Matrix<Rows, Cols>
Matrix<N2, N2> mat = new Matrix<>(Nat.N2(), Nat.N2());
mat.set(0, 0, 2.0); mat.set(0, 1, 1.0);
mat.set(1, 0, 1.0); mat.set(1, 1, 3.0);

Matrix<N2, N2> inv = mat.inv(); // Invert matrix
double det = mat.det();          // Compute determinant
```

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
  <div><a href="../03_concept_matrices_transforms/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 10: Matrix Transformations</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 3 Overview</a></div>
  <div><a href="../../04_calculus/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 4: Calculus →</a></div>
</div>
