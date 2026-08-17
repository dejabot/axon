# Concept 01: Byte-Pair Encoding (BPE) & Vocabulary Lookups

Computers and neural networks cannot perform calculus or matrix multiplication on raw letters like `"r"`, `"o"`, `"b"`, `"o"`, `"t"`. Before an AI can read, reason, or generate text, words must be broken down into discrete numeric units called **Tokens**.

> Open the interactive demo below to type custom sentences and watch Byte-Pair Encoding (BPE) split text into color-coded subwords and vocabulary integer IDs.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Tokenization & BPE Visualizer"></iframe>

---

## The Everyday Problem

Suppose you send a voice or text command to your autonomous robot:

```text
"Align to Reef and intake the Note"
```

How should a neural network convert this string into numbers?

### Approach 1: Character-Level (One number per letter)
* `"A" = 65, "l" = 108, "i" = 105, ...`
* **Problem:** Sequences become ridiculously long. A 500-word paragraph turns into 3,000 separate tokens, making attention computation 36× slower!

### Approach 2: Word-Level (One number per dictionary word)
* `"Align" = 4210, "to" = 12, "Reef" = 8901`
* **Problem:** If a user makes a typo (`"Algn"`), uses robot slang, or writes a new compound word (`"swervepath"`), the model has no idea what to do (Unknown Word `[UNK]`).

---

## 1. The Modern Solution: Byte-Pair Encoding (BPE)

**Byte-Pair Encoding (BPE)** is a hybrid subword tokenizer:
1. Start with individual characters.
2. Count the most frequent adjacent character pairs across a massive text dataset.
3. Merge frequent pairs into new subword units (e.g. `"ing"`, `"auto"`, `"bot"`, `"pre"`).
4. Repeat for thousands of merges until you have a fixed vocabulary of 32,000 to 100,000 tokens.

Common words become a single token (`"robot"` → `[robot]`), while rare or compound words are cleanly split into understandable pieces (`"swervebot"` → `[swerve, bot]`).

---

## 2. Solving It in Code (Java)

Here is a clean BPE subword encoder and vocabulary lookup in Java:

```java
import java.util.*;

public class SimpleTokenizer {
    // Fixed vocabulary: Token String -> Integer ID
    private final Map<String, Integer> vocab = new HashMap<>();

    public SimpleTokenizer() {
        // Sample vocabulary entries
        vocab.put("auto", 101);
        vocab.put("nomous", 102);
        vocab.put("robot", 103);
        vocab.put("swerve", 104);
        vocab.put("drive", 105);
        vocab.put("align", 106);
    }

    public List<Integer> encode(String text) {
        List<Integer> tokenIds = new ArrayList<>();
        String[] words = text.toLowerCase().split("\\s+");

        for (String word : words) {
            if (vocab.containsKey(word)) {
                tokenIds.add(vocab.get(word));
            } else {
                // Greedy subword matching
                boolean matched = false;
                for (String sub : vocab.keySet()) {
                    if (word.startsWith(sub)) {
                        tokenIds.add(vocab.get(sub));
                        String rest = word.substring(sub.length());
                        if (vocab.containsKey(rest)) {
                            tokenIds.add(vocab.get(rest));
                            matched = true;
                            break;
                        }
                    }
                }
                if (!matched) tokenIds.add(0); // [UNK] token
            }
        }
        return tokenIds;
    }

    public static void main(String[] args) {
        SimpleTokenizer tokenizer = new SimpleTokenizer();
        String prompt = "autonomous robot swerve drive";
        List<Integer> tokens = tokenizer.encode(prompt);

        System.out.println("Prompt: " + prompt);
        System.out.println("Token IDs: " + tokens);
        // Output: [101, 102, 103, 104, 105] (5 tokens)
    }
}
```

---

## 3. Math! Translation Sidebar

In formal Transformer literature, tokenization is represented as a mapping function:

```text
T: String → (t₁, t₂, ..., t_N) where tᵢ ∈ {0, 1, 2, ..., |V| - 1}
```

### How to Read This Out Loud:
* `T` ("Tokenizer"): Converts raw text into an ordered sequence of integer IDs.
* `|V|` ("cardinality of V" or "vocabulary size"): The total number of unique tokens in the dictionary (e.g. 50,257 in GPT-2, 32,000 in LLaMA, 100,000+ in GPT-4).
* `tᵢ`: The token ID at sequence position `i`.

---

## 4. Bridge to Modern LLMs

* **Tiktoken & SentencePiece:** Production LLMs use hyper-optimized BPE implementations written in Rust or C++ that process billions of characters per second.
* **Special Tokens:** Tokenizers also inject structural marker tokens into sequences:
  * `<|begin_of_text|>`: Tells the model a new document starts here.
  * `<|im_start|>user / assistant<|im_end|>`: Delineates chat dialog turns.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1: Embeddings</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">LLM Axon Home</a></div>
  <div><a href="../02_concept_vector_embeddings/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Vector Embeddings →</a></div>
</div>
