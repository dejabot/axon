# Axon Reviewer Specification & Audit Rubric

## Purpose & Scope

This is the single standard for **every concept in every axon** — Math, Machine Learning, Large Language Models, Physics, Kinematics, Localization and Reinforcement Learning. A concept is audited against the 8-point rubric below before it is committed.

Nothing here is subject-specific. Where a rule mentions an example from one axon, it is illustrating the rule, not narrowing it.

---

## The Standard Concept Structure

Every concept `README.md` follows this six-section shape, in this order. The companion `demo.html` is embedded via `<iframe>` immediately under the title.

1. **The Real-World Problem** — a concrete scenario, in plain language with a diagram, that the reader cannot yet solve.
2. **Building It From First Principles** — the result derived step by step from something the reader already believes. No formula, algorithm or claim appears before its justification.
3. **"Math!" Sidebars** — formal notation introduced as a translation of the prose, each with an explicit "read this out loud as…" line. Interleaved into section 2, never gathered at the end.
4. **Code** — a from-scratch tier that hides nothing, then the production tier a practitioner would actually write. See Language Policy.
5. **Bridge to Real Systems** — where this is actually used, named specifically.
6. **Checkpoints & Exploration Prompts** — 2 review questions with fully worked solutions, then 2 open-ended deep-dive prompts.

---

## Design Principles

These are the rules that decide what goes in and what stays out. Most were learned by getting them wrong.

### One concept teaches one idea

The reader should finish able to **use** it. Supporting material earns its place only when the main idea is incomplete without it, and *"this is fascinating"* is not that test. A passage the reader could skip while still applying the concept correctly belongs in a Deep Dive prompt — that is what those prompts are for.

When a section starts teaching a second subject, cut it to the one sentence the main idea needs and move the rest to a deep dive. Prefer one example worked all the way through to three sketched.

### Length follows the topic

The six sections are a shape, not a quota. A concept built on a real derivation earns a long section 2. A concept that is a definition plus its applications does not, and padding it with adjacent material produces a worse page than a short honest one.

Most concepts land at 1,800–2,800 words, or 30–45 minutes including code, demo and checkpoints. Some legitimately land far shorter. Judge against the topic, never against a target. **Under-length and over-length are equally serious failures**: the first usually means results are being asserted rather than derived, the second usually means padding.

The test for every paragraph: does it derive something, or prevent a real bug? If neither, delete it.

### Examples must be honest

Three tests, all of which real drafts have failed:

* **Does the mathematics do work the reader needs?** A gamepad stick already reports x and y, so decomposing one into components solves a problem that does not exist. A steered wheel's state genuinely is an angle and a speed, so converting it is real work.
* **Does it cost vocabulary?** An opening that must first explain a mechanism makes the reader learn two things to learn one, and the mechanism is the one they did not come for. Prefer "a wheel pointed 30° off down-field at 4.0 m/s" to "a swerve module at a 30° azimuth"; name the jargon after the idea has landed.
* **Is it real?** A contrived example is the most reliable signal that a topic was included to fill space. If you had to invent an implausible mechanism to justify a section, delete the section rather than the mechanism.

Where a module can run one mechanism across all its concepts, do that rather than inventing a fresh vignette each time.

### Ground in real systems, but never force it

Every concept must connect to something real and **named** — a specific architecture, algorithm, mechanism or failure. "AI uses this too" is not a grounding.

Where a concept genuinely serves both robotics and machine learning, ground it in both; that dual grounding is a large part of this curriculum's value. **But do not manufacture a connection that is not there.** A strained robotics tie-in on a KV-cache concept, or a forced ML angle on gearbox inertia, is the contrived-example failure wearing a different hat. One honest grounding beats two, one of which is invented.

### Diagrams must agree with the prose

Every number in a figure must match the number in the text, and the figure's geometry must match its own labels. A diagram labelled 30° whose arc actually sweeps 40° teaches the wrong thing to any reader who measures it, and no automated check will catch it. Verify angles, lengths and ratios in figures numerically before accepting them.

---

## Language & Spelling

**American English throughout** — prose, code comments, identifiers, diagram labels and demo telemetry alike.

The common slips: *meter* not metre, *center* not centre, *behavior* not behaviour, *color* not colour, *neighbor* not neighbour, *labeled* / *labeling* not labelled / labelling, *traveled* / *traveling* not travelled / travelling, *analyze* not analyse, *gray* not grey. Verbs and their nouns take *-ize* / *-ization*: memorize, normalize, optimize, generalize, minimize, maximize, penalize, initialize, vectorize, characterize, parameterize, regularize, discretize.

This matters more than house style: the curriculum's audience writes FRC code against WPILib, whose own API is American (`getCenter`, `Color`), and a page that says "metre" beside code that says `meters` reads as careless.

---

## Notation

Pages are rendered by KaTeX, loaded in the site layout. Both Unicode and LaTeX are available, and the choice between them is about legibility, not policy.

### Which to use

**LaTeX by default for display mathematics.** Any standalone, set-apart formula is `$$…$$`. This is the default, not an escape hatch. Plain-text fenced blocks approximate structure with parentheses and stacked characters, and the approximation is always worse:

```
   distance = √( (cos θ − 0)² + (sin θ − 0)² )  =  √( cos²θ + sin²θ )  =  1
```

versus a real radical with the expression genuinely underneath it, a real fraction with a real bar, a matrix with real brackets. Do not put equations in fenced code blocks.

**Unicode for inline symbols in prose.** `θ`, `Δ`, `Σ`, `≥`, `≠`, `≈`, `·`, `²`, `x₁`. Writing "the angle θ" is better than "the angle $\theta$" — it reads well in the source, needs no renderer, and pastes straight into code. Reach for inline `$…$` only when an inline expression carries structure: a fraction, an expression superscript, a subscripted index.

**Fenced blocks are for code and for genuinely tabular text** — comparison tables, worked numeric traces, pseudo-code, terminal output. If it is an equation, it is `$$…$$`.

### How to write it

| Purpose | Author as | Notes |
|---|---|---|
| Inline math | `$…$` | Passes through kramdown verbatim |
| Display math | `$$…$$` | kramdown rewrites it to `\[…\]`, which KaTeX renders |

**Never author `\(…\)` or `\[…\]`.** kramdown strips the backslashes before KaTeX ever sees them, and the math renders as bare parentheses. This is verified behaviour, not a guess.

**Never leave an unpaired `$`.** An odd delimiter swallows the rest of the paragraph into a math span.

**Code fences are safe.** KaTeX skips `<pre>` and `<code>`, so a `$` inside a code block is left alone.

### Subscripts

Inside math delimiters, use LaTeX subscripts freely: `$v_{i+1}$`. Outside them, `v_{i+1}` renders as literal characters — use `v[i+1]`, which also matches the array indexing in the concept's own code. Never mix `vᵢ₊₁`-style Unicode with brackets on the same page.

---

## Language Policy

Every code section leads with a **from-scratch tier** that hides nothing, then a **production tier** — the library call a practitioner would write.

| Concept serves | From-scratch tier | Production tier(s) |
|---|---|---|
| Robotics only | Plain Java | WPILib |
| Machine learning only | Plain Python | PyTorch |
| **Both** | **Plain Python** — closest to the notation, so the derivation stays visible | **WPILib (Java) and PyTorch**, where each genuinely illuminates |

By axon: Geometry, Trigonometry, Physics, Kinematics and Localization are robotics. Machine Learning, LLMs and Reinforcement Learning are ML. Linear Algebra, Calculus and Probability are mixed concept by concept — the dual-consumer concepts are vectors, dot products, matrix multiplication, the chain rule, gradients, the normal distribution, Bayes' rule and maximum likelihood.

* **"Where appropriate" has teeth.** A dual concept does not mechanically emit three code blocks. Dot products earn both tiers (projection onto a heading, cosine similarity between embeddings); eigenvectors earn only PyTorch.
* **Signpost every block with its language** as a subheading — "First Principles (Python)", "In a Robot Project (Java & WPILib)", "In a Model (PyTorch)". A two-language page is unreadable without it.
* **No NumPy in the from-scratch tier.** Lists and loops keep the arithmetic visible; a vectorised one-liner teaches nothing about what is being vectorised. NumPy may appear in a production tier as a stepping stone to PyTorch.
* **Tiers must agree numerically.** The production tier must produce the same numbers as the from-scratch tier on the same input, and the concept should say so. A reader who cannot connect the tiers has learned an API, not an idea.
* **Libraries are not prerequisites.** The prerequisite chain governs *ideas*, not tooling. The from-scratch tier is load-bearing; the production tier is illustrative. A Math concept may show PyTorch long before the frameworks module exists, exactly as Geometry Concept 01 shows `Translation2d` with no WPILib primer anywhere. Never withhold a production example on prerequisite grounds.
* TensorFlow and Keras appear only in the frameworks module's comparison appendix.
* **WPILib is the only production tier for robotics.** Do not reference team-specific frameworks or read from team robot repositories. Axon teaches the underlying ideas, not any one team's framework.

---

## Prerequisite Discipline

A concept may use only what the reader has already been given. This applies across axons, not just within one: Localization needs frames from Math Module 2, matrices from Module 3 and covariance from Module 5, and must not be written as though it can assume them early.

When a concept needs an unavailable tool, **move the concept or move the tool** — never forward-reference and hope. Each axon outline states the prerequisite chain explicitly, and that statement is the contract handed to an authoring agent.

Cross-module restructuring is proposed to a human, never executed by a concept author.

---

## 8-Point Audit Rubric

| # | Checkpoint | Pass criteria |
|---|---|---|
| **1** | **Math renders, text is clean** | Math uses `$…$` or `$$…$$` only — never authored `\(…\)` or `\[…\]`, whose backslashes kramdown strips before KaTeX sees them. No unpaired `$`. No brace sub/superscripts outside a math delimiter. No decorative emoji. |
| **2** | **Depth proportionate to the topic** | No hand-waving, no skipped steps, **and no padding**. Judged against the topic, not a word target. Past 45 minutes, ask whether it is two concepts. |
| **3** | **Six-section structure** | All six sections present and in order, with "Math!" sidebars interleaved rather than appended. |
| **4** | **No black boxes** | Every result traces to a stated starting assumption. Named prerequisite techniques are taught, not assumed — SOH-CAH-TOA, the separating axis, the chain rule. |
| **5** | **Correct, consistent visuals** | Zero ASCII art. Inline SVGs render in both themes. **Figures agree numerically with the prose** — angles, lengths and ratios verified, not eyeballed. |
| **6** | **Honest grounding** | Connected to at least one named real system. Dual robotics/ML grounding where genuine; no manufactured connections. |
| **7** | **Working demo** | `demo.html` loads `assets/theme.js` and `assets/axon.css`, repaints on `axon-theme-changed`, supports mouse and touch, shows live telemetry, uses no external CDN. **Verified by loading it in a browser** — a demo can pass code review and render blank. |
| **8** | **Prerequisite compliance** | Uses nothing from a later module. Forward references are named as pointers, never used. |

---

## Common Failure Modes

Empirical — every one of these shipped at least once in this repository.

1. **Asserting instead of deriving.** The formula appears with no account of where it came from. Symptom: a concept well under length.
2. **Padding instead of deriving.** Adjacent topics absorbed to reach a word count. Symptoms: a concept well over length, a contrived example, or a section teaching a second subject.
3. **The unearned prerequisite.** Teaching frames with a rotation the reader has not met, or a matrix before matrices exist. Usually invisible to the author, who knows the tool.
4. **Correct code, wrong lesson.** Naive addition presented as equivalent to a library call that actually rotates — right for heading 0°, wrong everywhere else, and it survives testing.
5. **The blank demo.** A canvas sized from a container that is sized from the canvas grows without bound on resize until allocation fails. Passes code review; renders nothing.
6. **The lying diagram.** A figure whose geometry contradicts its labels.
7. **Stale prose about structure.** Text describing an ordering that has since changed. Link checkers miss it because the links still resolve. Sweep for it after every restructuring.

---

## Review Process & Verdict

1. Evaluate all 8 checkpoints.
2. Run `python3 tools/audit.py <path>` for the mechanical checks: LaTeX, Liquid tags that break the Jekyll build, word count, broken links, demo canvas sizing.
3. Load the demo in a browser. Confirm it renders, that canvas height is stable across repeated resize events, and that the telemetry is numerically correct.
4. Verify the arithmetic in every worked example and every figure.
5. Verdict:
   * **`[PASS]`** — ready to commit.
   * **`[REVISE]`** — list specific deficiencies and required fixes.
