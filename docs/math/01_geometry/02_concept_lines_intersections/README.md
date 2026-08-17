# Concept 02: Lines, Segments & Intersections

> **▶ Interactive Demo: [Path Crossing & Clearance Visualizer](demo.html)**
>
> Drag the endpoints of a planned path and a field barrier. Watch the orientation tests flip sign, the intersection point appear, and the clearance distance update live.

<iframe src="demo.html" width="100%" height="560" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Does This Path Cross That Barrier?

Autonomous routines are built out of straight runs. "Drive from the starting line to the scoring position" is a segment from one point to another. Before committing to that run, the software has to answer two questions that Concept 01 gave us no tools for:

1. **Does the path cross something it must not cross?** A field barrier, the edge of a protected zone, the line an opponent's robot is currently driving along.
2. **If it does not cross, how close does it come?** Clearing a wall by two centimetres is not clearing it, once you account for wheel slip.

<div style="text-align: center; margin: 20px 0;">
  <svg width="380" height="200" viewBox="0 0 380 200" style="max-width: 100%; height: auto;" role="img" aria-label="A planned robot path crossing one barrier and passing near another.">
    <line x1="25" y1="170" x2="360" y2="170" stroke="currentColor" stroke-opacity="0.25" stroke-width="1.5" />
    <line x1="25" y1="170" x2="25" y2="20" stroke="currentColor" stroke-opacity="0.25" stroke-width="1.5" />
    <line x1="150" y1="30" x2="150" y2="130" stroke="#f43f5e" stroke-width="4" stroke-linecap="round" />
    <text x="112" y="24" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">barrier C→D</text>
    <line x1="245" y1="60" x2="330" y2="105" stroke="#94a3b8" stroke-width="4" stroke-linecap="round" />
    <text x="258" y="52" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">wall</text>
    <line x1="55" y1="140" x2="320" y2="45" stroke="#fbbf24" stroke-width="3" />
    <circle cx="55" cy="140" r="6" fill="#fbbf24" />
    <circle cx="320" cy="45" r="6" fill="#fbbf24" />
    <text x="40" y="160" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">A (start)</text>
    <text x="300" y="34" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">B (goal)</text>
    <circle cx="150" cy="106" r="7" fill="none" stroke="#4ade80" stroke-width="2.5" />
    <text x="158" y="122" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">crossing</text>
    <line x1="288" y1="56" x2="296" y2="76" stroke="#c084fc" stroke-width="2" stroke-dasharray="3,3" />
    <text x="300" y="72" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">clearance</text>
  </svg>
</div>

Both questions are about lines, and both have clean answers that need nothing beyond addition, multiplication and one square root.

---

## 2. Building the Math

### Step 1: Why slope is the wrong description

School algebra describes a line as `y = mx + b`, where `m` is the slope. It is a fine description for graphing, and a poor one for robots, for one blunt reason: a vertical line has no slope. Run "rise over run" on a line going straight up and you divide by zero.

That is not a rare edge case on a field. A barrier running straight across the field, a robot driving straight down-field, an alliance wall — these are exactly the vertical and horizontal lines that break the formula. Any geometry routine built on slope will work in testing and fail on the one path that happens to be axis-aligned.

### Step 2: Parametric form — describe the walk, not the graph

A better description throws away the idea of a graph and describes a journey. Start at point `A`. Head in the direction that takes you toward `B`. That direction is the displacement `r = B − A`, which we already know how to compute from Concept 01. Now walk some multiple `t` of that displacement:

```
   P(t) = A + t · r        where r = B − A
```

Read it as: "the point you reach after travelling `t` of the way from A toward B." Written out in coordinates it is two ordinary equations:

```
   x(t) = Aₓ + t · rₓ
   y(t) = A_y + t · r_y
```

This form has no division anywhere, so vertical lines are entirely unremarkable. It also hands you something slope never could: the parameter `t` is a physically meaningful number.

```
   t = 0     you are at A
   t = 0.5   you are at the midpoint
   t = 1     you are at B
   t < 0     behind A, on the line but before the start
   t > 1     past B
```

That distinction is exactly the difference between a **line** (all values of `t`, extending forever both ways), a **ray** (`t ≥ 0`), and a **segment** (`0 ≤ t ≤ 1`). A path is a segment. A wall is usually a segment. Confusing the three is the single most common source of "my collision check says the path is blocked by a barrier that is nowhere near it" — the barrier's infinite line is blocking it, not the barrier.

> ### Math!
> ```
>    P(t) = A + t·(B − A),   t ∈ [0, 1]
> ```
> Read as **"P of t equals A plus t times the quantity B minus A, for t in the closed interval zero to one."** The symbol `∈` means "is an element of" or informally "is in". Square brackets `[0, 1]` mean the endpoints are included; round brackets `(0, 1)` would exclude them. This is called the **parametric form** because the whole line is generated by sweeping one parameter.

### Step 3: The 2D cross product, and which side you are on

Everything that follows rests on one small computation. Given two vectors `u = (uₓ, u_y)` and `v = (vₓ, v_y)`, define:

```
   cross(u, v) = uₓ · v_y − u_y · vₓ
```

It takes two vectors and returns a single number. Two facts make it powerful.

**Fact one: its magnitude is an area.** `|cross(u, v)|` is the area of the parallelogram spanned by `u` and `v`. You can see why in a special case: take `u = (a, 0)` lying flat along X and `v = (0, b)` pointing straight up. The parallelogram is a rectangle of area `a·b`, and the formula gives `a·b − 0·0 = a·b`. ✓ As you tilt `v` toward `u`, the parallelogram flattens and its area shrinks; when `v` points the same way as `u` the parallelogram has collapsed to a line of zero area, and indeed `cross((a,0), (ka,0)) = a·0 − 0·ka = 0`.

**Fact two: its sign tells you a direction of turn.** Zero means `u` and `v` are parallel. Positive means `v` is counter-clockwise from `u`; negative means clockwise. Check it with the same example: `cross((1,0), (0,1)) = 1·1 − 0·0 = +1`, and Y is indeed counter-clockwise from X.

<div style="text-align: center; margin: 20px 0;">
  <svg width="360" height="180" viewBox="0 0 360 180" style="max-width: 100%; height: auto;" role="img" aria-label="Three diagrams showing a point left of a line, right of a line, and on the line.">
    <g>
      <line x1="20" y1="140" x2="110" y2="40" stroke="#38bdf8" stroke-width="2.5" />
      <circle cx="95" cy="120" r="6" fill="#4ade80" />
      <text x="14" y="166" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">cross &lt; 0 (right)</text>
    </g>
    <g>
      <line x1="140" y1="140" x2="230" y2="40" stroke="#38bdf8" stroke-width="2.5" />
      <circle cx="152" cy="58" r="6" fill="#c084fc" />
      <text x="132" y="166" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">cross &gt; 0 (left)</text>
    </g>
    <g>
      <line x1="260" y1="140" x2="350" y2="40" stroke="#38bdf8" stroke-width="2.5" />
      <circle cx="305" cy="90" r="6" fill="#fbbf24" />
      <text x="264" y="166" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">cross = 0 (on it)</text>
    </g>
  </svg>
</div>

Fact two gives us the **orientation test**. To ask which side of the line through `A` and `B` a point `P` lies on, form the two vectors leaving `A` and cross them:

```
   orient(A, B, P) = cross(B − A, P − A)
```

Positive means `P` is to the left of the direction of travel from `A` to `B`, negative means to the right, zero means exactly on the line. That single number is the workhorse of computational geometry.

> ### Math!
> The 2D cross product is not really a cross product — the true cross product is defined in 3D and returns a vector. What we computed is its z-component, the only one that survives when both inputs lie flat in the XY plane. You will also see it written `u × v` and called the **perp dot product** or the **wedge product**, `u ∧ v`. Read `cross(u, v)` aloud as **"u cross v"**. It anti-commutes: `cross(v, u) = −cross(u, v)`. Swapping the arguments flips which side you consider "left", which is worth remembering when a collision test reports every answer backwards.

### Step 4: Do two segments cross?

Take segment `AB` (the planned path) and segment `CD` (the barrier). Think about what crossing means.

If the path genuinely cuts through the barrier, then the barrier's two endpoints must sit on **opposite sides** of the path's line — otherwise the whole barrier is off to one side and the path sails past it. Symmetrically, the path's two endpoints must sit on opposite sides of the barrier's line. Neither condition alone is enough: a short barrier can straddle the path's infinite line while sitting far away from the actual path segment.

Both conditions together are exactly right:

```
   d1 = orient(A, B, C)      d2 = orient(A, B, D)
   d3 = orient(C, D, A)      d4 = orient(C, D, B)

   the segments cross  ⟺  (d1 and d2 have opposite signs)
                       and (d3 and d4 have opposite signs)
```

"Opposite signs" is cheap to test: `d1 · d2 < 0`. No division, no square roots, no trigonometry — just four multiplications and some subtractions per orientation test. This is fast enough to run against every barrier on the field, every cycle, forever.

> ### Math!
> The symbol `⟺` is read **"if and only if"**, and it is a strong claim: it says the left side is true in exactly the cases where the right side is true, with no exceptions in either direction. Mathematicians abbreviate it "iff". It is stronger than `⟹` ("implies"), which only promises one direction.

The `= 0` cases — an endpoint sitting exactly on the other segment — are genuinely ambiguous and need a deliberate decision rather than an accident. Does a path that just grazes the corner of a barrier count as a collision? For robot safety the answer should be yes, so treat zero as touching. Real code should also compare against a small tolerance rather than exact zero, because floating-point arithmetic will essentially never produce a clean `0.0`.

### Step 5: Where do they cross?

Knowing *that* two segments cross, we often want the point. Write both in parametric form and demand they meet:

```
   A + t·r = C + u·s        where r = B − A and s = D − C
```

Two unknowns, `t` and `u`. The elegant way to isolate `t` is to cross both sides with `s`, using the fact that `cross(s, s) = 0` — any vector crossed with itself spans a parallelogram of zero area, so the `u` term is annihilated:

```
   cross(A + t·r, s) = cross(C + u·s, s)
   cross(A, s) + t·cross(r, s) = cross(C, s) + 0
   t · cross(r, s) = cross(C − A, s)
```

Which gives, at last:

```
   t = cross(C − A, s) / cross(r, s)
   u = cross(C − A, r) / cross(r, s)
```

Substitute `t` back into `P(t) = A + t·r` to get the crossing point.

The denominator `cross(r, s)` is doing something important. It is zero exactly when `r` and `s` are parallel — the two segments point the same way and never converge. So the division-by-zero case is not a numerical nuisance to be guarded against defensively; it *is* the geometric answer "these lines are parallel". Test it before dividing and report parallel rather than returning a `NaN` that will silently poison every downstream calculation.

Once you have `t` and `u`, the segment test from Step 4 falls out as a bonus: the crossing lies on both segments precisely when `0 ≤ t ≤ 1` and `0 ≤ u ≤ 1`.

### Step 6: How close does the path come?

For clearance we want the shortest distance from a point `P` to the segment `AB`. Start with the infinite line, where the cross product answers it immediately.

The parallelogram spanned by `B − A` and `P − A` has area `|cross(B − A, P − A)|`. But the area of any parallelogram is also base times height. Take `|B − A|` as the base; then the height is precisely the perpendicular distance we are looking for. Rearranging:

```
   distanceToLine = |cross(B − A, P − A)| / |B − A|
```

The base length in the denominator comes from Concept 01's distance formula. No trigonometry required — the cross product supplied the perpendicular for us.

For a **segment**, the perpendicular may land beyond the ends, in which case the nearest point is an endpoint instead. Find where the perpendicular foot lands by intersecting `AB` with the line through `P` running perpendicular to it. Getting a perpendicular direction in 2D costs nothing: rotating any vector `(x, y)` a quarter turn counter-clockwise gives `(−y, x)`, an operation usually written `perp(v)`. Feed that perpendicular line into the Step 5 formula, read off `t`, and:

```
   t < 0        nearest point is A
   0 ≤ t ≤ 1    nearest point is the perpendicular foot
   t > 1        nearest point is B
```

Clamping `t` into `[0, 1]` and evaluating `P(t)` handles all three cases in one line, with no branching.

If you push that perpendicular-intersection algebra through and simplify, the cross products cancel and `t` collapses to a shorter expression:

```
   t = ( (P − A)ₓ · rₓ + (P − A)_y · r_y ) / ( rₓ² + r_y² )
```

That numerator — multiply matching components and add — is the **dot product**, the cross product's counterpart, and it is what the code below actually computes because it is fewer operations. The linear algebra module derives it properly and explains why it measures alignment rather than area. For now it is enough to know the two routes give the same `t`.

---

## 3. Solving It in Code (Java & WPILib)

### First-Principles Java

```java
import edu.wpi.first.math.geometry.Translation2d;

/** Signed area of the parallelogram spanned by u and v. Sign gives the turn direction. */
static double cross(Translation2d u, Translation2d v) {
    return u.getX() * v.getY() - u.getY() * v.getX();
}

/** Positive if P is left of the directed line A to B, negative if right, zero if on it. */
static double orient(Translation2d a, Translation2d b, Translation2d p) {
    return cross(b.minus(a), p.minus(a));
}

/** True if segment AB properly crosses segment CD. Touching counts as crossing. */
static boolean segmentsCross(Translation2d a, Translation2d b,
                             Translation2d c, Translation2d d) {
    double d1 = orient(a, b, c), d2 = orient(a, b, d);
    double d3 = orient(c, d, a), d4 = orient(c, d, b);
    return d1 * d2 <= 0 && d3 * d4 <= 0;
}

/** Shortest distance from p to the segment ab, handling the past-the-end cases. */
static double distanceToSegment(Translation2d a, Translation2d b, Translation2d p) {
    Translation2d r = b.minus(a);
    double lengthSquared = r.getX() * r.getX() + r.getY() * r.getY();

    if (lengthSquared == 0.0) return p.getDistance(a);   // degenerate: A and B coincide

    // Where along AB the perpendicular from p lands, before clamping.
    double t = (p.minus(a).getX() * r.getX() + p.minus(a).getY() * r.getY()) / lengthSquared;
    t = Math.max(0.0, Math.min(1.0, t));                 // clamp onto the segment

    Translation2d nearest = a.plus(r.times(t));
    return p.getDistance(nearest);
}
```

```java
// Is the planned run from the starting line to the scoring position clear?
Translation2d start = new Translation2d(2.0, 1.0);
Translation2d goal  = new Translation2d(8.0, 6.0);
Translation2d barrierC = new Translation2d(5.0, 0.5);
Translation2d barrierD = new Translation2d(5.0, 7.0);

boolean blocked = segmentsCross(start, goal, barrierC, barrierD);
double clearance = distanceToSegment(barrierC, barrierD, new Translation2d(3.0, 4.0));

System.out.printf("blocked: %b, clearance %.2f m%n", blocked, clearance);
```

### Production WPILib Equivalent

WPILib gives you `Translation2d` for the points and vector arithmetic — `minus`, `plus`, `times`, `getDistance`, `getNorm` — but it has no segment-intersection primitive, because the right answer depends on decisions only your team can make: whether touching counts, what tolerance to use, whether the barrier is a segment or an infinite line. This is a routine that belongs in your own `GeometryUtil` class, written once and unit-tested.

Two habits keep it robust. Build it out of `Translation2d` rather than loose doubles, so the compiler stops you from mixing up an X with a Y. And feed the clearance number into your trajectory constraints rather than into a boolean — "how close" degrades gracefully into slowing down, where "is it blocked" can only stop.

---

## 4. Bridge to Machine Learning & Modern Autonomy

The orientation test from Step 3 is a linear classifier. That is not an analogy; it is the same arithmetic.

A **perceptron**, the ancestor of every neural network in this curriculum, classifies a point by computing `w₁x₁ + w₂x₂ + b` and looking at the sign: positive is one class, negative is the other. Expand `orient(A, B, P)` and you get `(Bₓ − Aₓ)(P_y − A_y) − (B_y − A_y)(Pₓ − Aₓ)`, which regroups into exactly that shape — a weighted sum of `P`'s coordinates plus a constant. The line through `A` and `B` is the perceptron's **decision boundary**, and "which side of the line" is the classification. When the machine learning axon shows a network warping a decision boundary to separate two clusters, it is bending this same object.

The zero case matters there too. Points where the expression equals zero sit exactly on the boundary, and the *distance* to that boundary — computed by the base-times-height argument in Step 6 — is what **support vector machines** maximize. An SVM's entire training objective is "place the line so that the nearest training point is as far from it as possible", which is the clearance calculation applied to data instead of barriers.

On the autonomy side, Step 5 is **ray casting**, the core loop of occupancy-grid mapping and simulated LiDAR. A range sensor is modelled as a ray from the sensor origin, intersected against every wall segment in the map; the smallest positive `t` is the reported distance. Run that a few hundred times per scan and you have synthetic sensor data for testing, or, run in reverse, the visibility check that path planners like RRT and A\* use to decide whether two waypoints can be connected by a straight edge.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1
Path `A = (0, 0)` to `B = (4, 4)`. Barrier `C = (0, 4)` to `D = (4, 0)`. Use orientation tests to decide whether they cross, then find the crossing point.

**Solution:**
1. `r = B − A = (4, 4)` and `s = D − C = (4, −4)`.
2. `orient(A, B, C) = cross((4,4), (0,4)) = 4·4 − 4·0 = +16`.
3. `orient(A, B, D) = cross((4,4), (4,0)) = 4·0 − 4·4 = −16`. Opposite signs ✓
4. By symmetry the other pair also gives `+16` and `−16`. Opposite signs ✓ — so they cross.
5. `cross(r, s) = 4·(−4) − 4·4 = −32`, non-zero, so not parallel.
6. `t = cross(C − A, s) / cross(r, s) = cross((0,4), (4,−4)) / (−32) = (0·(−4) − 4·4)/(−32) = (−16)/(−32) = 0.5`.
7. The crossing is at `P(0.5) = (0,0) + 0.5·(4,4) = (2, 2)` — the centre, as the symmetry of the picture demands.

---

### Checkpoint 2
A teammate's collision check reports that a path from `(1, 1)` to `(2, 2)` is blocked by a barrier from `(8, 0)` to `(8, 5)`, which is metres away. Their code tests only whether the barrier's endpoints fall on opposite sides of the path. What did they get wrong, and what does the missing test contribute?

**Solution:**
They implemented only half of Step 4. The barrier's endpoints `(8, 0)` and `(8, 5)` do sit on opposite sides of the *infinite line* through `(1,1)` and `(2,2)` — that line is `y = x`, and `(8, 0)` is below it while `(8, 5)` is above. The test passes, so they report a collision.

The missing test is the symmetric one: are the path's endpoints on opposite sides of the barrier's line? The barrier's line is the vertical `x = 8`, and both `(1,1)` and `(2,2)` are to the left of it, so `d3` and `d4` share a sign and the second condition fails. Both conditions are required. Without the second, the code is really testing the path against an infinitely long barrier.

---

### Deep Dive 1
Step 4's test treats a grazing touch as a collision, and Step 5 warns that floating-point arithmetic rarely yields exactly `0.0`. Investigate what happens when the two segments are very nearly parallel: compute `cross(r, s)` for segments at 0.01 degrees apart with coordinates of realistic field magnitude, and observe how a tiny denominator inflates the error in `t`. Then work out what tolerance your collision check should use, and argue whether it should be an absolute number of metres or scaled relative to the segment lengths.

### Deep Dive 2
This concept tested a path against barriers one at a time. A real field has dozens, and a match adds moving robots. Research **spatial partitioning** — uniform grids, quadtrees, and bounding-volume hierarchies — and work out how each reduces the number of segment tests from "every barrier, every cycle" to something closer to constant. Then connect this back to Concept 03: why is a cheap bounding-box rejection test the standard first filter before running the exact segment arithmetic derived here?

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_concept_coordinates_distance/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: Coordinates & Distance</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="../03_concept_bounding_boxes/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 03: Bounding Boxes →</a></div>
</div>
