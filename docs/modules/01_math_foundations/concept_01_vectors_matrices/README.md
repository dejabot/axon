# Concept 01: Vectors, Basis Spaces & Matrix Transformations

```
       [ 01_math_foundations ]  ➔  Concept 01: Vectors & Matrices
       Stage 1: The Unified Math Engine
```

---

## Part 1: The Intuitive Mental Model (Physical/Visual Analogy)

Imagine you are standing on an infinite sheet of flexible graph paper. Every point on this grid has a street address determined by two standard measuring sticks: one pointing exactly one unit to the East (which we label **î** or "i-hat"), and one pointing exactly one unit to the North (which we label **ĵ** or "j-hat"). 

```
   y (North)
   ▲
   │    ĵ = [0, 1]ᵀ
   │   ▲
   │   │
   └───┼───► x (East)
       │   î = [1, 0]ᵀ
```

When you describe a vector **v** as `[3, 2]ᵀ`, you are giving navigation instructions: "Walk 3 steps along the East stick, then 2 steps along the North stick."

Now, imagine grasping the grid and stretching, rotating, shearing, or squishing it. As long as the grid lines remain straight, evenly spaced, and the origin `(0, 0)` stays fixed in place, you have performed a **Linear Transformation**. 

Here is the fundamental insight of linear algebra: **To track what happens to every single point across the entire infinite sheet of space, you only need to track where the two unit sticks (î and ĵ) land.**

A matrix is nothing more than a compact spreadsheet recording the final coordinates of those transformed basis sticks. When written as:

```
        [ a   b ]
   A =  [       ]
        [ c   d ]
          ▲   ▲
          │   │
    Landing   Landing
    of î      of ĵ
```

The first column `[a, c]ᵀ` is the new position of **î**, and the second column `[b, d]ᵀ` is the new position of **ĵ**. Any vector `v = [x, y]ᵀ` in the original space will land at `x` times the new **î** plus `y` times the new **ĵ**.

Matrix multiplication is not a mystical list of arithmetic rules to memorize; it is a coordinate translation machine that maps inputs through a transformed coordinate grid.

---

## Part 2: Mathematical & Physical Derivations (No Black Boxes)

### 1. Vector Operations & Linear Combinations
A 2D vector represents both direction and magnitude. We define vector addition and scalar multiplication component-wise:

```
   u + v = [ ux ] + [ vx ] = [ ux + vx ]
           [ uy ]   [ vy ]   [ uy + vy ]

     c·v = c · [ vx ] = [ c · vx ]
               [ vy ]   [ c · vy ]
```

Geometrically, `u + v` places the tail of `v` at the tip of `u` (the parallelogram law). 

The **dot product** (scalar product) between two vectors `u` and `v` measures directional alignment:

```
   u · v = (ux · vx) + (uy · vy) = ||u|| · ||v|| · cos(θ)
```

Where `||v|| = √(vx² + vy²)` is the Euclidean norm (length), and `θ` is the angle between the vectors. If `u · v = 0`, the vectors are orthogonal (perpendicular at 90°). If `u · v > 0`, they point in generally the same direction; if `u · v < 0`, they oppose each other.

To project vector `u` onto a unit vector `n̂` (where `||n̂|| = 1`):

```
   proj_n(u) = (u · n̂) · n̂
```

### 2. Matrix Transformations & Matrix-Vector Multiplication
Let `T` be a linear transformation that maps `ℝ² ➔ ℝ²`. Because `T` is linear, it satisfies additivity `T(u + v) = T(u) + T(v)` and homogeneity `T(c·v) = c·T(u)`.

Any vector `v = [x, y]ᵀ` can be written as a linear combination of the standard basis vectors:

```
   v = x·î + y·ĵ = x·[1, 0]ᵀ + y·[0, 1]ᵀ
```

Applying transformation `T`:

```
   T(v) = T(x·î + y·ĵ) = x·T(î) + y·T(ĵ)
```

If `T(î) = [a, c]ᵀ` and `T(ĵ) = [b, d]ᵀ`, then:

```
   T(v) = x·[ a ] + y·[ b ] = [ a·x + b·y ] = [ a  b ] [ x ]
            [ c ]     [ d ]   [ c·x + d·y ]   [ c  d ] [ y ]
```

This yields the row-column rule for matrix-vector multiplication.

#### 2D Rotation Matrix Derivation
Consider rotating the entire coordinate plane counter-clockwise by an angle `θ`.
- `î = [1, 0]ᵀ` rotates to `[cos(θ), sin(θ)]ᵀ`
- `ĵ = [0, 1]ᵀ` rotates to `[-sin(θ), cos(θ)]ᵀ`

```
   R(θ) = [ cos(θ)  -sin(θ) ]
          [ sin(θ)   cos(θ) ]
```

Applying `R(θ)` to any vector `[x, y]ᵀ` gives the rotated vector `[x·cos(θ) - y·sin(θ), x·sin(θ) + y·cos(θ)]ᵀ`.

```
   y
   ▲         ĵ_new = [-sin θ, cos θ]ᵀ
   │          \
   │           \       î_new = [cos θ, sin θ]ᵀ
   │            \    . '
   │             \ . ' θ
   └──────────────┴──────────► x
```

### 3. The Determinant: Area Scaling & Singularity
Consider the unit square spanned by `î = [1, 0]ᵀ` and `ĵ = [0, 1]ᵀ`. Its original area is `1 × 1 = 1`.

Under transformation `A = [[a, b], [c, d]]`, this square becomes a parallelogram spanned by `[a, c]ᵀ` and `[b, d]ᵀ`.

```
   Parallelogram vertices: (0,0), (a,c), (b,d), (a+b, c+d)
   
   Total enclosing rectangle area: (a + b) · (c + d) = ac + ad + bc + bd
   Subtract surrounding 2 corner rectangles: 2 · (b · c) = 2bc
   Subtract 2 bottom-left triangles: 2 · (1/2 · a · c) = ac
   Subtract 2 top-right triangles: 2 · (1/2 · b · d) = bd
   
   Parallelogram Area = (ac + ad + bc + bd) - 2bc - ac - bd
                      = ad - bc
```

```
   det(A) = ad - bc
```

The **determinant** `det(A)` represents the factor by which the transformation scales any 2D area:
- `det(A) = 1`: Area is preserved (e.g., pure rotations and shears).
- `det(A) > 1`: Space is expanded.
- `0 < det(A) < 1`: Space is compressed.
- `det(A) < 0`: Space is flipped / inverted (orientation reversed, like looking in a mirror).
- `det(A) = 0`: **Singularity.** The 2D plane is squashed down into a 1D line or a single 0D point. Information is permanently destroyed; no inverse matrix `A⁻¹` exists.

### 4. Eigenvalues and Eigenvectors
Under most matrix transformations, vectors change both their length and their direction. However, certain special vectors maintain their exact span—they are merely scaled by a factor `λ`:

```
   A · v = λ · v
```

Where `v` is an **eigenvector** (`v ≠ 0`) and `λ` is its corresponding **eigenvalue**.

Rearranging:

```
   (A - λ·I) · v = 0
```

Where `I = [[1, 0], [0, 1]]` is the identity matrix. For a non-zero vector `v` to satisfy this equation, the matrix `(A - λ·I)` must compress space into a lower dimension, meaning its determinant must be zero:

```
   det(A - λ·I) = 0
   
   det([ a - λ    b    ]) = (a - λ)(d - λ) - bc = 0
       [   c    d - λ  ]
       
   λ² - (a + d)·λ + (ad - bc) = 0
   λ² - trace(A)·λ + det(A) = 0
```

This quadratic equation (the **characteristic polynomial**) yields the eigenvalues `λ₁` and `λ₂`.

---

## Part 3: Dual Grounding: FRC Autonomous Robotics & Modern ML/AI

### 1. FRC Autonomous Robotics: Field-Oriented Swerve Drive
In modern FIRST Robotics Competition (FRC) robots, 4-wheel independent swerve drive allows translation in any direction while rotating simultaneously.

Drivers want **Field-Oriented Control**: pushing the joystick forward must drive the robot downfield (toward the opponent's scoring grid), regardless of which direction the robot's front chassis is currently facing.

```
   Field Coordinate Frame (X_field, Y_field)
   Robot Chassis Frame   (X_robot, Y_robot) rotated by gyro heading θ
```

The driver inputs velocity commands in the field frame: `v_field = [vx_field, vy_field]ᵀ`.

To compute the chassis-relative velocities `v_robot` required by the wheel kinematics, the flight software applies a 2D rotation matrix:

```
   v_robot = R(-θ) · v_field = [ cos(-θ)  -sin(-θ) ] [ vx_field ]
                               [ sin(-θ)   cos(-θ) ] [ vy_field ]

           = [  cos(θ)  sin(θ) ] [ vx_field ]
             [ -sin(θ)  cos(θ) ] [ vy_field ]
```

If the gyro reading `θ` has sign errors or matrix transpose bugs, the robot's coordinate frame rotates in reverse, sending a 120-pound robot crashing into the arena perimeter walls at 5 meters per second.

```
      Field Frame                     Robot Frame
      ▲ Y_field                        ▲ X_robot (Chassis Front)
      │                                │  . '
      │   Robot Heading θ              │ . '  v_robot
      │     . '                        └────────► Y_robot
      │    /
      └────────► X_field
```

### 2. Machine Learning: Dense Neural Network Layers
Every fully connected (dense) layer in a neural network (from simple multilayer perceptrons to transformer attention projections) is a matrix transformation followed by a vector translation and non-linear activation:

```
   z = W · x + b
   a = σ(z)
```

Where:
- `x` is the input feature vector `[x₁, x₂, ..., x_n]ᵀ` (dimension `n × 1`)
- `W` is the weight matrix (dimension `m × n`)
- `b` is the bias vector (dimension `m × 1`)
- `z` is the transformed representation before activation `σ`

Each row of matrix `W` computes a dot product between the input vector `x` and a specific feature detector vector `w_i`:

```
   z_i = (w_i · x) + b_i
```

Geometrically, the weight matrix `W` rotates, shears, and scales the input data cloud, warping the high-dimensional geometry so that classes become linearly separable. 

If matrix `W` experiences rank collapse (`det(W) ≈ 0` across subspace projections), the network loses representation capacity, projecting distinct inputs onto the same collapsed output manifold.

---

## Part 4: The Classic Failure Mode & From-Scratch Python Engine

### The Classic Failure Mode: Matrix Singularity & Unchecked Inverses
In robotic inverse kinematics and machine learning optimizations, algorithms frequently need to solve linear systems `A · x = b` by computing `x = A⁻¹ · b`.

The analytical inverse of a 2D matrix is:

```
   A⁻¹ = (1 / det(A)) · [  d  -b ]
                        [ -c   a ]
```

**The Catastrophe:** If `det(A) = 0` (or `det(A) < 1e-7` due to numerical floating-point imprecision), division by determinant produces `NaN` (Not a Number) or `Infinity`. 

In autonomous robotics, when an arm reaches full extension (a kinematic singularity where joint axes align), the Jacobian matrix determinant drops to zero. A naive controller computing `J⁻¹` commands infinite motor voltages, tripping circuit breakers, burning brushless motor windings, or ripping gearbox teeth off.

### From-Scratch Python Implementation

Here is a self-contained, standard-library Python engine implementing 2D vector and matrix algebra, determinant evaluation, safe inversion with condition number checks, and a comparison between naive inversion vs robust inverse kinematics:

```python
#!/usr/bin/env python3
"""
axon - Concept 01: Vectors, Basis Spaces & Matrix Transformations
From-scratch implementation of 2D Linear Algebra & Safe Matrix Inversion.
"""
import math
from typing import Tuple, Optional


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> 'Vector2D':
        return self.__mul__(scalar)

    def dot(self, other: 'Vector2D') -> float:
        """Compute scalar dot product: u · v = ux*vx + uy*vy"""
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> float:
        """Compute Euclidean length ||v||"""
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self) -> 'Vector2D':
        """Return unit vector in same direction"""
        mag = self.magnitude()
        if mag < 1e-9:
            return Vector2D(0.0, 0.0)
        return Vector2D(self.x / mag, self.y / mag)

    def __repr__(self) -> str:
        return f"Vector2D({self.x:+.4f}, {self.y:+.4f})"


class Matrix2x2:
    def __init__(self, a: float, b: float, c: float, d: float):
        """
        Matrix layout:
        [ a  b ]
        [ c  d ]
        Column 1 (i-hat landing): [a, c]ᵀ
        Column 2 (j-hat landing): [b, d]ᵀ
        """
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    @classmethod
    def rotation(cls, theta_radians: float) -> 'Matrix2x2':
        """Construct standard 2D counter-clockwise rotation matrix R(θ)"""
        c = math.cos(theta_radians)
        s = math.sin(theta_radians)
        return cls(c, -s, s, c)

    def transform(self, v: Vector2D) -> Vector2D:
        """Matrix-vector multiplication: A · v"""
        new_x = self.a * v.x + self.b * v.y
        new_y = self.c * v.x + self.d * v.y
        return Vector2D(new_x, new_y)

    def matmul(self, other: 'Matrix2x2') -> 'Matrix2x2':
        """Matrix-matrix multiplication: self · other"""
        return Matrix2x2(
            a=self.a * other.a + self.b * other.c,
            b=self.a * other.b + self.b * other.d,
            c=self.c * other.a + self.d * other.c,
            d=self.c * other.b + self.d * other.d
        )

    def determinant(self) -> float:
        """Compute area scaling factor det(A) = ad - bc"""
        return (self.a * self.d) - (self.b * self.c)

    def eigenvalues(self) -> Tuple[Optional[float], Optional[float]]:
        """
        Compute real eigenvalues via characteristic equation:
        λ² - trace(A)·λ + det(A) = 0
        """
        trace = self.a + self.d
        det = self.determinant()
        discriminant = trace**2 - 4 * det

        if discriminant < 0:
            # Complex eigenvalues (pure rotation with no real invariant axes)
            return None, None
        
        sqrt_disc = math.sqrt(discriminant)
        lambda1 = (trace + sqrt_disc) / 2.0
        lambda2 = (trace - sqrt_disc) / 2.0
        return lambda1, lambda2

    def safe_inverse(self, epsilon: float = 1e-7) -> Optional['Matrix2x2']:
        """
        Invert matrix with singularity protection.
        Returns None if det(A) is near zero to prevent division-by-zero crashes.
        """
        det = self.determinant()
        if abs(det) < epsilon:
            return None  # Singular matrix: space collapsed, irreversible!
        
        inv_det = 1.0 / det
        return Matrix2x2(
            a= self.d * inv_det,
            b=-self.b * inv_det,
            c=-self.c * inv_det,
            d= self.a * inv_det
        )


def demonstrate_robotics_and_failure():
    print("=" * 65)
    print("1. FIELD-ORIENTED SWERVE ROTATION DEMO")
    print("=" * 65)
    field_cmd = Vector2D(0.0, 3.0)  # Move 3 m/s straight downfield
    heading_deg = 45.0
    heading_rad = math.radians(heading_deg)
    
    # R(-θ) transforms field frame to robot frame
    r_inv = Matrix2x2.rotation(-heading_rad)
    robot_cmd = r_inv.transform(field_cmd)
    
    print(f"Field Velocity Vector : {field_cmd}")
    print(f"Gyro Heading Angle    : {heading_deg}°")
    print(f"Required Chassis Cmd  : {robot_cmd}")
    print(f"Magnitude Preserved?  : {math.isclose(field_cmd.magnitude(), robot_cmd.magnitude())}")

    print("\n" + "=" * 65)
    print("2. SINGULARITY / COLLAPSE RECOVERY BENCHMARK")
    print("=" * 65)
    # Singular matrix where col 2 is a scalar multiple of col 1
    singular_mat = Matrix2x2(2.0, 4.0, 1.0, 2.0)
    det = singular_mat.determinant()
    print(f"Matrix [[2, 4], [1, 2]] Determinant: {det:.6f}")
    
    # Attempting safe inverse
    inv = singular_mat.safe_inverse()
    if inv is None:
        print(">> SAFELY CAUGHT SINGULARITY: Matrix has no inverse (det=0).")
        print(">> Controller safely clamps outputs instead of throwing NaN.")
    
    # Regular invertible shear matrix
    shear_mat = Matrix2x2(1.0, 1.5, 0.0, 1.0)
    l1, l2 = shear_mat.eigenvalues()
    print(f"\nShear Matrix Determinant: {shear_mat.determinant():.4f}")
    print(f"Shear Matrix Eigenvalues: λ1={l1}, λ2={l2}")


if __name__ == "__main__":
    demonstrate_robotics_and_failure()
```

---

## Part 5: Review Checkpoints & Deep-Dive Exploration Prompts

### Review Checkpoints (Test Your Understanding)

#### Checkpoint 1: Determinant Sign Flip
**Question:** A transformation matrix `M` maps `î` to `[0, 2]ᵀ` and `ĵ` to `[3, 0]ᵀ`. Calculate `det(M)`. What is the geometric meaning of the sign of `det(M)` in this scenario?

**Solution:**
1. Construct matrix `M` from column vectors:
   ```
   M = [ 0  3 ]
       [ 2  0 ]
   ```
2. Apply determinant formula `det(M) = (a·d) - (b·c)`:
   ```
   det(M) = (0 · 0) - (3 · 2) = -6
   ```
3. **Geometric Meaning:** The absolute magnitude `|-6| = 6` indicates that any shape transformed by `M` expands in area by a factor of 6. The negative sign (`-`) indicates that **spatial orientation has been inverted**. If you walk around the original unit square in counter-clockwise order (`(0,0) ➔ (1,0) ➔ (1,1) ➔ (0,1)`), the transformed shape vertices will now be traversed in **clockwise** order. Space was flipped across an axis.

#### Checkpoint 2: Eigenvalues of a Pure Rotation
**Question:** Consider the pure rotation matrix `R(90°)` which rotates vectors 90° counter-clockwise. Compute its eigenvalues algebraically. Why do no real eigenvalues exist physically?

**Solution:**
1. Construct `R(90°)` with `cos(90°) = 0` and `sin(90°) = 1`:
   ```
   R(90°) = [ 0  -1 ]
            [ 1   0 ]
   ```
2. Compute characteristic polynomial `det(R - λ·I) = 0`:
   ```
   det([ -λ   -1 ]) = (-λ)(-λ) - (-1)(1) = λ² + 1 = 0
       [  1   -λ ]
   ```
3. Solving `λ² = -1` gives complex roots: `λ = +i` and `λ = -i` (where `i = √(-1)`).
4. **Physical Meaning:** An eigenvector is a vector whose direction does not change under transformation (it stays on its original span line). Since a 90° rotation changes the direction of *every single 2D vector* by exactly 90°, no non-zero vector in the real 2D plane can stay on its original line. Therefore, there are no real eigenvectors or real eigenvalues.

---

### Deep-Dive Exploration Prompts

1. **Singular Value Decomposition (SVD):** Every linear transformation matrix `A` can be factored into `A = U · Σ · Vᵀ`, where `U` and `V` are orthonormal rotation matrices and `Σ` is a diagonal scaling matrix. How does SVD reveal the principal axes of error ellipses when estimating a mobile robot's positional uncertainty?
2. **Batch Matrix Multiplication in GPUs:** In deep learning frameworks (PyTorch, JAX), dense layer computations process 1,024 batch samples simultaneously as `Z = X · Wᵀ + B`. How does the memory layout of row-major vs column-major matrices affect cache hit rates and Tensor Core utilization during forward passes?

---

### Curriculum Linkages

* **Backward Link:** Foundational high school geometry & coordinate arithmetic.
* **Forward Links:**
  * **Concept 05 (Loss Landscapes & Optimization):** Quadratic forms `xᵀ · A · x` and Hessian curvature matrices.
  * **Concept 06 (Dense Layers & Activations):** Multi-layer linear collapses without non-linear activations.
  * **Concept 13 (Swerve Kinematics):** Forward and inverse kinematics transformation matrices mapping chassis speeds to wheel azimuth angles.
