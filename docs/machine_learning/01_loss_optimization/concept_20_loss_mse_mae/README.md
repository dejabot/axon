# Concept 20: Measuring Errors with Loss Functions (MSE & MAE)

How does a machine learning model or an autonomous robot know how well it is performing? Before we can make a model smarter, we must measure its mistakes with a single number: **Loss** (or **Cost**).

> Open the interactive demo below to adjust the model's prediction line and watch the residual errors, Mean Squared Error (MSE) penalty, and Mean Absolute Error (MAE) update in real time.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Loss Functions Interactive Visualizer"></iframe>

---

## The Everyday Robot Problem

Suppose you are tuning your robot's shooter flywheel. You test shooting at 5 different field distances and record the measured landing distances compared to your target goal:

* Distance 1: Target = 2.0 m, Model Shot = 2.2 m (Missed by +0.2 m)
* Distance 2: Target = 3.0 m, Model Shot = 2.9 m (Missed by -0.1 m)
* Distance 3: Target = 4.0 m, Model Shot = 5.0 m (Missed by +1.0 m — big miss!)

How do you combine these misses into a single score that tells you whether your shooter model is getting better or worse?

---

## 1. Residual Error (The Raw Difference)

For each shot `i`, the **residual error** is simply:

```python
error = prediction - actual
```

If we just added up raw errors, positive and negative misses would cancel out! For example, missing by `+1.0 m` and `-1.0 m` would average to `0.0 m` (perfect score), even though the robot missed every single shot.

To prevent cancellation, we have two classic solutions:
1. **Mean Absolute Error (MAE):** Take the absolute value of each error: `|prediction - actual|`.
2. **Mean Squared Error (MSE):** Square each error: `(prediction - actual)²`.

---

## 2. Python Implementation

Here is how we calculate both MSE and MAE in pure Python:

```python
# Actual target distances vs predicted landing distances
actuals = [2.0, 3.0, 4.0, 5.0]
predictions = [2.2, 2.9, 5.0, 4.8]

# 1. Mean Absolute Error (MAE)
mae = sum(abs(p - a) for p, a in zip(predictions, actuals)) / len(actuals)

# 2. Mean Squared Error (MSE)
mse = sum((p - a) ** 2 for p, a in zip(predictions, actuals)) / len(actuals)

print(f"MAE: {mae:.3f} meters")
print(f"MSE: {mse:.3f} meters²")
```

---

## 3. Math! Translation Sidebar

Here is how mathematicians and machine learning engineers write these equations:

```text
MAE = (1 / N) · ∑ |ŷᵢ - yᵢ|

MSE = (1 / N) · ∑ (ŷᵢ - yᵢ)²
```

### How to Read This Out Loud:
* `yᵢ` ("y sub i"): The actual true value for test sample `i`.
* `ŷᵢ` ("y-hat sub i"): The predicted value produced by your model for test sample `i`.
* `∑` ("sigma" / sum): Add up the terms for all `N` data points.
* `(1 / N)`: Divide by the total number of points `N` to get the average.

### MSE vs. MAE: When to Use Which?

| Loss Function | Formula | How it Treats Large Errors | Best For |
| :--- | :--- | :--- | :--- |
| **MSE (Mean Squared Error)** | `(p - a)²` | **Heavy quadratic penalty:** A 2-meter miss is penalized 4× more than a 1-meter miss! | Smooth gradients, standard regression, shooter calibration. |
| **MAE (Mean Absolute Error)** | `\|p - a\|` | **Linear penalty:** A 2-meter miss is penalized exactly 2× more than a 1-meter miss. | Robustness when sensor data has random outlier spikes. |

---

## 4. Bridge to Machine Learning & Robotics

* **Smooth Derivatives for Gradient Descent:** Why is MSE the gold standard in deep learning regression? Because squaring creates a smooth parabolic bowl curve whose derivative is clean and easy to calculate: `d/dŷ (ŷ - y)² = 2 · (ŷ - y)`.
* **Neural Network Output Heads:** In vision models that predict continuous values (such as the bounding box coordinates `[x, y, w, h]` or the robot's distance to target), the final loss layer minimizes MSE (or Smooth L1 loss).

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1: Loss & Optimization</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">ML Axon Home</a></div>
  <div><a href="../concept_21_cross_entropy_loss/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 21: Cross-Entropy Loss →</a></div>
</div>
