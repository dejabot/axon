# Axon Sprint Brainstorming & Content Alignment

This document serves as the pre-generation scratchpad for the `axon` curriculum. Before authoring any sprint in `modules/` and `interactive/`, use this template to align on the core intuitions, mathematical derivations, real-world failure modes, interactive visualizer mechanics, and code architecture.

---

## The Sprint Alignment Template

Copy and paste this empty template when planning an upcoming sprint:

```markdown
### Sprint [Number]: [Topic Name]
* **Target Time:** 20–30 minutes
* **1. The Intuitive Mental Model (Physical/Visual Analogy):**
  - [What everyday physical analogy or visual metaphor explains this before introducing any formulas?]
* **2. Mathematical & Physical Derivations (No Black Boxes):**
  - [What equations must be derived step-by-step from first principles?]
  - [What geometric diagrams or text grids are needed to support the derivation?]
* **3. Grounded FRC & ML/AI Objectives:**
  - FRC Robotics Mapping: [e.g., Swerve azimuth, elevator gravity feedforward, gyro drift]
  - Machine Learning Mapping: [e.g., Dense layer weights, loss landscape slope, gradient update]
* **4. The "Classic Failure Mode" (What breaks if you do this naively?):**
  - [e.g., 340-degree swerve spin, integral windup on jam, infinite jerk gear stripping, exploding gradients]
* **5. Interactive HTML5/Canvas Demo Design:**
  - Visual Layout: [What is drawn on canvas? e.g., Vector arrows, unit circle, 3-tier motion curves]
  - Interactive Sliders: [What parameters can the user drag? e.g., target angle, mass, learning rate]
  - Live Stat Readouts: [What numbers update in real time? e.g., determinant, velocity, loss]
* **6. Code Implementation Specifications:**
  - Language: Python / Clean Pseudo-code
  - Classes/Functions to write from scratch: [e.g., Vector2d, atan2 wrapper, SimpleMLP, EKF]
* **7. Two-Way Conceptual Links:**
  - Backward Link: [Which foundational math sprint does this build upon?]
  - Forward Link: [Which future robotics or ML sprint will use this?]
* **8. Checkpoints & Exploration Prompts:**
  - 2 Review Questions + Worked Answers
  - 2 Deep-Dive Exploration Prompts
  