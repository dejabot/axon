# Module 4: Calculus, Motion & Optimization

Welcome to **Module 4: Calculus, Motion & Optimization**. In this module, we explore the mathematics of motion and optimization—from speedometer rates of change and elevator jerk to area integration and gradient descent.

---

## Concepts in this Module
* **[Concept 12: Rates of Change & Derivatives](concept_12_rates_of_change/)**
  * *The Everyday Problem:* How does an optical encoder turn wheel tick counts into instantaneous robot velocity?
  * *Code & Math:* Secant slope vs. tangent slope, numerical differentiation `dx / dt`, velocity from position.
  * *Visualizer:* [concept_12_rates_of_change/demo.html](concept_12_rates_of_change/demo.html)

* **[Concept 13: Acceleration, Jerk & S-Curves](concept_13_acceleration_jerk/)**
  * *The Everyday Problem:* Why does slamming an elevator motor to full power snap roller chains and spill boiling coffee?
  * *Code & Math:* Higher derivatives (`da/dt`), Newton's law `F = m·a`, S-curve motion profiling with bounded jerk.
  * *Visualizer:* [concept_13_acceleration_jerk/demo.html](concept_13_acceleration_jerk/demo.html)

* **[Concept 14: Accumulation, Area & Numerical Integration](concept_14_accumulation_integrals/)**
  * *The Everyday Problem:* How does a robot track where it is on the field by adding up speed measurements over time?
  * *Code & Math:* Area under a velocity curve, Forward Euler vs. Trapezoidal integration accuracy.
  * *Visualizer:* [concept_14_accumulation_integrals/demo.html](concept_14_accumulation_integrals/demo.html)

* **[Concept 15: Multivariable Gradients & Hill Climbing](concept_15_gradients_multivariable/)**
  * *The Everyday Problem:* How does an autonomous robot steer around obstacles using artificial potential fields?
  * *Code & Math:* Partial derivatives (`∂f/∂x`, `∂f/∂y`), gradient vector `∇f` (steepest uphill), and Gradient Descent `-∇f`.
  * *Visualizer:* [concept_15_gradients_multivariable/demo.html](concept_15_gradients_multivariable/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../03_linear_algebra/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 3: Linear Algebra</a></div>
  <div><a href="./" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 4 Overview</a></div>
  <div><a href="concept_12_rates_of_change/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 12: Rates of Change →</a></div>
</div>
