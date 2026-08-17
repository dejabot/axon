# Module 1: Tokenization & Vector Embeddings

Welcome to **Module 1: Tokenization & Vector Embeddings**. In this module, we explore how neural networks convert human text, code, and natural language instructions into high-dimensional geometric vectors that preserve deep semantic relationships.

---

## Concepts in this Module
* **[Concept 01: Byte-Pair Encoding (BPE) & Vocabulary Lookups](01_concept_tokenization_bpe/)**
  * *The Everyday Problem:* How does a language model break arbitrary words, typos, and robot commands into subword chunks that map to integer IDs in a fixed vocabulary?
  * *Code & Math:* Subword frequency merging, vocabulary lookup tables, and token integer representations.
  * *Visualizer:* [01_concept_tokenization_bpe/demo.html](01_concept_tokenization_bpe/demo.html)

* **[Concept 02: High-Dimensional Semantic Vectors & Cosine Distance](02_concept_vector_embeddings/)**
  * *The Everyday Problem:* How do we represent words as geometric coordinate points in space such that related concepts cluster together and analogies can be calculated with vector math?
  * *Code & Math:* Dense embedding vectors, dot product projections, and cosine semantic similarity `cos(θ) = (u · v) / (|u| · |v|)`.
  * *Visualizer:* [02_concept_vector_embeddings/demo.html](02_concept_vector_embeddings/demo.html)

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← LLM Axon Home</a></div>
  <div><a href="./" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="01_concept_tokenization_bpe/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 01: Tokenization & BPE →</a></div>
</div>
