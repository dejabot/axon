# Concept 03: Linear Interpolation, Lookup Tables & Blending

> **▶ Interactive Demo: [Interpolation, Lookup Tables & the Angle Trap](demo.html)**
>
> Sweep `t` and watch the two lerp formulas disagree in their last digits, drag a shooter calibration table, and see a naive angle blend take the long way round.

<iframe src="demo.html" width="100%" height="620" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Shooter You Only Measured Five Times

Your team spends a Saturday calibrating the shooter: park at a measured distance, sweep the flywheel speed until the game piece goes in reliably, write it down, move back. By the end of the day you have five rows in a notebook:

```
   distance (m)    flywheel (RPM)
   2.0             2450
   3.0             2980
   4.5             3610
   6.0             4100
   7.5             4390
```

Then the match starts, the driver stops at 5.0 metres, and the code must produce a number. There is no row for 5.0 metres, and there never will be — the five you have took hours.

<div style="text-align: center; margin: 20px 0;">
  <svg width="420" height="210" viewBox="0 0 420 210" style="max-width: 100%; height: auto;" role="img" aria-label="A robot at an unmeasured distance from the goal, between two calibrated distances.">
    <line x1="20" y1="165" x2="405" y2="165" stroke="currentColor" stroke-opacity="0.25" stroke-width="1.5" />
    <rect x="378" y="45" width="14" height="120" fill="none" stroke="#f43f5e" stroke-width="3" />
    <text x="336" y="38" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">goal</text>
    <g stroke="currentColor" stroke-opacity="0.45" stroke-width="1.5">
      <line x1="60" y1="160" x2="60" y2="176" />
      <line x1="140" y1="160" x2="140" y2="176" />
      <line x1="255" y1="160" x2="255" y2="176" />
      <line x1="330" y1="160" x2="330" y2="176" />
    </g>
    <g fill="#38bdf8">
      <circle cx="60" cy="165" r="5" /><circle cx="140" cy="165" r="5" />
      <circle cx="255" cy="165" r="5" /><circle cx="330" cy="165" r="5" />
    </g>
    <g fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">
      <text x="46" y="192">2.0 m</text><text x="126" y="192">3.0 m</text>
      <text x="241" y="192">4.5 m</text><text x="316" y="192">6.0 m</text>
    </g>
    <g fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="bold">
      <text x="40" y="152">2450</text><text x="120" y="152">2980</text>
      <text x="235" y="152">3610</text><text x="310" y="152">4100</text>
    </g>
    <rect x="272" y="128" width="34" height="30" fill="none" stroke="#fbbf24" stroke-width="2.5" rx="3" />
    <text x="262" y="120" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">5.0 m — ?</text>
    <line x1="289" y1="160" x2="289" y2="176" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3" />
  </svg>
</div>

The gap between the rows is where the robot actually lives. Filling it takes one short formula you have already derived — plus one numerical trap.

---

## 2. Building the Math

### Step 1: You already built this, unnamed

Concept 02 described a line as a walk:

```
   P(t) = A + t · (B − A)
```

read out loud as "the point you reach after travelling `t` of the way from A toward B." That sentence *is* the definition of **linear interpolation** — you have been using it for a whole concept without the word.

Nothing in the formula cares that `A` and `B` are points; subtract, scale and add work just as well on plain numbers. So drop the geometry:

```
   lerp(a, b, t) = a + t · (b − a)
```

Now `a` and `b` can be flywheel speeds, voltages or brightness values, and `t` is the blend fraction: 0 gives `a`, 1 gives `b`, 0.5 gives the average.

> ### Math!
> ```
>    lerp(a, b, t) = a + t·(b − a),    t ∈ [0, 1]
> ```
> Read as **"lerp of a, b, t equals a plus t times the quantity b minus a."** Programmers pronounce `lerp` to rhyme with "burp". *Interpolation* is Latin for polishing between: inventing a value between two you know.

### Step 2: The same formula, written two ways

Multiply the definition out:

```
   a + t·b − t·a  =  (1 − t)·a + t·b
```

Algebraically identical. Read aloud, though, the second says something new: **take `(1 − t)` of `a` and `t` of `b`, and add them** — a weighted average whose weights always sum to 1. That is the reading you meet in graphics and machine learning, where 30% opacity is weights 0.7 and 0.3.

Use whichever spelling reads more clearly for what you are doing. There is one caution to carry away, though: identical on paper is not identical once a computer rounds them.

A `double` rounds after every operation, and these two forms round in different places. The practical consequence is that the first form can land a hair short of `b` when `t = 1` — off by about `0.0000000000000004` — so a check like `if (position == target)` may never fire.

The habit that fixes it is worth having anyway, for any floating-point comparison:

```java
   // Never test floating-point values for exact equality.
   if (Math.abs(position - target) < 0.01) { /* close enough */ }
```

That is all you need to use interpolation safely. Deep Dive 1 chases the full story, which is genuinely interesting: each form has one guarantee the other lacks, and that is why C++ gives `std::lerp` its own carefully specified implementation instead of just picking one.

### Step 3: Running it backwards

Constantly you need the reverse: given a value, what fraction of the way along is it? Solve the definition for `t`:

```
   v = a + t·(b − a)
   v − a = t·(b − a)
   t = (v − a) / (b − a)
```

That is **inverse lerp**, better known as normalization. A sensor reading 3.1 V across a 0.2–4.8 V range sits `(3.1 − 0.2) / (4.8 − 0.2) = 0.630` of the way along; feed that `t` into a `lerp` over a different range and you have **remapped** it onto metres: `lerp(0.3, 5.0, 0.630) = 3.263 m`. The denominator is the only failure mode — if `a = b` there is no answer, so guard it rather than let a `NaN` escape into a control loop.

> ### Math!
> ```
>    invLerp(a, b, v) = (v − a) / (b − a),    a ≠ b
> ```
> Read as **"inverse lerp of a, b, v equals v minus a, over b minus a."** Statistics calls it **min-max normalization**; graphics calls it `unlerp`. The two undo each other: `invLerp(a, b, lerp(a, b, t)) = t`.

### Step 4: Interpolating lookup tables, and the dangerous edge

A table with more than two rows is lerp applied to the right pair:

1. **Find the bracketing pair** — the adjacent rows whose keys satisfy `key[i] ≤ query ≤ key[i+1]`.
2. **Inverse-lerp the keys**: `t = (query − key[i]) / (key[i+1] − key[i])`.
3. **Lerp the values** with that same `t`.

At 5.0 m the bracket is (4.5, 3610) and (6.0, 4100), so `t = 0.5 / 1.5 = 0.3333` and the answer is `3610 + 0.3333 × 490 = 3773.3 RPM`. Five measurements have become a continuous function.

**The table must be sorted by key.** The bracketing step assumes a query falling between two adjacent keys makes that pair *the* bracket — true only if keys increase monotonically. Unsorted, several non-adjacent pairs could straddle the query and binary search returns an arbitrary row. That is why WPILib's interpolating table is a **tree map**: sorted order is a structural invariant, so the table cannot enter an invalid state.

<div style="text-align: center; margin: 20px 0;">
  <svg width="420" height="220" viewBox="0 0 420 220" style="max-width: 100%; height: auto;" role="img" aria-label="A calibration curve with a clamped flat continuation and an extrapolated rising continuation past the last measured point.">
    <line x1="45" y1="185" x2="405" y2="185" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <line x1="45" y1="185" x2="45" y2="20" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <text x="330" y="207" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">distance</text>
    <text x="14" y="30" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">RPM</text>
    <polyline points="70,158 120,130 195,97 270,71 305,56" fill="none" stroke="#38bdf8" stroke-width="3" />
    <g fill="#38bdf8">
      <circle cx="70" cy="158" r="5" /><circle cx="120" cy="130" r="5" /><circle cx="195" cy="97" r="5" />
      <circle cx="270" cy="71" r="5" /><circle cx="305" cy="56" r="5" />
    </g>
    <line x1="305" y1="56" x2="395" y2="56" stroke="#4ade80" stroke-width="3" stroke-dasharray="6,4" />
    <text x="316" y="48" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">clamped</text>
    <line x1="305" y1="56" x2="395" y2="20" stroke="#f43f5e" stroke-width="3" stroke-dasharray="6,4" />
    <text x="286" y="16" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">extrapolated — untested</text>
    <line x1="305" y1="20" x2="305" y2="185" stroke="currentColor" stroke-opacity="0.25" stroke-width="1.5" stroke-dasharray="4,4" />
    <text x="228" y="200" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">last measurement</text>
  </svg>
</div>

Nothing stops `t` from leaving `[0, 1]`. Query at 9.0 m and the last two rows give `t = 3.0 / 1.5 = 2.0`, so **extrapolation** cheerfully returns `4100 + 2.0 × 290 = 4680 RPM` — a speed your flywheel has never spun at, whose current draw and balance nobody checked. The safe default for a calibration table is to **clamp** `t` into `[0, 1]` first, so an out-of-range query returns the last *measured* value rather than an invented one, and to log loudly when it happens.

### Step 5: Two loose ends

**Two inputs at once.** When the table is indexed by two variables — an image, indexed by row and column, is exactly this — lerp along one axis twice, then lerp between those two results. That is **bilinear interpolation**: four corner values blended by weights that multiply an x-weight by a y-weight. Every image resize does it.

**Angles are not numbers on a line.** A turret at 350° blending toward 10° gives `lerp(350, 10, 0.5) = 180°` — pointing exactly backwards, sweeping 340° the wrong way to reach a target 20° away. The bug is not in `lerp`; it is that an angle lives on a circle, where 350 and 10 are adjacent though the numerals differ by 340. The fix is angle wrapping from **Module 2 (Trigonometry & Angles)**, generalised to 3D as **SLERP** in its quaternion concept. Until then: never lerp a raw angle.

---

## 3. Solving It in Code (Java & WPILib)

### First-Principles Java

```java
/** Weighted-average form: exact at both endpoints. */
static double lerp(double a, double b, double t) {
    return (1.0 - t) * a + t * b;
}

/** Where v sits between a and b, as a fraction. Zero-width ranges have no answer. */
static double inverseLerp(double a, double b, double v) {
    if (Math.abs(b - a) < 1e-12) {
        throw new IllegalArgumentException("inverseLerp on a zero-width range");
    }
    return (v - a) / (b - a);
}

static double clamp(double v, double lo, double hi) {
    return Math.max(lo, Math.min(hi, v));
}

/** A sorted calibration table. Keys must be strictly increasing. */
class InterpolatingTable {
    private final double[] keys;      // distances in metres
    private final double[] values;    // flywheel RPM

    InterpolatingTable(double[] keys, double[] values) {
        for (int i = 1; i < keys.length; i++) {
            if (keys[i] <= keys[i - 1]) {
                throw new IllegalArgumentException("table keys must strictly increase");
            }
        }
        this.keys = keys;
        this.values = values;
    }

    double get(double query) {
        // Clamp: a query outside the calibrated range returns the nearest measurement,
        // never an extrapolated command the mechanism has not been tested at.
        int last = keys.length - 1;
        if (query <= keys[0]) return values[0];
        if (query >= keys[last]) return values[last];

        // Binary search for the bracketing pair: keys[lo] <= query <= keys[lo + 1].
        int lo = 0, hi = last;
        while (hi - lo > 1) {
            int mid = (lo + hi) / 2;
            if (keys[mid] <= query) lo = mid; else hi = mid;
        }
        return lerp(values[lo], values[lo + 1], inverseLerp(keys[lo], keys[lo + 1], query));
    }
}
```

```java
double[] distances = { 2.0, 3.0, 4.5, 6.0, 7.5 };
double[] rpms      = { 2450, 2980, 3610, 4100, 4390 };
InterpolatingTable shooter = new InterpolatingTable(distances, rpms);

System.out.printf("5.0 m -> %.1f RPM%n", shooter.get(5.0));   // 3773.3
System.out.printf("9.0 m -> %.1f RPM%n", shooter.get(9.0));   // 4390.0, clamped
```

### Production WPILib Equivalent

`MathUtil.interpolate(startValue, endValue, t)` is lerp with `t` clamped to `[0, 1]`, `MathUtil.inverseInterpolate` is the reverse, `MathUtil.clamp` is the clamp. WPILib writes `interpolate` in the `a + t·(b − a)` form, so it inherits Step 2's endpoint wobble.

```java
import edu.wpi.first.math.MathUtil;
import edu.wpi.first.math.interpolation.InterpolatingDoubleTreeMap;
import edu.wpi.first.math.geometry.Translation2d;

InterpolatingDoubleTreeMap shooterTable = new InterpolatingDoubleTreeMap();
shooterTable.put(2.0, 2450.0);
shooterTable.put(3.0, 2980.0);
shooterTable.put(4.5, 3610.0);
shooterTable.put(6.0, 4100.0);
shooterTable.put(7.5, 4390.0);

double rpm   = shooterTable.get(5.0);                         // ≈ 3773.3
double volts = MathUtil.interpolate(0.0, 12.0, 0.25);         // 3.0
double frac  = MathUtil.inverseInterpolate(0.2, 4.8, 3.1);    // ≈ 0.630
double safeT = MathUtil.clamp(1.8, 0.0, 1.0);                 // 1.0

// Geometry interpolates too: Translation2d blends its X and Y independently.
Translation2d mid = new Translation2d(2.0, 1.0)
        .interpolate(new Translation2d(8.0, 6.0), 0.5);       // (5.0, 3.5)
```

Insert the rows in any order — the tree map sorts them, which is the whole point. Two cautions: confirm against your WPILib version that the map clamps rather than extrapolates, and remember that any `interpolate` touching a heading meets Step 5's angle trap.

---

## 4. Bridge to Machine Learning & Modern Autonomy

Bilinear interpolation is what made per-pixel object detection accurate. **Mask R-CNN** must pull a fixed-size feature patch out of a region proposal whose coordinates are arbitrary real numbers. Its predecessor, RoI pooling, rounded those coordinates onto integer feature-map cells, twice. On a feature map downsampled by 32, a half-cell rounding error is 16 pixels of misalignment in the original image: invisible for a bounding box, catastrophic for a mask. **RoIAlign** deletes both roundings by sampling at the exact fractional coordinates and blending the four neighbouring feature cells bilinearly — Step 5's formula on learned features instead of colours — and bought a large relative gain in mask accuracy at the strictest threshold. That blend is also differentiable in its sampling coordinates, so gradients flow back through the sampling itself, which is what makes **Spatial Transformer Networks** possible. Even PyTorch's much-cursed `align_corners` flag is only a Step 3 question: does the inverse lerp map pixel *centres* or *edges*?

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1
Using the table from Section 1, find the commanded RPM at 3.6 m, then what 9.0 m returns clamped and extrapolated, and say which you would ship.

**Solution:**
1. **Bracket.** 3.6 lies between keys 3.0 and 4.5: the pair is (3.0, 2980) and (4.5, 3610).
2. **Inverse-lerp the keys.** `t = (3.6 − 3.0) / (4.5 − 3.0) = 0.6 / 1.5 = 0.4`.
3. **Lerp the values.** `0.6 × 2980 + 0.4 × 3610 = 1788 + 1444 = 3232 RPM`. Cross-check with the other form: `2980 + 0.4 × 630 = 3232`. ✓
4. **9.0 m.** Clamped, `t` becomes 1 and the table returns the last measurement, **4390 RPM**. Extrapolated from (6.0, 4100) and (7.5, 4390), `t = 3.0 / 1.5 = 2.0` gives `4100 + 2.0 × 290 = 4680 RPM`.
5. **Ship the clamped version.** 4390 is a speed the mechanism has run at; 4680 is not. The clamped shot falls short — a visible, recoverable miss. The extrapolated one commands untested hardware.

---

### Checkpoint 2
A swerve azimuth is at 350°, the target is 10°, and someone calls `lerp(350, 10, t)` in the smoothing code. Compute the command at `t = 0.25`, `0.5` and `0.75`, compare with the short-way answers, and name the assumption that failed.

**Solution:**

Naive, `350 + t × (10 − 350) = 350 − 340t`:

```
   t = 0.25   350 − 85  = 265°
   t = 0.50   350 − 170 = 180°
   t = 0.75   350 − 255 = 95°
```

The short way covers `+20°` in total, going 350 → 360/0 → 10: 355°, 0°, 5°. The naive version drags the wheel across the carpet nearly a full turn to reach a target 20° away. The failed assumption is that **the shortest route between two values is the difference of the numbers** — true on a line, false on a circle. Module 2 folds that difference into `[−180°, 180°]` first.

---

### Deep Dive 1
Write a Java `lerp` guaranteeing both endpoint exactness and monotonicity, as `std::lerp` does and neither simple form does. Test both forms over millions of random `(a, b, t)` triples, counting three failures: `result != b` at `t = 1`; a result outside the interval spanned by `a` and `b`; and a result that *decreases* when `t` is nudged up one step with `Math.nextUp`. Then work out why a correct implementation must branch on whether `a` and `b` share a sign.

### Deep Dive 2
A piecewise-linear table cuts a straight chord across whatever curve the physics follows, with the worst error in the middle of the widest gap. Sample a smooth function at 3, 5 and 9 points and measure the maximum interpolation error. How does it shrink as you double the samples, and where should the points go if you are allowed only nine?

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../02_concept_lines_intersections/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 02: Lines & Intersections</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="../04_concept_bounding_boxes/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 04: Bounding Boxes →</a></div>
</div>
