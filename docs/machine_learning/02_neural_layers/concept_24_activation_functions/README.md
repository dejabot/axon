# Concept 24: Non-Linear Activation Functions (ReLU, GELU, Sigmoid)

In Concept 23, we saw that a linear layer computes `y = W @ x + b`. But what happens if you stack two linear layers back-to-back?

```text
Layer 2 Output = W₂ · (W₁ · x + b₁) + b₂
               = (W₂ · W₁) · x + (W₂ · b₁ + b₂)
               = W_combined · x + b_combined
```

Multiplying matrices together just produces another straight line! A network with 1,000 linear layers cannot learn a circle, a curve, or the XOR gate.

To bend space and learn complex patterns, neural networks use **Non-Linear Activation Functions**.

> Open the interactive demo below to compare ReLU, GELU, and Sigmoid curves, and see how stacking activated neurons creates piecewise curves.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Activation Functions Interactive Visualizer"></iframe>

---

## 1. The Big Three Activation Functions

### 1. ReLU (Rectified Linear Unit)
The simplest and most popular activation function in deep learning:

```python
def relu(x):
    return max(0.0, x)
```

* If `x < 0`: Output is flat `0.0`.
* If `x >= 0`: Output is simply `x`.
* **Why it's great:** Blazing fast to compute on GPUs, and its derivative is either `0` or `1`, which prevents gradients from vanishing.

---

### 2. Solving It in Code (Java)

### First-Principles Java: Activation Functions
```java
public class ActivationFunctions {
    public static double relu(double x) {
        return Math.max(0.0, x);
    }

    public static double sigmoid(double x) {
        return 1.0 / (1.0 + Math.exp(-x));
    }

    public static double gelu(double x) {
        return 0.5 * x * (1.0 + Math.tanh(Math.sqrt(2.0 / Math.PI) * (x + 0.044715 * Math.pow(x, 3))));
    }

    public static void main(String[] args) {
        double[] logits = {-3.0, -1.0, 0.0, 1.0, 3.0};

        for (double z : logits) {
            System.out.printf("z = %5.1f | ReLU = %5.2f | Sigmoid = %5.3f | GELU = %5.3f%n",
                z, relu(z), sigmoid(z), gelu(z));
        }
    }
}
```

---

## 3. Sigmoid (The Gatekeeper)
Squashes any real number from `-∞` to `+∞` into a probability range between `0.0` and `1.0`:

```python
def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))
```

* **Best For:** Output layers of binary classifiers (e.g. `Game Piece Present? True / False`).

---

## 2. Python Implementation

Here is how different activations shape an array of raw neuron outputs (called **logits**):

```python
import math

logits = [-3.0, -1.0, 0.0, 1.0, 3.0]

relu_out = [max(0.0, z) for z in logits]
sigmoid_out = [1.0 / (1.0 + math.exp(-z)) for z in logits]

print("Raw Logits: ", logits)
print("ReLU Output:", relu_out)
print("Sigmoid Output: ", [round(s, 3) for s in sigmoid_out])
```

---

## 3. Math! Translation Sidebar

Here are the formal mathematical definitions:

```text
ReLU(z) = max(0, z)

σ(z) = 1 / (1 + e^(-z))

GELU(z) = z · Φ(z)
```

### How to Read This Out Loud:
* `ReLU(z)` ("ree-loo of z"): The rectified linear activation of input `z`.
* `σ(z)` ("sigma of z"): The sigmoid logistic function.
* `e^(-z)` ("e to the negative z"): Euler's number `e ≈ 2.71828` raised to `-z`.
* `Φ(z)` ("phi of z"): The cumulative distribution function of the standard normal distribution.

---

## 4. The Universal Approximation Theorem

Why are non-linear activations so powerful?

By combining just two ReLU neurons with different slopes and offsets:
* `Neuron 1: h₁ = max(0, x - 1)` (turns on at `x = 1`)
* `Neuron 2: h₂ = max(0, x - 3)` (turns on at `x = 3`)
* `Output: y = h₁ - h₂`

You can create a flat step, a bump, a triangle, or a curve! According to the **Universal Approximation Theorem**, a neural network with just one hidden layer and non-linear activations can approximate **any continuous function in the universe** to arbitrary precision.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_23_dense_layers/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 23: Linear Layers</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../../03_backpropagation/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 3: Backpropagation →</a></div>
</div>
