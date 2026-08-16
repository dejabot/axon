# Concept 04: Multivariable Calculus, Gradients & The Chain Rule

```
       Module 1: Math Foundations  ➔  Concept 04: Gradients & Chain Rule
```

> **▶ Interactive Demo: [Multivariable Gradients & Potential Fields Visualizer](demo.html)**
>
> Open in your browser or explore the embedded frame below to test scalar loss landscapes f(x, y), orthogonal gradient ascent vectors ∇f, and roll a particle downhill with momentum and learning rate controls.

<iframe src="demo.html" width="100%" height="560" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--code-bg, #0a0d14);"></iframe>

---

## 1. Intuitive Mental Model

Imagine you are hiking blindfolded on a foggy, mountainous terrain. Underneath your boots is an uneven physical surface where your elevation (height above sea level) is given by a mathematical function `z = f(x, y)`, where `x` is your coordinate East-West and `y` is your coordinate North-South.

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="200" viewBox="0 0 340 200" style="max-width: 100%; height: auto;">
    <defs>
      <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#fbbf24" />
      </marker>
      <marker id="arrow-green4" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#4ade80" />
      </marker>
    </defs>
    <!-- Contours -->
    <ellipse cx="170" cy="100" rx="140" ry="70" fill="none" stroke="#334155" stroke-width="1.5" />
    <ellipse cx="170" cy="100" rx="95" ry="48" fill="none" stroke="#475569" stroke-width="1.5" />
    <ellipse cx="170" cy="100" rx="50" ry="25" fill="none" stroke="#64748b" stroke-width="1.5" />
    <!-- Current Point -->
    <circle cx="210" cy="100" r="5" fill="#38bdf8" />
    <!-- Steepest Ascent Vector -->
    <line x1="210" y1="100" x2="270" y2="100" stroke="#fbbf24" stroke-width="3" marker-end="url(#arrow-amber)" />
    <!-- Steepest Descent Vector -->
    <line x1="210" y1="100" x2="150" y2="100" stroke="#4ade80" stroke-width="3" marker-end="url(#arrow-green4)" />
    <!-- Labels -->
    <text x="250" y="85" fill="#fbbf24" font-family="monospace" font-weight="bold" font-size="11">∇f (Ascent)</text>
    <text x="110" y="85" fill="#4ade80" font-family="monospace" font-weight="bold" font-size="11">-∇f (Descent)</text>
    <text x="145" y="105" fill="#94a3b8" font-family="monospace" font-size="10">Minimum</text>
  </svg>
</div>

1. **Partial Derivative `∂f/∂x`:** If you keep your North-South position strictly locked and take one small step directly **East**, how much does your elevation change? That slope is the partial derivative with respect to `x`.
2. **Partial Derivative `∂f/∂y`:** If you keep your East-West position strictly locked and take one small step directly **North**, how much does your elevation change? That slope is the partial derivative with respect to `y`.
3. **The Gradient Vector `∇f`:** If you combine both slopes into a single 2D vector `[∂f/∂x, ∂f/∂y]ᵀ`, this arrow points in the direction of **Steepest Ascent** (the fastest way uphill). Its length `||∇f||` is the exact steepness of that slope.

If you want to walk downhill to find the lowest valley floor (e.g., minimizing error in machine learning or navigating a robot away from obstacles), you take steps in the opposite direction: **`-∇f` (Gradient Descent)**.

---

## 2. Mathematical & Physical Derivations

### Partial Derivatives & The Total Differential
Let `f: ℝ² ➔ ℝ` be a scalar function of two variables `(x, y)`. The partial derivatives are defined by holding one variable constant while taking the limit of the other:

```
   ∂f / ∂x = lim [ (f(x + Δx, y) - f(x, y)) / Δx ]
             Δx➔0

   ∂f / ∂y = lim [ (f(x, y + Δy) - f(x, y)) / Δy ]
             Δy➔0
```

When both `x` and `y` change simultaneously by small amounts `dx` and `dy`, the **total differential** `df` (the resulting change in elevation) is:

```
   df = (∂f / ∂x) · dx + (∂f / ∂y) · dy
```

### The Gradient Vector `∇f` (Del Operator)
We define the vector gradient operator `∇` (del / nabla) as the column vector of all first-order partial derivatives:

```
          [ ∂f / ∂x ]
   ∇f =   [ ∂f / ∂y ]
```

Notice that the total differential `df` can be written as a vector dot product between the gradient vector `∇f` and the displacement step vector `dr = [dx, dy]ᵀ`:

```
   df = ∇f · dr = ||∇f|| · ||dr|| · cos(θ)
```

Where `θ` is the angle between the gradient vector and the chosen step direction `dr`.

### Proof: Why the Gradient Points in the Direction of Steepest Ascent
Let `û` be an arbitrary unit direction vector (`||û|| = 1`). The **directional derivative** `D_u(f)` measures the rate of change of `f` in direction `û`:

```
   D_u(f) = ∇f · û = ||∇f|| · ||û|| · cos(θ) = ||∇f|| · cos(θ)
```

To maximize the rate of increase:
- The cosine function reaches its global maximum value of `+1` if and only if `cos(θ) = 1`, which means `θ = 0°`.
- When `θ = 0°`, the step direction `û` is parallel to `∇f`.

**Conclusion:** The gradient `∇f` points in the direction of maximum instantaneous rate of increase (**Steepest Ascent**), with maximum rate `||∇f||`. 

Conversely, to minimize `f` as quickly as possible:
- `cos(θ) = -1` when `θ = 180°` (pointing directly opposite).
- **Steepest Descent** occurs in the direction `-∇f`.

### Orthogonality to Level Curves (Contour Lines)
A **level curve** (contour line) is the set of all points `(x, y)` where elevation is constant: `f(x, y) = C`.

Along a level curve, elevation does not change, so `df = 0`:

```
   df = ∇f · dr = 0
```

Because the dot product of `∇f` and the tangent displacement `dr` along the level curve is zero, **the gradient vector `∇f` is always strictly perpendicular (orthogonal) to the level curves of the function.**

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="150" viewBox="0 0 300 150" style="max-width: 100%; height: auto;">
    <path d="M 30 100 Q 150 40 270 100" fill="none" stroke="#64748b" stroke-width="2" />
    <text x="210" y="65" fill="#94a3b8" font-family="monospace" font-size="10">Contour f(x,y) = C</text>
    <line x1="150" y1="70" x2="150" y2="15" stroke="#fbbf24" stroke-width="3" marker-end="url(#arrow-amber)" />
    <text x="158" y="30" fill="#fbbf24" font-family="monospace" font-weight="bold" font-size="11">∇f ⊥ Tangent (90°)</text>
    <circle cx="150" cy="70" r="4" fill="#38bdf8" />
  </svg>
</div>

### The Multivariable Chain Rule
Suppose a scalar loss `L` depends on intermediate variables `u(t)` and `v(t)`, which themselves depend on a primary parameter `t`.

The multivariable chain rule sums the rates of change flowing through every intermediate path:

```
   dL / dt = (∂L / ∂u) · (du / dt) + (∂L / ∂v) · (dv / dt)
```

In vector matrix form:

```
   dL / dt = [ ∂L / ∂u , ∂L / ∂v ] · [ du / dt ]
                                     [ dv / dt ]
           = ∇L_uv · (dr / dt)
```

If `y = g(x)` where `g: ℝⁿ ➔ ℝᵐ` is a vector-valued function, the matrix of all partial derivatives is the **Jacobian Matrix `J`**:

```
        [ ∂y₁/∂x₁  ∂y₁/∂x₂  ...  ∂y₁/∂xₙ ]
   J =  [ ∂y₂/∂x₁  ∂y₂/∂x₂  ...  ∂y₂/∂xₙ ]
        [    :        :             :    ]
        [ ∂yₘ/∂x₁  ∂yₘ/∂x₂  ...  ∂yₘ/∂xₙ ]
```

The multivariable chain rule for composite functions `z = f(g(x))` is:

```
   ∇_x(z) = J_g(x)ᵀ · ∇_y(z)
```

---

## 3. Dual Grounding: FRC Robotics & Modern ML

### FRC Autonomous Robotics: Artificial Potential Field Obstacle Avoidance

#### Potential Field Navigation
An autonomous robot at position `p = [x, y]ᵀ` must navigate to a goal position `p_goal` while actively avoiding dynamic defender robots at `p_obs`.

We construct an artificial scalar potential energy surface `U(p) = U_att(p) + U_rep(p)`:
1. **Attractive Potential (Goal Pull):** Parabolic bowl pulling toward goal:
   ```
   U_att(p) = (1/2) · k_att · ||p - p_goal||²
   ```
2. **Repulsive Potential (Obstacle Push):** Tall mountain repelling away from obstacles within distance threshold `d₀`:
   ```
   U_rep(p) = (1/2) · k_rep · ( (1 / d(p)) - (1 / d₀) )²    if d(p) ≤ d₀
   ```

The robot software continuously computes the virtual force vector:

```
   F_total = -∇U(p) = -∇U_att(p) - ∇U_rep(p)
           = -k_att · (p - p_goal) + k_rep · ( (1/d) - (1/d₀) ) · (1 / d²) · ∇d
```

The swerve chassis drives along `-∇U(p)`, automatically bending around defenders without requiring graph search.

### Machine Learning: Gradient Descent & Backpropagation

#### Gradient Descent Optimization
In deep neural networks with millions of parameters `W`, we define an objective loss function `L(W)` measuring prediction error.

To minimize the loss, we iteratively update parameters in the direction of steepest descent:

```
   W[k+1] = W[k] - η · ∇_W(L)
```

Where `η` is the **learning rate**.

#### Vector Backpropagation via the Chain Rule
For a 2-layer neural network with loss `L = (1/2) · ||y_pred - y_true||²` where `y_pred = W₂ · a₁` and `a₁ = σ(W₁ · x)`:

Applying the multivariable chain rule backward:

```
   ∂L / ∂W₂ = (y_pred - y_true) · (a₁)ᵀ
   ∂L / ∂a₁ = (W₂)ᵀ · (y_pred - y_true)
   ∂L / ∂W₁ = [ (∂L / ∂a₁) ⊙ σ'(W₁ · x) ] · (x)ᵀ
```

Where `⊙` is the element-wise Hadamard product.

---

## 4. Classic Failure Mode & Python Engine

### The Classic Failure Mode: Exploding Gradients & The "Valley Ping-Pong"
Consider optimizing on an anisotropic loss surface (an elongated, narrow ravine):
```
   f(x, y) = 0.5 · (x² + 20.0 · y²)
```

The partial derivatives are:
- `∂f/∂x = x` (Gentle slope along the ravine floor)
- `∂f/∂y = 20.0 · y` (Steep slope across the ravine walls)

**The Catastrophe:**
1. If the learning rate `η = 0.11` is chosen slightly too large for the steep `y` dimension (where stability requires `η < 2 / 20.0 = 0.10`):
2. In the `x` dimension, `x[k+1] = (1 - 0.11)·x = 0.89·x` converges slowly.
3. In the `y` dimension: `y[k+1] = y - 0.11·(20.0·y) = (1 - 2.2)·y = -1.2·y`.
4. **Result:** The update overshoots the ravine floor, oscillating with exponentially increasing amplitude until floating-point overflow (`NaN`). The optimizer ping-pongs wildly off the walls.

### From-Scratch Python Implementation

```python
#!/usr/bin/env python3
"""
axon - Concept 04: Multivariable Calculus, Gradients & Chain Rule
From-scratch implementation of Potential Fields and Gradient Optimizers.
"""
import math
from typing import Tuple, List


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __repr__(self) -> str:
        return f"[{self.x:+.4f}, {self.y:+.4f}]"


def ravines_surface(x: float, y: float) -> Tuple[float, Vector2D]:
    """Anisotropic ravine: f(x, y) = 0.5*(x² + 20*y²)"""
    loss = 0.5 * (x**2 + 20.0 * (y**2))
    df_dx = x
    df_dy = 20.0 * y
    return loss, Vector2D(df_dx, df_dy)


def potential_field(robot: Vector2D, goal: Vector2D, obstacle: Vector2D) -> Tuple[float, Vector2D]:
    """
    Artificial Potential Field:
    U_total = U_att(goal) + U_rep(obstacle)
    """
    k_att = 1.0
    k_rep = 2.5
    d_safe = 1.5

    d_goal = (robot - goal).magnitude()
    u_att = 0.5 * k_att * (d_goal ** 2)
    grad_att = (robot - goal) * k_att

    d_obs_vec = robot - obstacle
    d_obs = d_obs_vec.magnitude()

    if d_obs < 0.05:
        d_obs = 0.05

    if d_obs <= d_safe:
        diff = (1.0 / d_obs) - (1.0 / d_safe)
        u_rep = 0.5 * k_rep * (diff ** 2)
        scale = -k_rep * diff * (1.0 / (d_obs**3))
        grad_rep = d_obs_vec * scale
    else:
        u_rep = 0.0
        grad_rep = Vector2D(0.0, 0.0)

    total_potential = u_att + u_rep
    total_force = (grad_att + grad_rep) * -1.0  # Force is -∇U
    return total_potential, total_force


def simulate_gradient_descent(lr: float, steps: int = 6):
    print(f"\n--- Gradient Descent on Ravine (Learning Rate η = {lr:.2f}) ---")
    pos = Vector2D(2.0, 1.0)
    for step in range(steps):
        loss, grad = ravines_surface(pos.x, pos.y)
        print(f"Step {step}: Pos={pos} | Loss={loss:8.4f} | Grad_Norm={grad.magnitude():8.4f}")
        pos = Vector2D(pos.x - lr * grad.x, pos.y - lr * grad.y)
        if math.isnan(pos.x) or abs(pos.y) > 1e4:
            print(f">> DIVERGED TO INFINITY (Ping-pong explosion) at step {step+1}!")
            break


if __name__ == "__main__":
    print("=" * 65)
    print("1. ARTIFICIAL POTENTIAL FIELD NAVIGATION")
    print("=" * 65)
    robot = Vector2D(-2.0, 0.2)
    goal = Vector2D(2.0, 0.0)
    obs = Vector2D(0.0, 0.0)

    pot, force = potential_field(robot, goal, obs)
    print(f"Robot Pos: {robot} | Goal: {goal} | Obstacle: {obs}")
    print(f"Total Potential Energy U : {pot:.4f}")
    print(f"Steering Force Vector -∇U : {force} (Magnitude: {force.magnitude():.4f} N)")

    print("\n" + "=" * 65)
    print("2. LEARNING RATE STABILITY BENCHMARK")
    print("=" * 65)
    simulate_gradient_descent(lr=0.08)  # Stable
    simulate_gradient_descent(lr=0.11)  # Unstable explosion
```

---

## 5. Review Checkpoints & Deep-Dive Prompts

### Review Checkpoints

#### Checkpoint 1: Gradient and Directional Derivative Calculation
**Question:** Consider the scalar loss function `f(x, y) = x³ - 3·x·y + 2·y²`.
1. Compute the analytical gradient vector `∇f(x, y)`.
2. Evaluate the gradient at point `P = (2, 1)`.
3. Compute the directional derivative at point `P` in the direction of unit vector `û = [1/√2, 1/√2]ᵀ`.

**Solution:**
1. Compute partial derivatives:
   ```
   ∂f / ∂x = 3·x² - 3·y
   ∂f / ∂y = -3·x + 4·y
   ∇f(x, y) = [ 3·x² - 3·y , -3·x + 4·y ]ᵀ
   ```
2. Evaluate at `(2, 1)`:
   ```
   ∂f / ∂x = 3·(2)² - 3·(1) = 12 - 3 = 9
   ∂f / ∂y = -3·(2) + 4·(1) = -6 + 4 = -2
   ∇f(2, 1) = [ 9 , -2 ]ᵀ
   ```
3. Directional derivative `D_u(f) = ∇f · û`:
   ```
   D_u(f) = (9) · (1/√2) + (-2) · (1/√2) = 7 / √2 ≈ +4.9497
   ```

#### Checkpoint 2: The Chain Rule on Composite Neural Losses
**Question:** Let loss `L = (1/2)·(z - y_true)²` where `z = w₁·x₁ + w₂·x₂ + b`. 
Use the chain rule to derive the exact partial derivative `∂L / ∂w₁`.

**Solution:**
1. Identify intermediate variable: `z = w₁·x₁ + w₂·x₂ + b`.
2. Differentiate `L` with respect to `z`:
   ```
   ∂L / ∂z = 2 · (1/2) · (z - y_true) · (1) = (z - y_true)
   ```
3. Differentiate `z` with respect to parameter `w₁`:
   ```
   ∂z / ∂w₁ = x₁
   ```
4. Apply the single-variable chain rule:
   ```
   ∂L / ∂w₁ = (∂L / ∂z) · (∂z / ∂w₁) = (z - y_true) · x₁
   ```

---

### Deep-Dive Exploration Prompts

1. **The Hessian Matrix & Second-Order Curvature:** The Hessian matrix `H` contains all second-order partial derivatives `∂²f / ∂x_i ∂x_j`. How do the eigenvalues of `H` determine whether a critical point (`∇f = 0`) is a local minimum, local maximum, or a saddle point?
2. **Momentum & Adam Optimizers:** Heavy-ball momentum adds a velocity term `v[k+1] = β·v[k] + (1-β)·∇f`. How does this physical analogy of a rolling ball with mass prevent the optimizer from ping-ponging across steep ravine walls?
