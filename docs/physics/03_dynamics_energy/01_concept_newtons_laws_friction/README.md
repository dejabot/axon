# Concept 01: Forces, Acceleration & Wheel Traction Limits

A modern 4-wheel swerve drive powered by brushless Kraken motors can theoretically produce over **3,000 Newtons** of wheel thrust. But if you slam the throttle forward on the driver station, the wheels can instantly break traction, shred the carpet, and spin out without accelerating the robot.

No matter how powerful your motors are, your robot can never accelerate faster than the physical limits of **Static Friction** between your wheel tread and the carpet.

> Open the interactive demo below to adjust commanded motor thrust, carpet friction coefficient `μ`, and robot mass, and observe how exceeding the Friction Circle causes catastrophic wheel slip.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Friction Circle & Wheel Slip Visualizer"></iframe>

---

## 1. Static Friction & The Theoretical Acceleration Ceiling

When a wheel rolls without slipping, the contact patch between the rubber tread and the carpet fibers is momentarily stationary relative to the ground. The maximum horizontal force the wheels can exert is governed by **Coulomb's Law of Static Friction**:

```text
F_traction_max = μ_s · N = μ_s · (m · g)
```

* `μ_s`: Coefficient of static friction (typically **1.2 to 1.5** for nitrile roughtop / neoprene tread on FRC cordura carpet).
* `N`: Total normal force exerted by the ground on the robot (`m · g`).

### The Acceleration Ceiling:
Applying Newton's Second Law (`F = m · a`):

```text
a_max = F_traction_max / m = (μ_s · m · g) / m = μ_s · g
```

Notice that robot mass `m` cancels out! If your tread coefficient is `μ_s = 1.3`, the absolute maximum possible acceleration of your robot is:

```text
a_max = 1.3 · 9.81 m/s² = 12.75 m/s² (~1.3 G's)
```

---

## 2. Static vs. Kinetic Friction: The "Slip Cliff"

```
 Friction Force
      ▲
      │       Peak Static Grip (μ_s ≈ 1.35)
      │          ┌───┐
      │         /     \  ◄── The Slip Cliff!
      │        /       └─────────────────────► Kinetic Sliding (μ_k ≈ 0.85)
      │       /
      └──────/────────────────────────────────► Commanded Motor Force
```

* **Static Grip (`μ_s ≈ 1.35`):** The tread teeth interlock with carpet fibers.
* **Kinetic Sliding (`μ_k ≈ 0.85`):** Once wheel speed exceeds ground speed and the tire slips, friction drops by **nearly 40%**!

Spinning your wheels does not make the robot accelerate faster—it reduces your pushing force and turns expensive tread into blue rubber dust.

---

## 3. The 2D Friction Circle

When a swerve robot accelerates forward while simultaneously executing a sharp high-speed turn, the wheel treads must share their available grip between **forward traction (`F_forward`)** and **lateral centripetal force (`F_lateral`)**:

```text
√( F_forward² + F_lateral² ) ≤ μ_s · N
```

If you demand 100% of your grip for forward acceleration, you have **0% remaining** for turning without sliding out.

---

## 4. Solving It in Code (Java & WPILib)

Here is how to calculate maximum allowable motor torque before wheel slip in Java:

```java
public class TractionLimits {
    public static final double GRAVITY = 9.81;

    public static double computeMaxTractionForce(double robotMassKg, double frictionCoeff) {
        double normalForce = robotMassKg * GRAVITY;
        return frictionCoeff * normalForce;
    }

    public static double computeMaxMotorTorque(double maxTractionN, double wheelRadiusMeters, double gearRatio, int numMotors) {
        // Force per wheel
        double forcePerWheel = maxTractionN / numMotors;
        // Wheel axle torque
        double axleTorque = forcePerWheel * wheelRadiusMeters;
        // Motor rotor torque before gearbox
        return axleTorque / gearRatio;
    }

    public static void main(String[] args) {
        double robotMass = 55.0;       // 55 kg robot
        double mu = 1.35;              // Nitrile tread on carpet
        double wheelRadius = 0.0508;   // 2-inch radius (4-inch wheel)
        double swerveGearRatio = 6.75; // L2 swerve
        int numMotors = 4;

        double maxForce = computeMaxTractionForce(robotMass, mu);
        double maxAccel = maxForce / robotMass;
        double slipTorque = computeMaxMotorTorque(maxForce, wheelRadius, swerveGearRatio, numMotors);

        System.out.printf("Max Ground Traction Force: %.1f N%n", maxForce);
        System.out.printf("Max Acceleration Limit:     %.2f m/s² (%.2f G)%n", maxAccel, maxAccel / GRAVITY);
        System.out.printf("Motor Slip Torque Limit:    %.2f Nm per motor%n", slipTorque);
    }
}
```

---

## 5. Math! Translation Sidebar

The formal friction limit constraint in swerve dynamics:

```text
||F_wheel|| ≤ μ_s · F_z
where F_z = (m · g) / 4 + ΔF_weight_transfer
```

### Dynamic Weight Transfer:
* When accelerating forward at `a`, the robot's center of mass height `h_cg` creates a pitch torque that transfers normal force from the front wheels to the rear wheels: `ΔF = (m · a · h_cg) / (2 · L)`.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 3 Overview</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">Physics Axon Home</a></div>
  <div><a href="../02_concept_work_energy_momentum/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Work, Energy & Momentum →</a></div>
</div>
