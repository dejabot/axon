# Concept 15: Multivariable Gradients & Hill Climbing

> **▶ Interactive Demo: [Potential Field & Gradient Visualizer](demo.html)**
>
> Open the interactive demo below to drag the robot on the 2D contour map and watch the gradient vector $\nabla U$ (uphill) and steering force $-\nabla U$ (downhill toward goal) update live.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Hiking in the Fog
Imagine you are hiking blindfolded on a foggy, hilly mountain. Your elevation (height) is given by a 2D terrain surface `z = f(x, y)`:
* `x` is your coordinate East-West.
* `y` is your coordinate North-South.

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="170" viewBox="0 0 300 170" style="max-width: 100%; height: auto;">
    <!-- Contours -->
    <ellipse cx="150" cy="85" rx="110" ry="55" fill="none" stroke="#334155" stroke-width="1.5" />
    <ellipse cx="150" cy="85" rx="70" ry="35" fill="none" stroke="#475569" stroke-width="1.5" />
    <!-- Current Point -->
    <circle cx="180" cy="85" r="5" fill="#38bdf8" />
    <!-- Uphill Arrow -->
    <line x1="180" y1="85" x2="230" y2="85" stroke="#fbbf24" stroke-width="3" />
    <circle cx="230" cy="85" r="3" fill="#fbbf24" />
    <text x="205" y="70" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="11">∇f (Uphill)</text>
    
    <!-- Downhill Arrow -->
    <line x1="180" y1="85" x2="130" y2="85" stroke="#4ade80" stroke-width="3" />
    <circle cx="130" cy="85" r="3" fill="#4ade80" />
    <text x="95" y="70" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="11">-∇f (Downhill)</text>
  </svg>
</div>

1. **Partial Derivative `∂f/∂x`:** If you freeze your North-South position and take one step **East**, how much does elevation change?
2. **Partial Derivative `∂f/∂y`:** If you freeze your East-West position and take one step **North**, how much does elevation change?
3. **The Gradient Vector `∇f`:** If you bundle both slopes into a 2D arrow `[∂f/∂x, ∂f/∂y]ᵀ`, this vector points in the direction of **Steepest Ascent** (the fastest way uphill).
4. **Gradient Descent `-∇f`:** To walk downhill to the lowest valley floor as fast as possible, step in the exact opposite direction: **`-∇f`**.

---

## 2. Solving It in Code: Artificial Potential Fields
In autonomous robotics, we steer around obstacles by creating a virtual energy surface `U(x, y)`:
* The goal is a low bowl pulling the robot in.
* Obstacles are tall mountains repelling the robot away.
* The steering force is simply **`-∇U`**!

```python
def potential_field_force(robot_x, robot_y, goal_x=4.0, goal_y=0.0, obs_x=2.0, obs_y=0.0):
    """
    Computes steering force vector -∇U to navigate toward goal while avoiding obstacle.
    """
    # 1. Attractive pull toward goal: U_att = 0.5 * dist_to_goal^2
    pull_x = -(robot_x - goal_x)
    pull_y = -(robot_y - goal_y)
    
    # 2. Repulsive push from obstacle
    dx_obs = robot_x - obs_x
    dy_obs = robot_y - obs_y
    dist_obs_sq = max(0.1, dx_obs**2 + dy_obs**2)
    push_x = (dx_obs / (dist_obs_sq**1.5)) * 2.0
    push_y = (dy_obs / (dist_obs_sq**1.5)) * 2.0
    
    # Total downhill steering force: F = -∇U
    fx = pull_x + push_x
    fy = pull_y + push_y
    return fx, fy

# Robot approaching obstacle at (2.0, 0.0)
fx, fy = potential_field_force(robot_x=1.5, robot_y=0.2)
print(f"Steering Force Vector: [{fx:.2f}, {fy:.2f}] N")
# Output automatically bends around the obstacle!
```

---

> 💡 **Math Sidebar: The Gradient Vector (Del / Nabla ∇)**
>
> In multivariable calculus, the gradient of a 2D scalar surface `f(x, y)` is written as:
>
> ```
>          [ ∂f / ∂x ]
>   ∇f =   [         ]
>          [ ∂f / ∂y ]
> ```
>
> **How to read this out loud:**
> * `∇` is pronounced *"del"* or *"nabla"*.
> * `∂` is the partial derivative symbol.
> * `∇f` is the arrow pointing straight uphill.
> * `-∇f` is the arrow pointing straight downhill (**Gradient Descent**).

---

## 3. Bridge to Machine Learning: Training Deep Neural Networks
In deep learning:
* A neural network has an error loss function `Loss(weights)`.
* Training the AI means finding the lowest point on this loss mountain using **Gradient Descent**:
  ```
  weights_new = weights_old - learning_rate · ∇Loss
  ```
* Calculating these partial derivatives layer by layer using the chain rule is called **Backpropagation**!

---

## 4. Review Checkpoints
### Checkpoint 1
Given the loss function `f(x, y) = x² + 3·y²`:
1. Find the partial derivatives `∂f/∂x` and `∂f/∂y`.
2. Compute the gradient vector `∇f` at `(2, 1)`.

**Solution:**
1. `∂f/∂x = 2·x`, `∂f/∂y = 6·y`.
2. At `(2, 1)`: `∇f = [2(2), 6(1)]ᵀ = [4, 6]ᵀ`.

---

### Checkpoint 2
Which direction should a robot or optimizer step to minimize loss as fast as possible?

**Solution:**
In the direction of **`-∇f` (Negative Gradient / Steepest Descent)**. At point `(2, 1)`, step along `[-4, -6]ᵀ`.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_14_accumulation_integrals/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 14: Integration & Accumulation</a></div>
  <div><a href="../README.md" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 4 Overview</a></div>
  <div><a href="../../05_probability/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 5: Probability →</a></div>
</div>
