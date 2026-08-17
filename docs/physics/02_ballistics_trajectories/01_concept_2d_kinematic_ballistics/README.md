# Concept 01: 2D Parabolic Projectile Motion & Launch Angles

In modern competitive robotics, game pieces must be launched accurately across the field into elevated goals (such as the Speaker, Hub, or Upper Port) from any arbitrary distance between **2 and 8 meters**.

To score reliably on every shot, the robot's control system must calculate the exact **exit velocity (`v₀`)** and **hood angle (`θ`)** using the fundamental physics of 2D projectile kinematics.

> Open the interactive demo below to adjust launch angle, flywheel speed, and target distance, and observe the parabolic arc trajectory hitting or missing the elevated target basket.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="2D Projectile Ballistics Sandbox"></iframe>

---

## 1. Kinematic Decomposition

When a game piece leaves the shooter flywheel at angle `θ` with initial speed `v₀`, its motion separates cleanly into independent horizontal and vertical axes:

```
               ▲ Y (Vertical under Gravity g)
               │         Apex (Peak)
               │          ┌───┐
     Launch ───┼──►      /     \
       (v₀, θ) │        /       \       Target Basket (x_target, y_target)
               │       /         \       ┌─┐
     Shooter ──┼──────┘           \─────►│ │
      (y₀)     │                         └─┘
               └───────────────────────────────► X (Horizontal at Constant Speed)
```

### 1. Horizontal Motion (Zero Acceleration):
```text
x(t) = v₀ · cos(θ) · t
```
Rearranging for time of flight `t`:
```text
t = x / (v₀ · cos(θ))
```

### 2. Vertical Motion (Under Constant Gravity `g = 9.81 m/s²`):
```text
y(t) = y₀ + v₀ · sin(θ) · t - ½ · g · t²
```

---

## 2. The 2D Trajectory Equation: Height as a Function of Distance

Substituting time `t = x / (v₀ · cos(θ))` into the vertical equation eliminates time entirely, giving the shape of the flight parabola:

```text
y(x) = y₀ + x · tan(θ) - (g · x²) / (2 · v₀² · cos²(θ))
```

---

## 3. Solving for Required Launch Speed (v₀)

If your robot vision system measures the target distance `Δx` and target height `Δy = y_target - y₀`, and you set your adjustable hood to angle `θ`, what exit speed `v₀` is needed?

Rearranging the trajectory equation for `v₀`:

```text
v₀ = √( (g · Δx²) / ( 2 · cos²(θ) · (Δx · tan(θ) - Δy) ) )
```

---

## 4. Solving It in Code (Java & WPILib)

Here is a clean ballistic trajectory solver in Java:

```java
public class BallisticsSolver {
    public static final double GRAVITY = 9.81; // m/s^2

    public static double computeRequiredSpeed(double targetDistX, double deltaHeightY, double angleRadians) {
        double cos = Math.cos(angleRadians);
        double tan = Math.tan(angleRadians);

        double numerator = GRAVITY * targetDistX * targetDistX;
        double denominator = 2.0 * cos * cos * (targetDistX * tan - deltaHeightY);

        if (denominator <= 0) {
            throw new IllegalArgumentException("Angle too low to reach target height!");
        }

        return Math.sqrt(numerator / denominator);
    }

    public static double speedToFlywheelRPM(double exitVelocityMps, double wheelRadiusMeters) {
        // Linear wheel surface speed: v = omega * r
        double radPerSec = exitVelocityMps / wheelRadiusMeters;
        return radPerSec * (60.0 / (2.0 * Math.PI));
    }

    public static void main(String[] args) {
        double distance = 4.5;               // 4.5 meters to target
        double deltaHeight = 2.1 - 0.6;      // 1.5 meter elevation change
        double launchAngle = Math.toRadians(55.0); // 55 degree hood

        double requiredSpeed = computeRequiredSpeed(distance, deltaHeight, launchAngle);
        double wheelRadius = 0.0508;         // 2-inch radius (4-inch wheel)
        double rpm = speedToFlywheelRPM(requiredSpeed, wheelRadius);

        System.out.printf("Target Distance: %.1f m | Required Exit Speed: %.2f m/s%n", distance, requiredSpeed);
        System.out.printf("Flywheel Setpoint: %.0f RPM%n", rpm);
        // Output: ~10.42 m/s -> ~1960 RPM
    }
}
```

---

## 5. Math! Translation Sidebar

The formal kinematic trajectory arc:

```text
y(x) = y₀ + x · tan(θ) - ½ · g · ( x / (v₀ · cos(θ)) )²
```

### Time of Flight and Apex Height:
* **Apex Peak Height:** `y_max = y₀ + (v₀² · sin²(θ)) / (2 · g)`
* **Total Flight Time:** `t_flight = (v₀ · sin(θ) + √(v₀² · sin²(θ) + 2·g·(y₀ - y_target))) / g`

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 2 Overview</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">Physics Axon Home</a></div>
  <div><a href="../02_concept_drag_spin_shooting_on_move/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Drag, Spin & Moving Shots →</a></div>
</div>
