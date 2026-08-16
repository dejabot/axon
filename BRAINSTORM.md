# Axon Curriculum Brainstorming & Content Alignment

This document serves as the pre-generation scratchpad for the `axon` curriculum. Before authoring any concept in `docs/modules/`, use this template to align on the core intuitions, mathematical derivations, real-world failure modes, interactive visualizer mechanics, and code architecture.

---

## The Concept Alignment Template

Copy and paste this template when planning an upcoming concept:

```markdown
### Module [Number]: [Module Name] ➔ Concept [Number]: [Concept Name]
* Target Time: 20–30 minutes
* 1. Intuitive Mental Model (Physical/Visual Analogy):
  - [Everyday physical analogy or visual metaphor before introducing formulas]
* 2. Mathematical & Physical Derivations (No Black Boxes):
  - [Equations derived step-by-step from first principles]
  - [Geometric diagrams or text grids needed to support the derivation]
* 3. Dual Grounding: FRC Robotics & Modern ML:
  - FRC Robotics Mapping: [e.g., Swerve azimuth, elevator gravity feedforward, gyro drift]
  - Machine Learning Mapping: [e.g., Dense layer weights, loss landscape slope, gradient update]
* 4. Classic Failure Mode & Python Engine:
  - [e.g., 340-degree swerve spin, matrix singularity, infinite jerk gear stripping, exploding gradients]
  - Complete, self-contained Python script comparing naive vs correct implementation
* 5. Interactive HTML5/Canvas Demo Design:
  - Visual Layout: [Canvas elements, coordinate frames, animated mechanisms]
  - Interactive Sliders: [Draggable parameters e.g., target angle, mass, learning rate]
  - Live Telemetry: [Real-time statistics e.g., determinant, velocity, loss norm]
* 6. Curriculum Linkages:
  - Backward Link: [Foundational concept this builds upon]
  - Forward Link: [Future concept that utilizes this]
* 7. Checkpoints & Exploration Prompts:
  - 2 Review Questions + Worked Solutions
  - 2 Deep-Dive Exploration Prompts
```