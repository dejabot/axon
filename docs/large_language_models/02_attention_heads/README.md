# Module 2: Scaled Dot-Product & Self-Attention

Welcome to **Module 2: Scaled Dot-Product & Self-Attention**. In this module, we dissect the mathematical heart of the Transformer architecture—how tokens dynamically route information and attend to context across a sequence.

---

## Concepts in this Module
* **[Concept 01: Scaled Dot-Product & Self-Attention (Q, K, V)](01_concept_scaled_dot_product/)**
  * *The Everyday Problem:* When reading *"The robot picked up the Note because it was close"*, how does the network know that *"it"* refers to the Note and not the robot?
  * *Code & Math:* Linear Query, Key, and Value projections (`Q`, `K`, `V`), the scaling factor `1 / √(d_k)`, and `Attention(Q, K, V) = Softmax(Q · Kᵀ / √(d_k)) · V`.
  * *Visualizer:* [01_concept_scaled_dot_product/demo.html](01_concept_scaled_dot_product/demo.html)

* **[Concept 02: Multi-Head Attention & Feature Subspaces](02_concept_multi_head_attention/)**
  * *The Everyday Problem:* Why is a single attention head not enough to track grammar, physical robot geometry, and game targets simultaneously?
  * *Code & Math:* Projecting into multiple parallel subspace heads, computing independent attention distributions, concatenating, and applying the final output projection matrix `W_O`.
  * *Visualizer:* [02_concept_multi_head_attention/demo.html](02_concept_multi_head_attention/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_embeddings/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1: Embeddings</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">LLM Axon Home</a></div>
  <div><a href="01_concept_scaled_dot_product/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: Scaled Dot-Product →</a></div>
</div>
