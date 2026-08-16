# Axon Curriculum Authoring Specification

## Overview
Axon is a 25-concept curriculum designed for rigorous, first-principles mastery of applied mathematics, physical dynamics, modern control theory, deep machine learning, and autonomous robotics.

The curriculum is structured around a two-level taxonomy: **Modules and Concepts**.

---

## 1. Hierarchy: Modules & Concepts

Axon uses two organizational levels:
1. **Modules (1 through 5):** The major subject domains.
2. **Concepts (1 through 25):** The individual core topics and companion visualizers.

```
axon/
├── README.md                       <-- Repository root curriculum overview
└── docs/
    ├── README.md                   <-- Curriculum documentation overview
    ├── assets/
    │   ├── axon.css                <-- Shared design system tokens & theme styles
    │   └── theme.js                <-- Floating dark/light toggle & local storage sync
    └── modules/
        ├── 01_math_foundations/
        │   ├── README.md           <-- Rendered by default when browsing the module directory
        │   └── concept_01_vectors_matrices/
        │       ├── README.md       <-- Rendered by default when browsing the concept directory
        │       └── demo.html       <-- Standalone interactive visualizer (HTML5/Canvas)
```

The 5 Modules:
- **Module 1: Math Foundations** (Concepts 01–04, including 2D/3D Quaternions)
- **Module 2: Machine Learning** (Concepts 05–08)
- **Module 3: Control & Physics** (Concepts 09–12)
- **Module 4: Swerve & Sensor Fusion** (Concepts 13–16)
- **Module 5: Reinforcement Learning & Agents** (Concepts 17–25)

## 2. Pedagogical Architecture: From High-School Math to Advanced ML & Robotics

Axon is specifically designed to provide an intuitive, first-principles on-ramp for students with high-school algebra, geometry, and trigonometry, bridging them into the university-level rigor of [*Mathematics for Machine Learning* (MML)](https://mml-book.github.io/book/mml-book.pdf) by Deisenroth, Faisal, and Ong.

### Mapping to the MML Textbook Foundations

| MML Book Chapter | Core Mathematical Topics | Axon Curriculum Alignment |
|---|---|---|
| **Ch 2: Linear Algebra** | Vector spaces, basis, linear independence, linear mappings, matrix rank | **Module 1 (Concept 01)** & **Module 4 (Concept 13)** |
| **Ch 3: Analytic Geometry** | Norms, inner products, orthogonality, projections, 2D/3D rotations | **Module 1 (Concepts 01, 02)** |
| **Ch 4: Matrix Decompositions** | Determinants, eigenvalues/eigenvectors, SVD, Cholesky | **Module 1 (Concept 01)**, **Module 2 (Concept 08)** & **Module 3 (Concept 12)** |
| **Ch 5: Vector Calculus** | Univariate differentiation, gradients, Jacobians, Hessians, Chain Rule, Backprop | **Module 1 (Concepts 03, 04)** & **Module 2 (Concepts 06, 07)** |
| **Ch 6: Probability & Distributions** | Probability space, Bayes' rule, Gaussian distributions, Covariance matrices | **Module 4 (Concepts 15, 16: AprilTags & EKF)** |
| **Ch 7: Continuous Optimization** | Gradient descent, learning rates, momentum, constrained optimization | **Module 1 (Concept 04)** & **Module 2 (Concept 05)** |
| **Part II: ML Problems (Ch 8–12)** | Linear regression, dimensionality reduction (PCA), classification | **Module 2 (Concepts 05–08)** & **Module 5 (Concepts 17–25)** |

---

## 3. Directory & Colocation Architectures

### A. The Strict NO-LaTeX Policy
- **Never use LaTeX delimiters** (`$`, `$$`, `\(`, `\)`, `\[`, `\]`, `\begin{matrix}`, `\frac{...}`, etc.).
- Reason: LaTeX delimiters render inconsistently across markdown readers (GitHub web, mobile apps, local IDE previews, raw terminal cat/less) and require heavy JavaScript parsing engines.
- **Use Unicode Math & Clean Text Grids:**
  - Symbols: `·` (dot product), `×` (cross product), `∇` (gradient), `∂` (partial derivative), `∫` (integral), `∑` (sum), `ᵀ` (transpose), `θ` (theta), `ω` (angular velocity), `α` (alpha), `β` (beta), `λ` (lambda), `σ` (sigma), `Δ` (delta), `dt` (infinitesimal time), `√` (square root), `≈` (approximately equal), `≠`, `≤`, `≥`, `∈`, `ℝ`.
  - Exponents and Subscripts: `x²`, `y³`, `x_i`, `v_trans`, `k_p`, `W^[l]`, `a^[l]`, `q_w`, `q_x`.

### B. Clean Embedded Visuals & Interactive Demos (No ASCII Art)
- **No ASCII character diagrams or pseudo-text art.**
- **Embedded Interactive Demos:** Embed the companion visualizer directly at the top of the guide via `<iframe src="demo.html" width="100%" height="560" style="border:1px solid var(--border-color, #334155); border-radius:10px; margin: 16px 0;"></iframe>`.
- **Inline Vector SVGs:** For specific mathematical geometries (coordinate transformations, unit circles, quaternion sphere projections, S-curves, contour gradient fields), embed clean, responsive inline SVGs with adaptive stroke colors for crisp rendering.

### C. Clean Professional Text
- Avoid emojis or decorative icons in headings, section titles, and body markdown.
- Maintain a clean, professional, textbook-grade technical publication aesthetic.

### D. Word Count Target
- Every `README.md` must be a substantial, in-depth guide between **1,200 and 1,500 words** (excluding code blocks).

---

## 3. The 5 Concept Guide Sections

Every concept `README.md` contains 5 clean, direct sections:

1. **1. Intuitive Mental Model**
   - Physical or geometric intuition with embedded interactive visualizer.
2. **2. Mathematical & Physical Derivations**
   - Derivations from first principles with responsive inline SVG geometric figures.
3. **3. Dual Grounding: FRC Robotics & Modern ML**
   - **FRC Robotics Application:** Specific mechanism or autonomous control problem.
   - **Machine Learning Application:** Specific ML architectural component or algorithm.
4. **4. Classic Failure Mode & Python Engine**
   - Concrete analysis of real-world bugs from naive implementation.
   - Complete, self-contained, runnable Python code comparing naive vs correct implementation.
5. **5. Review Checkpoints & Deep-Dive Prompts**
   - 2 conceptual/mathematical questions with detailed worked solutions.
   - 2 deep-dive exploration prompts.

*(Note: Curriculum Linkages section has been removed to keep content focused directly on concept mastery.)*

---

## 4. Interactive Visualizer Specification (`demo.html`)

Every concept folder includes an interactive `demo.html` satisfying:
- **Zero External Dependencies:** No CDN libraries, no external scripts or fonts. Works 100% offline.
- **Top-Right Theme Toggle:** Dark Mode (default) and Light Mode with instant cross-page synchronization via `localStorage ('axon_theme')`.
- **Input Controls:** Sliders, buttons, and toggles with live numeric readouts.
- **Canvas Visualizer:** HTML5 2D/3D Canvas rendering with crisp DPI scaling and contrast-calibrated colors.
- **Mobile & Touch Ready:** Full support for touch events alongside mouse drag events.
- **Real-Time Telemetry:** Live mathematical statistics updating at 60 FPS.
