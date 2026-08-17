# Concept 03: Discrete Distributions & Softmax

> **▶ Interactive Demo: [Softmax & Temperature Visualizer](demo.html)**
>
> Open the interactive demo below to adjust the raw class logits and drag the Temperature slider to observe how temperature turns sharp greedy argmax into smooth probability distributions.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Turning Raw Scores into Confidences
When a robot's computer vision neural network inspects an object on the field, the raw output layer generates unconstrained real numbers called **logits**:

* **Game Piece (Note):** `+3.2`
* **Field Element (Reef):** `+1.1`
* **Opponent Robot:** `-0.8`

<div style="text-align: center; margin: 20px 0;">
  <svg width="320" height="150" viewBox="0 0 320 150" style="max-width: 100%; height: auto;">
    <!-- Raw Logits (Left) -->
    <rect x="20" y="20" width="100" height="110" fill="none" stroke="#334155" stroke-width="1.5" rx="6" />
    <text x="30" y="45" fill="#38bdf8" font-family="sans-serif" font-size="11">Note: +3.2</text>
    <text x="30" y="75" fill="#94a3b8" font-family="sans-serif" font-size="11">Reef: +1.1</text>
    <text x="30" y="105" fill="#f43f5e" font-family="sans-serif" font-size="11">Robot: -0.8</text>
    
    <!-- Arrow with Softmax -->
    <line x1="130" y1="75" x2="180" y2="75" stroke="#fbbf24" stroke-width="2.5" />
    <polygon points="180,70 190,75 180,80" fill="#fbbf24" />
    <text x="135" y="65" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="10">Softmax</text>
    
    <!-- Probabilities (Right) -->
    <rect x="200" y="20" width="100" height="110" fill="none" stroke="#334155" stroke-width="1.5" rx="6" />
    <text x="210" y="45" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="11">Note: 88.0%</text>
    <text x="210" y="75" fill="#4ade80" font-family="sans-serif" font-size="11">Reef: 10.7%</text>
    <text x="210" y="105" fill="#4ade80" font-family="sans-serif" font-size="11">Robot: 1.3%</text>
  </svg>
</div>

Logits have two major problems:
1. They can be negative (e.g. `-0.8`), but probabilities can never be negative.
2. Their sum is not `1.0` (`3.2 + 1.1 - 0.8 = 3.5 ≠ 1.0`).

How do we convert raw numbers into clean, calibrated probabilities that sum to 100%?

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java: Softmax Probabilities
```java
// Raw neuron outputs (logits)
double[] logits = {2.5, 1.0, 0.2}; // [Note, Coral, Algae]

// 1. Exponentiate each logit
double expSum = 0.0;
double[] expValues = new double[logits.length];
for (int i = 0; i < logits.length; i++) {
    expValues[i] = Math.exp(logits[i]);
    expSum += expValues[i];
}

// 2. Normalize to sum to 1.0 (100%)
double[] probabilities = new double[logits.length];
for (int i = 0; i < logits.length; i++) {
    probabilities[i] = expValues[i] / expSum;
}

System.out.printf("P(Note): %.1f%%, P(Coral): %.1f%%, P(Algae): %.1f%%%n",
    probabilities[0] * 100, probabilities[1] * 100, probabilities[2] * 100);
```

---

## 3. Bridge to Machine Learning: LLM Token Generation
In Large Language Models (like ChatGPT, Gemini, and Claude):
* The AI computes logits across its entire 32,000-word dictionary for the next token.
* **Temperature Sampling:**
  * When coding or doing math, the user sets `Temperature = 0.2` (predictable, deterministic answers).
  * When writing poetry or creative stories, the user sets `Temperature = 0.8` (sampling diverse tokens).

---

## 4. Review Checkpoints
### Checkpoint 1
A classifier outputs two logits: `z₁ = 0.0` and `z₂ = 0.0`.
What are the resulting probabilities?

**Solution:**
* `e⁰ = 1.0`, `e⁰ = 1.0`.
* `P₁ = 1.0 / (1.0 + 1.0) = 0.50 (50%)`.
* `P₂ = 1.0 / (1.0 + 1.0) = 0.50 (50%)`.
Equal logits always yield equal probabilities!

---

### Checkpoint 2
Why can't we simply divide logits by their sum (i.e. `zᵢ / ∑ z`) instead of using exponentials?

**Solution:**
Because negative logits (e.g. `-0.8`) would produce invalid negative probabilities, and if the sum of logits happened to equal zero (`∑ z = 0`), the formula would crash from division by zero! Exponentiation guarantees every term is strictly positive (e^z > 0).

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../02_concept_bayes_sensor_fusion/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 17: Bayes' Rule & Sensor Fusion</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 5 Overview</a></div>
  <div><a href="../04_concept_expected_value_decision/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 19: Expected Value & Decisions →</a></div>
</div>
