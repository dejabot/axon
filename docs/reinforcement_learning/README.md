# Axon 07: Reinforcement Learning & Agentic Decision Systems

Welcome to the **Reinforcement Learning & Agentic Decision Systems Axon**. This track synthesizes mathematics, physics models, and deep learning into autonomous decision agents capable of mastering high-stakes games, strategic alliance coordination, and real-time robot control policies.

---

## Modules in this Axon

### [1. Markov Decision Processes & Reward Engineering](01_mdp_rewards/README.md)
* *The Real-World Problem:* How do we frame a complex physical robotics task as an optimization problem of states, actions, and rewards?
* *Concepts:* States $S$, Actions $A$, Transition probabilities $P(s' \mid s, a)$, Discount factor $\gamma$, Sparse vs. Dense reward shaping, and reward hacking pitfalls.

---

### [2. Value Functions & Deep Q-Learning](02_q_learning/README.md)
* *The Real-World Problem:* How does an agent learn the long-term value of taking an action before seeing the final match outcome?
* *Concepts:* State-Value $V(s)$, Action-Value $Q(s, a)$, Bellman Optimality equations, Deep Q-Networks (DQN), Experience Replay, and Target Networks.

---

### [3. Policy Gradients & Actor-Critic Methods](03_policy_gradients/README.md)
* *The Real-World Problem:* How do we train an agent to output continuous voltage and steering velocities directly without discretizing actions?
* *Concepts:* Policy function $\pi_\theta(a \mid s)$, REINFORCE algorithm, Advantage Actor-Critic (A2C), and Proximal Policy Optimization (PPO).

---

### [4. Monte Carlo Tree Search & Match Strategists](04_mcts_game_agents/README.md)
* *The Real-World Problem:* How can an autonomous multi-robot alliance plan optimal endgame scoring cycles, defense counter-strategies, and cooperative climbing paths?
* *Concepts:* Tree traversal (Selection, Expansion, Simulation, Backpropagation), Upper Confidence Bounds for Trees (UCT), AlphaZero hybrid policy-value search, and real-time alliance strategists.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../localization/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Previous Axon: Localization & State Estimation</a></div>
  <div><a href="../README.md" style="color: var(--muted, #94a3b8); text-decoration: none;">Curriculum Home</a></div>
  <div><a href="../math/README.md" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Restart Track: Math Foundations ↺</a></div>
</div>
