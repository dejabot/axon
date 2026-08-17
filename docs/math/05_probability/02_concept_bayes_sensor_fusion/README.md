# Concept 02: Bayes' Rule & 1D Sensor Fusion

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

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java: 1D Kalman Sensor Fusion
```java
// Sensor 1: Wheel Odometry (Position = 5.2m, variance = 0.09)
double odomPos = 5.20;
double odomVar = 0.09;

// Sensor 2: Vision AprilTag (Position = 4.8m, variance = 0.04)
double visionPos = 4.80;
double visionVar = 0.04;

// Optimal Bayes / Kalman Fusion:
// Fused variance: 1 / var_fused = (1 / odomVar) + (1 / visionVar)
double fusedVar = 1.0 / ( (1.0 / odomVar) + (1.0 / visionVar) );

// Fused mean: Weighted average proportional to inverse variance
double fusedPos = fusedVar * ( (odomPos / odomVar) + (visionPos / visionVar) );

System.out.printf("Fused Robot Position: %.3f m (±%.3f m)%n", fusedPos, Math.sqrt(fusedVar));
// Output: 4.923 m (closer to vision because vision is more accurate!)
```

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
  <div><a href="../01_concept_sensor_noise_normal/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 16: Sensor Noise & Normal Dist</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 5 Overview</a></div>
  <div><a href="../03_concept_discrete_softmax/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 18: Discrete Softmax →</a></div>
</div>
