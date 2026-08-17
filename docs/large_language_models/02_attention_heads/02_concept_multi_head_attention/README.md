# Concept 02: Multi-Head Attention & Feature Subspaces

In Concept 01, we saw how a single attention head routes information between tokens. But human language and robot commands contain multiple simultaneous relationships:

* **Grammar / Coreference:** Who performed the action?
* **Spatial Geometry:** Where is the game piece located relative to the field?
* **Physical Attributes:** What color, shape, or state is the target in?

If a model only had one attention head, it would be forced to average all these different relationships into one blurry mix.

> Open the interactive demo below to toggle between 4 specialized Attention Heads and observe how different heads attend to syntax, physical locations, and robot hardware actions in parallel.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Multi-Head Attention Subspace Visualizer"></iframe>

---

## Why Split into Multiple Heads?

Instead of running a single massive attention calculation of dimension `d_model = 768`, Transformers split the vector space into `h = 8` or `12` parallel **Heads** of smaller dimension `d_k = 64` (`768 = 12 × 64`).

```
                    Input Embeddings X (N × 768)
                                 │
         ┌───────────────┬───────┴───────┬───────────────┐
         ▼               ▼               ▼               ▼
     [Head 1]        [Head 2]        [Head 3]        [Head 4]
   (d_k = 64)      (d_k = 64)      (d_k = 64)      (d_k = 64)
   Tracks Action   Tracks Objects  Tracks Geometry  Tracks Timing
         │               │               │               │
         └───────────────┬───────────────┴───────────────┘
                         ▼
        Concatenate: [head₁ | head₂ | ... | head_h] (N × 768)
                         │
                         ▼
             Linear Output Projection W_O
                         │
                         ▼
                Context Output (N × 768)
```

Each head projects the tokens into its own private mathematical **subspace**, allowing the model to focus on different aspects of meaning at the exact same time.

---

## 1. The Multi-Head Workflow

1. **Linear Projections:** For each head `i`, project the input `X` using learned weight matrices `W_Q^(i)`, `W_K^(i)`, and `W_V^(i)`.
2. **Parallel Self-Attention:** Compute `head_i = Attention(Q_i, K_i, V_i)`.
3. **Concatenation:** Glue all `h` output vectors together side-by-side: `[head_1, head_2, ..., head_h]`.
4. **Final Linear Projection:** Multiply by the output matrix `W_O` so the different heads can communicate and combine their discoveries.

---

## 2. Solving It in Code (Java)

Here is a clean multi-head attention concatenation and output projection in Java:

```java
public class MultiHeadAttention {
    public static double[] multiHeadCombine(double[][] headOutputs, double[][] W_O) {
        int numHeads = headOutputs.length;       // e.g. 4 heads
        int headDim = headOutputs[0].length;     // e.g. 64 dimensions each
        int totalDim = numHeads * headDim;       // 256 total dimensions

        // 1. Concatenate all head outputs into one flat vector
        double[] concatenated = new double[totalDim];
        int index = 0;
        for (int h = 0; h < numHeads; h++) {
            for (int d = 0; d < headDim; d++) {
                concatenated[index++] = headOutputs[h][d];
            }
        }

        // 2. Multiply by Output Projection Matrix W_O: out = concat @ W_O
        double[] finalOutput = new double[totalDim];
        for (int i = 0; i < totalDim; i++) {
            double sum = 0.0;
            for (int j = 0; j < totalDim; j++) {
                sum += concatenated[j] * W_O[j][i];
            }
            finalOutput[i] = sum;
        }

        return finalOutput;
    }

    public static void main(String[] args) {
        double[][] headOutputs = {
            {1.0, 0.5}, // Head 1 (Syntax)
            {0.2, 0.9}, // Head 2 (Spatial)
            {0.8, 0.1}, // Head 3 (Action)
            {0.4, 0.7}  // Head 4 (Object)
        };

        // Identity-like projection matrix
        double[][] W_O = new double[8][8];
        for (int i = 0; i < 8; i++) W_O[i][i] = 1.0;

        double[] combined = multiHeadCombine(headOutputs, W_O);
        System.out.printf("Combined Multi-Head Vector Length: %d dimensions%n", combined.length);
    }
}
```

---

## 3. Math! Translation Sidebar

Here is how Multi-Head Attention is formulated:

```text
MultiHead(Q, K, V) = Concat(head₁, head₂, ..., head_h) · W_O
where headᵢ = Attention(Q · W_Q^(i), K · W_K^(i), V · W_V^(i))
```

### How to Read This Out Loud:
* `h`: Number of attention heads (typically 8 to 128 in modern models).
* `Concat(...)`: Stacking the head output vectors side-by-side.
* `W_O` ("W-output"): A learned linear transformation matrix that maps the concatenated heads back to `d_model`.

---

## 4. Bridge to Modern LLM Architecture: GQA

* **Multi-Head Attention (MHA):** Every head has its own `Q`, `K`, and `V` matrices. (Requires large KV-caches).
* **Grouped-Query Attention (GQA):** Used in **LLaMA 3, Mistral, and Gemma**. Multiple Query heads share the same Key and Value heads (`8 Q-heads per 1 KV-head`). This reduces memory bandwidth during generation by 8× with zero quality loss!

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_concept_scaled_dot_product/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: Scaled Dot-Product</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../../03_transformers/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 3: The Transformer Architecture →</a></div>
</div>
