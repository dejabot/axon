# Concept 05: Angle Wrapping & Shortest Angular Distance

> **▶ Interactive Demo: [Shortest Angular Distance & the Swerve Flip](demo.html)**
>
> Drag the current angle and the target angle. Both routes are drawn with their lengths in degrees; switch on the swerve optimization and watch a 165° slew collapse to 15°.

<iframe src="demo.html" width="100%" height="660" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Wheel That Goes the Long Way Round

A steered wheel is sitting at 350°. The path follower wants it at 10° — 20° away, a twitch, three hundredths of a second of steering.

The code computes the error the way code computes every other error:

```
   error = target − current = 10° − 350° = −340°
```

and the module obeys, slewing 340° the wrong way round the circle to reach a direction it was already 20° from.

<div style="text-align: center; margin: 20px 0;">
  <svg width="400" height="290" viewBox="0 0 400 290" style="max-width: 100%; height: auto;" role="img" aria-label="A circle with the wheel's current direction at 350 degrees and its target at 10 degrees. A short 20 degree arc joins them the near way, while a long 340 degree arc drawn inside the circle takes the far way round.">
    <circle cx="180" cy="135" r="90" fill="none" stroke="currentColor" stroke-opacity="0.28" stroke-width="2" />
    <line x1="72" y1="135" x2="288" y2="135" stroke="currentColor" stroke-opacity="0.22" stroke-width="1.5" />
    <line x1="180" y1="27" x2="180" y2="243" stroke="currentColor" stroke-opacity="0.22" stroke-width="1.5" />
    <path d="M 243.0 146.1 A 64 64 0 1 1 243.0 123.9" fill="none" stroke="#f43f5e" stroke-width="3" />
    <polygon points="244.7,133.8 247.4,123.1 238.6,124.7" fill="#f43f5e" />
    <path d="M 268.6 150.6 A 90 90 0 0 0 268.6 119.4" fill="none" stroke="#4ade80" stroke-width="4" />
    <polygon points="266.9,109.6 273.0,118.6 264.2,120.2" fill="#4ade80" />
    <line x1="180" y1="135" x2="268.6" y2="150.6" stroke="#38bdf8" stroke-width="2.5" />
    <circle cx="268.6" cy="150.6" r="5" fill="#38bdf8" />
    <line x1="180" y1="135" x2="268.6" y2="119.4" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="5,4" />
    <circle cx="268.6" cy="119.4" r="5" fill="#fbbf24" />
    <text x="272" y="184" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">now: 350°</text>
    <text x="272" y="98" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">target: 10°</text>
    <text x="278" y="139" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">20°</text>
    <text x="52" y="216" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">what the code commands: −340°</text>
    <circle cx="180" cy="135" r="3.5" fill="currentColor" fill-opacity="0.7" />
    <text x="10" y="266" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">The wheel is 20° from its target. Subtracting the two numbers says 340°.</text>
  </svg>
</div>

The cost is not theoretical. A module slewing at roughly 700°/s covers 20° in about 0.03 s and 340° in about 0.49 s, so it is out of position for nearly half a second — while being asked to *drive* the whole time. A wheel pointed away from the direction it travels does not roll; it is dragged sideways across the carpet. That is **scrub**: heat, tread wear, and a side force the other three modules must fight. The symptom is a visible lurch at the moment the path changes direction — every time the trajectory curves.

Nothing in that subtraction is arithmetically wrong. `10 − 350` really is `−340`. What is wrong is an assumption underneath it that nobody wrote down.

---

## 2. Building the Math

### Step 1: Angles live on a circle, not a line

Concept 01 finished with a small observation: walking right around the rim brings you back to the same point, so `cos(θ + 360°) = cos θ`. That is stronger than it looks. It does not say 350° and 710° *behave similarly*; it says a wheel commanded to 350°, to −10°, or to 710° ends up in **exactly the same orientation**. No measurement — no encoder, no camera, no protractor — can tell those commands apart: they are three names for one direction.

A number line has no such property: there, 350 and −10 are 360 apart, and every value is a distinct place. Subtraction is built for that line — `b − a` answers "how far along the line from a to b", and it is *the* answer because a line offers one route. Feed a circle into a tool built for a line and it answers a question you did not ask. That is the whole bug; everything below is bookkeeping.

> ### Math!
> ```
>    a ≡ b  (mod 360°)     whenever  a − b = 360°·k  for some whole number k
> ```
> Read out loud as **"a is congruent to b, modulo 360 degrees"** — the two numbers name the same direction. So `350° ≡ −10° ≡ 710°`, with `k` counting whole laps between spellings. Congruence is the circle's replacement for equality.

### Step 2: Every honest answer at once

Ask the question the mechanism cares about: **by how much must the wheel rotate to end up pointing at the target?**

If some amount `d` works, so does `d + 360°` — the same rotation with a spare lap thrown in. So does `d − 360°`, and `d + 720°`. From 350° toward 10° the naive subtraction handed us `−340°`, so the full set of rotations landing the wheel on target is

```
   … , −1060° , −700° , −340° , +20° , +380° , +740° , …
```

spaced exactly 360° apart, running forever in both directions. Check two: `350 + 20 = 370 ≡ 10` ✓, and `350 + 380 = 730 = 10 + 720 ≡ 10` ✓.

So the naive difference was never *wrong*: it computed one member of an infinite family and handed it over as the only one. The fix is not to repair the subtraction but to **choose the right member** — the smallest, the least rotating.

### Step 3: Folding the answer into a half-turn band

Two equivalent ways.

**Recipe one — add or subtract 360 until it is in range.** Push the naive difference toward zero a full turn at a time until it lands between −180° and +180°:

```
   d = −340°
   d ≤ −180°, so add 360:  −340 + 360 = +20°
   +20° is in range. Stop.
```

As a loop:

```
   while (d >  180°)  d = d − 360°
   while (d ≤ −180°)  d = d + 360°
```

**Recipe two — one line with a remainder.** The loop subtracts the right multiple of 360 one step at a time; a remainder operator finds it in one. Shift the band to start at zero, take the remainder, shift back:

```
   wrap(d) = ( (d + 180°) mod 360° ) − 180°
```

The `+180°` slides the band `(−180°, 180°]` onto `(0°, 360°]`, `mod 360°` collapses everything into it, and `−180°` slides it back. On our number: `−340 + 180 = −160`; `−160 mod 360 = 200`; `200 − 180 = +20`. Same answer as the loop ✓

Run both on the reverse trip — a wheel at 10° commanded to 350°, naive difference `+340`:

```
   loop:   340 > 180, so 340 − 360 = −20°
   mod:    (340 + 180) mod 360 − 180 = 520 mod 360 − 180 = 160 − 180 = −20°
```

Agreed: **−20°**, 20° in the *negative* direction. The loop makes the mechanism obvious; the remainder version runs in constant time however far out of range the input is — which matters for a gyro that has accumulated eleven laps.

> ### Math!
> ```
>    wrap(d) = ( (d + 180°) mod 360° ) − 180°          in degrees
>    wrap(d) = ( (d + π)    mod 2π   ) − π             in radians
> ```
> Read out loud as **"wrap of d equals d plus 180, mod 360, minus 180."** One warning: **`mod` here is the mathematical modulo, whose result is never negative.** Java's `%` is a *remainder* and keeps the sign of its left operand, so `−160 % 360` is `−160`, not `200`. Written naively, the one-liner silently returns the wrong branch for every negative input. Section 3 fixes it explicitly.

### Step 4: Why the folded answer is always the shortest route

Two arguments, and they are why this is a derivation and not a recipe.

**Exactly one candidate lands in the band.** Step 2's family is a set of numbers spaced exactly 360 apart, and the band `(−180°, +180°]` is exactly 360 wide and half-open — one endpoint in, the other out. Evenly spaced marks laid across a gap one spacing wide, open at one end, cover exactly one mark. So the fold never has a choice to make and never fails.

<div style="text-align: center; margin: 20px 0;">
  <svg width="440" height="150" viewBox="0 0 440 150" style="max-width: 100%; height: auto;" role="img" aria-label="A number line marked with the candidate rotations minus 700, minus 340, plus 20, plus 380 and plus 740, spaced 360 apart. A shaded band from minus 180 to plus 180 contains only the plus 20 candidate.">
    <rect x="169.6" y="52" width="100.8" height="56" fill="#4ade80" fill-opacity="0.13" stroke="#4ade80" stroke-opacity="0.5" stroke-width="1.5" />
    <line x1="14" y1="90" x2="432" y2="90" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <g stroke="#f43f5e" stroke-width="2">
      <line x1="24" y1="82" x2="24" y2="98" />
      <line x1="124.8" y1="82" x2="124.8" y2="98" />
      <line x1="326.4" y1="82" x2="326.4" y2="98" />
      <line x1="427.2" y1="82" x2="427.2" y2="98" />
    </g>
    <g fill="#f43f5e">
      <circle cx="24" cy="90" r="4" /><circle cx="124.8" cy="90" r="4" />
      <circle cx="326.4" cy="90" r="4" /><circle cx="427.2" cy="90" r="4" />
    </g>
    <line x1="225.6" y1="78" x2="225.6" y2="102" stroke="#4ade80" stroke-width="3" />
    <circle cx="225.6" cy="90" r="6" fill="#4ade80" />
    <g fill="#f43f5e" font-family="sans-serif" font-size="10.5" font-weight="bold">
      <text x="6" y="122">−700°</text><text x="106" y="122">−340°</text>
      <text x="310" y="122">+380°</text><text x="408" y="122">+740°</text>
    </g>
    <text x="208" y="122" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">+20°</text>
    <text x="150" y="44" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">−180°</text>
    <text x="252" y="44" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">+180°</text>
    <text x="8" y="140" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">Every candidate points the wheel at 10°. They sit 360° apart, the band is 360° wide, so exactly one is inside.</text>
  </svg>
</div>

**Anything outside the band has a shorter partner.** Take a candidate with magnitude above 180 — say `−340`. Step one place along the family toward zero and you get `+20`. In general, if `|d| > 180°`, its neighbor on the zero side has magnitude `360° − |d|`, which is below 180°. And notice the sum:

```
   |−340°| + |+20°| = 340 + 20 = 360°
```

Not a coincidence: going one way round and going the other together make exactly one lap, always. So the two routes between any pair of directions have lengths summing to 360°, and **the shorter is always the one at or below 180°** — precisely the one the fold keeps.

### Step 5: The cases, including the one with no answer

```
   current   target    naive d      wrapped     what the wheel does
   ------------------------------------------------------------------
    350°       10°      −340°        +20°       20° counter-clockwise
     10°      350°      +340°        −20°       20° clockwise
     90°     −170°      −260°       +100°       100° counter-clockwise
   −170°      170°      +340°        −20°       20° clockwise
    720°       10°      −710°        +10°       10° counter-clockwise
      0°      180°      +180°        ±180°      ambiguous — see below
```

Work the fourth row by hand, the one that bites in autonomous. Naive: `170 − (−170) = +340`. Wrapped: `340 > 180`, so `340 − 360 = −20`. The heading controller turns 20° clockwise, and `−170 − 20 = −190 ≡ 170` ✓. The fifth row shows the fold is not only about signs: a gyro wound to 720° names the same direction as 0°, and the wrap strips the dead laps.

The last row is different in kind. At exactly 180° apart the two routes are `+180°` and `−180°` — the same length. There is no shortest route, because **both are shortest**, and our recipes even disagree: the loop form leaves `+180` alone while the remainder form returns `−180`. Neither is wrong.

What matters is not which sign you get but that a controller never chooses it fresh every cycle. Real headings carry a degree or so of noise; at a 180° target that noise pushes the error across the boundary every few milliseconds, the sign flips, and the mechanism dithers instead of turning. The fix is **hysteresis**: hold the committed direction until the error is well clear of 180°. Do not chase the tie — remove it.

### Step 6: Closing the loop — interpolating an angle

Geometry Concept 03 built linear interpolation, then stopped at a warning: a turret at 350° blending toward 10° with `lerp(350, 10, 0.5)` returns 180°, pointing exactly backwards. It named the cause — an angle lives on a circle — and handed the fix here.

Lerp is `a + t·(b − a)`: start at `a`, travel `t` of the way along the difference. Exactly one thing in it is broken — the `(b − a)`. Wrap that difference first:

```
   lerpAngle(a, b, t) = a + t · wrap(b − a)
```

From 350° to 10°, `wrap(10 − 350) = +20`, so the blend is `350 + 20t`:

```
   t = 0.25   350 + 5  = 355°
   t = 0.50   350 + 10 = 360° ≡ 0°
   t = 0.75   350 + 15 = 365° ≡ 5°
   t = 1.00   350 + 20 = 370° ≡ 10°
```

The turret sweeps 355°, 0°, 5°, 10° — the near way, 20° in all. The naive version gave 265°, 180°, 95°, 10°, dragging the mechanism 340° round the back. Same formula, one wrap.

<div style="text-align: center; margin: 20px 0;">
  <svg width="400" height="220" viewBox="0 0 400 220" style="max-width: 100%; height: auto;" role="img" aria-label="A circle showing a naive interpolation from 350 to 10 degrees passing through 265, 180 and 95 degrees the long way, beside a wrapped interpolation passing through 355, 0 and 5 degrees the short way.">
    <circle cx="150" cy="110" r="80" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="1.5" />
    <path d="M 207.1 120.1 A 58 58 0 1 1 207.1 99.9" fill="none" stroke="#f43f5e" stroke-width="2.5" />
    <g fill="#f43f5e">
      <circle cx="207.1" cy="120.1" r="4" /><circle cx="144.9" cy="167.8" r="4" />
      <circle cx="92.0" cy="110.0" r="4" /><circle cx="144.9" cy="52.2" r="4" />
      <circle cx="207.1" cy="99.9" r="4" />
    </g>
    <g fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="bold">
      <text x="150" y="182">265°</text><text x="62" y="106">180°</text><text x="150" y="48">95°</text>
    </g>
    <path d="M 228.8 123.9 A 80 80 0 0 0 228.8 96.1" fill="none" stroke="#4ade80" stroke-width="4" />
    <g fill="#4ade80">
      <circle cx="228.8" cy="123.9" r="4.5" /><circle cx="229.7" cy="117.0" r="4.5" />
      <circle cx="230.0" cy="110.0" r="4.5" /><circle cx="229.7" cy="103.0" r="4.5" />
      <circle cx="228.8" cy="96.1" r="4.5" />
    </g>
    <text x="242" y="104" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">wrapped: 355°, 0°, 5°</text>
    <text x="242" y="126" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">start 350° → end 10°</text>
    <text x="18" y="200" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">naive lerp(350, 10, t): 265°, 180°, 95°</text>
    <circle cx="150" cy="110" r="3" fill="currentColor" fill-opacity="0.7" />
    <text x="18" y="216" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">Both blends end at 10°. Only one stays near the target the whole way.</text>
  </svg>
</div>

> ### Math!
> ```
>    lerpAngle(a, b, t) = a + t · wrap(b − a)
> ```
> Read out loud as **"a plus t times the wrapped difference from a to b."** Note which of Geometry Concept 03's two spellings survived: the weighted-average form `(1 − t)·a + t·b` has **no** angle version — it averages positions directly and holds no difference to wrap.

### Step 7: The payoff — a steered wheel never turns more than 90°

A steered wheel has two motors: one aims it, one spins it. Its command is a pair — an angle θ and a speed v — which Concept 01 turned into the velocity `(v cos θ, v sin θ)`.

Ask what happens if you aim the wheel at the *opposite* angle and drive it backwards. On the unit circle the point at `θ + 180°` is diametrically opposite the point at θ, so both its coordinates negate:

```
   cos(θ + 180°) = −cos θ            sin(θ + 180°) = −sin θ
```

Feed that in with a negated speed:

```
   (−v)·cos(θ + 180°) = (−v)·(−cos θ) = v cos θ
   (−v)·sin(θ + 180°) = (−v)·(−sin θ) = v sin θ
```

Identical. **Every command has exactly two spellings**: `(θ, v)` and `(θ + 180°, −v)`. So when a command arrives, we get to pick.

Let `e = wrap(θ − current)` and `e′ = wrap(θ + 180° − current)` be the shortest slews to the command and to its twin. If `e` is positive, `e + 180°` lands between 180° and 360°, so the fold subtracts 360: `e′ = e − 180°`. If `e` is negative or zero, `e + 180°` is already in band and `e′ = e + 180°`. Either way:

```
   |e| + |e′| = 180°
```

The two options always split 180°, so flipping wins exactly when the flipped slew is smaller:

```
   180° − |e| < |e|      ⟺      |e| > 90°
```

**That is where 90 comes from.** Not a tuned constant with alternatives worth trying — half of the 180° the two options always share. The consequence is a guarantee: after this check a steered wheel never rotates more than 90° for any command — if the direct route exceeded 90° the flip was shorter, and if it did not, it was already inside the bound.

<div style="text-align: center; margin: 20px 0;">
  <svg width="420" height="250" viewBox="0 0 420 250" style="max-width: 100%; height: auto;" role="img" aria-label="A circle with the wheel currently at 10 degrees, a command at 175 degrees requiring a 165 degree slew, and the flipped command at minus 5 degrees requiring only a 15 degree slew with the drive speed negated.">
    <circle cx="175" cy="125" r="92" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" />
    <line x1="83.4" y1="117.0" x2="266.7" y2="133.0" stroke="#c084fc" stroke-width="2" stroke-dasharray="6,5" />
    <path d="M 265.6 109.0 A 92 92 0 0 0 83.4 117.0" fill="none" stroke="#f43f5e" stroke-width="3" />
    <path d="M 240.0 113.5 A 66 66 0 0 1 240.7 130.8" fill="none" stroke="#4ade80" stroke-width="4" />
    <line x1="175" y1="125" x2="265.6" y2="109.0" stroke="#38bdf8" stroke-width="2.5" />
    <circle cx="265.6" cy="109.0" r="5" fill="#38bdf8" />
    <circle cx="83.4" cy="117.0" r="5" fill="#f43f5e" />
    <circle cx="266.7" cy="133.0" r="5" fill="#4ade80" />
    <text x="272" y="102" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">now: 10°</text>
    <text x="4" y="92" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">commanded</text>
    <text x="4" y="105" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">175°, +3.5 m/s</text>
    <text x="272" y="150" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">flipped: −5°</text>
    <text x="272" y="163" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">−3.5 m/s</text>
    <text x="126" y="26" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">slew 165°</text>
    <text x="192" y="152" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">slew 15°</text>
    <text x="82" y="196" fill="#c084fc" font-family="sans-serif" font-size="10.5" font-weight="bold">one axis, two directions</text>
    <circle cx="175" cy="125" r="3.5" fill="currentColor" fill-opacity="0.7" />
    <text x="8" y="238" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">165° + 15° = 180°. Both settings push the robot in exactly the same direction.</text>
  </svg>
</div>

The figure's numbers, worked. The wheel is at 10°; the command is 175° at 3.5 m/s.

1. **Direct route.** `e = wrap(175 − 10) = +165°`. More than 90°, so flip.
2. **Flipped command.** `wrap(175 + 180) = wrap(355) = −5°`, at `−3.5` m/s.
3. **Flipped route.** `e′ = wrap(−5 − 10) = −15°`. Against the rule: `165 + 15 = 180` ✓
4. **Same push?** Direct gives `(3.5·cos 175°, 3.5·sin 175°) = (−3.487, +0.305)` m/s. Flipped gives `(−3.5·cos(−5°), −3.5·sin(−5°)) = (−3.487, +0.305)` m/s ✓
5. **Cost.** At 700°/s, 165° takes 0.24 s and 15° takes 0.02 s.

Same motion, a tenth of the steering. The flip does reverse the drive motor — but the alternative was swinging the wheel 165° across the carpet while driving, which reverses the robot's push anyway and scrubs the tread doing it.

---

## 3. Solving It in Code (Java & WPILib)

### First Principles (Java)

```java
/**
 * Folds any angle difference into the band (-180, +180].
 *
 * Java's % is a REMAINDER, not a mathematical modulo: it keeps the sign of the
 * left operand, so (-160.0 % 360.0) is -160.0 rather than 200.0. The correction
 * below is what turns it into the modulo the derivation assumed.
 */
static double wrapDegrees(double degrees) {
    double r = (degrees + 180.0) % 360.0;
    if (r <= 0.0) r += 360.0;           // push a non-positive remainder into (0, 360]
    return r - 180.0;
}

/** The same fold written as the loop, for comparison. Identical output. */
static double wrapByLoop(double degrees) {
    double d = degrees;
    while (d > 180.0)   d -= 360.0;
    while (d <= -180.0) d += 360.0;
    return d;
}

/** Shortest rotation that takes `current` onto `target`. */
static double shortestDifference(double targetDeg, double currentDeg) {
    return wrapDegrees(targetDeg - currentDeg);
}

/** Geometry Concept 03's lerp, with the difference wrapped before traveling it. */
static double lerpAngle(double aDeg, double bDeg, double t) {
    return aDeg + t * shortestDifference(bDeg, aDeg);
}
```

```java
System.out.println(shortestDifference(10.0, 350.0));   //  +20.0
System.out.println(shortestDifference(350.0, 10.0));   //  -20.0
System.out.println(shortestDifference(170.0, -170.0)); //  -20.0
System.out.println(shortestDifference(10.0, 720.0));   //  +10.0
System.out.println(wrapByLoop(-340.0));                //  +20.0, agrees

// The turret blend Geometry Concept 03 warned about, now correct.
for (double t : new double[] { 0.25, 0.5, 0.75, 1.0 }) {
    double raw = lerpAngle(350.0, 10.0, t);
    System.out.printf("t=%.2f  %.1f  (= %.1f wrapped)%n", t, raw, wrapDegrees(raw));
}
// t=0.25  355.0  (= -5.0 wrapped)     <- 355 and -5 are the same direction
// t=0.50  360.0  (=  0.0 wrapped)
// t=0.75  365.0  (=  5.0 wrapped)
// t=1.00  370.0  (= 10.0 wrapped)
```

Step 7's flip is six lines once the wrap exists:

```java
record ModuleState(double speedMps, double angleDeg) { }

/** Never steer more than 90 degrees: past that, aim the other way and drive backwards. */
static ModuleState optimize(ModuleState desired, double currentAngleDeg) {
    double error = shortestDifference(desired.angleDeg(), currentAngleDeg);
    if (Math.abs(error) > 90.0) {                    // strictly greater: the 90 tie never flips
        return new ModuleState(-desired.speedMps(),
                               wrapDegrees(desired.angleDeg() + 180.0));
    }
    return desired;
}

ModuleState desired = new ModuleState(3.5, 175.0);
ModuleState best    = optimize(desired, 10.0);
// best.speedMps() = -3.5, best.angleDeg() = -5.0
// slew required:  shortestDifference(-5.0, 10.0) = -15.0  instead of +165.0
```

Comparing with `> 90.0` rather than `>= 90.0` settles Step 5's tie by policy: at exactly 90° both options cost the same, so the choice cannot be wrong, and determinism stops a noisy encoder toggling the drive motor's sign.

### In a Robot Project (Java & WPILib)

WPILib supplies every piece of this, in radians.

```java
import edu.wpi.first.math.MathUtil;
import edu.wpi.first.math.controller.PIDController;
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.math.kinematics.SwerveModuleState;

// 1. The fold itself. angleModulus wraps into (-pi, pi].
double err = MathUtil.angleModulus(Math.toRadians(10.0 - 350.0));   // +0.3491 rad = +20.0 deg

// inputModulus is the same machinery for any period at all — degrees, a
// 0..4095 absolute encoder, hours in a day.
double errDeg = MathUtil.inputModulus(10.0 - 350.0, -180.0, 180.0); // +20.0

// 2. Rotation2d subtraction is ALREADY the wrapped difference. Concept 01 noted
// that a Rotation2d stores (cos, sin) rather than an angle, so it can never leave
// the circle; minus() composes rotations and the result reads back through atan2,
// which lands in (-pi, pi] by construction. Nothing to wrap afterwards.
Rotation2d current = Rotation2d.fromDegrees(350.0);
Rotation2d target  = Rotation2d.fromDegrees(10.0);
double shortest = target.minus(current).getDegrees();               // +20.0

// 3. The 180 flip. Same numbers as the from-scratch version above.
SwerveModuleState desired = new SwerveModuleState(3.5, Rotation2d.fromDegrees(175.0));
desired.optimize(Rotation2d.fromDegrees(10.0));
// desired.speedMetersPerSecond = -3.5
// desired.angle                = -5.0 deg
// Note it returns void and edits the state in place. The static form you will
// see in older code and tutorials, SwerveModuleState.optimize(state, angle),
// returned a new state and is now deprecated in favour of this one.
```

Both tiers return `+20.0` for the heading difference and `(−3.5 m/s, −5.0°)` for the optimized module — the same numbers, derived and imported.

**And the same bug at a different layer.** A heading controller computes `error = setpoint − measurement` internally, on a line, exactly as Section 1 did:

```java
PIDController headingPid = new PIDController(4.0, 0.0, 0.2);

// Without this line, a setpoint of 10 deg with the robot at 350 deg produces an
// error of -340 deg and the robot spins almost all the way round the field.
headingPid.enableContinuousInput(-180.0, 180.0);

double output = headingPid.calculate(350.0, 10.0);   // driven by +20 deg, not -340
```

`enableContinuousInput` tells the controller its input axis is a circle, wrapping the error with `inputModulus` before the P, I and D terms ever see it. Call it on **every** controller fed an angle — including the `ProfiledPIDController` steering a module and a trajectory follower's theta controller — and pass the **same units as your setpoint**, since `enableContinuousInput(-Math.PI, Math.PI)` on a controller fed degrees is worse than not calling it at all.

---

## 4. Bridge to Real Systems

**Swerve module optimization.** `SwerveModuleState.optimize` is Step 7 shipped: called on every module, every 20 ms loop, in essentially every FRC swerve codebase. Its companion is `enableContinuousInput` on the steering and heading controllers — Step 3 shipped. When a team reports that their robot "unwinds" or "takes the long way" after a rotation, the missing line is almost always one of those two.

**Anything living on a circle needs this, and not only angles.** A compass bearing rolls over from 359 to 0, a wave's phase at 2π, clock time at midnight — which is why "how long between 23:30 and 00:15" is not `00:15 − 23:30`. `MathUtil.inputModulus` takes an arbitrary range because the period is not always 360: an absolute encoder reporting 0 to 4095 counts wraps at 4096, and the identical fold applies.

**In machine learning the fix is to refuse the discontinuity entirely.** Give a model one output holding degrees and train it on squared error, and the loss lies at the seam: predicting 359° when the truth is 1° is off by 2°, but the loss reports 358² and shoves the model hard the wrong way. So angles are fed and predicted as a **(cos θ, sin θ) pair** — two outputs, continuous everywhere, no seam for the loss to trip over — with `atan2` from Concept 04 recovering the angle. Rotated-bounding-box detectors do this for object orientation, and tabular models encode hour-of-day the same way so 23:00 and 01:00 sit near each other. Which is exactly what `Rotation2d` does: store the pair, never the number.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1

The robot's heading is −175° and autonomous commands +175°. Find the shortest turn with both recipes, then say what a `PIDController` without `enableContinuousInput` would command.

**Solution:**

1. **Naive difference.** `175 − (−175) = +350°`.
2. **Loop recipe.** `350 > 180`, so `350 − 360 = −10°`.
3. **Remainder recipe.** `(350 + 180) mod 360 − 180 = 530 mod 360 − 180 = 170 − 180 = −10°`. Agrees ✓
4. **Sanity check.** `−175 − 10 = −185 ≡ 175` ✓, and the routes sum to a lap: `350 + 10 = 360` ✓
5. **The answer.** Turn **10° clockwise**. **Without continuous input**, the controller instead sees `+350°` and drives the robot 350° counter-clockwise — 35 times the rotation, in the wrong direction.

---

### Checkpoint 2

A steered wheel sits at 100°. The command is 4.0 m/s at 350°. Optimize it, verify the velocity is unchanged, and state the slew saved.

**Solution:**

1. **Direct route.** `e = wrap(350 − 100) = wrap(250)`. Since `250 > 180`, `250 − 360 = −110°`. `|−110| > 90`, so flipping wins.
3. **Flipped command.** `wrap(350 + 180) = wrap(530) = 530 − 360 = 170°`, at `−4.0` m/s.
4. **Flipped route.** `e′ = wrap(170 − 100) = +70°`. Check the split: `110 + 70 = 180` ✓
5. **Same velocity?** Original: `(4.0·cos 350°, 4.0·sin 350°) = (3.939, −0.695)` m/s. Optimized: `(−4.0·cos 170°, −4.0·sin 170°) = (3.939, −0.695)` m/s ✓
6. **Saving.** 70° of slew instead of 110° — at 700°/s, 0.10 s instead of 0.16 s.

---

### Deep Dive 1

Wrapping assumes the mechanism can keep turning, and plenty cannot: a turret fed by a wire harness may have hard stops at ±270°, so the shortest *angular* route sometimes snaps a cable. Given a current angle, a target and a pair of hard stops, decide between the wrapped route and its 360°-longer partner, and describe where on the circle the wrapped answer must be rejected. Then handle a target unreachable without first unwinding.

### Deep Dive 2

Step 5 claimed a target 180° away makes a controller dither. Test it. Simulate a heading error sitting at 180° with ±0.5° of noise, wrap it for 1,000 cycles, and count the sign changes. Then add hysteresis — hold the previous direction until the error drops below some threshold — and find the smallest threshold that stops the flipping. Repeat for the 90° tie in the module flip, where a wrong choice reverses a drive motor, and decide whether the two thresholds should match.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../04_concept_atan2_heading/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 04: 4-Quadrant atan2</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../06_concept_law_of_cosines/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 06: Law of Cosines →</a></div>
</div>
