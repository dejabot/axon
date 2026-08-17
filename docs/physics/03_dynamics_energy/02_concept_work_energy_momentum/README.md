# Concept 02: Work, Kinetic Energy & Elevator Counterbalancing

Physics in robotics is governed by the conservation of **Work, Energy, and Momentum**:

1. **Kinetic Energy (`KE = ½ · m · v²`):** A 60 kg robot sprinting at 5.5 m/s carries nearly **900 Joules** of kinetic energy that must be safely absorbed by bumpers during defense collisions.
2. **Gravitational Potential Energy (`PE = m · g · h`):** An elevator lifting a heavy 15 kg carriage must continuously fight gravity with high motor stall current—unless you counterbalance it with **Constant-Force Springs**.

> Open the interactive demo below to adjust elevator mass and constant-force spring assistance, and observe how spring potential energy reduces the motor's holding voltage to near zero.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Elevator Counterbalancing & Work-Energy Visualizer"></iframe>

---

## 1. Kinetic Energy & Momentum in Collisions

When a robot of mass `m` moves at velocity `v`:

* **Linear Momentum (`p = m · v`):** Governs collision impulse (`F · Δt = Δp`).
* **Kinetic Energy (`KE = ½ · m · v²`):** Because energy scales with **velocity squared (`v²`)**, a robot driving at 6 m/s carries **4× more destructive energy** than one driving at 3 m/s!

---

## 2. The Elevator Gravity Problem

To hold a 12 kg elevator carriage stationary at a height of 1.5 meters, gravity constantly pulls downward with a force:

```text
F_gravity = m · g = 12.0 kg · 9.81 m/s² = 117.7 Newtons
```

Without compensation, the lift motors must continuously apply holding voltage (`~2.5 to 3.5 Volts`), drawing steady stall current, draining the battery, and heating up motor coils.

Furthermore, moving **UP** requires fighting `F_gravity + F_accel`, while moving **DOWN** is accelerated by gravity (`-F_gravity + F_accel`), making control asymmetrical.

---

## 3. The Counterbalance Solution: Constant-Force Springs

A **Constant-Force Spring** (made from pre-stressed coiled spring steel) exerts an almost perfectly constant upward pulling force `F_spring` regardless of how far the elevator extends.

```
       Top Pulley
          ┌─┐
          │ │
          └┬┘
           │ 
       ┌───┴───┐ ◄── Pulling Force F_spring (Constant ~118 N)
       │Carriage│
       │(12 kg) │
       └───┬───┘ ◄── Gravity F_g = m · g (118 N)
```

By sizing springs such that `F_spring ≈ m_carriage · g`:

```text
F_net_gravity = (m · g) - F_spring ≈ 0 Newtons
```

### Benefits of Mechanical Counterbalancing:
1. **Holding Current Drops to 0 Amps:** The elevator floats in mid-air at any height with zero battery drain.
2. **Symmetrical Motion:** Lifting up and lowering down feel identical to the control loop.
3. **Double the Speed:** 100% of motor torque is dedicated to pure acceleration rather than fighting Earth's gravity.

---

## 4. Solving It in Code (Java & WPILib)

```java
public class ElevatorPhysics {
    public static final double GRAVITY = 9.81;

    public static double computeRequiredHoldingVoltage(
            double carriageMassKg, 
            double springAssistN, 
            double spoolRadiusMeters, 
            double gearRatio, 
            double motorKt, 
            double motorR) {
        
        // 1. Net downward force after spring assist
        double netForceDown = (carriageMassKg * GRAVITY) - springAssistN;

        // 2. Torque required at motor shaft
        double spoolTorque = netForceDown * spoolRadiusMeters;
        double motorTorque = spoolTorque / gearRatio;

        // 3. Motor current and required holding voltage
        double currentAmps = motorTorque / motorKt;
        double holdingVolts = currentAmps * motorR;

        return Math.max(0.0, holdingVolts);
    }

    public static void main(String[] args) {
        double mass = 12.0;            // 12 kg carriage
        double spoolRadius = 0.0254;   // 1-inch spool radius
        double gearRatio = 15.0;       // 15:1 gearbox
        double kt = 0.019;             // Kraken motor Kt
        double r = 0.025;              // Kraken internal resistance

        // Case A: Uncompensated Elevator (0 N Spring)
        double voltsUnbalanced = computeRequiredHoldingVoltage(mass, 0.0, spoolRadius, gearRatio, kt, r);

        // Case B: Counterbalanced Elevator (Two 55 N Springs = 110 N)
        double voltsBalanced = computeRequiredHoldingVoltage(mass, 110.0, spoolRadius, gearRatio, kt, r);

        System.out.printf("Holding Voltage WITHOUT Springs: %.2f Volts (High Heat!)%n", voltsUnbalanced);
        System.out.printf("Holding Voltage WITH Springs:    %.2f Volts (Cool & Efficient)%n", voltsBalanced);
        // Output: ~3.28V drops to ~0.21V!
    }
}
```

---

## 5. Math! Translation Sidebar

Work-Energy and Potential Energy formulations:

```text
W = ∫ F · dx = ΔKE + ΔPE
PE_total = m · g · h - F_spring · h ≈ 0
```

### Kinetic Energy in Robot Collisions:
* `KE = ½ · m · v²`
* A 60 kg robot moving at `5.5 m/s` delivers `½ · 60 · (5.5)² = 907.5 Joules`. Compressible foam bumpers provide `~0.05m` of deceleration distance, resulting in peak impact forces of `F_impact = W / d = 907.5 / 0.05 = 18,150 Newtons` (~4,000 lbs of force)!

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_concept_newtons_laws_friction/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: Traction Limits</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 3 Overview</a></div>
  <div><a href="../../04_control_physics/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 4: Control Physics & Voltage Models →</a></div>
</div>
