# Axon Curriculum Specification & Style Guide

## 1. Pedagogical Architecture & Style Guidelines

Axon is a first-principles curriculum designed for students and engineers learning mathematics, physics, machine learning, and autonomous robotics (specifically FIRST Robotics Competition / FRC and modern AI systems).

Every concept guide adheres to the following principles:

1. **FRC & Everyday Grounding First:**
   - Start with a concrete, relatable scenario (e.g. *"Our robot is at (2m, 3m) and needs to aim at the target"*).
   - Use plain, everyday language. Avoid assumed terminology (e.g. do not introduce $\hat{i}$ and $\hat{j}$ without grounding them as simple 1-step grid moves).
2. **Simple Python Code First:**
   - Show how the problem is calculated in 5–15 lines of clean, readable Python with descriptive variable names before presenting formal equations.
3. **Clean, Focused Interactive Visualizers:**
   - Include a simple, non-distracting HTML5/Canvas visualizer in `demo.html` with fixed dark/light theme toggle.
4. **"Math!" Sidebars & Step-by-Step Equations:**
   - Use `> 💡 Math Sidebar:` or `> 📐 Math Translation:` callouts to introduce formal terminology:
     - *"This is the mathematical term for what we just built in code..."*
     - *"How to read this equation out loud (symbol by symbol)..."*
5. **Bridge to Machine Learning:**
   - Explicitly show how the same mathematical concept is used in modern AI and neural networks.
6. **2 Review Questions:**
   - Provide 2 clear, bite-sized checkpoints with step-by-step arithmetic and explanations.
7. **Strict No-LaTeX Policy:**
   - Use clean, standard Unicode text (`x² + y² = d²`, `θ = atan2(y, x)`, `∇f = [∂f/∂x, ∂f/∂y]ᵀ`) rather than LaTeX delimiters (`$`, `$$`, `\frac`, etc.).

---

## 2. Curriculum Module Hierarchy

```
axon/
├── README.md                                  <-- Repository root curriculum index
└── docs/
    ├── README.md                              <-- Curriculum documentation overview
    ├── assets/
    │   ├── css/site.css                       <-- Jekyll documentation styles
    │   ├── axon.css                           <-- Shared design tokens for interactive demos
    │   └── theme.js                           <-- Top-right floating ☾/☀ toggle & sync
    └── modules/
        ├── 01_geometry/                       <-- Module 1: Geometry (Concepts 01–03)
        ├── 02_trigonometry/                   <-- Module 2: Trigonometry & Angles (Concepts 04–07)
        ├── 03_linear_algebra/                 <-- Module 3: Linear Algebra (Concepts 08–11)
        ├── 04_calculus/                       <-- Module 4: Calculus & Motion (Concepts 12–15)
        └── 05_machine_learning/               <-- Module 5: Machine Learning (Concepts 16–20)
```
