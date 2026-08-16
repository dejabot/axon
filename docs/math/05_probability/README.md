# Module 5: Probability & Uncertainty

Welcome to **Module 5: Probability & Uncertainty**. In robotics and artificial intelligence, the physical world is never 100% predictable: sensors have electrical noise, wheels slip on carpet, and camera detections have uncertainty.

This module introduces the mathematical tools required to quantify, model, and make decisions under uncertainty—from bell curves and sensor fusion to probability distributions and Monte Carlo expectations.

---

## Concepts in this Module
* **[Concept 16: Sensor Noise & Normal Distributions](concept_16_sensor_noise_normal/)**
  * *The Everyday Problem:* Why does an AprilTag distance sensor reading jitter between 3.8m and 4.2m, and what is the "true" distance?
  * *Code & Math:* Sample mean μ (mean), sample variance \σ^2, standard deviation σ (standard deviation), and the Gaussian Bell Curve.
  * *Visualizer:* [concept_16_sensor_noise_normal/demo.html](concept_16_sensor_noise_normal/demo.html)

* **[Concept 17: Bayes' Rule & 1D Sensor Fusion](concept_17_bayes_sensor_fusion/)**
  * *The Everyday Problem:* How do we combine a noisy vision estimate with a wheel odometry estimate into a single, highly confident belief?
  * *Code & Math:* Prior, Likelihood, Posterior, and 1D Kalman filter sensor fusion (multiplying two Gaussians).
  * *Visualizer:* [concept_17_bayes_sensor_fusion/demo.html](concept_17_bayes_sensor_fusion/demo.html)

* **[Concept 18: Discrete Distributions & Softmax](concept_18_discrete_softmax/)**
  * *The Everyday Problem:* How does an autonomous object detector turn raw model scores into percentages that sum to 100%?
  * *Code & Math:* Categorical distributions, the Softmax function, and temperature scaling.
  * *Visualizer:* [concept_18_discrete_softmax/demo.html](concept_18_discrete_softmax/demo.html)

* **[Concept 19: Expected Value & Decision Making](concept_19_expected_value_decision/)**
  * *The Everyday Problem:* In the final 20 seconds of an FRC match, should your alliance attempt a risky high-point climb or take guaranteed safe points?
  * *Code & Math:* Expected Value E[X] = \sum x_i \cdot P(x_i), risk variance, and Monte Carlo simulation.
  * *Visualizer:* [concept_19_expected_value_decision/demo.html](concept_19_expected_value_decision/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../04_calculus/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 4: Calculus</a></div>
  <div><a href="./" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 5 Overview</a></div>
  <div><a href="concept_16_sensor_noise_normal/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 16: Sensor Noise & Normal Dist →</a></div>
</div>
