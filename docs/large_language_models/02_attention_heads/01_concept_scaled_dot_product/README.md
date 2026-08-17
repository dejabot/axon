# Concept 01: Scaled Dot-Product & Self-Attention

Static word embeddings are not enough to understand language. The word `"bank"` has one meaning in *"river bank"* and an entirely different meaning in *"money in the bank"*.

To understand meaning in context, Transformers use **Self-Attention** to dynamically route information between all tokens in a sequence.

> Open the interactive demo below to inspect an attention matrix heatmap and observe how tokens like *"it"* dynamically route attention to their referring nouns.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Scaled Dot-Product Attention Heatmap"></iframe>

---

## The Query, Key, Value (Q, K, V) Mental Model

Think of Self-Attention like a database retrieval or search engine lookup:

1. **Query (Q):** *"What information am I searching for?"*
   * Example: The pronoun token `"it"` asks: *"Find me the physical object in this sentence."*
2. **Key (K):** *"What information do I contain?"*
   * Example: The token `"Note"` advertises: *"I am an orange foam game piece."*
3. **Value (V):** *"What information should I transmit if matched?"*
   * The actual semantic representation routed forward into the next layer.

---

## 1. The 4 Steps of Scaled Dot-Product Attention

### Step 1: Compute Raw Match Scores
Take the dot product between every Query and Key vector:

```text
Score(i, j) = Qᵢ · Kⱼ
```

### Step 2: Scale by Square Root of Dimension
When vector dimension `d_k` is large (e.g. 64 or 128), dot products can grow huge (e.g. +50 or +100). This pushes Softmax into flat saturation zones where gradients vanish. Dividing by `√(d_k)` stabilizes the variance to `1.0`:

```text
Scaled_Score(i, j) = (Qᵢ · Kⱼ) / √(d_k)
```

### Step 3: Softmax Probabilities
Turn raw scores into normalized attention weights that sum to 100% across the row:

```text
Attention_Weights = Softmax(Scaled_Score)
```

### Step 4: Weighted Sum of Values
Multiply the attention weights by the Value vectors to produce the new context-enriched representation:

```text
Output_Vector = ∑ (Attention_Weightⱼ · Vⱼ)
```

---

## 2. Solving It in Code (Java)

Here is how Scaled Dot-Product Attention is computed for a token in pure Java:

```java
public class SelfAttention {
    public static double[] computeAttention(double[] query, double[][] keys, double[][] values, int d_k) {
        int seqLen = keys.length;
        double[] rawScores = new double[seqLen];
        double scale = Math.sqrt(d_k);

        // 1. Scaled dot products: (Q · K) / sqrt(d_k)
        for (int j = 0; j < seqLen; j++) {
            double dot = 0.0;
            for (int d = 0; d < query.length; d++) {
                dot += query[d] * keys[j][d];
            }
            rawScores[j] = dot / scale;
        }

        // 2. Softmax normalization
        double expSum = 0.0;
        double[] expScores = new double[seqLen];
        for (int j = 0; j < seqLen; j++) {
            expScores[j] = Math.exp(rawScores[j]);
            expSum += expScores[j];
        }

        double[] attentionWeights = new double[seqLen];
        for (int j = 0; j < seqLen; j++) {
            attentionWeights[j] = expScores[j] / expSum;
        }

        // 3. Weighted sum of Values: sum(weight_j * V_j)
        int valDim = values[0].length;
        double[] contextOut = new double[valDim];
        for (int j = 0; j < seqLen; j++) {
            for (int d = 0; d < valDim; d++) {
                contextOut[d] += attentionWeights[j] * values[j][d];
            }
        }

        return contextOut;
    }

    public static void main(String[] args) {
        double[] query = {1.2, 0.8};
        double[][] keys = { {1.1, 0.9}, {-0.8, 0.4}, {0.2, -1.0} };
        double[][] values = { {5.0, 2.0}, {1.0, 8.0}, {3.0, 3.0} };

        double[] context = computeAttention(query, keys, values, 2);
        System.out.printf("Enriched Context Vector: [%.2f, %.2f]%n", context[0], context[1]);
    }
}
```

---

## 3. Math! Translation Sidebar

Here is the famous equation from the original 2017 Transformer paper (*"Attention Is All You Need"*):

```text
Attention(Q, K, V) = Softmax( (Q · Kᵀ) / √(d_k) ) · V
```

### Dimension Tracking:
* `Q` has shape `(N, d_k)` (where `N` is sequence length, `d_k` is head dimension).
* `Kᵀ` has shape `(d_k, N)`.
* `Q · Kᵀ` has shape `(N, N)` — an `N × N` square grid where row `i` contains the attention scores of token `i` toward all tokens `j`.
* Multiplying by `V` `(N, d_v)` yields `(N, d_v)` — the final context-mixed vectors.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 2 Overview</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">LLM Axon Home</a></div>
  <div><a href="../02_concept_multi_head_attention/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Multi-Head Attention →</a></div>
</div>
