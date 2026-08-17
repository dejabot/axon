# Concept 02: Coordinate Frames (Field vs. Robot vs. Camera)

> **▶ Interactive Demo: [Frame Transformation Visualizer](demo.html)**
>
> Open the interactive demo below to see how a target's position changes depending on whether you measure it from the **Field Origin** or from the **Robot's Perspective**.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Camera's Eyes vs. The Field
Imagine your robot's front-facing camera spots a game piece on the floor. 

The camera reports:
> *"The piece is 1.5 meters ahead of me and 0.5 meters to my left."*

These measurements are in the **Robot Frame** (local coordinates relative to the robot itself).

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="180" viewBox="0 0 340 180" style="max-width: 100%; height: auto;">
    <!-- Field Axes -->
    <line x1="30" y1="150" x2="310" y2="150" stroke="#334155" stroke-width="1.5" />
    <line x1="30" y1="150" x2="30" y2="20" stroke="#334155" stroke-width="1.5" />
    <text x="35" y="140" fill="#94a3b8" font-family="sans-serif" font-size="11">Field (0, 0)</text>
    
    <!-- Robot at (4, 2) -->
    <g transform="translate(130, 90)">
      <rect x="-15" y="-15" width="30" height="30" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" rx="4" />
      <line x1="0" y1="0" x2="40" y2="0" stroke="#38bdf8" stroke-width="2" />
      <line x1="0" y1="0" x2="0" y2="-40" stroke="#4ade80" stroke-width="2" />
      <text x="5" y="25" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="10">Robot (4m, 2m)</text>
    </g>
    
    <!-- Note at (5.5, 2.5) -->
    <circle cx="180" cy="70" r="7" fill="#fbbf24" />
    <text x="195" y="75" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="11">Game Piece</text>
    <line x1="130" y1="90" x2="180" y2="70" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3" />
  </svg>
</div>

If your autonomous routine wants to drive to that game piece, your navigation system needs its coordinates on the **Field Frame** (global coordinates where the field origin is at `(0, 0)`).

If the robot is located at `(x = 4.0m, y = 2.0m)` facing directly East:
* Global X = `robot_x + local_x = 4.0 + 1.5 = 5.5 meters`.
* Global Y = `robot_y + local_y = 2.0 + 0.5 = 2.5 meters`.

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java
Converting a local offset into global field coordinates:

```java
// 1. Robot position in Global Field Coordinates
double robotFieldX = 5.0;
double robotFieldY = 3.0;

// 2. Camera offset relative to Robot Center
double cameraOffsetX = 0.3; // 30 cm forward
double cameraOffsetY = 0.0; // centered left/right

// 3. Detected Game Piece relative to Camera
double pieceCameraX = 1.5;  // 1.5 meters ahead of camera lens
double pieceCameraY = -0.4; // 0.4 meters to the right

// 4. Transform to Global Field Coordinates
double pieceFieldX = robotFieldX + cameraOffsetX + pieceCameraX; // 5.0 + 0.3 + 1.5 = 6.8 m
double pieceFieldY = robotFieldY + cameraOffsetY + pieceCameraY; // 3.0 + 0.0 - 0.4 = 2.6 m

System.out.printf("Piece on Field: (%.2f, %.2f) m%n", pieceFieldX, pieceFieldY);
```

### Production WPILib Equivalent
WPILib handles rigid-body spatial transforms using `Pose2d` and `Transform2d`:

```java
import edu.wpi.first.math.geometry.Pose2d;
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.math.geometry.Transform2d;
import edu.wpi.first.math.geometry.Translation2d;

Pose2d robotPose = new Pose2d(5.0, 3.0, Rotation2d.fromDegrees(0));
Transform2d robotToCamera = new Transform2d(new Translation2d(0.3, 0.0), new Rotation2d());
Transform2d cameraToPiece = new Transform2d(new Translation2d(1.5, -0.4), new Rotation2d());

// Chained spatial transform
Pose2d pieceFieldPose = robotPose.plus(robotToCamera).plus(cameraToPiece);
```

---

## 3. The 3 Common Frames in Robotics
Every modern robot codebase (such as WPILib) works with three standard frames of reference:

| Frame | Origin (0, 0) | Use Case |
|---|---|---|
| **Field Frame** | Corner of the playing field carpet | Autonomous path following, alliance scoring targets |
| **Robot Frame** | Center of the robot's drive base | Chassis velocity commands (`vx` forward, `vy` strafe) |
| **Camera Frame** | Optical center of the camera lens | AprilTag 3D detections, target bounding boxes |

---

## 4. Bridge to Machine Learning: 3D Object Detection
In autonomous driving AI (like Tesla Autopilot or Waymo) and robot vision:
1. Neural networks process camera images to find bounding boxes in **Pixel Coordinates** `(u, v)`.
2. Depth sensors convert pixels into **Camera Frame Coordinates** `(x, y, z)`.
3. The self-driving car's planner transforms camera coordinates into the **Global Map Frame** so the vehicle can steer around other cars on the road.

---

## 5. Review Checkpoints
### Checkpoint 1
Your robot is at Field position `(x = 6.0m, y = 3.0m)`. A distance sensor on the rear bumper detects a wall `0.8 meters` behind the robot (`local_x = -0.8m, local_y = 0.0m`).
What is the field position of the wall?

**Solution:**
1. `wall_field_x = robot_x + local_x = 6.0 + (-0.8) = 5.2 meters`.
2. `wall_field_y = robot_y + local_y = 3.0 + 0.0 = 3.0 meters`.
3. The wall is located at `(5.2, 3.0)` on the field.

---

### Checkpoint 2
Why can't an autonomous path planner send camera-relative coordinates directly to the drivetrain?

**Solution:**
Because as the robot moves, its camera moves too! If the target was at `1.5m ahead` and the robot moves `1.0m forward`, the relative position changes to `0.5m ahead`. The path planner must convert all targets to a fixed **Field Frame** so targets don't appear to jump around when the robot moves.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_01_coordinates_distance/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: Coordinates & Distance</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="../concept_03_bounding_boxes/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 03: Bounding Boxes →</a></div>
</div>
