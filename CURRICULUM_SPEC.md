# Axon Curriculum Authoring Specification

## Overview
Axon is a 25-concept curriculum designed for rigorous, first-principles mastery of applied mathematics, physical dynamics, modern control theory, deep machine learning, and autonomous robotics.

The curriculum is structured around a simple, two-level taxonomy: **Modules and Concepts**.

---

## 1. Hierarchy: Modules & Concepts

Axon uses exactly two organizational levels:
1. **Modules (1 through 5):** The major subject domains.
2. **Concepts (1 through 25):** The individual core topics and companion visualizers.

```
docs/
├── README.md                       <-- Curriculum overview and module links
└── modules/
    ├── 01_math_foundations/
    │   ├── README.md               <-- Module overview and concept directory links
    │   └── concept_01_vectors_matrices/
    │       ├── README.md           <-- Concept guide (1,200–1,500 words)
    │       └── demo.html           <-- Interactive visualizer (Standalone HTML5/Canvas)
```

The 5 Modules:
- **Module 1: Math Foundations** (Concepts 01–04)
- **Module 2: Machine Learning** (Concepts 05–08)
- **Module 3: Control & Physics** (Concepts 09–12)
- **Module 4: Swerve & Sensor Fusion** (Concepts 13–16)
- **Module 5: Reinforcement Learning & Agents** (Concepts 17–25)

---

## 2. Formatting & Style Rules

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

### B. Clean Professional Text (No Emojis / Decorative Icons)
- Avoid emojis or decorative icons in headings, section titles, and body markdown.
- Maintain a clean, professional, textbook-grade technical publication aesthetic.

### C. Word Count Target
- Every `README.md` must be a substantial, in-depth guide between **1,200 and 1,500 words**.
- No hand-waving or skipping algebraic steps.

---

## 3. The 5 Concept Guide Sections

Every concept `README.md` contains 5 clean, direct sections:

1. **1. Intuitive Mental Model**
   - Explain the concept using an intuitive real-world physical or geometric analogy before introducing any formal notation.
2. **2. Mathematical & Physical Derivations**
   - Derive the core formulas step-by-step from first principles.
   - Provide visual ASCII/Unicode diagrams, coordinate frames, and transformation grids.
3. **3. Dual Grounding: FRC Robotics & Modern ML**
   - **FRC Robotics Application:** Specific mechanism or autonomous control problem.
   - **Machine Learning Application:** Specific ML architectural component or algorithm.
4. **4. Classic Failure Mode & Python Engine**
   - Concrete analysis of real-world bugs from naive implementation.
   - Complete, self-contained, runnable Python code comparing naive vs correct implementation.
5. **5. Review Checkpoints & Deep-Dive Prompts**
   - 2 conceptual/mathematical questions with detailed worked solutions.
   - 2 deep-dive exploration prompts.
   - Explicit Backward Link(s) and Forward Link(s) connecting to other concepts.

---

## 4. Interactive Visualizer Specification (`demo.html`)

Every concept folder includes an interactive `demo.html` satisfying:
- **Zero External Dependencies:** No CDN libraries, no external scripts or fonts. Works 100% offline.
- **Top-Right Theme Toggle:** Dark Mode (default) and Light Mode with instant cross-page synchronization via `localStorage ('axon_theme')`.
- **Input Controls:** Sliders, buttons, and toggles with live numeric readouts.
- **Canvas Visualizer:** HTML5 2D Canvas rendering with crisp DPI scaling and contrast-calibrated colors.
- **Mobile & Touch Ready:** Full support for touch events alongside mouse drag events.
- **Real-Time Telemetry:** Live mathematical statistics updating at 60 FPS.
