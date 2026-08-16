# Concept 17: Bayes' Rule & 1D Sensor Fusion

> **▶ Interactive Demo: [1D Kalman Sensor Fusion Sandbox](demo.html)**
>
> Open the interactive demo below to drag the Prior (Wheel Odometry) and Measurement (Vision Camera) curves and watch the combined Posterior belief become narrower and more confident than either sensor alone.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Two Conflicting Sensors
Suppose your robot is attempting to localize itself on the field:
1. **Wheel Odometry (Prior):** Predicts position `x₁ = 4.00m` with high confidence (`σ₁ = 0.20m`).
2. **Vision Camera (Measurement):** Detects an AprilTag and reports `x₂ = 4.50m`, but with lower confidence (`σ₂ = 0.40m`) due to camera blur.

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="150" viewBox="0 0 300 150" style="max-width: 100%; height: auto;">
    <!-- Odometry Curve (Blue) -->
    <path d="M 40 130 C 80 130 90 40 110 40 C 130 40 140 130 180 130" fill="none" stroke="#38bdf8" stroke-width="2" />
    <text x="85" y="30" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="10">Odometry: 4.0m</text>
    
    <!-- Vision Curve (Amber) -->
    <path d="M 110 130 C 150 130 160 70 190 70 C 220 70 230 130 270 130" fill="none" stroke="#fbbf24" stroke-width="2" />
    <text x="175" y="60" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="10">Vision: 4.5m</text>
    
    <!-- Fused Posterior (Green) -->
    <path d="M 70 130 C 100 130 115 15 125 15 C 135 15 150 130 180 130" fill="none" stroke="#4ade80" stroke-width="3" />
    <text x="135" y="15" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="11">Fused: 4.10m</text>
    <line x1="20" y1="130" x2="280" y2="130" stroke="#334155" stroke-width="1.5" />
  </svg>
</div>

Which sensor should the robot believe?
Neither sensor is 100% right! Instead of blindly picking one, we mathematically blend both readings according to their relative uncertainties.

---

## 2. Solving It in Code: 1D Kalman Fusion
The optimal way to fuse two Gaussian sensors is the **Kalman Filter update formula**:

```python
def fuse_two_sensors(mu_prior, sigma_prior, mu_meas, sigma_meas):
    """
    Fuses two independent Gaussian estimates into a single optimal posterior belief.
    """
    var_prior = sigma_prior ** 2
    var_meas = sigma_meas ** 2
    
    # 1. Kalman Gain: How much weight to give the new vision measurement
    kalman_gain = var_prior / (var_prior + var_meas)
    
    # 2. Updated Mean (Blended estimate)
    fused_mu = mu_prior + kalman_gain * (mu_meas - mu_prior)
    
    # 3. Updated Variance (Always smaller than either sensor alone!)
    fused_var = (1.0 - kalman_gain) * var_prior
    fused_sigma = fused_var ** 0.5
    
    return fused_mu, fused_sigma

# Fuse Odometry (4.00m ± 0.20m) with Vision (4.50m ± 0.40m)
mu, sigma = fuse_two_sensors(4.00, 0.20, 4.50, 0.40)

print(f"Optimal Estimated Position : {mu:.3f} meters")  # 4.100m
print(f"Combined Uncertainty (σ)   : ±{sigma:.3f} meters")  # ±0.179m (Tighter than both!)
```

---

> 💡 **Math Sidebar: Bayes' Rule**
>
> In probability theory, updating our belief after observing new evidence is governed by **Bayes' Theorem**:
>
> ```
>                            P(Sensor | State) · P(State)
>    P(State | Sensor)  =   ------------------------------
>                                     P(Sensor)
> ```
>
> **How to interpret the terms:**
> * **`P(State)` [Prior]:** What we believed before looking at the camera (Wheel Odometry).
> * **`P(Sensor | State)` [Likelihood]:** What the camera just saw.
> * **`P(State | Sensor)` [Posterior]:** Our updated belief after combining both!
>
> Multiplying two Gaussian curves produces a new Gaussian that is **taller, narrower, and more certain** than either input!

---

## 3. Bridge to Machine Learning: Bayesian Inference
In machine learning and statistics:
* **Naive Bayes Classifiers:** Use Bayes' rule to compute the probability that an email is spam given the occurrence of specific keywords.
* **Maximum A Posteriori (MAP) Estimation:** Used in neural network regularization (like Weight Decay / L2 regularization), which treats the network weights as having a Gaussian prior centered at zero.

---

## 4. Review Checkpoints
### Checkpoint 1
If two identical sensors both measure distance with equal uncertainty `σ = 0.40m`, what weight (`Kalman Gain K`) is given to the second reading?

**Solution:**
`K = σ₁² / (σ₁² + σ₂²) = 0.40² / (0.40² + 0.40²) = 0.50 (50%)`.
The algorithm takes the exact 50/50 average of the two readings!

---

### Checkpoint 2
Why is the fused uncertainty `σ = 0.179m` smaller than both `0.20m` and `0.40m`?

**Solution:**
Because two independent sensor readings provide more total information than one sensor alone. Combining multiple noisy perspectives always reduces overall uncertainty.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_16_sensor_noise_normal/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 16: Sensor Noise & Normal Dist</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 5 Overview</a></div>
  <div><a href="../concept_18_discrete_softmax/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 18: Discrete Softmax →</a></div>
</div>
