# Concept 03: Single-Variable Motion Calculus & Jerk

```
       Module 1: Math Foundations  ➔  Concept 03: Motion Calculus & Jerk
```

> **▶ Interactive Demo: [Single-Variable Motion Calculus & Jerk Visualizer](demo.html)**
>
> Open in your browser or explore the embedded frame below to observe higher-order derivatives of motion (Position ➔ Velocity ➔ Acceleration ➔ Jerk) and compare S-Curve smoothing against destructive step profiles.

<iframe src="demo.html" width="100%" height="560" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--code-bg, #0a0d14);"></iframe>

---

## 1. Intuitive Mental Model

Imagine you are standing inside an elevator holding a full cup of hot coffee filled to the very brim.

1. **Velocity `v` (Position change):** If the elevator is traveling upward at a constant speed of 10 meters per second, the coffee remains completely still and flat in the cup. Velocity alone creates no physical forces on your body.
2. **Acceleration `a` (Velocity change):** When the elevator begins moving from rest, it accelerates upward. You feel heavier in your feet, and the coffee level compresses against the cup bottom with extra force `F = m·(g + a)`. Because the acceleration is steady, the liquid surface remains level and smooth.
3. **Jerk `j` (Acceleration change):** What happens if the motor instantly applies full torque in 0 milliseconds? The elevator floor violently snaps upward. The sudden, instantaneous leap in acceleration sloshes the coffee violently against the sides, splashing boiling liquid across your hand.

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="170" viewBox="0 0 340 170" style="max-width: 100%; height: auto;">
    <!-- S-Curve (Smooth) -->
    <path d="M 30 130 C 60 130 70 50 110 50 L 140 50" fill="none" stroke="#4ade80" stroke-width="3" />
    <text x="30" y="35" fill="#4ade80" font-family="monospace" font-weight="bold" font-size="11">Smooth S-Curve (Bounded Jerk)</text>
    <text x="30" y="150" fill="#94a3b8" font-family="monospace" font-size="10">Continuous acceleration</text>
    
    <!-- Trapezoidal Step (Infinite Jerk) -->
    <path d="M 200 130 L 200 50 L 310 50" fill="none" stroke="#f43f5e" stroke-width="3" />
    <text x="200" y="35" fill="#f43f5e" font-family="monospace" font-weight="bold" font-size="11">Step Profile (Infinite Jerk)</text>
    <text x="200" y="150" fill="#f43f5e" font-family="monospace" font-size="10">Instant shock: F = m·a</text>
  </svg>
</div>

Calculus is the mathematical framework for measuring and controlling these continuous rates of change. In autonomous robotics and deep learning optimization, ignoring higher-order derivatives like **Jerk** or using naive discrete integration breaks mechanisms and destabilizes algorithms.

---

## 2. Mathematical & Physical Derivations

### The Derivative as an Instantaneous Limit
The average rate of change of a physical quantity `x(t)` over a time interval `Δt` is:

```
   v_avg = (x(t + Δt) - x(t)) / Δt
```

Taking the limit as the observation interval shrinks to zero (`Δt ➔ 0`) yields the instantaneous derivative:

```
   v(t) = dx / dt = lim [ (x(t + Δt) - x(t)) / Δt ]
                    Δt➔0
```

Geometrically, the derivative is the exact slope of the tangent line to the function at time `t`.

```
   Position:     x(t)
   Velocity:     v(t) = dx / dt = x'(t)
   Acceleration: a(t) = dv / dt = d²x / dt² = x''(t)
   Jerk:         j(t) = da / dt = d³x / dt³ = x'''(t)
   Snap (Jounce): s(t) = dj / dt = d⁴x / dt⁴
```

### The Fundamental Theorem of Calculus & Definite Integration
Differentiation and integration are inverse operations. If we know an acceleration profile `a(t)` over time, we compute velocity and position by accumulating infinitesimal slices `a(t)·dt`:

```
   v(t) = v(0) + ∫₀ᵗ a(τ) dτ
   x(t) = x(0) + ∫₀ᵗ v(τ) dτ
```

For constant acceleration `a(t) = a₀`:
- `v(t) = v₀ + a₀·t`
- `x(t) = x₀ + v₀·t + (1/2)·a₀·t²`

### Why Trapezoidal Profiles Have Infinite Jerk
Standard robotics libraries often generate **Trapezoidal Velocity Profiles**:
1. Accelerate at constant `+a_max` until reaching target cruising speed `v_max`.
2. Cruise at constant velocity `v_max` (`a = 0`).
3. Decelerate at constant `-a_max` until stopping at target position.

At the exact transition points where acceleration jumps instantaneously from `0` to `+a_max` in zero seconds (`Δt = 0`):

```
   jerk = lim [ (+a_max - 0) / Δt ] = a_max / 0 = +∞
          Δt➔0
```

An infinite derivative represents an unphysical impulse force `F = m·a`. In the physical world, applying an instantaneous acceleration step excites high-frequency structural resonances, stretches timing belts, snaps roller chains, and shears gearbox teeth.

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="150" viewBox="0 0 340 150" style="max-width: 100%; height: auto;">
    <line x1="30" y1="120" x2="310" y2="120" stroke="#334155" stroke-width="1.5" />
    <!-- Velocity curve -->
    <path d="M 30 120 L 90 40 L 230 40 L 290 120" fill="none" stroke="#38bdf8" stroke-width="3" />
    <text x="35" y="30" fill="#38bdf8" font-family="monospace" font-weight="bold" font-size="11">Trapezoidal Velocity v(t)</text>
    <circle cx="90" cy="40" r="4" fill="#f43f5e" />
    <circle cx="230" cy="40" r="4" fill="#f43f5e" />
    <text x="95" y="35" fill="#f43f5e" font-family="monospace" font-size="10">j = +∞</text>
    <text x="235" y="35" fill="#f43f5e" font-family="monospace" font-size="10">j = -∞</text>
  </svg>
</div>

### S-Curve (Jerk-Limited) Motion Profile Derivation
To ensure smooth motion, we bound the maximum jerk to a finite constant `j_max`. 

An **S-Curve Profile** consists of 7 distinct time phases:
1. **Ramp-up Acceleration:** `j(t) = +j_max` ➔ `a(t) = j_max · t` ➔ `v(t) = (1/2)·j_max · t²`
2. **Constant Acceleration:** `j(t) = 0` ➔ `a(t) = a_max` ➔ `v(t) = v₁ + a_max · t`
3. **Ramp-down Acceleration:** `j(t) = -j_max` ➔ `a(t) = a_max - j_max · t`
4. **Constant Cruising Velocity:** `j(t) = 0`, `a(t) = 0`, `v(t) = v_max`
5. **Ramp-up Deceleration:** `j(t) = -j_max` ➔ `a(t) = -j_max · t`
6. **Constant Deceleration:** `j(t) = 0` ➔ `a(t) = -a_max`
7. **Ramp-down Deceleration:** `j(t) = +j_max` ➔ `a(t) ➔ 0` smooth stop at target `x_target`.

Because `a(t)` is continuous (differentiable everywhere), mechanical forces vary smoothly without shock impulses.

### Discrete Numerical Integration in Control Loops
A digital robot controller samples sensor readings at discrete time steps `k, k+1, k+2, ...`.

#### Forward Euler Integration (1st-Order Explicit)
Assumes rate of change remains constant across the entire interval `dt`:

```
   v[k+1] = v[k] + a[k] · dt
   x[k+1] = x[k] + v[k] · dt
```
- Truncation Error: `O(dt)` per step.
- Physical Flaw: Underestimates position during acceleration by using outdated initial velocities.

#### Trapezoidal Integration (Heun's 2nd-Order Method)
Averages the rate of change between the start and end of the time step:

```
   v[k+1] = v[k] + (1/2) · (a[k] + a[k+1]) · dt
   x[k+1] = x[k] + (1/2) · (v[k] + v[k+1]) · dt
```
- Truncation Error: `O(dt²)` per step.
- Captures quadratic position curves exactly under constant acceleration.

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="150" viewBox="0 0 340 150" style="max-width: 100%; height: auto;">
    <!-- Euler Rectangle -->
    <rect x="40" y="70" width="80" height="50" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="1.5" />
    <text x="40" y="55" fill="#f43f5e" font-family="monospace" font-size="10">Euler: Rectangular O(dt)</text>
    
    <!-- Trapezoid Slice -->
    <polygon points="190,120 190,70 270,30 270,120" fill="rgba(74, 222, 128, 0.2)" stroke="#4ade80" stroke-width="1.5" />
    <text x="190" y="20" fill="#4ade80" font-family="monospace" font-weight="bold" font-size="10">Trapezoid: Exact O(dt²)</text>
    
    <line x1="20" y1="120" x2="300" y2="120" stroke="#334155" stroke-width="1.5" />
  </svg>
</div>

---

## 3. Dual Grounding: FRC Robotics & Modern ML

### FRC Autonomous Robotics: High-Speed Elevator Control & Acceleration Feedforward

#### High-Speed Cascade Elevator
An FRC game elevator carrying an intake mechanism must travel 2.0 meters upward in under 0.8 seconds. 

If commanded with a naive Trapezoidal profile with infinite jerk:
- The sudden torque step snaps aluminum carriage mountings and stretches roller chains by 2-3mm.
- The instantaneous jerk excites structural resonance at 15-25 Hz, causing the elevator mast to oscillate violently at the top.

Switching to a jerk-bounded S-curve profile (`j_max = 50 m/s³`) eliminates mechanical resonance, landing the mechanism precisely at the goal with zero mast wobble.

#### Complete Physical Feedforward Equation
To track a trajectory accurately, the motor voltage `V_cmd` is computed in real time using the physical derivatives of motion:

```
   V_cmd = kS · sign(v) + kV · v(t) + kA · a(t) + kG
```

Where:
- `kS` overcomes static friction (volts)
- `kV · v` balances back-electromotive force (volts per m/s)
- `kA · a` delivers dynamic torque `F = m·a` needed to accelerate system inertia (volts per m/s²)
- `kG` counteracts downward gravity (volts)

### Machine Learning: Continuous Gradient Flow & ODE-Nets

#### Gradient Descent as Euler Integration of Continuous Gradient Flow
Training a deep neural network with gradient descent:

```
   w[k+1] = w[k] - η · ∇L(w[k])
```

Is mathematically equivalent to performing **Forward Euler numerical integration** on the continuous-time ordinary differential equation (ODE) known as **Gradient Flow**:

```
   dw / dt = -∇L(w)
```

Where the learning rate `η` is the discrete integration step size `dt`.

If the learning rate `η` is chosen too large (violating the Lipschitz stability limit `η > 2 / L_max`), the discrete Euler integrator diverges to infinity—manifesting as exploding loss (`loss = NaN`).

#### Neural Ordinary Differential Equations (Neural ODEs)
Modern continuous-depth architectures replace stacked discrete residual layers `h[k+1] = h[k] + f(h[k], W[k])` with continuous dynamical systems:

```
   dh(t) / dt = f_θ(h(t), t)
```

Adaptive Runge-Kutta numerical integrators solve this ODE forward in time to compute outputs, and the continuous adjoint sensitivity method computes parameter gradients backward in time.

---

## 4. Classic Failure Mode & Python Engine

### The Classic Failure Mode: The "Instant Voltage Step" Gearbox Stripper
A rookie control engineer writes an autonomous drive command:
```python
# NAIVE VOLTAGE STEP:
if autonomous_timer < 1.0:
    motor.set_voltage(12.0)  # Slam full 12 Volts instantly!
```

**The Catastrophe:**
1. A stationary brushless motor (e.g., NEO or Falcon 500) has zero back-EMF (`ω = 0`).
2. Applying 12V instantly pushes stall current: `I = V / R = 12V / 0.03Ω = 400 Amps`.
3. Motor delivers peak stall torque (4.69 N·m) in less than 2 milliseconds. Through a 12:1 planetary reduction, this delivers 56 N·m of torque into an aluminum gear train.
4. **Result:** The sun gear teeth shear off, the drivetrain loses all propulsion, and the robot dies on the competition field.

### From-Scratch Python Implementation

```python
#!/usr/bin/env python3
"""
axon - Concept 03: Single-Variable Motion Calculus & Jerk
From-scratch kinematic trajectory generation and numerical integration.
"""
import math
from typing import List, Tuple


class MotionState:
    def __init__(self, t: float, x: float, v: float, a: float, j: float):
        self.t = float(t)
        self.x = float(x)
        self.v = float(v)
        self.a = float(a)
        self.j = float(j)

    def __repr__(self) -> str:
        return f"t={self.t:5.3f}s | x={self.x:6.3f}m | v={self.v:6.3f}m/s | a={self.a:6.3f}m/s² | j={self.j:6.1f}m/s³"


class TrapezoidalProfile:
    def __init__(self, target_distance: float, max_v: float, max_a: float):
        self.dist = float(target_distance)
        self.max_v = float(max_v)
        self.max_a = float(max_a)

        self.t_accel = self.max_v / self.max_a
        self.d_accel = 0.5 * self.max_a * (self.t_accel ** 2)

        if 2.0 * self.d_accel > self.dist:
            self.d_accel = self.dist / 2.0
            self.max_v = math.sqrt(self.dist * self.max_a)
            self.t_accel = self.max_v / self.max_a
            self.t_cruise = 0.0
            self.d_cruise = 0.0
        else:
            self.d_cruise = self.dist - (2.0 * self.d_accel)
            self.t_cruise = self.d_cruise / self.max_v

        self.t_total = (2.0 * self.t_accel) + self.t_cruise

    def sample(self, t: float) -> MotionState:
        if t <= 0.0:
            return MotionState(t, 0.0, 0.0, 0.0, 0.0)
        elif t <= self.t_accel:
            a = self.max_a
            v = a * t
            x = 0.5 * a * (t ** 2)
            j = float('inf') if (t == 0.0 or t == self.t_accel) else 0.0
            return MotionState(t, x, v, a, j)
        elif t <= (self.t_accel + self.t_cruise):
            dt = t - self.t_accel
            a = 0.0
            v = self.max_v
            x = self.d_accel + (v * dt)
            return MotionState(t, x, v, a, 0.0)
        elif t <= self.t_total:
            dt = t - (self.t_accel + self.t_cruise)
            a = -self.max_a
            v = self.max_v + (a * dt)
            x = self.d_accel + self.d_cruise + (self.max_v * dt) + (0.5 * a * (dt ** 2))
            return MotionState(t, x, v, a, 0.0)
        else:
            return MotionState(t, self.dist, 0.0, 0.0, 0.0)


def benchmark_numerical_integration():
    print("=" * 70)
    print("NUMERICAL INTEGRATION BENCHMARK: EULER VS TRAPEZOIDAL")
    print("=" * 70)
    a_const = 3.0
    dt = 0.020
    duration = 1.0

    t_steps = int(duration / dt)
    x_true = 0.5 * a_const * (duration ** 2)
    v_true = a_const * duration

    # 1. Forward Euler Simulation
    x_euler, v_euler = 0.0, 0.0
    for _ in range(t_steps):
        x_euler += v_euler * dt
        v_euler += a_const * dt

    # 2. Trapezoidal (Heun) Simulation
    x_trap, v_trap = 0.0, 0.0
    for _ in range(t_steps):
        v_next = v_trap + a_const * dt
        x_trap += 0.5 * (v_trap + v_next) * dt
        v_trap = v_next

    print(f"Ground Truth Position (Analytical) : {x_true:8.4f} m | Velocity: {v_true:8.4f} m/s")
    print(f"Forward Euler Position (dt=20ms)   : {x_euler:8.4f} m | Error: {abs(x_true - x_euler)*1000:6.2f} mm")
    print(f"Trapezoidal Position   (dt=20ms)   : {x_trap:8.4f} m | Error: {abs(x_true - x_trap)*1000:6.2f} mm")


if __name__ == "__main__":
    profile = TrapezoidalProfile(target_distance=2.0, max_v=3.0, max_a=4.0)
    print(f"Generated Profile: Total Duration = {profile.t_total:.3f} s")
    for t_sample in [0.0, 0.25, profile.t_accel, profile.t_total]:
        state = profile.sample(t_sample)
        print(" ", state)

    print()
    benchmark_numerical_integration()
```

---

## 5. Review Checkpoints & Deep-Dive Prompts

### Review Checkpoints

#### Checkpoint 1: Higher Derivative Units & Dimensional Consistency
**Question:** A robot arm angular trajectory is given by `θ(t) = 2·t³ - 0.5·t⁴` radians.
1. Determine analytical equations for angular velocity `ω(t)`, angular acceleration `α(t)`, and angular jerk `j_angular(t)`.
2. Compute the instantaneous angular jerk at `t = 2.0` seconds and specify its physical units.

**Solution:**
1. Successively differentiate with respect to time `t`:
   ```
   ω(t) = dθ / dt = 6·t² - 2·t³
   α(t) = dω / dt = 12·t - 6·t²
   j_angular(t) = dα / dt = 12 - 12·t
   ```
2. Evaluate at `t = 2.0`:
   ```
   j_angular(2.0) = 12 - 12·(2.0) = 12 - 24 = -12.0 rad/s³
   ```
3. **Physical Units:** The angular jerk is **`-12.0 radians per second cubed` (`rad/s³`)**.

#### Checkpoint 2: Truncation Error in Euler vs Trapezoidal Integration
**Question:** A robot drives with constant jerk `j(t) = j₀`. 
Show mathematically why Forward Euler integration underestimates position by `O(dt)` while Trapezoidal integration reduces the step error to `O(dt²)`.

**Solution:**
1. Using Taylor Series expansion around `t = t_k`:
   ```
   x(t + dt) = x(t) + x'(t)·dt + (1/2)·x''(t)·dt² + (1/6)·x'''(t)·dt³ + ...
             = x[k] + v[k]·dt + (1/2)·a[k]·dt² + (1/6)·j₀·dt³
   ```
2. **Forward Euler Method:**
   ```
   x_euler[k+1] = x[k] + v[k]·dt
   ```
   Subtracting Euler from Taylor series leaves a local truncation error of `E_euler = (1/2)·a[k]·dt² + O(dt³)`. Across `N = 1/dt` steps, the global accumulated error is `N · O(dt²) = O(dt)`.
3. **Trapezoidal Method:**
   ```
   x_trap[k+1] = x[k] + (1/2)·(v[k] + v[k+1])·dt
   ```
   Since `v[k+1] ≈ v[k] + a[k]·dt + (1/2)·j₀·dt²`, substitution yields:
   ```
   x_trap[k+1] = x[k] + v[k]·dt + (1/2)·a[k]·dt² + (1/4)·j₀·dt³
   ```
   Comparing to Taylor series, the `(1/2)·a·dt²` term matches identically. The remaining error is only `(1/4 - 1/6)·j₀·dt³ = (1/12)·j₀·dt³`. The global error is reduced to `O(dt²)`.

---

### Deep-Dive Exploration Prompts

1. **Phase Plane Trajectory Analysis:** In state-space control, plotting velocity `v` versus position `x` creates a **Phase Plane**. What geometric shape does a constant-acceleration motion profile trace in the `(x, v)` phase plane, and how do time-optimal Bang-Bang controllers navigate switching curves?
2. **Symplectic Integrators in Robotics Simulations:** When simulating physical robot physics (e.g., in MuJoCo or Drake), standard explicit Euler causes artificial energy growth, making spring-damper mechanisms explode. How do **Symplectic Integrators** preserve total mechanical energy `H = T + V` over thousands of simulation seconds?
