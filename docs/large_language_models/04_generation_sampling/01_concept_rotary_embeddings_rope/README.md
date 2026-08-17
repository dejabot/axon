# Concept 01: Rotary Position Embeddings (RoPE) & Context Length

Self-Attention has a fundamental blind spot: it is **permutation invariant**. 

If you scramble the words in a sentence:
* *"Robot shoots Note into Reef"*
* *"Reef shoots Note into Robot"*

The raw dot-product attention scores would be **100% identical** without some way of encoding sequence order!

> Open the interactive demo below to rotate 2D vector coordinate pairs across token sequence positions `m` and observe how RoPE guarantees that attention scores depend strictly on the relative distance `(m - n)`.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Rotary Position Embeddings (RoPE) Visualizer"></iframe>

---

## 1. Absolute vs Relative Positional Embeddings

### The Old Approach: Absolute Addition (GPT-2, BERT)
In early models, a static position vector was added to the word embedding:

```text
x = Token_Embedding + Position_Embedding[m]
```

* **The Flaw:** If a model was trained on 2,048 tokens, position 2,049 had never been seen before, causing catastrophic degradation when reading longer documents.

---

## 2. The Modern Solution: Rotary Position Embedding (RoPE)

Introduced by Jianlin Su in 2021 and used in **LLaMA 3, Gemma, Mistral, and Qwen**, **RoPE** does not add numbers to vectors. Instead, it **rotates** vector coordinate pairs in 2D space.

1. Group the vector dimensions `(d_k = 64)` into 32 pairs of 2D coordinates: `(x₀, x₁)`, `(x₂, x₃)`, ...
2. For a token at sequence position `m`, rotate each 2D pair by an angle `m · θ`:

```text
[ x_new_0 ] = [ cos(mθ)  -sin(mθ) ] [ x₀ ]
[ x_new_1 ]   [ sin(mθ)   cos(mθ) ] [ x₁ ]
```

### The Magic Property: Pure Relative Distance
When you calculate the dot product between Query at position `m` and Key at position `n`:

```text
(R_m · Q) · (R_n · K)ᵀ = Q · R_(m - n) · Kᵀ
```

Because the rotation matrices subtract in dot products, the final attention score depends **only on the relative distance `(m - n)` between the words**, completely independent of their absolute index in a 128,000-token prompt!

---

## 3. Solving It in Code (Java)

Here is a clean implementation of 2D Rotary Embedding application in Java:

```java
public class RotaryEmbeddings {
    public static double[] applyRoPE(double[] vec, int position, double baseFreq) {
        int dim = vec.length;
        double[] rotated = new double[dim];

        // Process dimensions in pairs: (vec[2i], vec[2i + 1])
        for (int i = 0; i < dim / 2; i++) {
            // Frequency for pair i: theta_i = base^(-2i / dim)
            double theta = 1.0 / Math.pow(baseFreq, (2.0 * i) / dim);
            double angle = position * theta;

            double cos = Math.cos(angle);
            double sin = Math.sin(angle);

            double x0 = vec[2 * i];
            double x1 = vec[2 * i + 1];

            // 2D Rotation Matrix
            rotated[2 * i]     = x0 * cos - x1 * sin;
            rotated[2 * i + 1] = x0 * sin + x1 * cos;
        }

        return rotated;
    }

    public static void main(String[] args) {
        double[] q = {1.0, 0.0, 0.5, 0.8};

        double[] q_pos0 = applyRoPE(q, 0, 10000.0);
        double[] q_pos5 = applyRoPE(q, 5, 10000.0);

        System.out.printf("Position 0 Vector: [%.2f, %.2f]%n", q_pos0[0], q_pos0[1]);
        System.out.printf("Position 5 Vector: [%.2f, %.2f] (Rotated by 5θ)%n", q_pos5[0], q_pos5[1]);
    }
}
```

---

## 4. Math! Translation Sidebar

The formal 2D rotation operator for coordinate pair `i` at position `m`:

```text
R_θ,m = [ cos(m · θᵢ)   -sin(m · θᵢ) ]
        [ sin(m · θᵢ)    cos(m · θᵢ) ]
```

### Context Length Scaling (YaRN & LongRoPE):
* Modern LLMs achieve **128k to 1M token context windows** by scaling down the base rotation frequency `θ`, compressing long sequences so they fit into the network's known angular budget without retraining from scratch!

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 4 Overview</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">LLM Axon Home</a></div>
  <div><a href="../02_concept_temperature_top_p_sampling/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Temperature & Sampling →</a></div>
</div>
