# Concept 04: Multivariable Calculus, Gradients & The Chain Rule

```
       Module 1: Math Foundations  ➔  Concept 04: Gradients & Chain Rule
```

> **▶ Interactive Demo: [Multivariable Gradients & Potential Fields Visualizer](demo.html)**
>
> Open the visualizer in your browser or explore the embedded frame below to test scalar loss landscapes f(x, y), orthogonal gradient ascent vectors ∇f, and roll a particle downhill with momentum and learning rate controls.

<iframe src="demo.html" width="100%" height="560" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--code-bg, #0a0d14);"></iframe>

---

## 1. Intuitive Mental Model: Hiking Blindfolded in the Fog

Imagine you are hiking on a hilly terrain on a foggy day where you cannot see more than two inches in front of you. Underneath your feet, your elevation (height) is given by a function `z = f(x, y)`:
* `x` is your coordinate East-West.
* `y` is your coordinate North-South.

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="180" viewBox="0 0 300 180" style="max-width: 100%; height: auto;">
    <!-- Contours -->
    <ellipse cx="150" cy="90" rx="120" ry="60" fill="none" stroke="#334155" stroke-width="1.5" />
    <ellipse cx="150" cy="90" rx="80" ry="40" fill="none" stroke="#475569" stroke-width="1.5" />
    <ellipse cx="150" cy="90" rx="40" ry="20" fill="none" stroke="#64748b" stroke-width="1.5" />
    <!-- Current Point -->
    <circle cx="180" cy="90" r="5" fill="#38bdf8" />
    <!-- Ascent Vector -->
    <line x1="180" y1="90" x2="230" y2="90" stroke="#fbbf24" stroke-width="3" />
    <circle cx="230" cy="90" r="3" fill="#fbbf24" />
    <!-- Descent Vector -->
    <line x1="180" y1="90" x2="130" y2="90" stroke="#4ade80" stroke-width="3" />
    <circle cx="130" cy="90" r="3" fill="#4ade80" />
    
    <text x="210" y="75" fill="#fbbf24" font-family="monospace" font-weight="bold" font-size="11">∇f (Uphill)</text>
    <text x="95" y="75" fill="#4ade80" font-family="monospace" font-weight="bold" font-size="11">-∇f (Downhill)</text>
  </svg>
</div>

1. **Partial Derivative `∂f/∂x`:** If you freeze your North-South position and take one small step directly **East**, how much does your elevation change? That slope is the partial derivative with respect to `x`.
2. **Partial Derivative `∂f/∂y`:** If you freeze your East-West position and take one small step directly **North**, how much does your elevation change? That slope is the partial derivative with respect to `y`.
3. **The Gradient Vector `∇f`:** If you package both slopes together into a 2D arrow `[∂f/∂x, ∂f/∂y]ᵀ`, this vector points in the direction of **Steepest Ascent** (the fastest way uphill).
4. **Gradient Descent `-∇f`:** To walk downhill as quickly as possible (e.g. to minimize error in machine learning, or guide a robot to a goal), you step in the exact opposite direction: **`-∇f`**.

---

## 2. Core Mathematical Principles

### 1. The Gradient Vector
For a function `f(x, y)`:

```
          [ ∂f / ∂x ]
   ∇f =   [         ]
          [ ∂f / ∂y ]
```

* The **direction** of `∇f` is the fastest way uphill.
* The **magnitude** `||∇f|| = √((∂f/∂x)² + (∂f/∂y)²)` is the steepness of the slope.
* The gradient is always **perpendicular (orthogonal)** to the contour lines (level curves).

---

### 2. The Multivariable Chain Rule
In neural networks, the loss `L` depends on intermediate activations `y`, which depend on weights `w`.

If `L = f(y)` and `y = g(w)`, the rate of change is simply the product of their derivatives:

```
   dL / dw = (dL / dy) · (dy / dw)
```

In deep neural networks with millions of parameters, this exact same chain rule is called **Backpropagation**—passing error gradients backward from the output layer to the input layer.

---

## 3. Real-World Applications

### In Machine Learning: Gradient Descent Optimizer
When training an AI model with loss function `L(w)`:

```
   w_new = w_old - η · ∇L(w)
```
Where `η` (eta) is the **learning rate** (the step size).
* If `η` is too small: Learning takes forever.
* If `η` is too large: The optimizer overshoots the minimum and explodes into `NaN`.

### In Autonomous Robotics (FRC): Potential Fields Obstacle Avoidance
To navigate a robot toward a target while avoiding obstacle robots:
1. Create an attractive bowl pulling toward the goal: `U_att = (1/2)·k_att·(dist_to_goal)²`
2. Create a repulsive mountain pushing away from obstacles: `U_rep = (1/2)·k_rep·(1/dist_to_obs)²`
3. The steering force is simply **`-∇U_total`**! The robot effortlessly flows around defenders.

---

## 4. Python Implementation

Here is a clean implementation of 2D Gradient Descent and an Artificial Potential Field in pure Python:

```python
import math

def loss_surface(x, y):
    """
    A simple 2D bowl: f(x, y) = 0.5 * (x^2 + 4*y^2)
    Returns the loss value and the gradient [df/dx, df/dy].
    """
    loss = 0.5 * (x**2 + 4.0 * (y**2))
    df_dx = x
    df_dy = 4.0 * y
    return loss, [df_dx, df_dy]

def gradient_descent_step(x, y, learning_rate=0.1):
    """Takes one step downhill in the direction of -∇f."""
    loss, grad = loss_surface(x, y)
    x_new = x - learning_rate * grad[0]
    y_new = y - learning_rate * grad[1]
    return x_new, y_new, loss

# Start at position (3.0, 2.0) and take 5 steps downhill
x, y = 3.0, 2.0
print(f"Starting Point: ({x:.2f}, {y:.2f})")

for step in range(1, 6):
    x, y, loss = gradient_descent_step(x, y, learning_rate=0.15)
    print(f"Step {step}: pos=({x:+.3f}, {y:+.3f}) | loss={loss:.4f}")
```

---

## 5. Review Questions

### Question 1
Given the scalar elevation function `f(x, y) = 3·x² + 5·y²`:
1. Find the partial derivatives `∂f/∂x` and `∂f/∂y`.
2. Compute the gradient vector `∇f` at point `(2, 1)`.
3. Which direction should you step to decrease `f` as fast as possible?

**Answer:**
1. `∂f/∂x = 6·x`, `∂f/∂y = 10·y`
2. At `(2, 1)`: `∇f = [6(2), 10(1)]ᵀ = [12, 10]ᵀ`
3. Step in the direction of **`-∇f = [-12, -10]ᵀ`** (Steepest Descent).

---

### Question 2
What happens if you set the learning rate `η` too large when optimizing on a steep loss surface?

**Answer:**
The step size exceeds the width of the valley, causing the optimizer to overshoot the minimum and oscillate with increasing amplitude (ping-ponging), eventually diverging to infinity (`loss = NaN`).
