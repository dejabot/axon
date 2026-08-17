# Concept 23: Linear Layers (Weights, Biases & Dot Products)

Every neural network—from a simple robot sensor filter to a 100-billion-parameter language model—is constructed from basic mathematical units called **Linear Layers** (also called **Dense** or **Fully-Connected** layers).

> Open the interactive demo below to adjust the weights and bias of a 2-input neuron and watch how it creates a linear decision boundary across sensor data.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Linear Layer Interactive Visualizer"></iframe>

---

## The Everyday Robot Problem

Suppose you want to predict your robot's **Battery Voltage** during an intense match based on two live sensor readings:
1. `x₁`: Total motor current draw (Amps).
2. `x₂`: Battery temperature (°C).

How do we combine these two numbers into an accurate voltage prediction?

---

## 1. What Are Weights and Biases?

A linear neuron performs a weighted sum plus an offset:

```text
predicted_voltage = (w₁ · current) + (w₂ · temperature) + bias
```

* **Weights (`w₁`, `w₂`):** Measure the **influence** (or sensitivity) of each input.
  * Higher current causes a voltage drop: `w₁ = -0.018 V/Amp`.
  * Higher heat increases internal resistance: `w₂ = -0.025 V/°C`.
* **Bias (`b`):** The **baseline intercept** when all inputs are zero.
  * When current is `0 Amps` and temp is `0 °C`, a fully-charged battery sits at rest: `b = 12.60 V`.

---

## 2. Python Implementation

In Python, computing a linear layer with 2 inputs and 1 output is a clean dot product:

```python
# Inputs: [Current = 120.0 Amps, Temperature = 35.0 °C]
inputs = [120.0, 35.0]

# Learned Weights & Baseline Bias
weights = [-0.018, -0.025]
bias = 12.60

# Linear Layer Output: y = dot_product(w, x) + b
output = sum(w * x for w, x in zip(weights, inputs)) + bias

print(f"Predicted Battery Voltage: {output:.2f} Volts")
# Output: 12.60 - (2.16) - (0.875) = 9.56 Volts
```

For multiple inputs and multiple outputs, this is written as matrix multiplication: `y = W @ x + b`.

---

## 3. Math! Translation Sidebar

Here is how linear layers are written in machine learning literature:

```text
y = W · x + b
```

For a single neuron `i` receiving `M` inputs:

```text
yᵢ = ∑ (wᵢⱼ · xⱼ) + bᵢ
```

### How to Read This Out Loud:
* `W` ("capital W"): The **Weight Matrix**, where each row represents the weights for one neuron.
* `x` ("vector x"): The **Input Vector** containing the incoming features.
* `b` ("vector b"): The **Bias Vector** that shifts the output up or down.
* `·` or `@`: Vector dot product / matrix multiplication.

---

## 4. Geometric Meaning: Separation Planes

In 2D space, the equation `w₁ · x₁ + w₂ · x₂ + b = 0` defines a straight line. 
* Everything on one side of the line produces a positive output (`y > 0` → Safe Battery).
* Everything on the other side produces a negative output (`y < 0` → Brownout Warning!).

The **weights** determine the tilt (angle) of the separation line, while the **bias** slides the line left or right across the field.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 2: Neural Layers</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">ML Axon Home</a></div>
  <div><a href="../concept_24_activation_functions/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 24: Activation Functions →</a></div>
</div>
