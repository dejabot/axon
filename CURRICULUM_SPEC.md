# Axon Curriculum Specification

## Educational Mission

Axon bridges high-school mathematics and physics into modern machine learning, large language models, physical electromechanics, autonomous robotics (FIRST Robotics Competition / FRC), and agentic decision systems.

This document states the mission and the pedagogical principles. **REVIEWER_SPEC.md** turns them into the enforceable rubric every concept is audited against; where the two appear to disagree, REVIEWER_SPEC is the operative one.

---

## Pedagogical Rules

These apply identically to all seven axons.

1. **Derive, never assert.** Every result is built step by step from something the reader already believes. No formula, algorithm or claim appears before its justification. Named prerequisite techniques get taught, not assumed.

2. **One concept, one idea.** A concept succeeds when the reader can *use* the idea. Supporting material earns its place only when the main idea is incomplete without it; anything merely interesting belongs in a deep-dive prompt. Depth is measured against the topic, not against a word count — padding is as serious a failure as hand-waving.

3. **Open on a concrete problem the reader cannot yet solve.** Ground it in whatever domain the concept genuinely serves — a mechanism, a sensor, a model, a failure. Three tests: the mathematics must do work the reader actually needs, the scenario must cost no vocabulary they do not already have, and it must be real. A contrived scenario is the surest sign that a topic was included to fill space.

4. **Code-first, in the language of the domain**, so the reader recognizes it in the wild. Always two tiers: from-scratch code that hides nothing, then the production call a practitioner would write.
   * **Robotics concepts → Java & WPILib** (`Translation2d`, `Pose2d`, `Rotation2d`, `MathUtil`, `TrapezoidProfile`).
   * **Machine learning and LLM concepts → plain Python, then PyTorch.**
   * **Mathematical foundations → whichever consumer the concept serves**, and both where it genuinely serves both.

5. **"Math!" sidebars.** Formal notation introduced as a translation of the prose, with explicit pronunciation and a "read this out loud as…" line. Notation should never be the barrier.

6. **Bridge to real systems, honestly.** Name a specific architecture, algorithm or mechanism — never "AI uses this too". Where a concept genuinely serves both robotics and machine learning, show both, because that connection is much of this curriculum's value. Where it does not, one honest grounding beats two, one of which was invented.

7. **Respect the prerequisite chain.** A concept may use only what earlier concepts have given the reader. When a concept needs an unavailable tool, move the concept or move the tool; never forward-reference and hope. This constraint shapes the curriculum's structure, not just its prose.

8. **Interactive companion demos.** Focused HTML5/Canvas visualizers with dark and light themes, live telemetry, and mouse plus touch interaction. A demo is verified by loading it in a browser, never by reading its source.

---

## The 7 Axon Tracks

1. **`docs/math/`** — Mathematical Foundations: Geometry, Trigonometry, Linear Algebra, Calculus, Probability
2. **`docs/machine_learning/`** — Core Deep Learning, Computer Vision & Frameworks
3. **`docs/large_language_models/`** — Transformers & Generative AI
4. **`docs/physics/`** — Electromechanics, Dynamics, Ballistics & Feedback Control
5. **`docs/kinematics/`** — Chassis Speeds, Swerve & 2nd-Order Twist, Motion Profiling
6. **`docs/localization/`** — Wheel Odometry, AprilTag Vision & PnP, Extended Kalman Filter
7. **`docs/reinforcement_learning/`** — MDPs, Q-Learning, Policy Gradients, Monte Carlo Tree Search

Structure, status and prerequisite ordering for every axon live in **ROADMAP.md**. Per-axon outlines — the toolkit manifests handed to authoring agents — live alongside it, one per axon.
