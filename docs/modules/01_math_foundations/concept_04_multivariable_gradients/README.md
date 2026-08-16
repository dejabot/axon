# Concept 04: Multivariable Calculus, Gradients & The Chain Rule

```
       [ 01_math_foundations ]  ➔  Concept 04: Multivariable Gradients
       Stage 1: The Unified Math Engine
```

---

## Part 1: The Intuitive Mental Model (Physical/Visual Analogy)

Imagine you are hiking on a rugged mountain range in dense, blinding fog. You can only see the ground directly beneath your hiking boots. Your goal is to reach the highest mountain peak (or find the lowest valley floor to set up camp).

```
                      Foggy Mountain Landscape
                              Peak ▲ f(x, y) = High
                                 / \
                                /   \
                               /  ▲  \  ∇f points STEEPEST UPHILL
                              /   │   \
                             /    │    \
                            /     ● (x, y) Current Location
                           /     / \
                          /     /   \
                         /     /     \
   Valley Floor ────────┴─────┴───────┴──────
```

At any point `(x, y)` on the mountain, the terrain slopes in different directions:
- If you step strictly East (along the `x`-axis), the ground might slope gently upward.
- If you step strictly North (along the `y`-axis), the ground might drop steeply downward.

What single direction gives you the steepest climb?

If you calculate the slope along the East-West axis (`∂f/∂x`) and the slope along the North-South axis (`∂f/∂y`), and combine them into a single 2D vector, you get the **Gradient Vector** (**∇f**).

The gradient vector has two superpowers:
1. **Direction:** It points exactly in the direction of **maximum instantaneous ascent** (steepest uphill climb).
2. **Magnitude:** Its length `||∇f||` equals the steepness of that maximum slope.

To descend to the valley as fast as possible, you simply walk in the exact opposite direction: **-∇f**. This simple compass heading is the driving engine behind both machine learning optimization (Gradient Descent) and autonomous robot path planning (Potential Field Navigation).

---

## Part 2: Mathematical & Physical Derivations (No Black Boxes)

### 1. Functions of Multiple Variables & Partial Derivatives
Let `z = f(x, y)` represent a scalar field (surface height) over 2D coordinates `(x, y) ∈ ℝ²`.

The **partial derivative** with respect to `x` (`∂f/∂x` or `f_x`) measures the rate of change of `f` as `x` varies while holding `y` strictly constant:

```
   ∂f / ∂x = lim [ (f(x + Δx, y) - f(x, y)) / Δx ]
             Δx➔0
```

Similarly, the partial derivative with respect to `y` holds `x` constant:

```
   ∂f / ∂y = lim [ (f(x, y + Δy) - f(x, y)) / Δy ]
             Δy➔0
```

Geometrically, `∂f/∂x` is the slope of the tangent line to the 1D curve formed by slicing the 3D surface with a vertical plane parallel to the x-axis.

```
       z (Height)
       ▲             Slice at constant y = y₀
       │                . - ~ ~ - .
       │            . '             '.
       │          /     Slope = ∂f/∂x  \
       └─────────┼──────────────────────┼────► x
                (x₀, y₀)
```

### 2. The Gradient Vector (∇f)
The **gradient** of a scalar field `f(x, y)` (denoted `∇f` or "grad f") is the vector of all its first-order partial derivatives:

```
          [ ∂f / ∂x ]
   ∇f  =  [         ]
          [ ∂f / ∂y ]
```

For an `n`-dimensional function `f(x₁, x₂, ..., x_n)`:

```
   ∇f = [ ∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂x_n ]ᵀ
```

### 3. Directional Derivatives & Proof of Steepest Ascent
How fast does `f(x, y)` change if you move along an arbitrary unit direction vector `û = [ux, uy]ᵀ` (where `||û|| = √(ux² + uy²) = 1`)?

The **directional derivative** `D_u(f)` is defined as:

```
   D_u(f) = lim [ (f(x + h·ux, y + h·uy) - f(x, y)) / h ]
            h➔0
```

Using multivariable linear approximation:
`f(x + h·ux, y + h·uy) ≈ f(x, y) + (∂f/∂x)·(h·ux) + (∂f/∂y)·(h·uy)`

Substituting into the limit:

```
   D_u(f) = (∂f/∂x)·ux + (∂f/∂y)·uy = ∇f · û
```

The directional derivative is the **dot product** between the gradient vector `∇f` and the direction unit vector `û`.

#### Proof: Why ∇f is the Direction of Steepest Ascent
Using the geometric definition of the dot product:

```
   D_u(f) = ∇f · û = ||∇f|| · ||û|| · cos(θ) = ||∇f|| · cos(θ)
```

Where `θ` is the angle between `∇f` and `û`.
- Since `-1 ≤ cos(θ) ≤ +1`, the maximum possible value of `D_u(f)` occurs when `cos(θ) = +1` (`θ = 0°`).
- `θ = 0°` means that `û` points in the **exact same direction as ∇f**:
  `û_max = ∇f / ||∇f||` with maximum slope `||∇f||`.
- Conversely, the minimum (most negative) slope occurs when `cos(θ) = -1` (`θ = 180°`), pointing in the direction of **steepest descent**: **-∇f**.

### 4. Orthogonality to Level Curves (Contour Lines)
A **level curve** (or contour line) is the set of all points `(x, y)` where `f(x, y) = C` (constant height).

```
   Contour f(x, y) = C
   
           Tangent Vector T
          ◄────────────────●────────────────►
                           │
                           │  ∇f (Gradient is ALWAYS perpendicular at 90°)
                           ▼
```

Let `r(t) = [x(t), y(t)]ᵀ` parameterize a contour line where `f(x(t), y(t)) = C`.

Differentiating both sides with respect to `t` using the multivariable chain rule:

```
   d/dt [ f(x(t), y(t)) ] = d/dt [ C ]
   (∂f / ∂x)·(dx / dt) + (∂f / ∂y)·(dy / dt) = 0
   ∇f · r'(t) = 0
```

Since `r'(t)` is the tangent vector to the contour curve, **the gradient vector ∇f is always perpendicular (orthogonal at 90°) to the contour lines**.

### 5. The Multivariable Chain Rule
In single-variable calculus, `d/dt [f(g(t))] = f'(g(t)) · g'(t)`.

In multivariable systems, if `z = f(x, y)` where both `x = x(t)` and `y = y(t)` depend on time `t`, the total derivative accumulates rates of change across all paths:

```
   dz / dt = (∂f / ∂x) · (dx / dt) + (∂f / ∂y) · (dy / dt)
```

```
                 z = f(x, y)
                 /         \
          ∂f/∂x /           \ ∂f/∂y
               ▼             ▼
              x(t)          y(t)
               \             /
          dx/dt \           / dy/dt
                 ▼         ▼
                     t
```

#### Matrix-Vector Formulation (The Jacobian)
If an intermediate vector `y = g(x) ∈ ℝᵐ` is mapped to an output vector `z = f(y) ∈ ℝᵏ`, the multivariable chain rule becomes a **matrix multiplication of Jacobians**:

```
   J_composite = J_f(y) · J_g(x)
```

Where the Jacobian matrix `J` records all first-order partial derivatives `J_ij = ∂f_i / ∂x_j`.

---

## Part 3: Dual Grounding: FRC Autonomous Robotics & Modern ML/AI

### 1. FRC Autonomous Robotics: Potential Field Navigation & Inverse Kinematics

#### A. Artificial Potential Field Navigation
To navigate an autonomous robot through a field containing obstacles and a target scoring goal:
1. Define an **attractive potential** pulling the robot toward goal `p_goal`:
   `U_attract(p) = (1/2) · k_att · ||p - p_goal||²`
2. Define a **repulsive potential** pushing the robot away from obstacle `p_obs` within safety radius `d₀`:
   `U_repulse(p) = (1/2) · k_rep · (1/d - 1/d₀)²`  (for `d = ||p - p_obs|| ≤ d₀`)
3. Total potential: `U_total(p) = U_attract(p) + U_repulse(p)`.

The robot computes its instantaneous propulsion force command by taking the negative gradient:

```
   F_cmd = -∇U_total(p) = -∇U_attract(p) - ∇U_repulse(p)
```

```
   Attractive Gradient -∇U_att: Pulls toward Goal (Green)
   Repulsive Gradient  -∇U_rep: Pushes away from Obstacle (Red)
   Resulting Command   F_cmd  : Smoothly steers around defender!
```

#### B. Robot Arm Kinematic Jacobian
For a 2-joint robotic arm with joint angles `θ = [θ₁, θ₂]ᵀ`, forward kinematics gives end-effector position `p(θ) = [x(θ), y(θ)]ᵀ`.

The velocity relationship is given by the Jacobian matrix:

```
   [ vx ] = [ ∂x/∂θ₁   ∂x/∂θ₂ ] [ ω₁ ]
   [ vy ]   [ ∂y/∂θ₁   ∂y/∂θ₂ ] [ ω₂ ]
     v    =       J(θ)        ·   ω
```

### 2. Machine Learning: Gradient Descent & Deep Backpropagation

#### A. Gradient Descent Parameter Updates
In supervised machine learning, a loss function `L(W)` measures prediction error over network weights `W`.

To minimize loss, weights are iteratively updated in the direction of steepest descent:

```
   W[k+1] = W[k] - η · ∇_W L(W[k])
```

Where `η` is the learning rate.

#### B. Backpropagation as the Multivariable Chain Rule
For a deep neural network with layers `z^[l] = W^[l] · a^[l-1] + b^[l]` and `a^[l] = σ(z^[l])`:

To find how the final scalar loss `L` changes with respect to weight matrix `W^[l]`, backpropagation applies the chain rule backward through the computation graph:

```
   ∂L / ∂W^[l] = (∂L / ∂z^[l]) · (∂z^[l] / ∂W^[l])ᵀ = δ^[l] · (a^[l-1])ᵀ
```

Where error vector `δ^[l] = ∂L / ∂z^[l]` is propagated backward layer-by-layer:

```
   δ^[l-1] = ( (W^[l])ᵀ · δ^[l] ) ⊙ σ'(z^[l-1])
```

Without the multivariable chain rule, training deep neural networks with millions of parameters would be mathematically impossible.

---

## Part 4: The Classic Failure Mode & From-Scratch Python Engine

### The Classic Failure Mode: The "Ravine Trap" & Gradient Explosion
When optimizing ill-conditioned loss surfaces (such as the Rosenbrock function or deep networks with high curvature in one direction and flat slope in another):

```
   Loss Landscape: Long narrow valley (Ravine)
   
        ▲ y
        │    \  Gradient points mostly across steep walls!  /
        │     \   ◄───●───►                                /
        │      \     / \                                  /
        │       \   /   \                                /
        └──────────┴─────┴────────────────────────────────► x
                   Valley floor (Slow progress along x)
```

**The Catastrophe:**
1. The gradient `∇f` has massive magnitude along the steep valley walls (`y`-axis) but tiny magnitude along the shallow floor (`x`-axis).
2. Standard gradient descent with a fixed learning rate `η` violently bounces back and forth across the canyon walls.
3. If `η` is even slightly too large, the oscillations grow exponentially, throwing parameters to `±Infinity` (`loss = NaN`).

### From-Scratch Python Implementation

The following complete Python engine implements multivariable gradients, numerical gradient verification, and a comparison between standard Gradient Descent vs Gradient Descent with Momentum on a narrow curvature ravine:

```python
#!/usr/bin/env python3
"""
axon - Concept 04: Multivariable Calculus, Gradients & The Chain Rule
From-scratch multivariable gradient computation & optimization engine.
"""
import math
from typing import Tuple, Callable, List


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

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __repr__(self) -> str:
        return f"[{self.x:+.4f}, {self.y:+.4f}]ᵀ"


class LossLandscape:
    """
    Anisotropic Quadratic Ravine Loss Function:
    f(x, y) = 0.5 * (x² + 20 * y²)
    Steep curvature along y (k_y = 20), gentle curvature along x (k_x = 1).
    Global minimum is at (0, 0) with f(0, 0) = 0.
    """
    @staticmethod
    def evaluate(p: Vector2D) -> float:
        return 0.5 * (p.x**2 + 20.0 * (p.y**2))

    @staticmethod
    def analytical_gradient(p: Vector2D) -> Vector2D:
        """∇f = [∂f/∂x, ∂f/∂y]ᵀ = [x, 20·y]ᵀ"""
        df_dx = p.x
        df_dy = 20.0 * p.y
        return Vector2D(df_dx, df_dy)

    @staticmethod
    def numerical_gradient(p: Vector2D, h: float = 1e-5) -> Vector2D:
        """Compute numerical gradient via central finite differences"""
        f_x_plus = LossLandscape.evaluate(Vector2D(p.x + h, p.y))
        f_x_minus = LossLandscape.evaluate(Vector2D(p.x - h, p.y))
        df_dx = (f_x_plus - f_x_minus) / (2.0 * h)

        f_y_plus = LossLandscape.evaluate(Vector2D(p.x, p.y + h))
        f_y_minus = LossLandscape.evaluate(Vector2D(p.x, p.y - h))
        df_dy = (f_y_plus - f_y_minus) / (2.0 * h)

        return Vector2D(df_dx, df_dy)


def optimize_vanilla_gd(start: Vector2D, lr: float, steps: int = 15) -> List[Tuple[int, Vector2D, float]]:
    history = []
    p = Vector2D(start.x, start.y)
    for k in range(steps):
        loss = LossLandscape.evaluate(p)
        grad = LossLandscape.analytical_gradient(p)
        history.append((k, p, loss))
        # Vanilla Gradient Descent Update: p = p - lr * grad
        p = p - lr * grad
    return history


def optimize_momentum_gd(start: Vector2D, lr: float, beta: float = 0.8, steps: int = 15) -> List[Tuple[int, Vector2D, float]]:
    history = []
    p = Vector2D(start.x, start.y)
    v = Vector2D(0.0, 0.0)  # Velocity buffer
    for k in range(steps):
        loss = LossLandscape.evaluate(p)
        grad = LossLandscape.analytical_gradient(p)
        history.append((k, p, loss))
        # Momentum update: v = beta * v + (1 - beta) * grad
        v = (beta * v) + ((1.0 - beta) * grad)
        p = p - lr * v
    return history


def benchmark_optimizers():
    start_pos = Vector2D(5.0, 1.0)
    print("=" * 70)
    print("1. NUMERICAL VS ANALYTICAL GRADIENT VERIFICATION")
    print("=" * 70)
    grad_ana = LossLandscape.analytical_gradient(start_pos)
    grad_num = LossLandscape.numerical_gradient(start_pos)
    print(f"Position            : {start_pos}")
    print(f"Analytical Gradient : {grad_ana}")
    print(f"Numerical Gradient  : {grad_num}")
    diff = (grad_ana - grad_num).magnitude()
    print(f"Gradient Error Norm : {diff:.8e} (Finite difference verified!)")

    print("\n" + "=" * 70)
    print("2. OPTIMIZATION ON NARROW RAVINE (LR = 0.08)")
    print("=" * 70)
    hist_vanilla = optimize_vanilla_gd(start_pos, lr=0.08, steps=6)
    hist_momentum = optimize_momentum_gd(start_pos, lr=0.35, beta=0.75, steps=6)

    print("Step | Vanilla GD Position       | Loss     | Momentum GD Position      | Loss")
    print("-" * 75)
    for i in range(6):
        _, p_v, l_v = hist_vanilla[i]
        _, p_m, l_m = hist_momentum[i]
        print(f" {i:2d}  | {str(p_v):24s} | {l_v:8.4f} | {str(p_m):24s} | {l_m:8.4f}")


if __name__ == "__main__":
    benchmark_optimizers()
```

---

## Part 5: Review Checkpoints & Deep-Dive Exploration Prompts

### Review Checkpoints (Test Your Understanding)

#### Checkpoint 1: Computing 2D Gradient and Steepest Ascent
**Question:** Consider the objective function `f(x, y) = 3·x²·y - 4·y³ + 2·x`.
1. Compute the analytical gradient vector `∇f(x, y)`.
2. Evaluate `∇f` at the point `(1, 2)`.
3. What is the unit vector direction `û_max` of steepest ascent at `(1, 2)`, and what is the maximum slope?

**Solution:**
1. Compute partial derivatives:
   ```
   ∂f / ∂x = 6·x·y + 2
   ∂f / ∂y = 3·x² - 12·y²
   ∇f(x, y) = [ 6·x·y + 2,  3·x² - 12·y² ]ᵀ
   ```
2. Evaluate at `x = 1, y = 2`:
   ```
   ∂f/∂x = 6(1)(2) + 2 = 12 + 2 = 14
   ∂f/∂y = 3(1)² - 12(2)² = 3 - 48 = -45
   ∇f(1, 2) = [ 14, -45 ]ᵀ
   ```
3. **Direction of Steepest Ascent & Maximum Slope:**
   ```
   ||∇f|| = √(14² + (-45)²) = √(196 + 2025) = √2221 ≈ 47.127
   û_max = ∇f / ||∇f|| = [ 14 / 47.127, -45 / 47.127 ]ᵀ ≈ [ +0.2971, -0.9549 ]ᵀ
   ```
   The maximum slope is **`47.127`** along unit vector `[+0.2971, -0.9549]ᵀ`.

#### Checkpoint 2: Multivariable Chain Rule on a Kinematic Trajectory
**Question:** A scalar temperature field in an arena is `T(x, y) = 100 - (x² + 2·y²)`. A robot drives along a trajectory given by `x(t) = 3·cos(t)` and `y(t) = 2·sin(t)`.
Find the time rate of change of temperature experienced by the robot `dT/dt` at `t = π/4`.

**Solution:**
1. Compute partial derivatives of `T(x, y)`:
   - `∂T/∂x = -2·x`
   - `∂T/∂y = -4·y`
2. Compute time derivatives of position:
   - `dx/dt = -3·sin(t)`
   - `dy/dt = +2·cos(t)`
3. Apply multivariable chain rule:
   ```
   dT / dt = (∂T / ∂x)·(dx / dt) + (∂T / ∂y)·(dy / dt)
           = (-2·x)·(-3·sin t) + (-4·y)·(2·cos t)
           = 6·x·sin(t) - 8·y·cos(t)
   ```
4. Evaluate at `t = π/4` where `cos(π/4) = sin(π/4) = √2 / 2`:
   - `x = 3·(√2/2) = 1.5·√2`
   - `y = 2·(√2/2) = √2`
   ```
   dT/dt = 6·(1.5·√2)·(√2/2) - 8·(√2)·(√2/2)
         = 6·(1.5)·(1) - 8·(1) = 9 - 8 = +1.0
   ```
   The robot experiences a temperature rise of **`+1.0 degrees/second`**.

---

### Deep-Dive Exploration Prompts

1. **Second-Order Curvature & The Hessian Matrix:** While the gradient `∇f` contains first derivatives, the **Hessian matrix** `H_ij = ∂²f / ∂x_i ∂x_j` captures local curvature. How does Newton's optimization method `x[k+1] = x[k] - H⁻¹·∇f` achieve quadratic convergence compared to first-order gradient descent?
2. **Reverse-Mode vs Forward-Mode Automatic Differentiation:** In automatic differentiation engines (JAX, PyTorch), reverse-mode AD computes `∂y / ∂x` for `f: ℝⁿ ➔ ℝ¹` in a single backward sweep. Why is reverse-mode AD `O(1)` in computational passes for scalar loss functions with 100 billion parameters, while forward-mode AD would require 100 billion passes?

---

### Curriculum Linkages

* **Backward Link:** Concept 01 (Vectors, dot products) and Concept 03 (Derivatives).
* **Forward Links:**
  * **Concept 05 (Loss Landscapes & Optimization):** Gradient descent, Adam, and momentum algorithms.
  * **Concept 07 (Vector Calculus Backpropagation):** Reverse-mode gradient computation across deep computation graphs.
  * **Concept 18 (Policy Gradients):** Reinforcement learning policy gradient theorem `∇_θ J(θ) = E[ ∇_θ log π_θ(a|s) · Q(s, a) ]`.
