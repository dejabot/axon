# Concept 01: Computational Graphs & Vector Chain Rule

How does a computer calculate the exact derivative for every single weight in a 100-layer neural network? It doesn't write out a giant calculus formula by hand. Instead, it breaks the math down into a **Computational Graph** and applies the **Chain Rule** backward!

> Open the interactive demo below to trigger a Forward Pass (computing values left-to-right) followed by a Backward Pass (flowing gradient derivatives right-to-left).

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Computational Graph Interactive Visualizer"></iframe>

---

## The Everyday Robot Problem

Suppose you calculate your robot's shooter landing distance through a chain of 3 steps:

1. **Gearbox:** `flywheel_rpm = 3.0 · motor_speed`
2. **Wheel Surface:** `exit_velocity = 0.05 · flywheel_rpm`
3. **Trajectory & Loss:** `loss = (exit_velocity - 12.0)²`

If you want to know how much tweaking `motor_speed` will reduce the `loss`, you need the derivative:

```text
dLoss / d(motor_speed)
```

Instead of solving one giant equation, the **Chain Rule** states that we can simply compute the local slope at each step and **multiply them together**:

```text
dLoss / d(motor_speed) = (dLoss / d_exit_velocity) · (d_exit_velocity / d_flywheel_rpm) · (d_flywheel_rpm / d_motor_speed)
```

---

## 1. Local Derivatives at Each Step

Let's look at each step individually:
* **Step 1:** `flywheel_rpm = 3.0 · motor_speed`
  * Local slope: `d_rpm / d_speed = 3.0`
* **Step 2:** `exit_velocity = 0.05 · flywheel_rpm`
  * Local slope: `d_vel / d_rpm = 0.05`
* **Step 3:** `loss = (exit_velocity - 12.0)²`
  * Local slope: `d_loss / d_vel = 2 · (exit_velocity - 12.0)`

If `exit_velocity = 10.0 m/s` (we shot too short by -2.0 m/s):
* `d_loss / d_vel = 2 · (10.0 - 12.0) = -4.0`

Now, multiply them backward:
```text
dLoss / d(motor_speed) = (-4.0) · (0.05) · (3.0) = -0.60
```

This tells us: If we increase `motor_speed` by `+1.0`, our `loss` will drop by `-0.60`!

---

## 2. Solving It in Code (Java)

### First-Principles Java: Computational Graph Forward & Backward Passes
```java
public class ComputationalGraph {
    public static void main(String[] args) {
        // --- Forward Pass (Left to Right) ---
        double motorSpeed = 66.67;
        double flywheelRpm = 3.0 * motorSpeed;            // 200.0 RPM
        double exitVelocity = 0.05 * flywheelRpm;         // 10.0 m/s
        double targetVelocity = 12.0;
        double loss = Math.pow(exitVelocity - targetVelocity, 2); // 4.0 (m/s)^2

        // --- Backward Pass (Right to Left via Chain Rule) ---
        // 1. dLoss / d(exitVelocity)
        double dLoss_dVel = 2.0 * (exitVelocity - targetVelocity); // -4.0

        // 2. dLoss / d(flywheelRpm) = dLoss/dVel * dVel/dRpm
        double dLoss_dRpm = dLoss_dVel * 0.05;                     // -0.20

        // 3. dLoss / d(motorSpeed) = dLoss/dRpm * dRpm/dSpeed
        double dLoss_dSpeed = dLoss_dRpm * 3.0;                    // -0.60

        System.out.printf("Forward Loss: %.2f%n", loss);
        System.out.printf("Gradient dLoss / d(motorSpeed): %.2f%n", dLoss_dSpeed);
    }
}
```

---

## 3. Math! Translation Sidebar

Here is the general Chain Rule written in calculus notation:

```text
dz / dx = (dz / dy) · (dy / dx)
```

For a deep chain of `K` intermediate steps:

```text
dLoss / dx = ∏ (dx_(i+1) / dx_i)
```

### How to Read This Out Loud:
* `dz / dx` ("d z by d x" or "the derivative of z with respect to x"): How much `z` changes when `x` wiggles.
* `∏` ("capital pi" / product): Multiply all the local derivatives together along the path from output to input.

---

## 4. Bridge to Machine Learning

* **Autograd Graphs:** Every neural network framework (PyTorch, JAX, TensorFlow) builds a computational Directed Acyclic Graph (DAG) during the forward pass.
* **Backpropagation:** During `.backward()`, the framework traverses the graph in reverse topological order, multiplying local Jacobians to deliver exact gradients to every weight simultaneously!

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 3: Backpropagation</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">ML Axon Home</a></div>
  <div><a href="../02_concept_autograd_engine/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 26: Micro-Autograd Engine →</a></div>
</div>
