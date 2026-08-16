# Axon 02: Machine Learning & Vision

Welcome to the **Machine Learning & Vision Axon**. This track develops deep learning from first principles—moving from multi-dimensional loss landscapes and gradient optimization to deep neural network layers, vector backpropagation, and real-time computer vision object detection.

---

## Modules in this Axon

### [1. Loss Functions & Optimization](01_loss_optimization/README.md)
* *The Real-World Problem:* How does an autonomous model measure its own mistakes and adjust its weights to improve?
* *Concepts:* Mean Squared Error (MSE), Binary & Categorical Cross-Entropy, Gradient Descent, Learning Rates, and Adam Optimizer.

---

### [2. Neural Layers & Activation Functions](02_neural_layers/README.md)
* *The Real-World Problem:* Why can't linear equations learn curved decision boundaries, and how do neurons fire?
* *Concepts:* Dense weight matrices, biases, non-linear activation functions (ReLU, GELU, Sigmoid, Tanh), and Universal Approximation.

---

### [3. Vector Backpropagation Engine](03_backpropagation/README.md)
* *The Real-World Problem:* How does a network with 10 million parameters calculate the exact slope for every single weight simultaneously?
* *Concepts:* Computational DAG graphs, the multivariate Chain Rule, vector gradients, and building an autograd engine in pure Python.

---

### [4. Computer Vision & Object Detection](04_computer_vision/README.md)
* *The Real-World Problem:* How does a robot detect, classify, and track game pieces or field targets from raw camera pixel streams at 60 FPS?
* *Concepts:* 2D Spatial Convolutions, Feature Maps, YOLO single-shot architectures, bounding box regression, and Non-Maximum Suppression (NMS).

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../math/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Previous Axon: Math Foundations</a></div>
  <div><a href="../README.md" style="color: var(--muted, #94a3b8); text-decoration: none;">Curriculum Home</a></div>
  <div><a href="../large_language_models/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Next Axon: Large Language Models →</a></div>
</div>
