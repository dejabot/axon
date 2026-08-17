# Axon 1: Mathematical Foundations — Working Outline

This is the agreement document for the Math axon, and the **toolkit manifest** handed to each concept-authoring agent. Its job is to make the prerequisite chain explicit, so that no concept reaches for a tool the reader has not yet been given.

**Status:** `[deep]` meets the bar · `[thin]` needs a pass · `[new]` not yet written

**Time target:** ~30 minutes per concept. Prose 1,800–2,400 words (2,800 hard ceiling), plus code, demo and two worked checkpoints.

---

## The Prerequisite Chain

Each module states what the reader arrives holding. A concept may use anything above its own line and nothing below it.

```
   Module 1  Geometry      arithmetic, square roots, coordinates
   Module 2  Trigonometry  + everything from Module 1
   Module 3  Linear Alg.   + cos/sin, rotation, frames
   Module 4  Calculus      + vectors, matrices, dot products
   Module 5  Probability   + derivatives, integrals, gradients
```

Two consequences worth stating plainly, because both were violated in the original draft:

* **Geometry may not use `cos` or `sin`.** Anything needing an angle belongs in Module 2 or later.
* **Trigonometry may not use matrices at all** — not the notation, not multiplication. Rotation is taught in Module 2 as two scalar equations derived from where `î` and `ĵ` land. Frames are taught as rotate-then-translate. Module 3 then reveals those same equations as a matrix, which lands as a payoff for a module's worth of hand computation rather than as an unearned definition. A single forward-pointer sentence in Module 2 ("these two equations are usually packed into an object called a matrix — Module 3 derives what that means") is the only mention permitted.

### Language frugality

Dual-language concepts cost roughly double the code and push toward the time ceiling, so they are reserved for concepts that genuinely serve both consumers. **Exactly four concepts are dual-language:**

* Module 3 Concept 2 — dot products (projection for robotics, cosine similarity for embeddings)
* Module 3 Concept 4 — matrix multiplication (transform composition, and the neural network forward pass)
* Module 4 Concept 2 — the chain rule (motion derivatives, and backpropagation)
* Module 5 Concept 5 — maximum likelihood (least squares for system identification, and cross-entropy for classifiers)

Every other concept picks its dominant consumer and cross-references the other.

### Time target

**30–45 minutes per concept.** Word count is a proxy, not the goal: 1,800–2,800 words of prose plus code, demo and two worked checkpoints typically lands in that window. Overrun it when splitting a topic would do more harm than the extra length — one coherent 50-minute concept beats two amputated halves. Do not exceed 45 minutes casually.

---

## Module 1: Geometry for Robotics — one concept outstanding

Arrives with: arithmetic, square roots, the Cartesian plane. Leaves with: distance, the cross product, orientation tests, interpolation, interval and polygon membership.

| # | Concept | Key derivations | Status |
|---|---|---|---|
| 1 | Coordinates, Poses & Pythagorean Distance | Pythagoras by area rearrangement; distance formula; squared-distance ranking; L1/L2/L∞ | `[deep]` |
| 2 | Lines, Segments & Intersections | Parametric form; 2D cross product; orientation test; segment intersection; clearance | `[deep]`, needs trim |
| 3 | Linear Interpolation, Lookup Tables & Blending | `lerp` named and generalised from Concept 02's parametric form; why `(1−t)a + tb` beats `a + t(b−a)` numerically; inverse lerp and remapping; clamping vs. extrapolation; interpolating lookup tables for shooter calibration; bilinear interpolation in 2D; **why angles cannot be lerped naively** | `[new]` |
| 4 | Bounding Boxes, Overlap & Collision | Interval overlap via De Morgan; separating axis; Minkowski inflation; IoU; swept boxes | `[deep]` |
| 5 | Polygons, Areas & Field Zones | Convex half-planes; ray-casting parity proof; half-open vertex rule; shoelace formula | `[deep]` |

---

## Module 2: Trigonometry & Angles — next

Arrives with: Module 1. Leaves with: `cos`/`sin`/`tan`, radians, the rotation matrix as a recipe, rigid transforms, `atan2`, angle wrapping, quaternions.

| # | Concept | Scope & key derivations | Language | Status |
|---|---|---|---|---|
| 1 | Right Triangles & the Unit Circle | **SOH-CAH-TOA taught explicitly.** Why ratios depend only on the angle (similar triangles). Hypotenuse-1 collapse. Extending the definition past 90° via the circle. Radians as arc length, and why `2π` rather than 360. `sin² + cos² = 1` as Pythagoras. | Java | `[thin]` |
| 2 | Rotating a Vector | Rotation from tracking `î` and `ĵ`; the two scalar equations; length preservation via `sin² + cos² = 1`; inverse by rotating `−θ`; composition = angle addition, which *derives* the angle-addition identities. **No matrix notation** — one forward-pointer sentence only. | Java | `[deep]`, needs matrix material lifted to Module 3 |
| 3 | Coordinate Frames (Field, Robot, Camera) | Rigid transform = rotate then translate, in scalar form. Chaining field→robot→camera. **Inverting a transform** and why it is not simply negating both parts. Which direction needs `−θ`. | Java | `[thin]` |
| 4 | Inverse Trig & 4-Quadrant Heading with atan2 | `asin`/`acos`/`atan` and their restricted ranges; why `atan(y/x)` loses a quadrant; how `atan2` recovers it; the `(0,0)` case | Java | `[thin]` |
| 5 | Angle Wrapping & Shortest Angular Distance | Angles as a circle not a line; modular difference into `[−π, π]`; the 340°-instead-of-20° failure; swerve's 180° flip with speed inversion | Java | `[thin]` |
| 6 | Law of Sines, Law of Cosines & Two-Link Arms | Law of cosines as generalised Pythagoras (derive by dropping a perpendicular); solving a triangle from three sides; two-link arm reach and elbow-up/elbow-down ambiguity | Java | `[new]` |
| 7 | 3D Rotations, Gimbal Lock & Quaternions | Euler angles and their order dependence; gimbal lock as a lost degree of freedom; quaternions as an axis-angle encoding; why IMUs report them | Java | `[thin]` |

---

## Module 3: Linear Algebra & Transformations

Arrives with: Modules 1–2. Leaves with: matrices as transformations, matrix multiplication, inverses, least squares, eigenvectors.

| # | Concept | Scope & key derivations | Language | Status |
|---|---|---|---|---|
| 1 | Vectors, Scaling & Basis Spaces | Vector as displacement vs. position; scalar multiplication; linear combinations; basis and span; why `î`, `ĵ` are a choice | Java | `[thin]` |
| 2 | Dot Products, Projections & Alignment | Two definitions (component sum and `‖a‖‖b‖cos θ`) and the proof they agree; projection; orthogonality; cosine similarity | **Both** | `[thin]` |
| 3 | Matrices as Coordinate Transformers | A matrix is where the basis vectors land; reading a matrix by its columns. **The payoff concept: Module 2's two rotation equations are revealed as `R(θ)`**, with its columns being exactly the `î` and `ĵ` images derived there. Orthogonality, and inverse = transpose. | Java | `[thin]` |
| 4 | Matrix Multiplication & Composition | Multiplication derived as "apply one transform then the other"; why it is not commutative; why inner dimensions must match. Rigid transforms and homogeneous coordinates, closing the loop on Module 2's frame chaining. The neural network forward pass as the same operation. | **Both** | `[new]` |
| 5 | Determinants, Inverses & Singularity | Determinant as signed area scaling; zero determinant means collapse and no inverse; 2×2 inverse formula; condition number as a practical warning | Java | `[thin]` |
| 6 | Solving Linear Systems & Least Squares | Systems as `Ax = b`; over-determined systems from noisy sensors; the normal equations; fitting `kS`, `kV`, `kA` from telemetry | Java | `[new]` |
| 7 | Eigenvectors & Eigenvalues | Vectors a transform only scales; characteristic equation for 2×2; what eigenvalues say about stability; preview of covariance and PCA | Python | `[new]` |

---

## Module 4: Calculus, Motion & Optimization

Arrives with: Modules 1–3. Leaves with: derivatives, the chain rule, integrals, gradients, and what makes optimisation hard.

| # | Concept | Scope & key derivations | Language | Status |
|---|---|---|---|---|
| 1 | Rates of Change & Derivatives | Average vs. instantaneous rate; the limit; derivative of `x²` from first principles; position→velocity | Java | `[thin]` |
| 2 | Derivative Rules & the Chain Rule | Power, sum and product rules; **the chain rule derived and drilled**, since backpropagation is nothing else; composing three or more functions | **Both** | `[new]` |
| 3 | Acceleration, Jerk & S-Curves | Second and third derivatives; why unbounded jerk damages mechanisms; trapezoidal vs. S-curve profiles | Java | `[thin]` |
| 4 | Accumulation, Area & Numerical Integration | Integral as accumulated area; the fundamental theorem stated and motivated; Riemann vs. trapezoidal at a 20 ms loop rate; integrator drift | Java | `[thin]` |
| 5 | Partial Derivatives & Gradients | Holding variables fixed; the gradient vector; steepest ascent proved; level curves are orthogonal to the gradient | Python | `[thin]` |
| 6 | Optimization, Critical Points & Saddles | Zero gradient means stationary, not minimum; second-derivative test; saddle points and why they dominate in high dimensions; convex vs. non-convex | Python | `[new]` |

---

## Module 5: Probability & Uncertainty

Arrives with: Modules 1–4. Leaves with: distributions, covariance, Bayes, softmax, expected value.

| # | Concept | Scope & key derivations | Language | Status |
|---|---|---|---|---|
| 1 | Random Variables, Sensor Noise & the Normal Distribution | Randomness as a distribution not a number; mean and variance; the shape of the Gaussian and why noise tends toward it; the 68/95/99.7 rule | Java | `[thin]` |
| 2 | Variance, Covariance & Correlation | Variance as expected squared deviation; covariance as joint variation; the covariance matrix; correlation vs. causation; the uncertainty ellipse | Java | `[new]` |
| 3 | Bayes' Rule & 1D Sensor Fusion | Conditional probability; Bayes derived from the joint; prior/likelihood/posterior; fusing two Gaussians and why the result is more confident than either | Java | `[thin]` |
| 4 | Discrete Distributions & Softmax | Probability mass; why logits are not probabilities; softmax derived from exponentiate-and-normalise; temperature; the max-subtraction stability trick | Python | `[thin]` |
| 5 | Maximum Likelihood Estimation | Likelihood as `P(data \| θ)` read as a function of `θ`, not of the data — the conceptual flip the whole concept turns on. Independence gives a product; **why we take the log** (underflow, sums differentiate cleanly, and monotonicity leaves the argmax untouched — the same argument that dropped the square root in Geometry Concept 01). Derive the MLE of a Gaussian mean and get the sample mean. **The two payoffs: Gaussian noise ⟹ least squares, and categorical ⟹ cross-entropy.** MAP as MLE plus a prior, and an L2 penalty as a Gaussian prior. | **Both** | `[new]` |
| 6 | Expected Value & Decision Making | Expectation as a probability-weighted average; expected value of a strategy; variance as risk; when the higher-expected-value choice is still wrong | Java | `[thin]` |

---

## Totals

```
   Module 1  Geometry       5 concepts   4 deep, 1 new
   Module 2  Trigonometry   7 concepts   1 deep, 5 thin, 1 new
   Module 3  Linear Algebra 7 concepts   5 thin, 2 new
   Module 4  Calculus       6 concepts   4 thin, 2 new
   Module 5  Probability    6 concepts   4 thin, 2 new
   ------------------------------------------------
   Axon 1 total            31 concepts   ~18 hours of study
```

---

## Authoring Loop

One concept at a time, each in a fresh agent context.

1. **Author agent** receives: this outline, its own concept's row, the two adjacent concepts' rows (so it can hand off cleanly), and the module's prerequisite line. It does not receive the rest of the curriculum — that is the point.
2. It writes `README.md` and `demo.html` against REVIEWER_SPEC.
3. **Review agent** audits against the 7-point rubric, and must load the demo in a browser and screenshot it, because a demo can pass code review while rendering blank.
4. **Integration** — nav footers, indexes, link check, word count — runs once per module, not per concept.

Cross-module moves are proposed to the human, never executed by a concept agent. That is how indexes silently break.
