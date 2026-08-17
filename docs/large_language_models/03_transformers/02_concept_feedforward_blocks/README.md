# Concept 02: The Transformer Decoder Block (SwiGLU & Feed-Forward)

Self-Attention allows tokens to look at and talk to each other. But attention alone only *mixes* existing information—it does not transform, compute, or recall new facts.

The "thinking" and factual memory retrieval in a Transformer happens inside the **Feed-Forward Network (FFN)**, assembled into the complete **Transformer Decoder Block**.

> Open the interactive demo below to step through every stage of a Transformer Decoder Block and trace tensor dimensions from `(N, 768)` up to `(N, 3072)` and back.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Transformer Block Architecture Inspector"></iframe>

---

## 1. The Role of the Feed-Forward Network

After tokens have exchanged context via Self-Attention, each token vector passes **independently** through a multi-layer perceptron (MLP).

The standard pattern expands the representation into a wider hidden dimension (typically `4 × d_model` or `8/3 × d_model`) before compressing it back down:

```
Token Vector (768 dims) ──► Expand (3,072 dims) ──► Non-Linear Activation ──► Compress (768 dims)
```

Researchers have shown that these Feed-Forward layers act as **associative key-value memory banks**, storing facts, rules of syntax, and world knowledge learned during pre-training.

---

## 2. Modern Activation: SwiGLU

While the original 2017 Transformer used standard `ReLU`, modern state-of-the-art LLMs (such as **LLaMA, Gemma, and Mistral**) use **SwiGLU** (Swish Gated Linear Unit):

```text
SwiGLU(x) = ( Swish(x · W_gate) ⊙ (x · W_up) ) · W_down
where Swish(z) = z · Sigmoid(z)
```

SwiGLU splits the expansion into two parallel linear paths:
1. A **Gate Path** modulated by the smooth Swish activation.
2. A **Value Path** multiplied element-wise (`⊙`) with the gate.

This gating mechanism allows the network to dynamically filter out irrelevant features with high precision.

---

## 3. The Complete Transformer Block Forward Pass

```
                         Input x (N × d_model)
                                 │
                 ┌───────────────┴───────────────┐
                 │                               │ (Skip Connection)
                 ▼                               │
             RMSNorm(x)                          │
                 │                               │
                 ▼                               │
        Multi-Head Attention                     │
                 │                               │
                 ▼                               ▼
               Add ──────────────────────────────┘
                 │
                 │ (x_mid)
                 ├───────────────────────────────┐
                 │                               │ (Skip Connection)
                 ▼                               │
           RMSNorm(x_mid)                        │
                 │                               │
                 ▼                               │
            SwiGLU FFN                           │
                 │                               │
                 ▼                               ▼
               Add ──────────────────────────────┘
                 │
                 ▼
          Block Output (N × d_model)
```

---

## 4. Solving It in Code (Java)

Here is a clean implementation of the SwiGLU Feed-Forward computation in Java:

```java
public class SwiGLUBlock {
    public static double sigmoid(double z) {
        return 1.0 / (1.0 + Math.exp(-z));
    }

    public static double swish(double z) {
        return z * sigmoid(z);
    }

    public static double[] swigluFFN(double[] x, double[][] W_gate, double[][] W_up, double[][] W_down) {
        int hiddenDim = W_gate[0].length; // e.g. 3072 dims
        int modelDim = x.length;          // e.g. 768 dims

        // 1. Compute Gate and Up projections
        double[] hidden = new double[hiddenDim];
        for (int h = 0; h < hiddenDim; h++) {
            double gateVal = 0.0;
            double upVal = 0.0;
            for (int d = 0; d < modelDim; d++) {
                gateVal += x[d] * W_gate[d][h];
                upVal   += x[d] * W_up[d][h];
            }
            // SwiGLU: Swish(Gate) * Up
            hidden[h] = swish(gateVal) * upVal;
        }

        // 2. Down projection back to modelDim
        double[] output = new double[modelDim];
        for (int d = 0; d < modelDim; d++) {
            double sum = 0.0;
            for (int h = 0; h < hiddenDim; h++) {
                sum += hidden[h] * W_down[h][d];
            }
            output[d] = sum;
        }

        return output;
    }

    public static void main(String[] args) {
        double[] x = {0.5, -1.2, 0.8, 2.1};
        System.out.printf("SwiGLU forward pass ready with %d input dimensions.%n", x.length);
    }
}
```

---

## 5. Math! Translation Sidebar

The formal equations of a modern Pre-Norm Transformer Decoder Block:

```text
x₁ = x + MultiHead( RMSNorm(x) )
x_out = x₁ + SwiGLU( RMSNorm(x₁) )
```

### Parameter Breakdown:
* In a 7B parameter model, roughly **two-thirds of all parameters** reside in the Feed-Forward weight matrices (`W_gate`, `W_up`, `W_down`), with only one-third in the Attention projections.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_concept_residual_layernorm/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: Residuals & RMSNorm</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 3 Overview</a></div>
  <div><a href="../../04_generation_sampling/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 4: Generation & Sampling →</a></div>
</div>
