# Module 3: Vector Backpropagation Engine

Welcome to **Module 3: Vector Backpropagation Engine**. In this module, we demystify the inner mechanics of automatic differentiation (Autograd)—the engine behind PyTorch, TensorFlow, and all modern deep learning.

---

## Concepts in this Module
* **[Concept 01: Computational Graphs & Vector Chain Rule](01_concept_computational_graphs/)**
  * *The Everyday Problem:* How does a change in an early motor parameter or weight ripple through multiple calculations to affect the final loss?
  * *Code & Math:* Directed Acyclic Graphs (DAG), forward pass values, backward pass local derivatives, and the multivariate Chain Rule `dL/dx = dL/dy · dy/dx`.
  * *Visualizer:* [01_concept_computational_graphs/demo.html](01_concept_computational_graphs/demo.html)

* **[Concept 02: Building an Autograd Engine in Pure Python](02_concept_autograd_engine/)**
  * *The Everyday Problem:* How do PyTorch and neural network libraries calculate exact gradients for millions of parameters automatically without manual calculus?
  * *Code & Math:* The 30-line micro-autograd `Value` object, operator overloading (`__add__`, `__mul__`), and topological sort backward traversal.
  * *Visualizer:* [02_concept_autograd_engine/demo.html](02_concept_autograd_engine/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../02_neural_layers/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 2: Neural Layers</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">ML Axon Home</a></div>
  <div><a href="01_concept_computational_graphs/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 25: Computational Graphs →</a></div>
</div>
