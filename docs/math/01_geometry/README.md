# Module 1: Geometry for Robotics

Welcome to **Module 1: Geometry for Robotics**. This module builds the spatial vocabulary everything else in the curriculum depends on: where things are, how far apart they are, whether a path crosses an obstacle, whether two objects collide, and whether the robot is inside a scoring zone.

Every result here is derived from first principles, and every one of them is reachable with nothing but arithmetic and a square root. Angles and rotation deliberately wait for [Module 2: Trigonometry](../02_trigonometry/), which picks up exactly where this module stops.

---

## Concepts in this Module

* **[Concept 01: Coordinates, Poses & Pythagorean Distance](01_concept_coordinates_distance/)**
  * *The Everyday Problem:* Where is the robot on the field, and how far is it from the scoring target?
  * *Core Ideas:* Field coordinate conventions, a proof of the Pythagorean theorem, the distance formula, midpoints, squared distance as a cheaper comparison, the L1 and L∞ norms, and the `(x, y, θ)` pose.
  * *Visualizer:* [Field distance & norms](01_concept_coordinates_distance/demo.html)

* **[Concept 02: Lines, Segments & Intersections](02_concept_lines_intersections/)**
  * *The Everyday Problem:* Does the planned autonomous path cross a field barrier, and if not, by how much does it clear it?
  * *Core Ideas:* Why slope fails on vertical lines, parametric form, the 2D cross product, the orientation test, segment intersection, and point-to-segment clearance.
  * *Visualizer:* [Path crossing & clearance](02_concept_lines_intersections/demo.html)

* **[Concept 03: Linear Interpolation, Lookup Tables & Blending](03_concept_linear_interpolation/)**
  * *The Everyday Problem:* You measured shooter RPM at five distances. What do you command at a distance in between?
  * *Core Ideas:* `lerp` named and generalised from Concept 02's parametric form, why one algebraic form is numerically safer than its equal, inverse lerp and remapping, clamping versus extrapolation, interpolating lookup tables, bilinear interpolation, and why angles cannot be lerped naively.
  * *Visualizer:* [Interpolation & lookup tables](03_concept_linear_interpolation/demo.html)

* **[Concept 04: Bounding Boxes, Overlap & Collision](04_concept_bounding_boxes/)**
  * *The Everyday Problem:* The robot is a 0.9 metre box, not a dot. Will its bumpers hit anything?
  * *Core Ideas:* Interval overlap via De Morgan's law, the separating axis idea, half-extents, Minkowski inflation and configuration space, penetration depth, Intersection over Union, and swept boxes for tunneling.
  * *Visualizer:* [Collision & IoU sandbox](04_concept_bounding_boxes/demo.html)

* **[Concept 05: Polygons, Areas & Field Zones](05_concept_polygons_zones/)**
  * *The Everyday Problem:* Scoring zones are slanted five-sided regions, not rectangles. Is the robot inside one?
  * *Core Ideas:* Convex versus concave, half-plane membership tests, ray casting and the even-odd rule, the half-open rule for vertex crossings, and the shoelace area formula.
  * *Visualizer:* [Zone membership & shoelace area](05_concept_polygons_zones/demo.html)

---

## What This Module Deliberately Leaves Out

Rotation. A camera sighting converted into field coordinates needs `cos` and `sin` the moment the robot is not facing straight down-field, and the honest place for that is after the trigonometry has been built. [Module 2](../02_trigonometry/) opens with the unit circle, derives the rotation matrix from it, and then does coordinate frames properly.

Oriented bounding boxes are deferred for the same reason, and Concept 03 says where to resume once the tools exist.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Math Axon Home</a></div>
  <div><a href="./" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="01_concept_coordinates_distance/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: Coordinates & Distance →</a></div>
</div>
