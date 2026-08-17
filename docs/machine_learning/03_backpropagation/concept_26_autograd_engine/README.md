# Concept 26: Building an Autograd Engine in Pure Python

In Concept 25, we traced gradients through a computational graph by hand. Now, we will write a complete **Automatic Differentiation Engine (Autograd)**—the core foundation of PyTorch—in about 30 lines of pure Python!

> Open the interactive demo below to build and evaluate custom computational expressions and watch the autograd engine calculate exact gradients for every variable automatically.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Micro-Autograd Engine Interactive Visualizer"></iframe>

---

## The Everyday Robot Problem

Suppose you are writing an algorithm to optimize your robot's motor acceleration, arm feedforward voltage, and PID gains simultaneously. 

Writing out 20 pages of manual calculus derivatives by hand is tedious and error-prone. What if your code could record every math operation you perform, build a graph in the background, and calculate all partial derivatives automatically with a single call to `loss.backward()`?

---

## 1. The 30-Line `Value` Class

To build an autograd engine, we wrap raw floating-point numbers in a `Value` class that stores:
1. `data`: The scalar value (e.g. `3.0`).
2. `grad`: The derivative of the final output with respect to this value (starts at `0.0`).
3. `_prev`: The child nodes that produced this value.
4. `_backward`: A tiny function that applies the local Chain Rule.

```python
class Value:
    def __init__(self, data, _children=()):
        self.data = float(data)
        self.grad = 0.0
        self._prev = set(_children)
        self._backward = lambda: None

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other))
        
        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other))
        
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    def relu(self):
        out = Value(max(0.0, self.data), (self,))
        def _backward():
            self.grad += (1.0 if self.data > 0 else 0.0) * out.grad
        out._backward = _backward
        return out

    def backward(self):
        # 1. Build topological order of all nodes in the DAG
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        # 2. Base gradient: d(Out) / d(Out) = 1.0
        self.grad = 1.0
        
        # 3. Traverse in reverse order and propagate gradients!
        for node in reversed(topo):
            node._backward()
```

---

## 2. Using Our Autograd Engine

Now we can write math just like normal Python, and backpropagate with zero effort:

```python
# 1. Define input parameters
x = Value(2.0)
w = Value(3.0)
b = Value(1.0)

# 2. Forward pass: y = w * x + b
y = (w * x) + b           # y.data = 7.0

# 3. Loss: L = (y - 10.0)^2
target = Value(10.0)
diff = y + (target * -1.0) # diff.data = -3.0
loss = diff * diff        # loss.data = 9.0

# 4. Automatic differentiation!
loss.backward()

print(f"Loss: {loss.data:.2f}")
print(f"dL / dw: {w.grad:.2f}")   # Output: -12.00
print(f"dL / dx: {x.grad:.2f}")   # Output: -18.00
print(f"dL / db: {b.grad:.2f}")   # Output: -6.00
```

---

## 3. Math! Translation Sidebar

### Why `self.grad += ...` Instead of `self.grad = ...`?

When a single variable is used in more than one place (for example: `f = x * x`), the multivariable Chain Rule states that gradients from all branches **add together**:

```text
dL / dx = ∑ (dL / d_branchᵢ) · (d_branchᵢ / dx)
```

Using `+=` ensures that when multiple operations reuse the same weight, all gradient paths accumulate correctly without overwriting each other!

---

## 4. Bridge to PyTorch & Deep Learning

* **`torch.Tensor`:** PyTorch operates identically to our `Value` class, but instead of single scalars, it executes operations on multi-dimensional matrices and tensors in parallel on GPUs.
* **Training Loop:** Every deep learning training step in PyTorch follows the exact same 3-step rhythm:
  1. `loss = model(inputs)` (Forward Pass)
  2. `loss.backward()` (Backprop through computational graph)
  3. `optimizer.step()` (Gradient descent update)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_25_computational_graphs/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 25: Computational Graphs</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 3 Overview</a></div>
  <div><a href="../../04_computer_vision/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 4: Computer Vision →</a></div>
</div>
