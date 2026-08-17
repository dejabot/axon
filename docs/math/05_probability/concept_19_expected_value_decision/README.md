# Concept 19: Expected Value & Decision Making

> **▶ Interactive Demo: [Endgame Strategy Monte Carlo Simulator](demo.html)**
>
> Open the interactive demo below to simulate 1,000 matches comparing Safe vs. Risky autonomous strategies and watch the empirical match scores converge to their theoretical Expected Values.

<iframe src="demo.html" width="100%" height="450" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Endgame Dilemma
With 20 seconds remaining in an intense playoff match, your alliance is deciding its final autonomous action:

* **Strategy A (Safe Low Score):**
  * 100% chance of success ➔ **+2 points** (Guaranteed).
* **Strategy B (Risky Trap Climb):**
  * 65% chance of success ➔ **+5 points**.
  * 35% chance of failure ➔ **0 points**.

<div style="text-align: center; margin: 20px 0;">
  <svg width="320" height="150" viewBox="0 0 320 150" style="max-width: 100%; height: auto;">
    <!-- Strategy A -->
    <rect x="30" y="30" width="110" height="80" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2" rx="6" />
    <text x="40" y="60" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="12">Strategy A</text>
    <text x="40" y="85" fill="#94a3b8" font-family="sans-serif" font-size="11">100% ➔ +2 pts</text>
    <text x="40" y="130" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="12">E[A] = 2.0 pts</text>
    
    <!-- Strategy B -->
    <rect x="180" y="30" width="110" height="80" fill="rgba(74, 222, 128, 0.2)" stroke="#4ade80" stroke-width="2" rx="6" />
    <text x="190" y="60" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="12">Strategy B</text>
    <text x="190" y="85" fill="#94a3b8" font-family="sans-serif" font-size="11">65% ➔ +5 pts</text>
    <text x="190" y="130" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="12">E[B] = 3.25 pts</text>
  </svg>
</div>

Which decision yields the higher average point output in the long run?
How does an autonomous robot evaluate risk vs. reward dynamically during a match?

---

## 2. Solving It in Code (Java & WPILib)

### First-Principles Java: Expected Value & Strategy Decision
```java
// Strategy A: Reef High Goal (5 points, 70% success, 0 points on miss)
double evA = 0.70 * 5.0 + 0.30 * 0.0; // 3.50 points

// Strategy B: Reef Low Goal (2 points, 99% guaranteed)
double evB = 0.99 * 2.0 + 0.01 * 0.0; // 1.98 points

System.out.printf("Expected Value Strategy A (High): %.2f pts%n", evA);
System.out.printf("Expected Value Strategy B (Low):  %.2f pts%n", evB);

if (evA > evB) {
    System.out.println("Autonomous Decision: Attempt High Goal (Higher Long-Term Score)");
}
```

---

## 3. Bridge to Machine Learning: Reinforcement Learning & MCTS
In modern game-playing and autonomous AI:
* **Reinforcement Learning (Q-Learning):** The AI selects actions that maximize the **Expected Future Reward** (Q(s, a) = E[r + \γ \max Q(s', a')]).
* **Monte Carlo Tree Search (MCTS in AlphaZero & Game Bots):** The AI simulates thousands of random rollouts from the current board state to estimate the win probability of every legal move!

---

## 4. Review Checkpoints
### Checkpoint 1
An autonomous shooting routine has a 40% chance to score a 3-point goal, and a 60% chance to score a 1-point ball.
What is the expected point value per shot?

**Solution:**
`E[X] = (3)(0.40) + (1)(0.60) = 1.20 + 0.60 = 1.80 points`.

---

### Checkpoint 2
Why do autonomous robots use Monte Carlo simulations rather than just trusting single worst-case or best-case scenarios?

**Solution:**
Because reality is probabilistic. Monte Carlo simulations reveal the entire distribution of possible outcomes (both median payoff and variance), allowing the software to make optimal risk-adjusted decisions.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_18_discrete_softmax/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 18: Discrete Softmax</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 5 Overview</a></div>
  <div><a href="../../../machine_learning/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Next Axon: Machine Learning →</a></div>
</div>
