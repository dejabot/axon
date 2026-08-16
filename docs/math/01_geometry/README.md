# Module 1: Geometry for Robotics

Welcome to **Module 1: Geometry for Robotics**. In this module, we start with the absolute fundamentals of how robots perceive space, measure distances, navigate field coordinates, transform frames of reference, and avoid physical collisions.

---

## Concepts in this Module
* **[Concept 01: Coordinates, Poses & Pythagorean Distance](concept_01_coordinates_distance/README.md)**
  * *The Everyday Problem:* Where is the robot on the field, and how far is it from the scoring target?
  * *Code & Math:* `(x, y)` coordinate positions, the Pythagorean distance formula, and 2D robot poses `(x, y, θ)`.
  * *Visualizer:* [concept_01_coordinates_distance/demo.html](concept_01_coordinates_distance/demo.html)

* **[Concept 02: Coordinate Frames (Field vs. Robot vs. Camera)](concept_02_coordinate_frames/README.md)**
  * *The Everyday Problem:* The vision camera sees a game piece 1.5 meters ahead, but where is it on the playing field?
  * *Code & Math:* Frame offsets, origin translations, and converting local sensor measurements to global field coordinates.
  * *Visualizer:* [concept_02_coordinate_frames/demo.html](concept_02_coordinate_frames/demo.html)

* **[Concept 03: 2D Bounding Boxes & Collision Detection](concept_03_bounding_boxes/README.md)**
  * *The Everyday Problem:* How does autonomous path planning know if our robot's bumpers will bump into a field barrier or defender?
  * *Code & Math:* Axis-Aligned Bounding Boxes (AABB), robot bumper perimeters, and simple overlap checks.
  * *Visualizer:* [concept_03_bounding_boxes/demo.html](concept_03_bounding_boxes/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Math Axon Home</a></div>
  <div><a href="README.md" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="concept_01_coordinates_distance/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: Coordinates & Distance →</a></div>
</div>
