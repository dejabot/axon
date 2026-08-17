# Module 3: The Transformer Architecture

Welcome to **Module 3: The Transformer Architecture**. In this module, we assemble the individual components—Self-Attention, Layer Normalization, Residual Connections, and Feed-Forward Networks—into a complete, scalable deep learning block.

---

## Concepts in this Module
* **[Concept 01: Residual Skip Connections & RMSNorm](01_concept_residual_layernorm/)**
  * *The Everyday Problem:* When stacking 96 transformer layers on top of each other, how do gradients and information flow cleanly through the network without exploding or vanishing to zero?
  * *Code & Math:* The residual additive shortcut `x_next = x + SubLayer(x)` and Root Mean Square Normalization (RMSNorm) `x / √(mean(x²) + ε)`.
  * *Visualizer:* [01_concept_residual_layernorm/demo.html](01_concept_residual_layernorm/demo.html)

* **[Concept 02: The Transformer Decoder Block (SwiGLU & Feed-Forward)](02_concept_feedforward_blocks/)**
  * *The Everyday Problem:* Attention routes information between tokens, but where does the model actually "think", recall facts, and perform non-linear transformations?
  * *Code & Math:* Assembling the full Transformer Block: `Pre-RMSNorm → Multi-Head Attention → Residual Add → Pre-RMSNorm → SwiGLU Feed-Forward → Residual Add`.
  * *Visualizer:* [02_concept_feedforward_blocks/demo.html](02_concept_feedforward_blocks/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../02_attention_heads/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 2: Attention Heads</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">LLM Axon Home</a></div>
  <div><a href="01_concept_residual_layernorm/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: Residuals & RMSNorm →</a></div>
</div>
