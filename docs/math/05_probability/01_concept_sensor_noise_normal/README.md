# Concept 01: Sensor Noise & Normal Distributions

> **▶ Interactive Demo: [Sensor Noise & Bell Curve Visualizer](demo.html)**
>
> Open the interactive demo below to adjust the true distance μ (mean) and sensor noise σ (standard deviation) sliders, generate 1,000 live sensor readings, and watch the histogram match the theoretical Gaussian bell curve.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Jittery Sensor
Suppose an autonomous robot uses an optical distance sensor or an AprilTag camera to measure its distance from the field reef wall.

Even if the robot is parked completely still at a true distance of **4.00 meters**, 10 consecutive sensor readings might look like this:

```
[3.98, 4.04, 3.95, 4.01, 4.02, 3.97, 4.05, 3.99, 4.00, 3.99]
```

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="150" viewBox="0 0 300 150" style="max-width: 100%; height: auto;">
    <!-- Bell curve -->
    <path d="M 30 130 C 90 130 110 30 150 30 C 190 30 210 130 270 130" fill="none" stroke="#38bdf8" stroke-width="3" />
    <line x1="150" y1="30" x2="150" y2="130" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3" />
    <text x="155" y="55" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="11">Mean μ = 4.00m</text>
    
    <!-- 1-σ markers -->
    <line x1="120" y1="75" x2="180" y2="75" stroke="#4ade80" stroke-width="2" />
    <text x="135" y="92" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="10">±1σ (68%)</text>
    <line x1="20" y1="130" x2="280" y2="130" stroke="#334155" stroke-width="1.5" />
  </svg>
</div>

Why do sensors jitter?
Thermal vibrations inside electronics, photon shot noise in cameras, and minor electrical voltage fluctuations all add tiny, random errors. 

How do we model this uncertainty mathematically so our robot can trust its sensors safely?

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java: Simulating Sensor Gaussian Noise
```java
import java.util.Random;

Random rng = new Random();
double trueDistance = 5.00; // 5 meters
double sensorNoiseSigma = 0.08; // 8 cm standard deviation (±0.08 m)

for (int i = 0; i < 5; i++) {
    // nextGaussian() generates numbers from N(0, 1)
    double noisyReading = trueDistance + rng.nextGaussian() * sensorNoiseSigma;
    System.out.printf("Sample %d: %.3f meters%n", i + 1, noisyReading);
}
```

---

## 3. Bridge to Machine Learning: Diffusion Models & Weight Initialization
In modern generative AI:
* **Diffusion Models (Stable Diffusion / DALL-E):** Image generation begins by taking a pure image and progressively adding Gaussian noise (\mathcal{N}(0, \σ^2)). The neural network is trained to reverse this process by predicting and subtracting the Gaussian noise at each step!
* **Neural Network Initialization:** When initializing weights in deep networks (e.g. He or Xavier initialization), weights are drawn from a Gaussian distribution with mean 0 and a carefully chosen variance to prevent gradients from exploding or vanishing.

---

## 4. Review Checkpoints
### Checkpoint 1
A LiDAR sensor has mean `μ = 3.0m` and noise `σ = 0.05m`.
Between what two distances will `95%` of all sensor readings fall?

**Solution:**
Using the `±2σ` rule:
`[μ - 2σ, μ + 2σ] = [3.0 - 2(0.05), 3.0 + 2(0.05)] = [2.90m, 3.10m]`.

---

### Checkpoint 2
Sensor A has standard deviation `σ = 0.02m`. Sensor B has `σ = 0.10m`.
Which sensor is more precise, and why?

**Solution:**
**Sensor A** is much more precise because its spread (`0.02m`) is 5× smaller than Sensor B's (`0.10m`). Its bell curve is tall and narrow.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../../04_calculus/04_concept_gradients_multivariable/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 15: Gradients & Optimization</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 5 Overview</a></div>
  <div><a href="../02_concept_bayes_sensor_fusion/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 17: Bayes' Rule & Sensor Fusion →</a></div>
</div>
