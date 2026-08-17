# Concept 02: Closed-Loop PID Tuning & Step-Response Stability

Even with a strong physics feedforward model, robots encounter unexpected disturbances: battery voltage sag, worn carpet tread, and mechanical resistance.

To hold an arm firmly at 90° or steer a swerve wheel precisely to a target heading, we use a closed-loop **Proportional-Integral-Derivative (PID) Controller**.

However, poor PID tuning is the number one cause of mechanism destruction in robotics—causing violent oscillations, gear stripping, and excessive motor heating.

> Open the interactive demo below to adjust `kP`, `kI`, and `kD` sliders on a live robotic arm and observe rise time, overshoot percentage, and settling damping on the real-time oscilloscope.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="PID Closed-Loop Step Response Sandbox"></iframe>

---

## 1. The 3 PID Terms Explained Visually

```
 Error e(t) = Setpoint - Measurement
      │
      ├─► [ Proportional (kP · e) ] ──────► "The Virtual Spring" (Pushes harder when far away)
      │                                             │
      ├─► [ Integral (kI · ∫ e dt) ] ─────► "The Memory" (Clears persistent steady-state offset)
      │                                             │
      └─► [ Derivative (kD · de/dt) ] ────► "The Shock Absorber" (Dampens velocity to stop overshoot)
                                                    │
                                                    ▼
                                            [ + ] ──► Motor Voltage Output u(t)
```

### 1. Proportional (`kP` — The Spring):
* Output voltage is directly proportional to current error: `u_P = kP · error`.
* **Too Low:** Sluggish, fails to reach goal.
* **Too High:** Mechanism oscillates violently and rings like a tuning fork.

### 2. Integral (`kI` — The Memory):
* Sums error over time: `u_I = kI · (∑ error · Δt)`.
* Eliminates small steady-state errors caused by stiction or slight gravity mismatches.
* **Warning:** Too much `kI` causes **Integral Windup**, leading to massive delayed overshoot. Always clamp `setIntegratorRange()`.

### 3. Derivative (`kD` — The Shock Absorber):
* Measures the rate of change of error: `u_D = kD · (de / dt)`.
* Resists fast motion and acts as electronic viscous damping, stopping the mechanism smoothly right as it reaches the setpoint.

---

## 2. The 4 Key Step-Response Metrics

```
 Position (deg)
      ▲
      │                Peak Overshoot (Mp)
      │                   ┌───┐
 Setpoint ───┼───────────/─────\───┬─────────────────► Target (90°)
      │          /          \───┘  Tolerance Band (±2%)
      │        /
      │      /  ◄── Rise Time (tr)
      └─────/─────────────────────────────────────────► Time (seconds)
           0
```

1. **Rise Time (`t_r`):** Time required to first reach 90% of the setpoint.
2. **Peak Overshoot (`M_p`):** Maximum percentage by which the mechanism shoots past the goal.
3. **Settling Time (`t_s`):** Time required for oscillations to stay within an acceptable ±2% tolerance band.
4. **Steady-State Error (`e_ss`):** Remaining position offset after settling.

---

## 3. The Practical FRC Tuning Recipe

Follow this step-by-step procedure:

1. **Start with `kI = 0` and `kD = 0`:** Set feedforward gains (`kS`, `kV`, `kG`) first so the mechanism can move freely.
2. **Increase `kP`:** Double `kP` until the mechanism moves briskly to the target with moderate oscillation/overshoot.
3. **Increase `kD`:** Increase `kD` until the overshoot disappears and the mechanism comes to a crisp, critically damped stop.
4. **Add `kI` Only If Needed:** If a tiny 0.5° steady-state offset remains, add a very small `kI` with a strict integration limit (`setIntegratorRange(-1.0, 1.0)`).

---

## 4. Solving It in Code (Java & WPILib)

```java
import edu.wpi.first.math.controller.PIDController;
import edu.wpi.first.math.controller.ProfiledPIDController;
import edu.wpi.first.math.trajectory.TrapezoidProfile;

public class PIDTuningExamples {
    public static void main(String[] args) {
        // 1. Standard Discrete PID Controller (for high-speed velocity or steering)
        PIDController steerPID = new PIDController(4.5, 0.0, 0.25);
        steerPID.enableContinuousInput(-Math.PI, Math.PI); // Angle wrapping [-pi, +pi]
        steerPID.setTolerance(Math.toRadians(1.0));         // 1-degree tolerance band

        double currentAngle = 0.0;
        double targetAngle = Math.toRadians(90.0);
        double controlVolts = steerPID.calculate(currentAngle, targetAngle);

        System.out.printf("Steering PID Output: %.2f Volts (At Goal: %b)%n",
            controlVolts, steerPID.atSetpoint());

        // 2. Profiled PID Controller (Constrained by Trapezoidal Motion Profile)
        TrapezoidProfile.Constraints constraints = 
            new TrapezoidProfile.Constraints(3.0, 6.0); // maxVel=3.0 m/s, maxAcc=6.0 m/s²
        
        ProfiledPIDController armPID = new ProfiledPIDController(5.0, 0.0, 0.30, constraints);
        double armVolts = armPID.calculate(0.0, 1.5); // Smoothly profiles from 0m to 1.5m
        
        System.out.printf("Profiled Arm PID Output: %.2f Volts%n", armVolts);
    }
}
```

---

## 5. Math! Translation Sidebar

The continuous-time PID equation:

```text
u(t) = k_p · e(t) + k_i · ∫₀ᵗ e(τ) dτ + k_d · ( de(t) / dt )
```

### Critical Damping Ratio:
* A second-order system is **Critically Damped** (`ζ = 1.0`) when `kD = 2 · √(kP · J_total)`. At this exact balance, the mechanism reaches the setpoint in the fastest possible time with **zero overshoot**.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_concept_voltage_feedforward_models/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: Voltage Feedforward</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 4 Overview</a></div>
  <div><a href="../../../kinematics/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Next Axon: Kinematics & Motion Planning →</a></div>
</div>
