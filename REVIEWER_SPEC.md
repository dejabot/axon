# Axon Reviewer Specification & 7-Point Audit Rubric

## Purpose
The Reviewer Sub-Agent enforces rigorous standards across all Axon curriculum modules. Every concept must be audited against the 7-point rubric below before receiving approval (`[PASS]`) and being committed.

---

## 7-Point Quality Audit Rubric

| # | Checkpoint | Requirement | Pass Criteria |
|---|---|---|---|
| **1** | **Strict No-LaTeX & Clean Text Policy** | Zero LaTeX delimiters (`$`, `$$`, `\(`, `\)`, `\begin{matrix}`, `\frac`, etc.) in `README.md`. No decorative emojis in technical text. | Verified zero LaTeX occurrences. Clean Unicode math, text grids, and professional formatting without emoji clutter. |
| **2** | **Depth & Word Count** | Comprehensive, thorough explanations targeting 1,200–1,500 words. | Word count verified within 1,200–1,500 range (excluding code blocks). No hand-waving or skipping mathematical steps. |
| **3** | **Flattened Taxonomy & 5 Sections** | Follows the two-level hierarchy (Modules & Concepts) and 5 standard sections without Curriculum Linkages section. | Contains sections 1. Intuitive Mental Model, 2. Derivations, 3. Dual Grounding, 4. Failure Mode & Python Engine, 5. Checkpoints & Prompts. |
| **4** | **Embedded Visuals & Interactive Demos** | Zero ASCII art. Contains embedded companion visualizer iframe and responsive vector SVGs for geometric figures. | Verified zero ASCII box/line art. Companion `demo.html` is embedded via `<iframe>` alongside crisp inline SVGs for mathematical figures. |
| **5** | **Dual Grounding** | Concrete, detailed connections to both FRC Autonomous Robotics and Modern ML/AI. | Explicit, realistic robotics mechanism/problem (e.g. Swerve kinematics, gyro fusion, 3D quaternion orientations) AND machine learning architecture/algorithm (e.g. dense layer, backprop, quaternion neural embeddings). |
| **6** | **Failure Mode & Python Engine** | Clear analysis of a real-world catastrophe caused by naive implementation, accompanied by a runnable Python engine. | Includes real physical/algorithmic consequence of naive implementation, and complete, clean, runnable Python code comparing naive vs correct implementation. |
| **7** | **Interactive Demo & Dual-Theme Quality** | Standalone HTML5/Canvas visualizer in `demo.html` with top-right Dark/Light theme toggle. | Zero external CDN scripts/fonts, responsive dark-mode and light-mode theme switching with `localStorage` persistence, touch/mouse drag interactivity, real-time telemetry panel, 60fps canvas rendering. |

---

## Review Process & Verdict Output

The Reviewer sub-agent must execute a structured review with:
1. Checklist evaluation against each of the 7 checkpoints.
2. Exact word count, LaTeX scan, SVG/visual verification, and theme toggle confirmation.
3. Final Verdict:
   - **`[PASS]`**: All 7 points met with exceptional quality. Ready to commit.
   - **`[REVISE]`**: List specific deficiencies and required fixes.
