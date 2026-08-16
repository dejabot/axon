# Axon 03: Large Language Models & Transformers

Welcome to the **Large Language Models & Transformers Axon**. This track unpacks modern generative AI architectures—from high-dimensional semantic token embeddings and Scaled Dot-Product Attention to the full Transformer block and autoregressive sampling.

---

## Modules in this Axon

### 1. Tokenization & Vector Embeddings
* *The Real-World Problem:* How do neural networks read words, code, and symbols as mathematical points in high-dimensional space?
* *Key Concepts:* Byte-Pair Encoding (BPE), vocabulary token IDs, embedding lookup matrices, and vector cosine distance.

---

### 2. Scaled Dot-Product & Self-Attention
* *The Real-World Problem:* How does an AI know that "it" refers to the robot and not the target in a sentence?
* *Key Concepts:* Query, Key, and Value ($Q, K, V$) projections, matrix attention scores $\text{Softmax}(QK^T / \sqrt{d_k})$, and context mixing.

---

### 3. The Transformer Architecture
* *The Real-World Problem:* How do attention heads combine with feed-forward layers to reason across long sequences in parallel?
* *Key Concepts:* Multi-Head Attention (MHA), Residual skip connections, Layer Normalization / RMSNorm, and the modern Decoder block.

---

### 4. Generation, RoPE & Sampling
* *The Real-World Problem:* How does the model generate coherent text step-by-step without repeating itself or hallucinating?
* *Key Concepts:* Rotary Position Embeddings (RoPE), KV-Caching, Temperature, Top-$k$, Top-$p$ (Nucleus) sampling, and speculative decoding.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../machine_learning/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Previous Axon: Machine Learning</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Curriculum Home</a></div>
  <div><a href="../physics/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Next Axon: Physics & Actuation →</a></div>
</div>
