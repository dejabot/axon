# Concept 02: Aerodynamic Drag, Magnus Spin & Shooting on the Move

Ideal parabolic equations assume a physics test in a vacuum. In the real world:

1. **Aerodynamic Drag:** Foam game pieces (like the 2024 Note or 2022 Cargo) are lightweight with large surface areas, decelerating rapidly due to air resistance (`F_drag ∝ v²`).
2. **The Magnus Effect:** High-speed shooter flywheels induce heavy backspin, generating an upward aerodynamic lift force that flattens the trajectory.
3. **Shooting on the Move:** Autonomous robots do not stop moving to shoot. When driving at 3.5 m/s, the robot's chassis velocity adds vectorially to the game piece's exit speed.

> Open the interactive demo below to enable air drag, spin-induced Magnus lift, and robot chassis velocity, and observe how vector compensation adjusts turret angle and flywheel RPM.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Aerodynamic Drag & Moving Ballistics Simulator"></iframe>

---

## 1. Aerodynamic Drag Force

As a projectile moves through air with density `ρ` (1.225 kg/m³ at sea level) at speed `v`, air resistance exerts a decelerating force opposing velocity:

```text
F_drag = -½ · ρ · C_d · A · |v| · v
```

* `C_d`: Drag coefficient (dimensionless, ~0.4 to 0.8 for foam game pieces).
* `A`: Frontal cross-sectional area in m² (`π · r²`).

Because drag is proportional to **velocity squared (`v²`)**, shooting twice as fast creates **4× more air drag**!

---

## 2. The Magnus Effect (Backspin Lift)

When a game piece spins at angular speed `ω` around its horizontal axis:
* Air moves **faster** over the top of the piece (lower pressure).
* Air moves **slower** under the bottom of the piece (higher pressure).
* The resulting pressure difference generates an upward **Magnus Lift Force**:

```text
F_magnus = S · (ω × v)
```

Backspin keeps the game piece aloft longer, extending effective shooting range and flattening the entry angle into the target basket.

---

## 3. Shooting on the Move: Vector Addition

When your robot shoots while strafing or driving across the field at velocity vector `v_robot`:

```
           Target Goal
               ▲
               │
               │ Desired World Trajectory (v_world)
               │
               ├─────────────────────────┐
               │                         │
               ▲                         ▲
         v_shooter                 v_robot
      (Turret Heading)         (Chassis Speed)
```

The game piece's velocity in the global field coordinate frame is the vector sum:

```text
v_world = v_shooter + v_robot
```

To hit the target while driving, you must solve backwards for the required shooter heading:

```text
v_shooter = v_target_desired - v_robot
```

If you are strafing to the right at `2.0 m/s`, your shooter must aim slightly to the **left** by an angle `φ = atan2(-v_robot_y, v_shot_x)`!

---

## 4. Solving It in Code (Java & WPILib)

```java
import edu.wpi.first.math.geometry.Translation2d;
import edu.wpi.first.math.geometry.Rotation2d;

public class MovingShooterSolver {
    public static Translation2d computeMovingShooterVector(
            Translation2d targetRelativePos, 
            double timeOfFlightSec, 
            Translation2d robotVelocityMps) {
        
        // 1. Where will the target be relative to the moving robot when the shot lands?
        // Virtual Target Position = Current Target - (v_robot * timeOfFlight)
        Translation2d virtualTarget = targetRelativePos.minus(robotVelocityMps.times(timeOfFlightSec));

        // 2. Solve for required shooter azimuth heading and exit speed
        Rotation2d requiredShooterHeading = virtualTarget.getAngle();
        double requiredRange = virtualTarget.getNorm();

        System.out.printf("Virtual Target Range: %.2f m | Turret Lead Angle: %.1f°%n",
            requiredRange, requiredShooterHeading.getDegrees());

        return virtualTarget;
    }

    public static void main(String[] args) {
        // Target is 4.0m directly ahead (x=4.0, y=0.0)
        Translation2d targetPos = new Translation2d(4.0, 0.0);
        
        // Robot is strafing right at 2.0 m/s (vx=0.0, vy=-2.0)
        Translation2d robotVelocity = new Translation2d(0.0, -2.0);
        double estFlightTime = 0.50; // 0.5 seconds flight

        computeMovingShooterVector(targetPos, estFlightTime, robotVelocity);
        // Compensates by leading the shot 1.0 meter left!
    }
}
```

---

## 5. Math! Translation Sidebar

The complete differential equation of motion for a spinning projectile in air:

```text
m · a = m · g + F_drag + F_magnus
m · (dv / dt) = m · g - ½ · ρ · C_d · A · |v| · v + S · (ω × v)
```

Because this non-linear differential equation has no closed-form algebraic solution, robot coprocessors solve it in real time using 20ms **Runge-Kutta numerical integration** or pre-computed 2D lookup tables.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_concept_2d_kinematic_ballistics/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: 2D Ballistics</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../../03_dynamics_energy/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 3: Dynamics & Energy →</a></div>
</div>
