# Concept 02: High-Dimensional Semantic Vectors & Cosine Distance

In Concept 01, we saw how tokenizers assign an integer ID to each subword (`"robot" = 103`, `"coral" = 104`). But in arithmetic, `104 - 103 = 1` carries zero semantic meaning.

To understand meaning, neural networks transform discrete token IDs into dense coordinate vectors called **Embeddings**.

> Open the interactive demo below to explore a 2D semantic embedding space, select word vectors, and calculate their live Cosine Semantic Similarity.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Vector Embeddings & Cosine Similarity Visualizer"></iframe>

---

## The Everyday Robot Problem

How can an autonomous AI understand that the command `"Intake the orange ring"` means the exact same thing as `"Grab the Note"`, even though they share zero identical words?

Instead of comparing letters, we represent every token as a list of 768 to 4,096 continuous numbers (coordinates in a high-dimensional concept space):

```text
vec("Note")       = [ 0.82,  0.45, -0.12,  0.95, ...]
vec("Game Piece") = [ 0.79,  0.41, -0.09,  0.91, ...]
vec("Battery")    = [-0.65,  0.88,  0.54, -0.32, ...]
```

Because `"Note"` and `"Game Piece"` share similar physical attributes, their vectors point in nearly the **exact same direction** in space!

---

## 1. Cosine Semantic Similarity

How do we measure whether two high-dimensional vectors point in the same direction? 

We use the **Cosine Similarity** (the cosine of the angle `θ` between them):

```text
Cosine_Similarity(u, v) = (u · v) / (|u| · |v|)
```

* **`Similarity = +1.0` (`θ = 0°`):** The vectors point in the exact same direction (identical semantic meaning).
* **`Similarity = 0.0` (`θ = 90°`):** The vectors are orthogonal (completely unrelated concepts).
* **`Similarity = -1.0` (`θ = 180°`):** The vectors point in opposite directions.

---

## 2. Solving It in Code (Java)

Here is how we calculate the Cosine Similarity between two semantic embedding vectors in Java:

```java
public class EmbeddingSimilarity {
    public static double cosineSimilarity(double[] u, double[] v) {
        double dotProduct = 0.0;
        double normU = 0.0;
        double normV = 0.0;

        for (int i = 0; i < u.length; i++) {
            dotProduct += u[i] * v[i];
            normU += u[i] * u[i];
            normV += v[i] * v[i];
        }

        double denominator = Math.sqrt(normU) * Math.sqrt(normV);
        return denominator > 0 ? dotProduct / denominator : 0.0;
    }

    public static void main(String[] args) {
        // Simplified 3D embedding vectors
        double[] note = {0.82, 0.45, 0.95};
        double[] coral = {0.78, 0.41, 0.91};
        double[] battery = {-0.65, 0.88, -0.32};

        double simNoteCoral = cosineSimilarity(note, coral);
        double simNoteBattery = cosineSimilarity(note, battery);

        System.out.printf("Similarity(Note, Coral):   %.3f (High match!)%n", simNoteCoral);
        System.out.printf("Similarity(Note, Battery): %.3f (Unrelated)%n", simNoteBattery);
        // Output: 0.998 vs -0.154
    }
}
```

---

## 3. Vector Arithmetic & Analogies

Because embeddings map geometric directions to semantic concepts, you can perform literal math on human thoughts!

```text
vec("King") - vec("Man") + vec("Woman") ≈ vec("Queen")
vec("Shooter") - vec("Flywheel") + vec("Intake") ≈ vec("Rollers")
```

---

## 4. Math! Translation Sidebar

Here is how Cosine Similarity is written in linear algebra literature:

```text
cos(θ) = (u · v) / (||u|| · ||v||) = ∑ (uᵢ · vᵢ) / ( √(∑ uᵢ²) · √(∑ vᵢ²) )
```

### How to Read This Out Loud:
* `u · v` ("u dot v"): The dot product sum of element-wise multiplications.
* `||u||` ("norm of u"): The Euclidean length / magnitude of vector `u`.
* `cos(θ)`: The directional alignment score between `-1.0` and `+1.0`.

---

## 5. Bridge to RAG & Vector Databases

* **Retrieval-Augmented Generation (RAG):** When an LLM searches a 500-page robot manual or technical rulebook, it encodes user questions into embeddings and queries a **Vector Database** (like ChromaDB or Pinecone) for the top-k paragraphs with the highest Cosine Similarity.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_concept_tokenization_bpe/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: Tokenization & BPE</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="../../02_attention_heads/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 2: Attention Heads →</a></div>
</div>
