# Concept 01: The Unit Circle & Trigonometric Ratios

> **▶ Interactive Demo: [Joystick Unit Circle Visualizer](demo.html)**
>
> Open the interactive demo below to sweep the joystick angle \θ around the circle and see how `cos(θ)` (horizontal power) and `sin(θ)` (vertical power) respond in real time.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Gamepad Joystick Steering
When an FRC driver pushes the analog joystick on a controller:
* The joystick tilts by an angle `θ` (measured counter-clockwise from the positive X-axis).
* The joystick push has a length (magnitude) `r = 1.0` (full power).

<div style="text-align: center; margin: 20px 0;">
  <svg width="280" height="200" viewBox="0 0 280 200" style="max-width: 100%; height: auto;">
    <circle cx="140" cy="100" r="70" fill="none" stroke="#334155" stroke-width="1.5" />
    <line x1="40" y1="100" x2="240" y2="100" stroke="#475569" stroke-width="1" />
    <line x1="140" y1="20" x2="140" y2="180" stroke="#475569" stroke-width="1" />
    <!-- Joystick stick -->
    <line x1="140" y1="100" x2="189" y2="51" stroke="#fbbf24" stroke-width="3" />
    <circle cx="189" cy="51" r="5" fill="#fbbf24" />
    <!-- Shadows -->
    <line x1="140" y1="100" x2="189" y2="100" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="3,3" />
    <line x1="189" y1="100" x2="189" y2="51" stroke="#4ade80" stroke-width="2.5" stroke-dasharray="3,3" />
    <text x="150" y="118" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="11">cos(θ) [X]</text>
    <text x="195" y="80" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="11">sin(θ) [Y]</text>
  </svg>
</div>

How does the robot software break this diagonal stick push into two separate motor speeds:
1. **Forward/Backward speed `v_x`**?
2. **Left/Right strafe speed `v_y`**?

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java
Resolving joystick speed and angle into X and Y velocities:

```java
double speed = 4.0;              // 4.0 m/s total speed
double angleDegrees = 30.0;      // 30 degrees heading

// 1. Convert degrees to radians (Java trigonometric functions expect radians)
double angleRadians = Math.toRadians(angleDegrees);

// 2. Resolve into component speeds
double vx = speed * Math.cos(angleRadians); // Forward speed: 4.0 * 0.866 = 3.46 m/s
double vy = speed * Math.sin(angleRadians); // Strafe speed:  4.0 * 0.500 = 2.00 m/s

System.out.printf("Speeds -> vx: %.2f m/s, vy: %.2f m/s%n", vx, vy);
```

### Production WPILib Equivalent
In WPILib, `Rotation2d` stores trigonometric values without constant recalculation:

```java
import edu.wpi.first.math.geometry.Rotation2d;

Rotation2d heading = Rotation2d.fromDegrees(30.0);
double vx = speed * heading.getCos(); // 3.46 m/s
double vy = speed * heading.getSin(); // 2.00 m/s
```

---

## 3. Radians vs. Degrees
* **Degrees:** Humans divide a full circle into `360°` (convenient for compasses).
* **Radians:** Mathematics measures angles by the actual arc length traveled along a unit circle. Since the circumference of a circle is `2·π·r`, a full circle is **`2·π` radians** (`≈ 6.283 rad`).

```
   180° = π radians (≈ 3.14159 rad)
   90°  = π/2 radians (≈ 1.5708 rad)
```

> ⚠️ **Common Bug in Robotics:** Microcontroller math libraries (`Math.sin` in Java/C++/Python) always expect angles in **radians**, while gyro sensors often report in **degrees**. Always convert with `math.radians(deg)`!

---

## 4. Bridge to Machine Learning: Rotary Position Embeddings (RoPE)
In modern Large Language Models (like Llama and GPT-4):
* The AI needs to know the order of words in a sentence ("dog bites man" vs "man bites dog").
* State-of-the-art LLMs use **Rotary Position Embedding (RoPE)**, which rotates the internal numbers of each word by an angle proportional to its position in the sentence using `cos(m·θ)` and `sin(m·θ)`!

---

## 5. Review Checkpoints
### Checkpoint 1
The driver pushes the joystick straight North (`90°`).
What are `vx` and `vy`?

**Solution:**
* `vx = cos(90°) = 0.0` (Zero forward/backward speed)
* `vy = sin(90°) = 1.0` (Full strafe speed to the left)

---

### Checkpoint 2
If a robot drives with `vx = 0.6` m/s and `vy = 0.8` m/s, what is its total straight-line speed?

**Solution:**
* `speed = √(vx² + vy²) = √(0.6² + 0.8²) = √(0.36 + 0.64) = √1.0 = 1.0 m/s`.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../../01_geometry/04_concept_polygons_zones/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 04: Polygons & Zones</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../02_concept_rotating_vectors/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Rotating a Vector →</a></div>
</div>
