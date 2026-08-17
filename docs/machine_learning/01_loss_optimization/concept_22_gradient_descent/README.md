# Concept 22: Gradient Descent & Learning Rates

Once we have measured our errors with a loss function (Concepts 20 & 21), how do we automatically tune our parameters to make the loss as small as possible? 

The engine of modern AI is **Gradient Descent**.

> Open the interactive demo below to adjust the learning rate (step size), press "Step", and watch an optimization ball roll down the loss landscape toward the minimum.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Gradient Descent Interactive Visualizer"></iframe>

---

## The Everyday Robot Problem

Imagine you are standing on a foggy hill at night. You cannot see the bottom of the valley (where the error is lowest), but you can feel the slope of the ground beneath your feet.

Which way should you step to reach the bottom?
1. Feel the slope beneath your feet (the **Gradient**).
2. If the ground slopes upward to your right (positive slope), step to your **left**.
3. If the ground slopes upward to your left (negative slope), step to your **right**.
4. Always step in the **opposite direction of the uphill slope**!

---

## 1. The Gradient Descent Update Rule

In code, tuning a parameter `w` (like a shooter flywheel speed or a neural network weight) takes just one line:

```python
w_new = w - learning_rate * gradient
```

Why the minus sign?
* If `gradient > 0` (slope is pointing uphill to the right), subtracting a positive number moves `w` to the **left** (downhill).
* If `gradient < 0` (slope is pointing uphill to the left), subtracting a negative number moves `w` to the **right** (downhill).

---

## 2. Solving It in Code (Java)

### First-Principles Java: Gradient Descent Loop
```java
public class GradientDescent {
    public static void main(String[] args) {
        // Initial parameter guess
        double w = 8.0;
        double learningRate = 0.20;

        for (int step = 0; step < 20; step++) {
            // Loss = (w - 3.5)^2 + 2.0
            double loss = Math.pow(w - 3.5, 2) + 2.0;

            // Derivative: dLoss / dw = 2 * (w - 3.5)
            double gradient = 2.0 * (w - 3.5);

            // Step downhill: w_new = w - lr * gradient
            w = w - learningRate * gradient;

            System.out.printf("Step %02d: w = %.4f | Loss = %.4f | Slope = %.4f%n",
                step, w, loss, gradient);
        }
    }
}
```

---

## 3. Python Implementation

Here is gradient descent finding the minimum of a parabolic loss function `Loss(w) = (w - 3.5)² + 2.0` in 10 lines of code:

```python
# Initial guess for parameter w
w = 8.0
learning_rate = 0.20

for step in range(20):
    # Loss = (w - 3.5)^2 + 2.0
    loss = (w - 3.5) ** 2 + 2.0
    
    # Derivative: dLoss / dw = 2 * (w - 3.5)
    gradient = 2.0 * (w - 3.5)
    
    # Step downhill
    w = w - learning_rate * gradient
    
    print(f"Step {step:02d}: w = {w:.4f} | Loss = {loss:.4f} | Slope = {gradient:.4f}")
```

Within 15 steps, `w` converges smoothly from `8.0` to exactly `3.5000` (the optimal value where loss is lowest)!

---

## 4. Math! Translation Sidebar

Here is how gradient descent is written in mathematics and machine learning textbooks:

```text
θ_(t+1) = θ_t - α · ∇L(θ_t)
```

### How to Read This Out Loud:
* `θ_t` ("theta sub t"): The parameter values at iteration step `t`.
* `θ_(t+1)` ("theta sub t plus one"): The updated parameter values for the next step.
* `α` ("alpha"): The **learning rate** scalar (e.g. `0.001` to `0.1`).
* `∇L` ("grad L" / "del L"): The gradient vector of the loss function containing all partial derivatives `[dL/dw₁, dL/dw₂, ...]`.

---

## 5. Bridge to Machine Learning & Optimizers

* **Stochastic Gradient Descent (SGD):** In massive datasets (like millions of vision frames), computing the gradient across all data at once is too slow. SGD computes the gradient on small random batches (e.g. 32 images at a time).
* **Momentum & Adam Optimizer:** Plain gradient descent can get trapped in flat plateaus or oscillate in steep canyons. Modern optimizers like **Adam** maintain a running average of past gradients (momentum) and adapt the learning rate individually for every weight in the network.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_21_cross_entropy_loss/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 21: Cross-Entropy Loss</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="../../02_neural_layers/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 2: Neural Layers →</a></div>
</div>
