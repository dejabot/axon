# Concept 01: Brushless DC Motors, Back-EMF & Torque Curves

When an FRC robot pushes against a heavy defense barrier, motor current can instantly spike to over **300 Amps**, causing severe battery brownouts. Yet when the same robot cruises at full speed across an open field, current drops to a mere **15 Amps**.

Understanding why motors behave this way requires looking at the fundamental physics of **Back-Electromotive Force (Back-EMF)** and electromechanical torque curves.

> Open the interactive demo below to inspect live dynamometer curves for modern brushless motors (Kraken X60, Falcon 500, NEO) and observe torque, current draw, and peak mechanical power under varying voltage and load RPM.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="DC Motor Dynamometer Curves Visualizer"></iframe>

---

## 1. The Electromechanical Circuit

A DC motor consists of permanent magnets and wire coils with internal electrical resistance `R`. When you apply battery voltage `V_applied`:

1. **Current Creates Torque:** Flowing electric current `I` creates a magnetic field that exerts mechanical torque `τ` on the rotor:
   ```text
   τ = K_t · I
   ```
   *(where `K_t` is the Motor Torque Constant in Nm/Amp).*

2. **Spinning Creates Generator Voltage (Back-EMF):** As the rotor spins at angular velocity `ω`, the moving magnets induce a reverse electrical voltage inside the wire coils—acting like an internal generator that fights your battery:
   ```text
   V_emf = ω / K_v
   ```
   *(where `K_v` is the Motor Velocity Constant in rad/s per Volt).*

3. **Total Voltage Balance (Ohm's Law):**
   ```text
   V_applied = I · R + V_emf
   ```

Rearranging for current draw:

```text
I = (V_applied - ω / K_v) / R
```

---

## 2. The 4 Key Operating Points on a Dyno Curve

```
 Torque (Nm) ──► Max (Stall)
   │ \
   │   \  Torque Line (Decreases Linearly)
   │     \
   │       \   Peak Mechanical Power (at 50% RPM)
   │         \     ┌───┐
   │           \  /     \
   │             \       \
   └───────────────\───────\────► Motor RPM
  Stall (0 RPM)             Free Speed (Max RPM, 0 Torque)
```

1. **Stall Condition (`ω = 0`):**
   * The motor is blocked and cannot rotate.
   * `V_emf = 0V`. Current reaches maximum: `I_stall = V / R` (~300+ Amps!).
   * Output torque is at its maximum peak (`τ_stall = K_t · I_stall`), but mechanical power is **0 Watts** (`Power = τ · ω = 0`).

2. **Free Speed Condition (`τ = 0`):**
   * The motor spins with no external mechanical resistance.
   * `V_emf` almost matches `V_applied`. Current drops to near zero (`I_free`), producing zero useful torque.

3. **Peak Mechanical Power (`50% Free Speed`):**
   * Mechanical power is the product of torque and angular speed: `P_mech = τ · ω`.
   * The power curve is a parabola that reaches its absolute peak at **exactly half of free speed** (`½ · ω_free`).

4. **Maximum Efficiency (~85% Free Speed):**
   * Electrical energy is converted to mechanical output with minimum heat loss `I² · R`.

---

## 3. Solving It in Code (Java & WPILib)

### First-Principles Java
```java
public class MotorPhysics {
    public static double computeCurrent(double appliedVolts, double speedRadPerSec, double R, double Kv) {
        double vEmf = speedRadPerSec / Kv;
        return (appliedVolts - vEmf) / R;
    }

    public static double computeTorque(double currentAmps, double Kt) {
        return Kt * currentAmps;
    }
}
```

### Production WPILib Equivalent (`DCMotor`)
WPILib includes built-in, pre-measured physical constants for all major FRC motors in `edu.wpi.first.math.system.plant.DCMotor`:

```java
import edu.wpi.first.math.system.plant.DCMotor;

// 1. Get calibrated Kraken X60 physical motor model
DCMotor kraken = DCMotor.getKrakenX60(1);

double appliedVolts = 12.0;
double currentSpeedRadPerSec = 300.0; // ~2865 RPM (near 50% power)

// 2. Query WPILib for torque and current draw
double currentAmps = kraken.getCurrent(currentSpeedRadPerSec, appliedVolts);
double torqueNm = kraken.getTorque(currentAmps);
double mechPowerWatts = torqueNm * currentSpeedRadPerSec;

System.out.printf("Kraken X60 at 300 rad/s -> Current: %.1f A | Torque: %.2f Nm | Power: %.0f W%n",
    currentAmps, torqueNm, mechPowerWatts);
```

---

## 4. Math! Translation Sidebar

The electromechanical motor equation in physics literature:

```text
V = I · R + K_e · ω
τ = K_t · I
```

### The Inherent Equality of K_t and K_e:
* In standard SI metric units (`Newton-meters / Amp` and `Volts / (rad/sec)`), the torque constant `K_t` and back-EMF constant `K_e = 1 / K_v` are **mathematically identical**: `K_t = K_e`.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1 Overview</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">Physics Axon Home</a></div>
  <div><a href="../02_concept_gearboxes_reflected_inertia/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Gearboxes & Reflected Inertia →</a></div>
</div>
