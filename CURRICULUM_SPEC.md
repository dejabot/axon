# Axon Curriculum Authoring Specification

## Overview
Axon is a 25-concept curriculum designed for rigorous, first-principles mastery of applied mathematics, physical dynamics, modern control theory, deep machine learning, and autonomous robotics.

Every concept in Axon follows strict structural, stylistic, and technical standards to maintain exceptional quality, depth, and accessibility.

---

## 1. Directory & File Structure

Every concept resides in its own isolated directory under `docs/modules/`:

```
docs/modules/
└── <module_dir>/
    └── <concept_dir>/
        ├── README.md               <-- Main conceptual guide (1,200–1,500 words)
        └── demo.html               <-- Interactive visualizer (Standalone HTML5/Canvas)
```

For Module 1:
- `docs/modules/01_math_foundations/concept_01_vectors_matrices/`
- `docs/modules/01_math_foundations/concept_02_trig_angle_topology/`
- `docs/modules/01_math_foundations/concept_03_motion_calculus/`
- `docs/modules/01_math_foundations/concept_04_multivariable_gradients/`

---

## 2. Strict Formatting Rules

### A. The Strict NO-LaTeX Policy
- **Never use LaTeX delimiters** (`$`, `$$`, `\(`, `\)`, `\[`, `\]`, `\begin{matrix}`, `\frac{...}`, etc.).
- Reason: LaTeX delimiters render inconsistently across markdown readers (GitHub web, mobile apps, local IDE previews, raw terminal cat/less) and require heavy JavaScript parsing engines.
- **Use Unicode Math & Clean Text Grids:**
  - Symbols: `·` (dot product), `×` (cross product), `∇` (gradient), `∂` (partial derivative), `∫` (integral), `∑` (sum), `ᵀ` (transpose), `θ` (theta), `ω` (angular velocity), `α` (alpha), `β` (beta), `λ` (lambda), `σ` (sigma), `Δ` (delta), `dt` (infinitesimal time), `√` (square root), `≈` (approximately equal), `≠`, `≤`, `≥`, `∈`, `ℝ`.
  - Exponents and Subscripts: `x²`, `y³`, `x_i`, `v_trans`, `k_p`, `W^[l]`, `a^[l]`.
  - Vectors and Matrices: Use clean text matrix representations or brackets:
    ```
    [ x ]          [ a  b ]
    [ y ]    and   [ c  d ]
    ```
    or row/transpose notation `v = [vx, vy, ω]ᵀ`.

### B. Word Count Target
- Every `README.md` must be a substantial, in-depth guide between **1,200 and 1,500 words**.
- No hand-waving or skipping algebraic steps.

---

## 3. The 5-Part Concept Guide Structure

Every concept `README.md` must contain exactly the following 5 parts:

1. **Part 1: The Intuitive Mental Model (Physical/Visual Analogy)**
   - Explain the concept using an intuitive real-world physical or geometric analogy before introducing any formal notation.
   - Clarify what question this mathematical tool answers.

2. **Part 2: Mathematical & Physical Derivations (No Black Boxes)**
   - Derive the core formulas step-by-step from first principles.
   - Provide visual ASCII/Unicode diagrams, coordinate frames, and transformation grids.
   - Explain every term, dimension, and physical unit.

3. **Part 3: Dual Grounding: FRC Autonomous Robotics & Modern ML/AI**
   - **FRC Robotics Application:** Specific, high-stakes mechanism or autonomous application (e.g., Swerve module kinematics, elevator gravity compensation, gyro odometry).
   - **Machine Learning & AI Application:** Specific ML architectural component (e.g., Dense layer transformations, backpropagation chain rule, loss gradient descent).

4. **Part 4: The Classic Failure Mode & From-Scratch Python Engine**
   - **The Classic Failure Mode:** Describe a notorious real-world bug that happens when this concept is implemented naively (e.g., 340° swerve spin, matrix singularity crash, discrete Euler drift, exploding gradient).
   - **From-Scratch Python Implementation:** A self-contained, clean Python class/script (standard library only or minimal numpy) demonstrating the correct formulation vs the naive buggy formulation.

5. **Part 5: Review Checkpoints & Deep-Dive Exploration Prompts**
   - **Review Checkpoints:** 2 conceptual/mathematical questions with detailed worked solutions and physical explanations.
   - **Deep-Dive Prompts:** 2 open-ended research or engineering questions connecting to advanced robotics/ML systems.
   - **Two-Way Links:** Explicit Backward Link(s) and Forward Link(s) connecting to other concepts in the curriculum.

---

## 4. Interactive Visualizer Specification (`demo.html`)

Every concept folder must include an interactive `demo.html` satisfying:
- **Zero External Dependencies:** No CDN libraries, no external scripts or fonts. Works 100% offline and locally via `file://`.
- **Theme & Styling:** Premium dark-mode palette (`#0a0d14` background, `#141923` cards, vibrant neon accents `#38bdf8`, `#4ade80`, `#f43f5e`, `#fbbf24`, `#a855f7`).
- **Input Controls:** Sliders, buttons, and toggles with live numeric readouts.
- **Canvas Visualizer:** HTML5 2D Canvas rendering with crisp DPI scaling, coordinate grid, vector arrows, animations, and active state indicators.
- **Mobile & Touch Ready:** Full support for touch events (`touchstart`, `touchmove`, `touchend`) alongside mouse drag events.
- **Real-Time Telemetry Panel:** Live mathematical statistics (e.g., matrix determinant, vector magnitude, angle error, gradient vector) updating at 60 FPS.
