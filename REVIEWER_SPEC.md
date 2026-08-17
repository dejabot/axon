# Axon Reviewer Specification & 7-Point Audit Rubric

## Purpose
The Reviewer Sub-Agent enforces rigorous standards across all Axon curriculum modules. Every concept must be audited against the 7-point rubric below before receiving approval (`[PASS]`) and being committed.

---

## The Standard Concept Structure

Every concept `README.md` follows this six-section shape, in this order:

1. **The Real-World Problem** — an FRC or everyday scenario, stated in plain language with a diagram, that the reader cannot solve yet.
2. **Building the Math** — the result derived step by step from something the reader already believes. No formula appears before its justification.
3. **"Math!" Sidebars** — formal notation introduced as a translation of the prose, with an explicit "how to read this out loud" line. These are interleaved into section 2 rather than gathered at the end.
4. **Code (Java & WPILib)** — first-principles Java that mirrors the derivation line for line, followed by the production WPILib class that replaces it.
5. **Bridge to Machine Learning & Modern Autonomy** — a concrete architecture or algorithm, not a vague gesture at "AI uses this too".
6. **Checkpoints & Exploration Prompts** — 2 review questions with fully worked solutions, then 2 open-ended deep-dive prompts.

The companion `demo.html` is embedded via `<iframe>` immediately under the title.

---

## 7-Point Quality Audit Rubric

| # | Checkpoint | Requirement | Pass Criteria |
|---|---|---|---|
| **1** | **Strict No-LaTeX & Clean Text Policy** | Zero LaTeX delimiters (`$`, `$$`, `\(`, `\)`, `\begin{matrix}`, `\frac`, etc.) in `README.md`. No decorative emojis in technical text. | Verified zero LaTeX occurrences. Clean Unicode math, text grids, and professional formatting without emoji clutter. |
| **2** | **Depth & Word Count** | Comprehensive, thorough explanations targeting 1,800–2,800 words. | Word count verified within 1,800–2,800 range (excluding code blocks and SVG markup). No hand-waving or skipping mathematical steps. A concept that lands under 1,800 words is almost certainly asserting results it should be deriving. |
| **3** | **Flattened Taxonomy & 6 Sections** | Follows the two-level hierarchy (Modules & Concepts) and the six standard sections defined above. | Contains 1. Real-World Problem, 2. Building the Math, 3. "Math!" sidebars, 4. Java & WPILib code, 5. ML/Autonomy bridge, 6. Checkpoints & Prompts. |
| **4** | **No Black Boxes** | Every formula is derived, not asserted. Named prerequisite techniques are taught, not skipped. | Each result traces back to a stated starting assumption. Foundational named methods (e.g. SOH-CAH-TOA, the separating axis idea) appear explicitly rather than being silently assumed. |
| **5** | **Embedded Visuals & Interactive Demos** | Zero ASCII art. Contains embedded companion visualizer iframe and responsive vector SVGs for geometric figures. | Verified zero ASCII box/line art. Companion `demo.html` is embedded via `<iframe>` alongside crisp inline SVGs that render correctly in both themes. |
| **6** | **Dual Grounding** | Concrete, detailed connections to both FRC Autonomous Robotics and Modern ML/AI. | Explicit, realistic robotics mechanism/problem (e.g. swerve kinematics, gyro fusion, field-oriented drive) AND a named machine learning architecture/algorithm (e.g. rotary position embeddings, IoU-based detection loss, k-nearest neighbours in embedding space). |
| **7** | **Interactive Demo & Dual-Theme Quality** | Standalone HTML5/Canvas visualizer in `demo.html`. | Zero external CDN scripts/fonts, loads the shared `assets/theme.js` and `assets/axon.css`, repaints on the `axon-theme-changed` event, touch/mouse drag interactivity, real-time telemetry panel, smooth canvas rendering. |

---

## Language Policy

Teaching code is **Java with WPILib**, matching CURRICULUM_SPEC rule 3. Each code section shows first-principles Java first, then the production WPILib equivalent that a real robot project would use. Python appears only when the topic is itself a Python ecosystem (for example PyTorch tensor shapes in the machine learning axon).

---

## Review Process & Verdict Output

The Reviewer sub-agent must execute a structured review with:
1. Checklist evaluation against each of the 7 checkpoints.
2. Exact word count, LaTeX scan, SVG/visual verification, and theme toggle confirmation.
3. Link check: every relative link in the concept and its module index resolves to a file that exists.
4. Final Verdict:
   - **`[PASS]`**: All 7 points met with exceptional quality. Ready to commit.
   - **`[REVISE]`**: List specific deficiencies and required fixes.
