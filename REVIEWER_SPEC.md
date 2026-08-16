# Axon Reviewer Specification & 7-Point Audit Rubric

## Purpose
The Reviewer Sub-Agent enforces rigorous standards across all Axon curriculum modules. Every concept must be audited against the 7-point rubric below before receiving approval (`[PASS]`) and being committed.

---

## 7-Point Quality Audit Rubric

| # | Checkpoint | Requirement | Pass Criteria |
|---|---|---|---|
| **1** | **Strict No-LaTeX & Clean Text Policy** | Zero LaTeX delimiters (`$`, `$$`, `\(`, `\)`, `\begin{matrix}`, `\frac`, etc.) in `README.md`. No decorative emojis in technical text. | Verified zero LaTeX occurrences. Clean Unicode math, text grids, and professional formatting without emoji clutter. |
| **2** | **Depth & Word Count** | Comprehensive, thorough explanations targeting 1,200–1,500 words. | Word count verified within 1,200–1,500 range (excluding code blocks). No hand-waving or skipping mathematical steps. |
| **3** | **5-Part Structure & Module Index** | Strictly adheres to the 5 standard parts specified in `CURRICULUM_SPEC.md` and links from module `README.md`. | All 5 headings present and fully articulated: 1. Intuitive Mental Model, 2. Derivations, 3. Dual Grounding (FRC & ML), 4. Failure Mode & Python Engine, 5. Checkpoints & Prompts. Module-level `README.md` exists and links to concept. |
| **4** | **Dual Grounding** | Concrete, detailed connections to both FRC Autonomous Robotics and Modern ML/AI. | Explicit, realistic robotics mechanism/problem (e.g. Swerve kinematics, gyro fusion) AND machine learning architecture/algorithm (e.g. dense layer, backprop). |
| **5** | **Failure Mode & Python Engine** | Clear analysis of a real-world catastrophe caused by naive implementation, accompanied by a runnable Python engine. | Includes real physical/algorithmic consequence of naive implementation, and complete, clean, runnable Python code comparing naive vs correct implementation. |
| **6** | **Interactive Demo & Dual-Theme Quality** | Standalone HTML5/Canvas visualizer in `demo.html` with Dark/Light theme toggle. | Zero external CDN scripts/fonts, responsive dark-mode and light-mode theme switching with `localStorage` persistence, touch/mouse drag interactivity, real-time telemetry panel, 60fps canvas rendering. |
| **7** | **Two-Way Curriculum Links** | Clear bidirectional linkages to previous and future concepts. | Explicit Backward Link(s) and Forward Link(s) referencing specific concept numbers and topics in `ROADMAP.md`. |

---

## Review Process & Verdict Output

The Reviewer sub-agent must execute a structured review with:
1. Checklist evaluation against each of the 7 checkpoints.
2. Exact word count, LaTeX scan, and theme toggle confirmation.
3. Final Verdict:
   - **`[PASS]`**: All 7 points met with exceptional quality. Ready to commit.
   - **`[REVISE]`**: List specific deficiencies and required fixes.
