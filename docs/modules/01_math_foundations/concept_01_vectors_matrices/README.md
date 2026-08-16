# Concept 01: Vectors, Basis Spaces & Matrix Transformations

```
       Module 1: Math Foundations  ➔  Concept 01: Vectors & Matrices
```

> **▶ Interactive Demo: [2D Matrix Transformation & Basis Space Visualizer](demo.html)**
>
> Open the interactive visualizer in your browser or explore the embedded frame below to drag basis vectors î and ĵ, scale determinant areas, and observe transformations in real time.

<iframe src="demo.html" width="100%" height="560" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--code-bg, #0a0d14);"></iframe>

---

## 1. Intuitive Mental Model: Building from the Ground Up

### What is a Vector?
Forget abstract definitions for a moment. Think of a vector as an instruction on a sheet of graph paper:

> **"Start at the origin `(0, 0)`, walk 3 steps East, and then walk 2 steps North."**

We write this displacement as a column of numbers:

```
        [ 3 ]  <-- East  (x-axis)
   v =  [ 2 ]  <-- North (y-axis)
```

<div style="text-align: center; margin: 20px 0;">
  <svg width="280" height="180" viewBox="0 0 280 180" style="max-width: 100%; height: auto;">
    <line x1="30" y1="150" x2="250" y2="150" stroke="#334155" stroke-width="1.5" />
    <line x1="30" y1="150" x2="30" y2="20" stroke="#334155" stroke-width="1.5" />
    <!-- Dashed components -->
    <line x1="30" y1="150" x2="180" y2="150" stroke="#38bdf8" stroke-dasharray="4,4" stroke-width="2" />
    <line x1="180" y1="150" x2="180" y2="60" stroke="#4ade80" stroke-dasharray="4,4" stroke-width="2" />
    <!-- Vector Arrow -->
    <line x1="30" y1="150" x2="180" y2="60" stroke="#fbbf24" stroke-width="3" />
    <circle cx="180" cy="60" r="4" fill="#fbbf24" />
    <text x="90" y="170" fill="#38bdf8" font-family="monospace" font-size="12">x = +3 (East)</text>
    <text x="190" y="110" fill="#4ade80" font-family="monospace" font-size="12">y = +2 (North)</text>
    <text x="90" y="90" fill="#fbbf24" font-family="monospace" font-weight="bold" font-size="13">v = [3, 2]ᵀ</text>
  </svg>
</div>

Every 2D vector is characterized by two fundamental properties:
1. **Magnitude (Length):** How far you traveled: `||v|| = √(x² + y²) = √(3² + 2²) = √13 ≈ 3.61`
2. **Direction (Angle):** Which way you are pointing: `θ = atan2(y, x) = atan2(2, 3) ≈ 33.7°`

---

### What are Basis Vectors?
How does the coordinate system actually work? Underneath the surface, the graph paper has two basic "building blocks" (unit vectors):

* **`î` (i-hat):** One step of length 1 along the x-axis: `[1, 0]ᵀ`
* **`ĵ` (j-hat):** One step of length 1 along the y-axis: `[0, 1]ᵀ`

When you write the vector `[3, 2]ᵀ`, you are really saying:
```
   v = 3 · î + 2 · ĵ
     = 3 · [1, 0]ᵀ + 2 · [0, 1]ᵀ
     = [3, 2]ᵀ
```

The numbers `3` and `2` are just **scaling factors** (scalars) that tell you how much of `î` and `ĵ` to combine.

---

### What is a Matrix Transformation?
A matrix is not just a spreadsheet of numbers. **A matrix is a machine that moves the basis vectors `î` and `ĵ` to new landing spots.**

Suppose we apply a transformation matrix `A`:

```
       [ a   b ]
   A = [       ]
       [ c   d ]
```

Look closely at the columns of `A`:
* The **first column** `[a, c]ᵀ` is the new position where `î` lands!
* The **second column** `[b, d]ᵀ` is the new position where `ĵ` lands!

<div style="text-align: center; margin: 20px 0;">
  <svg width="320" height="180" viewBox="0 0 320 180" style="max-width: 100%; height: auto;">
    <line x1="40" y1="140" x2="280" y2="140" stroke="#334155" stroke-width="1.5" />
    <line x1="40" y1="140" x2="40" y2="20" stroke="#334155" stroke-width="1.5" />
    <!-- New î landing -->
    <line x1="40" y1="140" x2="160" y2="110" stroke="#4ade80" stroke-width="3" />
    <circle cx="160" cy="110" r="4" fill="#4ade80" />
    <text x="170" y="115" fill="#4ade80" font-family="monospace" font-size="12">î' = [a, c]ᵀ</text>
    <!-- New ĵ landing -->
    <line x1="40" y1="140" x2="80" y2="40" stroke="#f43f5e" stroke-width="3" />
    <circle cx="80" cy="40" r="4" fill="#f43f5e" />
    <text x="90" y="45" fill="#f43f5e" font-family="monospace" font-size="12">ĵ' = [b, d]ᵀ</text>
  </svg>
</div>

If you know where `î` and `ĵ` land, you know where **every single vector in the universe** lands. Why? Because matrix multiplication is linear:

```
   A · v = A · (x·î + y·ĵ)
         = x · (A·î) + y · (A·ĵ)
         = x · [a, c]ᵀ + y · [b, d]ᵀ
         = [ a·x + b·y ]
           [ c·x + d·y ]
```

---

## 2. Key Geometric Concepts

### 1. The Determinant: How Areas Scale
The **determinant** of a 2D matrix, `det(A) = a·d - b·c`, measures **how much the transformation stretches or shrinks areas**.

* If `det(A) = 1`: Areas are perfectly preserved (e.g., pure rotations).
* If `det(A) = 3`: The unit square of area 1 is stretched into a region of area 3.
* If `det(A) = -1`: The space is flipped inside out (like looking in a mirror / reflection).
* If `det(A) = 0`: The entire 2D plane is squished into a 1D line or a single 0D point. All area is lost.

> **Why Det = 0 Means Non-Invertible:**
> If you squash a 2D sheet of paper down into a 1D line (`det = 0`), you lose information. You cannot run the movie backward to reconstruct the original 2D coordinates. The matrix has no inverse.

---

### 2. Dot Product: Measuring Alignment
The dot product multiplies corresponding components of two vectors and sums them up:

```
   u · v = u_x · v_x + u_y · v_y
```

Geometrically, it equals:
```
   u · v = ||u|| · ||v|| · cos(θ)
```

* If `u · v > 0`: The two vectors point in generally the same direction (`θ < 90°`).
* If `u · v = 0`: The two vectors are strictly **perpendicular (orthogonal)** (`θ = 90°`).
* If `u · v < 0`: The two vectors point away from each other (`θ > 90°`).

---

## 3. Real-World Applications

### In Autonomous Robotics (FRC): Field-Centric vs Robot-Centric Driving
When an autonomous robot drives across the field, the driver pushes the joystick "Forward" relative to the driver station. 

However, if the robot is currently rotated by heading angle `θ`:
* The **Robot's Forward** is pointing in direction `[cos(θ), sin(θ)]ᵀ`.
* The **Robot's Left** is pointing in direction `[-sin(θ), cos(θ)]ᵀ`.

To translate the driver's field-relative command `[v_x, v_y]` into the robot's local frame, the robot multiplies by the 2D rotation matrix:

```
   [ v_robot_x ]   [  cos(θ)   sin(θ) ]   [ v_field_x ]
   [           ] = [                  ] · [           ]
   [ v_robot_y ]   [ -sin(θ)   cos(θ) ]   [ v_field_y ]
```

### In Machine Learning: Dense Linear Layers
In deep learning, every standard fully-connected layer computes:
```
   y = W · x + b
```
The weight matrix `W` rotates and stretches the input feature vector `x` into a new coordinate space where different classes (e.g., game pieces vs field barriers) become easier to separate.

---

## 4. Python Implementation

Here is how you transform a 2D vector and rotate coordinate frames in pure Python:

```python
import math

def transform_vector(A, v):
    """
    Multiplies 2x2 matrix A by 2D vector v.
    A = [[a, b], [c, d]], v = [x, y]
    """
    x_new = A[0][0] * v[0] + A[0][1] * v[1]
    y_new = A[1][0] * v[0] + A[1][1] * v[1]
    return [x_new, y_new]

def rotation_matrix(angle_radians):
    """Returns the 2D rotation matrix for a given angle."""
    c = math.cos(angle_radians)
    s = math.sin(angle_radians)
    return [
        [c, -s],
        [s,  c]
    ]

# Example: Rotate vector [1, 0] by 90 degrees (π/2 radians)
v = [1.0, 0.0]
R = rotation_matrix(math.pi / 2)
v_rotated = transform_vector(R, v)

print(f"Original vector : {v}")
print(f"Rotated by 90°  : [{v_rotated[0]:.2f}, {v_rotated[1]:.2f}]")  # Expected: [0.00, 1.00]
```

---

## 5. Review Questions

### Question 1
Suppose matrix `A` has columns `î' = [2, 0]ᵀ` and `ĵ' = [0, 3]ᵀ`.
1. What is the determinant `det(A)`?
2. If you apply this transformation to a circle with radius 1 (area = `π`), what will the new area be?

**Answer:**
1. `det(A) = (2)(3) - (0)(0) = 6`
2. The area is scaled by the determinant: `New Area = 6 · π ≈ 18.85`.

---

### Question 2
Two vectors are `u = [3, 4]ᵀ` and `v = [-4, 3]ᵀ`.
Compute their dot product `u · v`. What does this tell you about the angle between them?

**Answer:**
`u · v = (3)(-4) + (4)(3) = -12 + 12 = 0`.
Because the dot product is `0`, the angle between them is exactly `90°` (they are perpendicular).
