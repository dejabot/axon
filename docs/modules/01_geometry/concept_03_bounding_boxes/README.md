# Concept 03: 2D Bounding Boxes & Collision Detection

> **▶ Interactive Demo: [2D Collision Detection Sandbox](demo.html)**
>
> Open the interactive demo below to drag your robot toward field obstacles and watch the bounding box collision checks illuminate green (Safe) or red (Collision).

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Will the Robot Crash?
An FRC robot is not a zero-dimensional point on a map. A standard robot is a physical box with a bumper perimeter (e.g. 0.9 meters wide by 0.9 meters long).

When planning an autonomous trajectory through the field:
* The field has fixed obstacles (like the stage structure, charge station, or reef).
* Other robots (defense bots) are driving across the carpet.

<div style="text-align: center; margin: 20px 0;">
  <svg width="320" height="170" viewBox="0 0 320 170" style="max-width: 100%; height: auto;">
    <!-- Obstacle Box -->
    <rect x="170" y="40" width="90" height="80" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="2" rx="4" />
    <text x="180" y="85" fill="#f43f5e" font-family="sans-serif" font-weight="bold" font-size="12">Obstacle</text>
    
    <!-- Robot Box Safe -->
    <rect x="40" y="40" width="70" height="70" fill="rgba(74, 222, 128, 0.2)" stroke="#4ade80" stroke-width="2" rx="4" />
    <text x="50" y="80" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="12">Robot</text>
    
    <text x="40" y="145" fill="#94a3b8" font-family="sans-serif" font-size="11">X-Interval: [40, 110]</text>
    <text x="170" y="145" fill="#94a3b8" font-family="sans-serif" font-size="11">X-Interval: [170, 260]</text>
  </svg>
</div>

Before moving the drivetrain motors, how does the software know if our robot's bounding box overlaps with an obstacle?

---

## 2. Solving It in Code: The AABB Overlap Test
The fastest way to test for collisions is an **Axis-Aligned Bounding Box (AABB)** check. 

Two boxes overlap **if and only if** they overlap on **both the X-axis AND the Y-axis simultaneously**:

```python
def check_collision(box_a, box_b):
    """
    Checks if two 2D boxes overlap.
    Each box is defined by [x_min, y_min, x_max, y_max].
    """
    # Check if box_a is completely to the left or right of box_b
    no_x_overlap = (box_a['x_max'] < box_b['x_min']) or (box_a['x_min'] > box_b['x_max'])
    
    # Check if box_a is completely above or below box_b
    no_y_overlap = (box_a['y_max'] < box_b['y_min']) or (box_a['y_min'] > box_b['y_max'])
    
    # If there is separation on either axis, they do NOT collide!
    return not (no_x_overlap or no_y_overlap)

# Example: Robot bumper vs Field Barrier
robot = {'x_min': 2.0, 'y_min': 1.0, 'x_max': 2.9, 'y_max': 1.9}
barrier = {'x_min': 2.5, 'y_min': 1.5, 'x_max': 3.5, 'y_max': 2.5}

if check_collision(robot, barrier):
    print("COLLISION DETECTED! Stop motors immediately.")
else:
    print("Path is clear.")
```

---

> 💡 **Math Sidebar: Interval Intersection**
>
> In mathematics, a 2D box is the product of two 1D intervals: an X-interval `[x_min, x_max]` and a Y-interval `[y_min, y_max]`.
>
> Two boxes `A` and `B` intersect if:
> ```
>    (A_x ∩ B_x ≠ ∅)  AND  (A_y ∩ B_y ≠ ∅)
> ```
>
> **How to read this equation out loud:**
> * `∩` means **intersection** (the numbers shared in common).
> * `≠ ∅` means **not empty** (the two intervals overlap).
> * If the shadows cast on both walls overlap at the same time, the 3D objects are touching!

---

## 3. Bridge to Machine Learning: Object Detection & IoU
In computer vision (like YOLO detecting game pieces or AprilTags):
* The AI predicts a bounding box `[x_min, y_min, x_max, y_max]`.
* To measure accuracy against the true label, ML uses **Intersection over Union (IoU)**:

```
   IoU = (Area of Overlap) / (Total Combined Area)
```
* If `IoU > 0.5`, the AI successfully found and localized the target!

---

## 4. Review Checkpoints
### Checkpoint 1
Robot box A is at `x: [1.0, 2.0], y: [1.0, 2.0]`.
Obstacle B is at `x: [2.5, 3.5], y: [1.0, 2.0]`.
Do they collide?

**Solution:**
On the Y-axis, they overlap `[1.0, 2.0]`.
However, on the X-axis: `A_x_max (2.0) < B_x_min (2.5)`. There is a `0.5m` gap between them.
**Result: No collision** (Path is clear).

---

### Checkpoint 2
Why do autonomous path planners add a `10cm` padding (safety margin) around obstacle bounding boxes?

**Solution:**
Because real robots have momentum and minor odometry sensor drift! If you plan a path that passes within `1mm` of a barrier, slight wheel slip will cause the bumper to clip the obstacle. Adding a safety buffer guarantees physical clearance.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_02_coordinate_frames/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 02: Coordinate Frames</a></div>
  <div><a href="../README.md" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="../../02_trigonometry/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 2: Trigonometry →</a></div>
</div>
