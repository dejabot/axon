# Concept 01: Physics Feedforward: kS, kV, kA, and kG Models

A pure feedback controller (like standard PID) is **reactive**: it cannot do anything until an error has *already occurred*.

If you command a shooter flywheel to jump from 0 to 4,000 RPM, a pure PID loop sees a huge error, spikes maximum voltage, overshoots wildly, and takes seconds to settle.

In modern robotics, we use **Physics-Based Feedforward** to calculate the exact voltage required by physical laws *before* the motor even moves, leaving PID to handle only minor unexpected disturbances.

> Open the interactive demo below to compare PID-Only control against PID + Feedforward, and observe how `kS`, `kV`, `kA`, and `kG` eliminate tracking lag completely.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Physics Feedforward Voltage Model Simulator"></iframe>

---

## 1. The 4 Fundamental Voltage Terms

A mechanism requires voltage to overcome four distinct physical phenomena:

```text
V_feedforward = kS · sgn(v) + kV · v + kA · a + kG
```

### 1. `kS` (Static Friction Stiction Voltage):
* Even when a motor is barely moving, grease, bearings, and meshed gear teeth resist motion.
* `kS` is the minimum voltage (typically **0.1 to 0.35 Volts**) needed to break static friction and get the mechanism moving.
* Multiplied by `sgn(v)` (sign of velocity) so it always assists the direction of travel.

### 2. `kV` (Velocity & Back-EMF Voltage):
* As seen in Concept 01, spinning motors generate reverse Back-EMF voltage (`V = ω / K_v`).
* `kV` is the voltage required to sustain one unit of steady-state speed (e.g. `2.2 Volts per m/s` or `0.002 Volts per RPM`).

### 3. `kA` (Acceleration & Inertia Voltage):
* According to Newton's Second Law (`F = m · a`), accelerating a mass requires torque, which requires current and voltage.
* `kA` provides an instant voltage boost proportional to desired acceleration `a` (typically **0.15 to 0.45 Volts per m/s²**).

### 4. `kG` (Gravity Voltage):
* **For Elevators:** Constant upward voltage `kG` to cancel Earth's gravity (`m · g`).
* **For Rotating Arms:** Gravity torque changes with arm angle `θ`, so the voltage is modulated by `kG · cos(θ)`!

---

## 2. The Feedforward + Feedback Partnership

```
 Desired Trajectory (v, a) ──► [ Physics Feedforward (kS, kV, kA, kG) ] ──► 95% Base Voltage
                                                                                   │
                                                                                   ▼
 Target State ──┐                                                                 [ + ] ──► Total Voltage to Motor
                ▼                                                                  ▲
 Measurement ──► [ - ] ──► [ Feedback PID Controller ] ───────────────────────────┘ 5% Fine Correction
```

* **Feedforward does 95% of the heavy lifting:** It handles known physical forces (friction, back-EMF, inertia, gravity).
* **Feedback PID does the remaining 5%:** It corrects for minor battery voltage sag, carpet irregularities, and game piece compression.

---

## 3. Solving It in Code (Java & WPILib)

WPILib provides dedicated feedforward classes in `edu.wpi.first.math.controller`:

```java
import edu.wpi.first.math.controller.SimpleMotorFeedforward;
import edu.wpi.first.math.controller.ElevatorFeedforward;
import edu.wpi.first.math.controller.ArmFeedforward;

public class FeedforwardExamples {
    public static void main(String[] args) {
        // 1. Drivetrain & Flywheels (kS, kV, kA)
        SimpleMotorFeedforward flywheelFF = new SimpleMotorFeedforward(0.20, 0.0021, 0.0004);
        double flywheelTargetRpm = 4500.0;
        double flywheelTargetAccel = 2000.0; // RPM/s
        double flywheelVolts = flywheelFF.calculate(flywheelTargetRpm, flywheelTargetAccel);

        // 2. Linear Elevator (kS, kG, kV, kA)
        ElevatorFeedforward elevatorFF = new ElevatorFeedforward(0.15, 0.85, 2.40, 0.20);
        double elevatorVolts = elevatorFF.calculate(1.5, 3.0); // 1.5 m/s, 3.0 m/s²

        // 3. Rotating Arm (kS, kG*cos(theta), kV, kA)
        ArmFeedforward armFF = new ArmFeedforward(0.10, 0.60, 1.80, 0.15);
        double armAngleRad = Math.toRadians(30.0); // 30 degrees from horizontal
        double armVolts = armFF.calculate(armAngleRad, 2.0, 4.0);

        System.out.printf("Flywheel Voltage: %.2f V%n", flywheelVolts);
        System.out.printf("Elevator Voltage: %.2f V%n", elevatorVolts);
        System.out.printf("Arm Voltage:      %.2f V%n", armVolts);
    }
}
```

---

## 4. Math! Translation Sidebar

The formal system identification voltage equation:

```text
u(t) = kS · sgn(v(t)) + kV · v(t) + kA · a(t) + kG(θ)
```

### System Identification (SysId):
* WPILib includes an automated calibration tool called **SysId** that runs automated quasistatic (slow ramp) and dynamic (step voltage) test routines on your physical robot mechanism to measure `kS`, `kV`, and `kA` with 99%+ accuracy!

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 4 Overview</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">Physics Axon Home</a></div>
  <div><a href="../02_concept_closed_loop_pid_tuning/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Closed-Loop PID Tuning →</a></div>
</div>
