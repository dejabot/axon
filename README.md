# Axon: Applied Math, Physics, ML & Autonomous Robotics

**Axon** is a self-contained, first-principles curriculum designed to build mastery in applied linear algebra, trigonometry, calculus, actuator physics, classical/modern control theory, deep learning, reinforcement learning, and agentic autonomous robotics.

---

## 🎯 How to Use This Repository

### 1. The 20–30 Minute Daily/Weekly Sprint Format
Every topic is broken into a self-contained **Sprint** consisting of:
* A long-form Markdown study guide in `modules/` with first-principles derivations and zero black-box formulas.
* A companion interactive HTML5/Canvas visualizer in `interactive/` with real-time parameter sliders.
* From-scratch Python implementations and review checkpoint questions.

### 2. Viewing the Content
* **Offline on Your Laptop:** Double-click `index.html` to launch the master dashboard in any browser with interactive progress tracking.
* **On Mobile / Tablet:** Push this repository to GitHub and enable **GitHub Pages** (Settings ➔ Pages ➔ Source: `main`). The responsive, touch-ready visualizers and study guides will be accessible directly on your phone.

---

## 🤖 Generating Content with Antigravity

This repository uses a two-agent architecture:
1. **Author Agent:** Writes modules per `CURRICULUM_SPEC.md` and `ROADMAP.md`.
2. **Reviewer Sub-Agent:** Audits output against `REVIEWER_SPEC.md` before committing.

### To generate a sprint in Antigravity:
```text
Antigravity, generate Sprint 1 (modules/sprint_01.md and interactive/sprint_01_demo.html) following CURRICULUM_SPEC.md and ROADMAP.md. 
Then spawn the Reviewer Sub-Agent per REVIEWER_SPEC.md. Commit when it achieves [PASS].