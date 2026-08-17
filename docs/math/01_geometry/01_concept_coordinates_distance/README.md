# Concept 01: Coordinates, Poses & Pythagorean Distance

> **▶ Interactive Demo: [2D Field Distance Visualizer](demo.html)**
>
> Open the interactive demo below to drag the robot and target across the field and watch the distance calculation update live.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Where is the Robot?
Imagine standing at the corner of an FRC playing field. The field is a large rectangle:
* The long edge along the wall is the **X-axis** (from 0 to 16.5 meters).
* The short edge along the driver stations is the **Y-axis** (from 0 to 8.2 meters).

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="180" viewBox="0 0 340 180" style="max-width: 100%; height: auto;">
    <!-- Field Boundary -->
    <rect x="20" y="20" width="300" height="140" fill="none" stroke="#334155" stroke-width="2" rx="6" />
    <line x1="20" y1="160" x2="320" y2="160" stroke="#475569" stroke-width="2" />
    <line x1="20" y1="160" x2="20" y2="20" stroke="#475569" stroke-width="2" />
    
    <!-- Origin -->
    <circle cx="20" cy="160" r="4" fill="#38bdf8" />
    <text x="25" y="152" fill="#38bdf8" font-family="sans-serif" font-size="11">Origin (0, 0)</text>
    
    <!-- Target -->
    <circle cx="260" cy="50" r="6" fill="#f43f5e" />
    <text x="200" y="45" fill="#f43f5e" font-family="sans-serif" font-weight="bold" font-size="11">Target (12.0, 6.0)</text>
    
    <!-- Robot -->
    <rect x="70" y="100" width="20" height="20" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" rx="3" />
    <text x="50" y="135" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="11">Robot (3.0, 2.0)</text>
    
    <!-- Distance Line -->
    <line x1="80" y1="110" x2="260" y2="50" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="4,4" />
    <text x="160" y="75" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="12">Distance d</text>
  </svg>
</div>

If your robot is sitting at `(x = 3.0m, y = 2.0m)` and wants to shoot a game piece into a target at `(x = 12.0m, y = 6.0m)`:
1. How many meters East/West must the piece travel? `dx = 12.0 - 3.0 = 9.0 meters`.
2. How many meters North/South must the piece travel? `dy = 6.0 - 2.0 = 4.0 meters`.
3. How far is the target in a straight line?

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java
We can calculate the Euclidean distance using standard Java `Math`:

```java
// 1. Define robot and target positions (in meters)
double robotX = 3.0;
double robotY = 2.0;

double targetX = 12.0;
double targetY = 6.0;

// 2. Find differences in X and Y
double dx = targetX - robotX; // 12.0 - 3.0 = 9.0 meters
double dy = targetY - robotY; //  6.0 - 2.0 = 4.0 meters

// 3. Calculate straight-line distance (Pythagorean Theorem)
double distance = Math.hypot(dx, dy); // or Math.sqrt(dx * dx + dy * dy)

System.out.printf("Straight-line Distance: %.2f meters%n", distance);
// Output: 9.85 meters
```

### Production WPILib Equivalent
In WPILib, positions on the field are represented by `Translation2d` and `Pose2d`:

```java
import edu.wpi.first.math.geometry.Translation2d;

Translation2d robot = new Translation2d(3.0, 2.0);
Translation2d target = new Translation2d(12.0, 6.0);

// One-liner distance calculation
double distance = robot.getDistance(target);
```

---

## 3. What is a Robot Pose?
In robotics, knowing the robot's `(x, y)` location is only half the story. The robot also has a **heading angle `θ`** (which way its front bumper is facing).

We bundle these three numbers together into a **Pose**:

```python
# A 2D Robot Pose: (x, y, heading_degrees)
robot_pose = {
    "x": 3.0,          # meters along field length
    "y": 2.0,          # meters along field width
    "heading": 45.0    # facing 45 degrees North-East
}
```

Every autonomous path follower and odometry system tracks the robot's state as this `(x, y, θ)` pose tuple.

---

## 4. Bridge to Machine Learning: Distance in AI
In machine learning, we use this exact same distance formula (called **Euclidean Distance**) to compare items:
* Suppose an AI represents two images or words as lists of numbers called **feature vectors**:
  * Item A: `[3.0, 2.0]`
  * Item B: `[12.0, 6.0]`
* If the distance between two feature vectors is small, the AI knows the two items are very similar. If the distance is large, they are different!

---

## 5. Review Checkpoints
### Checkpoint 1
Your robot is at `(x = 1.0, y = 1.0)`. An AprilTag on the field wall is located at `(x = 4.0, y = 5.0)`.
Calculate the straight-line distance between the robot and the AprilTag.

**Solution:**
1. `dx = 4.0 - 1.0 = 3.0`
2. `dy = 5.0 - 1.0 = 4.0`
3. `d = √(3.0² + 4.0²) = √(9 + 16) = √25 = 5.0 meters`.

---

### Checkpoint 2
Why is an `(x, y)` position not enough by itself to aim a turret or shoot a note?

**Solution:**
Because the robot could be at the right `(x, y)` position but facing backward! You also need the heading angle `θ` (the full `(x, y, θ)` pose) to calculate how much the robot or turret must rotate to face the goal.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1: Geometry</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">Math Axon Home</a></div>
  <div><a href="../02_concept_coordinate_frames/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Coordinate Frames →</a></div>
</div>
