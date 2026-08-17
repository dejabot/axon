# Concept 02: Gear Ratios, Torque Multiplication & Reflected Inertia

A typical brushless motor produces **4 to 7 Nm** of torque and spins at a blazing **6,000 RPM**. But lifting a heavy 15 kg elevator or pivoting an intake arm requires **50+ Nm** of torque at a much calmer **200 RPM**.

To bridge this gap, robotic mechanisms use **Gearboxes** (planetary gearsets, spur gears, and belt reductions) to trade rotational speed for raw output torque.

Crucially, gearboxes do something even more miraculous to physical dynamics: they scale the **Reflected Load Inertia** felt by the motor by the **square of the gear ratio (`1 / G²`)**!

> Open the interactive demo below to adjust gear ratios `G` and load mass, and observe how a 10:1 reduction makes a heavy load feel 100× lighter to the motor rotor.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Gearbox & Reflected Inertia Visualizer"></iframe>

---

## 1. Speed Reduction & Torque Multiplication

When a driving motor pinion with `N_in` teeth meshes with a driven output gear with `N_out` teeth, the gear ratio `G` is:

```text
G = N_out / N_in
```

### 1. Rotational Speed Decreases Linearly:
```text
ω_out = ω_in / G
```

### 2. Output Torque Multiplies Linearly:
```text
τ_out = G · τ_in · η
```
*(where `η` is the mechanical efficiency of the gear train, typically 90–95% for spur gears and 75–85% for multi-stage planetaries).*

---

## 2. Reflected Load Inertia: The Square Law (`1 / G²`)

When your robot pivots a heavy 5 kg arm, the motor must exert torque to accelerate that rotating mass. How heavy does that load "feel" directly at the motor shaft?

We can derive this using the conservation of Kinetic Energy:

```text
Kinetic Energy = ½ · J_load · ω_load² = ½ · J_reflected · ω_motor²
```

Because `ω_load = ω_motor / G`, we substitute:

```text
½ · J_reflected · ω_motor² = ½ · J_load · (ω_motor / G)²
```

Canceling `½ · ω_motor²` from both sides yields the famous **Reflected Inertia Formula**:

```text
J_reflected = J_load / G²
```

### Why This Is a Superpower in Robot Design:
* A **5:1 reduction** reduces felt load inertia by **25×**.
* A **10:1 reduction** reduces felt load inertia by **100×**!
* A **25:1 reduction** reduces felt load inertia by **625×**!

A massive steel elevator carriage that weighs 20 kg feels like a 32-gram feather to the spinning motor rotor!

---

## 3. Inertia Matching for Maximum Mechanism Acceleration

If your gear ratio is too low (`G = 2:1`), the motor doesn't have enough torque to accelerate the heavy load. If your gear ratio is too high (`G = 200:1`), the motor wastes all its torque just spinning its own rotor up to speed.

The optimal gear ratio for maximum mechanism acceleration occurs when the reflected load inertia exactly matches the motor's internal rotor inertia:

```text
G_optimal = √( J_load / J_motor )
```

---

## 4. Solving It in Code (Java & WPILib)

```java
public class GearboxPhysics {
    public static double computeOutputTorque(double motorTorqueNm, double gearRatio, double efficiency) {
        return motorTorqueNm * gearRatio * efficiency;
    }

    public static double computeReflectedInertia(double loadInertiaKgM2, double gearRatio) {
        return loadInertiaKgM2 / (gearRatio * gearRatio);
    }

    public static double computeOptimalRatio(double loadInertia, double motorRotorInertia) {
        return Math.sqrt(loadInertia / motorRotorInertia);
    }

    public static void main(String[] args) {
        double motorTorque = 4.0;       // 4.0 Nm (Kraken under load)
        double gearRatio = 12.0;        // 12:1 reduction
        double efficiency = 0.90;       // 90% gearbox efficiency
        double armInertia = 0.50;       // 0.50 kg·m² load
        double krakenRotorInertia = 0.00007; // kg·m²

        double outputTorque = computeOutputTorque(motorTorque, gearRatio, efficiency);
        double reflectedInertia = computeReflectedInertia(armInertia, gearRatio);
        double optimalRatio = computeOptimalRatio(armInertia, krakenRotorInertia);

        System.out.printf("Output Torque:      %.1f Nm%n", outputTorque);
        System.out.printf("Reflected Inertia:  %.6f kg·m² (Reduced by 144×!)%n", reflectedInertia);
        System.out.printf("Optimal Ratio:      %.1f:1%n", optimalRatio);
    }
}
```

---

## 5. Math! Translation Sidebar

Formal gearbox equations in robotics dynamics:

```text
τ_load = G · τ_motor · η
J_total = J_motor + (J_load / G²)
α_motor = τ_net / J_total
```

### How to Read This Out Loud:
* `J_total`: Total equivalent moment of inertia seen by the motor rotor.
* `α_motor` ("alpha motor"): Angular acceleration in radians per second squared (`rad/s²`).

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_concept_motor_curves_back_emf/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: DC Motors & Back-EMF</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="../../02_ballistics_trajectories/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 2: Projectile Ballistics →</a></div>
</div>
