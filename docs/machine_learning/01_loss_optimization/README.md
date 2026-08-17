# Module 1: Loss Functions & Optimization

Welcome to **Module 1: Loss Functions & Optimization**. In this module, we explore how an autonomous model learns by quantifying its own prediction errors into mathematical score surfaces and using calculus slopes to adjust its weights automatically.

---

## Concepts in this Module
* **[Concept 01: Measuring Errors with Loss Functions (MSE & MAE)](01_concept_loss_mse_mae/)**
  * *The Everyday Problem:* The robot shoots a game piece toward a target. How do we turn the difference between where it landed and where we aimed into an error score?
  * *Code & Math:* Mean Squared Error (MSE), Mean Absolute Error (MAE), and quadratic penalty curves.

* **[Concept 02: Cross-Entropy & Classification Loss](02_concept_cross_entropy_loss/)**
  * *The Everyday Problem:* The vision camera predicts probabilities for 3 game piece types. How do we heavily penalize a model that is confidently wrong?
  * *Code & Math:* Negative Log-Likelihood, Cross-Entropy Loss `Loss = -ln(P_correct)`, and information surprise.

* **[Concept 03: Gradient Descent & Learning Rates](03_concept_gradient_descent/)**
  * *The Everyday Problem:* How does an autonomous optimizer roll down the error bowl to find the best settings without overshooting?
  * *Code & Math:* Weight updates `w_new = w - lr · ∇Loss`, step sizes, learning rate tuning, and local minima.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Machine Learning Axon Home</a></div>
  <div><a href="./" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="01_concept_loss_mse_mae/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 20: MSE & MAE Loss →</a></div>
</div>
