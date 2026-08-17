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

**Index pages link to concepts, never to demos.** Axon and module README files list concepts and link to the concept directory only. A demo is an implementation detail of the concept that owns it — it may be rewritten, split or replaced — so it is reached by reading the concept, not from a table of contents. Do not add "Interactive Visualizer" links to any index.

**Length follows the topic.** These six sections are a shape, not a quota. A concept built on a theorem — the Pythagorean theorem, the ray-casting parity argument, the separating axis — earns a long "Building the Math". A concept that is a definition plus its applications, such as linear interpolation, does not, and inflating it with adjacent material produces a worse page than a short honest one. When in doubt, cut. The test for every paragraph is whether it derives something or prevents a real bug; if it does neither, delete it.

---

## 7-Point Quality Audit Rubric

| # | Checkpoint | Requirement | Pass Criteria |
|---|---|---|---|
| **1** | **Strict No-LaTeX & Clean Text Policy** | Zero LaTeX delimiters (`$`, `$$`, `\(`, `\)`, `\begin{matrix}`, `\frac`, etc.) in `README.md`. No decorative emojis in technical text. | Verified zero LaTeX occurrences. Clean Unicode math, text grids, and professional formatting without emoji clutter. |
| **2** | **Depth Proportionate to the Topic** | A concept runs as long as its material genuinely requires, and no longer. Most land at 1,800–2,800 words (30–45 min); some legitimately land far shorter. | No hand-waving, no skipped steps — **and no padding**. Judge against the topic, not a target. A concept containing a real derivation that lands under 1,800 words is probably asserting; a concept with no theorem in it that reaches 1,800 words is probably padded. Both failures are equally bad. Past 45 minutes, ask whether it is two concepts. |
| **3** | **Flattened Taxonomy & 6 Sections** | Follows the two-level hierarchy (Modules & Concepts) and the six standard sections defined above. | Contains 1. Real-World Problem, 2. Building the Math, 3. "Math!" sidebars, 4. Java & WPILib code, 5. ML/Autonomy bridge, 6. Checkpoints & Prompts. |
| **4** | **No Black Boxes** | Every formula is derived, not asserted. Named prerequisite techniques are taught, not skipped. | Each result traces back to a stated starting assumption. Foundational named methods (e.g. SOH-CAH-TOA, the separating axis idea) appear explicitly rather than being silently assumed. |
| **5** | **Embedded Visuals & Interactive Demos** | Zero ASCII art. Contains embedded companion visualizer iframe and responsive vector SVGs for geometric figures. | Verified zero ASCII box/line art. Companion `demo.html` is embedded via `<iframe>` alongside crisp inline SVGs that render correctly in both themes. |
| **6** | **Dual Grounding** | Concrete, detailed connections to both FRC Autonomous Robotics and Modern ML/AI. | Explicit, realistic robotics mechanism/problem (e.g. swerve kinematics, gyro fusion, field-oriented drive) AND a named machine learning architecture/algorithm (e.g. rotary position embeddings, IoU-based detection loss, k-nearest neighbours in embedding space). |
| **7** | **Interactive Demo & Dual-Theme Quality** | Standalone HTML5/Canvas visualizer in `demo.html`. | Zero external CDN scripts/fonts, loads the shared `assets/theme.js` and `assets/axon.css`, repaints on the `axon-theme-changed` event, touch/mouse drag interactivity, real-time telemetry panel, smooth canvas rendering. |

---

## Language Policy

Teaching code follows the domain, matching CURRICULUM_SPEC rule 3. Every code section leads with a **from-scratch tier** that hides nothing, followed by the **production tier** — the library call a practitioner would actually write.

Which consumer a concept serves determines the shape:

| Concept serves | From-scratch tier | Production tier(s) |
|---|---|---|
| Robotics only | Plain Java | WPILib |
| Machine learning only | Plain Python | PyTorch |
| **Both** | **Plain Python** — it reads closest to the notation, so the derivation stays visible | **WPILib (Java) and PyTorch**, where each is genuinely illuminating |

By axon: Geometry, Trigonometry, Physics, Kinematics and Localization are robotics. Machine Learning, LLMs and Reinforcement Learning are ML. Linear Algebra, Calculus and Probability are mixed, concept by concept — the dual-consumer concepts are vectors, dot products, matrix multiplication, the chain rule, gradients, the normal distribution, Bayes' rule, and maximum likelihood.

**"Where appropriate" has teeth.** A dual concept does not mechanically emit three code blocks. Include a production tier only where it teaches something: dot products earn both (projection onto a swerve axis, cosine similarity between embeddings), while eigenvectors earn only PyTorch. Judge per concept.

**Signpost every code block with its language** as an explicit subheading — "First Principles (Python)", "In a Robot Project (Java & WPILib)", "In a Model (PyTorch)". A page carrying two languages is unreadable without it.

Rules for the from-scratch tier in Python: **no NumPy**. Lists and loops make the arithmetic visible, which is the entire point of that tier — a vectorised one-liner teaches nothing about what is being vectorised. NumPy may appear in the production tier as a stepping stone to PyTorch where it clarifies the leap.

Rules for the production tiers: they must produce the **same numbers** as the from-scratch tier on the same input, and the concept should say so explicitly. A reader who cannot connect the tiers has learned an API, not an idea.

**Libraries are not prerequisites.** The prerequisite chain governs mathematical tools, not tooling. The from-scratch tier is load-bearing — remove it and the derivation collapses. The production tier is illustrative — remove it and the reader loses a signpost, not an argument. So a Math concept may show PyTorch long before the frameworks module teaches PyTorch, exactly as Geometry Concept 01 already shows `Translation2d` with no WPILib primer anywhere in the curriculum. Introduce the call, say plainly what it does, and move on. Do not withhold a production example on prerequisite grounds.

Rules for the from-scratch tier in Python: **no NumPy**. Lists and loops make the arithmetic visible, which is the entire point of that tier — a vectorised one-liner teaches nothing about what is being vectorised. NumPy may appear in the production tier as a stepping stone to PyTorch where it clarifies the leap.

Rules for the PyTorch tier: it must produce the **same numbers** as the from-scratch tier on the same input, and the concept should say so explicitly. A reader who cannot connect the two tiers has learned an API, not an idea.

TensorFlow and Keras are not used in concept pages. They appear only in the frameworks module's comparison appendix, so that a reader who meets Keras elsewhere can map it onto what they already know.

### Out of scope: team-specific frameworks

**WPILib is the only production tier for robotics concepts.** It covers every concept in this curriculum, and Axon is a curriculum about the underlying mathematics, not a tutorial for any particular team's framework.

Do not reference Maroon Framework or any other team-specific framework, and do not read from team robot repositories. If a concept seems to need a framework primitive, it does not — express it in WPILib or in plain Java.

---

## Review Process & Verdict Output

The Reviewer sub-agent must execute a structured review with:
1. Checklist evaluation against each of the 7 checkpoints.
2. Exact word count, LaTeX scan, SVG/visual verification, and theme toggle confirmation.
3. Link check: every relative link in the concept and its module index resolves to a file that exists.
4. Final Verdict:
   - **`[PASS]`**: All 7 points met with exceptional quality. Ready to commit.
   - **`[REVISE]`**: List specific deficiencies and required fixes.
