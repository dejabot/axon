# Concept 02: Autoregressive Next-Token Sampling (Temperature, Top-k, Top-p)

Large Language Models do not generate entire sentences or paragraphs in a single step. Instead, they operate **autoregressively**: predicting exactly **one next token at a time**, appending it to the prompt, and feeding the updated sequence back into the model.

At the output of the final Transformer layer, the model produces un-normalized prediction scores called **Logits** across all 50,000+ vocabulary tokens.

How do we pick the winner?

> Open the interactive demo below to adjust Temperature, Top-k, and Top-p sliders, observe the live token probability distribution, and click "Generate Next Token" to sample tokens in real time.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Next-Token Generation & Sampling Sandbox"></iframe>

---

## 1. Temperature Scaling: Shaping the Distribution

Before applying Softmax, we divide all logits by a positive scalar called **Temperature (`T`)**:

```text
P(token_i) = exp( zᵢ / T ) / ∑ exp( zⱼ / T )
```

* **Low Temperature (`T → 0.0`, "Greedy Search"):** Exaggerates differences between logits. The top candidate approaches 100% probability. Ideal for deterministic coding, mathematical reasoning, and robot commands.
* **Balanced Temperature (`T = 0.7 - 0.8`):** Retains natural variety while filtering out gibberish. Standard setting for conversational chatbots.
* **High Temperature (`T > 1.2`):** Flattens the distribution so unlikely tokens have higher chances of being chosen. Increases creativity but risks hallucinations and typos.

---

## 2. Top-k & Top-p (Nucleus) Filtering

Pure sampling from a 50,000-word vocabulary can occasionally pick bizarre low-probability tokens from the long tail. We filter candidates using two complementary techniques:

### Top-k Filtering
Keep only the `k` highest-probability tokens (e.g. `k = 40`) and set all other token probabilities to zero.

### Top-p (Nucleus) Sampling
Sort all tokens in descending probability order and keep only the smallest group whose cumulative probability reaches threshold `p` (e.g. `p = 0.90`):

* If the model is **95% certain** of the next word, the nucleus contains only 1 token.
* If the model is **uncertain**, the nucleus expands dynamically to include 20+ reasonable candidates.

---

## 3. Solving It in Code (Java)

Here is a complete Next-Token Sampler in Java with Temperature and Top-p Nucleus filtering:

```java
import java.util.*;

public class TokenSampler {
    public record Candidate(String token, double prob) {}

    public static String sampleNextToken(double[] logits, String[] vocab, double temperature, double topP) {
        int n = logits.length;

        // 1. Temperature Scaling + Softmax
        double maxLogit = Double.NEGATIVE_INFINITY;
        for (double z : logits) maxLogit = Math.max(maxLogit, z / temperature);

        double expSum = 0.0;
        double[] probs = new double[n];
        for (int i = 0; i < n; i++) {
            probs[i] = Math.exp((logits[i] / temperature) - maxLogit);
            expSum += probs[i];
        }
        for (int i = 0; i < n; i++) probs[i] /= expSum;

        // 2. Sort Candidates Descending
        List<Candidate> candidates = new ArrayList<>();
        for (int i = 0; i < n; i++) candidates.add(new Candidate(vocab[i], probs[i]));
        candidates.sort((a, b) -> Double.compare(b.prob, a.prob));

        // 3. Top-p Nucleus Truncation
        List<Candidate> nucleus = new ArrayList<>();
        double cumulativeProb = 0.0;
        for (Candidate c : candidates) {
            nucleus.add(c);
            cumulativeProb += c.prob;
            if (cumulativeProb >= topP) break;
        }

        // 4. Sample from Nucleus
        double randomVal = Math.random() * cumulativeProb;
        double runningSum = 0.0;
        for (Candidate c : nucleus) {
            runningSum += c.prob;
            if (randomVal <= runningSum) return c.token;
        }

        return nucleus.get(0).token;
    }

    public static void main(String[] args) {
        String[] vocab = {"score", "intake", "align", "wait", "dance"};
        double[] logits = {6.2, 5.1, 4.0, 1.2, -2.5};

        String sampled = sampleNextToken(logits, vocab, 0.7, 0.90);
        System.out.printf("Sampled Next Token: \"%s\"%n", sampled);
    }
}
```

---

## 4. Math! Translation Sidebar

The formal mathematical definition of Nucleus Sampling:

```text
Nucleus S_p = smallest subset of V such that: ∑ P(x) ≥ p
```

### The KV-Cache Optimization:
* In autoregressive generation, calculating attention over previous tokens at every step is redundant.
* **KV-Caching** stores the Key and Value vectors of past tokens in GPU memory, reducing computation from `O(N²)` to `O(1)` per generated token!

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_concept_rotary_embeddings_rope/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: RoPE Embeddings</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 4 Overview</a></div>
  <div><a href="../../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">LLM Axon Home →</a></div>
</div>
