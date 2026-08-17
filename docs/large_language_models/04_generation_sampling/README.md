# Module 4: Generation, RoPE & Sampling

Welcome to **Module 4: Generation, RoPE & Sampling**. In this final module of the LLM Axon, we cover how models track word sequence order using geometric rotations (RoPE) and generate human-like text via autoregressive sampling strategies.

---

## Concepts in this Module
* **[Concept 01: Rotary Position Embeddings (RoPE) & Context Length](01_concept_rotary_embeddings_rope/)**
  * *The Everyday Problem:* Self-attention by itself is order-agnostic. Why does word order matter (*"dog bites robot"* vs *"robot bites dog"*), and how do modern LLMs rotate 2D vector pairs to encode sequence positions?
  * *Code & Math:* RoPE 2D rotation matrix `R_θ,m = [cos(mθ), -sin(mθ); sin(mθ), cos(mθ)]`, relative position preservation, and context window scaling (YaRN / RoPE scaling).

* **[Concept 02: Autoregressive Next-Token Sampling (Temperature, Top-k, Top-p)](02_concept_temperature_top_p_sampling/)**
  * *The Everyday Problem:* How does an LLM pick the next token? Why does greedy argmax repeat itself in loops, and how do Temperature scaling and Nucleus (Top-p) sampling balance creativity with logical precision?
  * *Code & Math:* Logits to probabilities via temperature `z_i / T`, Top-k truncation, Top-p cumulative cutoff, and KV-Cache autoregressive generation loops.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../03_transformers/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 3: Transformers</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">LLM Axon Home</a></div>
  <div><a href="01_concept_rotary_embeddings_rope/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: RoPE Embeddings →</a></div>
</div>
