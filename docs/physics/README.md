# Axon 04: Physics, Dynamics & Actuation

Welcome to the **Physics, Dynamics & Actuation Axon**. This track bridges mechanical laws and electrical motor characteristics into software models—from DC motor torque-speed curves and gearbox inertia to projectile ballistics, shooter trajectories, and feedforward control.

---

## Modules in this Axon

### 1. DC Motor Electromechanics
* *The Real-World Problem:* How much current and voltage does a brushless motor draw under varying loads and speeds?
* *Key Concepts:* Stall torque, free speed, Back-Electromotive Force (Back-EMF), torque constant K_t, velocity constant K_v, and electrical resistance R.

---

### 2. Gearboxes & Reflected Inertia
* *The Real-World Problem:* Why does adding a 10:1 planetary gearbox make an arm 100× harder to backdrive?
* *Key Concepts:* Gear ratios G, torque multiplication, speed reduction, and reflected rotational inertia (J_{\text{reflected}} = J_{\text{load}} / G²).

---

### 3. Projectile Ballistics & Shooter Trajectories
* *The Real-World Problem:* How does an autonomous robot calculate shooter flywheel RPM and hood angle to score a game piece into a target from any distance—even while driving across the field?
* *Key Concepts:* 2D parabolic projectile mechanics (y(t) = v0y*t - 0.5*g*t²), aerodynamic drag forces, Magnus effect spin stability, and Galilean vector addition for shooting on the move (v_{\text{launch}} = v_{\text{robot}} + v_{\text{shooter}}).

---

### 4. Physics Feedforward & Closed-Loop PID
* *The Real-World Problem:* Why does standard PID control lag behind fast targets, and how do we calculate the exact voltage required to hold an arm against gravity?
* *Key Concepts:* Voltage models (V = kS*sgn(v) + kV*v + kA*a + kG), velocity feedforward, and Proportional-Integral-Derivative (PID) closed-loop stabilization.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../large_language_models/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Previous Axon: Large Language Models</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Curriculum Home</a></div>
  <div><a href="../kinematics/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Next Axon: Kinematics & Motion →</a></div>
</div>
