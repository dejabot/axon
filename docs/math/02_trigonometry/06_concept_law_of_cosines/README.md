# Concept 06: Law of Sines, Law of Cosines & Two-Link Arms

> **▶ Interactive Demo: [Two-Link Arm Inverse Kinematics Explorer](demo.html)**
>
> Drag the target. Both elbow-up and elbow-down solutions redraw live, and dragging outside the reachable ring clamps to the rim rather than breaking.

<iframe src="demo.html" width="100%" height="640" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: An Arm With Two Joints

Bolt a 0.90 m segment to a motor on the robot's frame — the **shoulder**. On its far end bolt a second motor and a 0.60 m segment — the **elbow** — with a gripper on the end. Both segments are rigid steel: only the joint angles change.

<div style="text-align: center; margin: 20px 0;">
  <svg width="400" height="270" viewBox="0 0 400 262" style="max-width: 100%; height: auto;" role="img" aria-label="A two-segment arm mounted on a robot chassis. A 0.90 meter shoulder segment rises to an elbow, and a 0.60 meter segment reaches from there to a gripper at the target point, with both joint angles marked unknown.">
    <rect x="20" y="230" width="130" height="24" rx="4" fill="currentColor" fill-opacity="0.1" stroke="currentColor" stroke-opacity="0.45" stroke-width="1.5" />
    <circle cx="48" cy="256" r="6" fill="none" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <circle cx="122" cy="256" r="6" fill="none" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <text x="26" y="246" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">chassis</text>
    <line x1="60" y1="230" x2="60" y2="70" stroke="currentColor" stroke-opacity="0.18" stroke-width="1.5" stroke-dasharray="4,4" />
    <line x1="60" y1="230" x2="330" y2="230" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <line x1="60" y1="230" x2="196" y2="128" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.5" stroke-dasharray="6,4" />
    <text x="118" y="196" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">r = shoulder to target</text>
    <line x1="60" y1="230" x2="104.21" y2="83.53" stroke="#38bdf8" stroke-width="6" stroke-linecap="round" />
    <line x1="104.21" y1="83.53" x2="196" y2="128" stroke="#4ade80" stroke-width="6" stroke-linecap="round" />
    <text x="20" y="150" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">L1 = 0.90 m</text>
    <text x="130" y="80" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">L2 = 0.60 m</text>
    <circle cx="60" cy="230" r="7" fill="#fbbf24" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.5" />
    <circle cx="104.21" cy="83.53" r="7" fill="#fbbf24" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.5" />
    <circle cx="196" cy="128" r="6" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" />
    <text x="14" y="224" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">shoulder</text>
    <text x="70" y="66" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">elbow</text>
    <text x="204" y="126" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">target (0.80, 0.60)</text>
    <path d="M 96 230 A 36 36 0 0 0 70.4 195.6" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="98" y="220" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">θ1 = ?</text>
    <line x1="104.21" y1="83.53" x2="117.21" y2="40.45" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" stroke-dasharray="4,4" />
    <path d="M 115.77 45.24 A 40 40 0 0 1 140.21 100.97" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="146" y="62" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">θ2 = ?</text>
    <text x="220" y="248" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">Lengths fixed. Angles free.</text>
  </svg>
</div>

**Forward:** given the joint angles, where does the gripper end up? Concept 01 answers this. The shoulder segment ends one link out at angle θ1, and the elbow segment leaves that point at the combined angle θ1 + θ2 — two right triangles end to end:

```
   elbow.x   = L1 cos θ1                       elbow.y   = L1 sin θ1
   gripper.x = elbow.x + L2 cos(θ1 + θ2)       gripper.y = elbow.y + L2 sin(θ1 + θ2)
```

**Inverse:** the driver wants the gripper at a specific point, say 0.80 m out and 0.60 m up. What must the joint angles be? *That* has no answer yet, and is what this concept is for.

Shoulder, elbow and target form a triangle with sides 0.90, 0.60 and the straight-line distance `r` — and **there is no right angle in it**. Every tool in this module so far assumes a right triangle or an angle at the origin. A general triangle needs a general tool.

---

## 2. Building the Math: Generalizing Pythagoras

### Step 1: What a right angle was buying us

Geometry Concept 01 proved `a² + b² = c²` by area rearrangement — four copies of a right triangle packed into a square of side `a + b`, its area counted two ways. That proof stands and this concept does not repeat it. But notice what it needed: the legs meeting at *exactly* 90°. Open that corner and the far side stretches, close it and it shrinks, and `a² + b² = c²` says nothing about how wrong it now is.

So: **if the angle between two sides is not 90°, what replaces `a² + b² = c²`?**

### Step 2: Cutting the triangle into two right triangles

We know how to handle right triangles, so make right triangles: **drop a perpendicular from one vertex onto the opposite side.**

Name the triangle first: vertices A, B, C, each side named for the vertex it does *not* touch, so `a` is opposite A. We want `c`, opposite C.

Put C at the origin with side `b` along the positive X-axis, so A sits at `(b, 0)`. B is a distance `a` away in the direction of the angle at C, which by the unit-circle definition puts it at `(a cos C, a sin C)`, and the perpendicular from B has its foot at `(a cos C, 0)`.

<div style="text-align: center; margin: 20px 0;">
  <svg width="400" height="310" viewBox="0 0 300 232" style="max-width: 100%; height: auto;" role="img" aria-label="A triangle with vertices C at the origin, A on the positive x-axis and B above, with a perpendicular dropped from B to the x-axis splitting the base into a segment of length a cosine C and a segment of length b minus a cosine C.">
    <line x1="50" y1="200" x2="113.39" y2="64.05" stroke="#38bdf8" stroke-width="3" />
    <line x1="50" y1="200" x2="260" y2="200" stroke="currentColor" stroke-opacity="0.55" stroke-width="3" />
    <line x1="113.39" y1="64.05" x2="260" y2="200" stroke="#f43f5e" stroke-width="3" />
    <line x1="113.39" y1="64.05" x2="113.39" y2="200" stroke="#4ade80" stroke-width="2.5" stroke-dasharray="5,4" />
    <rect x="102.39" y="189" width="11" height="11" fill="none" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.5" />
    <path d="M 86 200 A 36 36 0 0 0 65.22 167.37" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="88" y="190" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">C</text>
    <circle cx="50" cy="200" r="4" fill="currentColor" fill-opacity="0.75" />
    <circle cx="260" cy="200" r="4" fill="currentColor" fill-opacity="0.75" />
    <circle cx="113.39" cy="64.05" r="4" fill="currentColor" fill-opacity="0.75" />
    <text x="34" y="216" fill="currentColor" fill-opacity="0.75" font-family="sans-serif" font-size="12" font-weight="bold">C</text>
    <text x="264" y="196" fill="currentColor" fill-opacity="0.75" font-family="sans-serif" font-size="12" font-weight="bold">A</text>
    <text x="108" y="54" fill="currentColor" fill-opacity="0.75" font-family="sans-serif" font-size="12" font-weight="bold">B</text>
    <text x="58" y="126" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">a</text>
    <text x="196" y="120" fill="#f43f5e" font-family="sans-serif" font-size="12" font-weight="bold">c</text>
    <text x="238" y="192" fill="currentColor" fill-opacity="0.7" font-family="sans-serif" font-size="12" font-weight="bold">b</text>
    <text x="120" y="136" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">a sin C</text>
    <text x="46" y="217" fill="#c084fc" font-family="sans-serif" font-size="10">a cos C</text>
    <text x="140" y="217" fill="#c084fc" font-family="sans-serif" font-size="10">b − a cos C</text>
    <line x1="50" y1="207" x2="113.39" y2="207" stroke="#c084fc" stroke-opacity="0.7" stroke-width="1.5" />
    <line x1="113.39" y1="207" x2="260" y2="207" stroke="#c084fc" stroke-opacity="0.7" stroke-width="1.5" />
    <text x="8" y="228" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">Drawn true to scale for a = 5, b = 7, C = 65°, giving c = 6.665.</text>
  </svg>
</div>

Look at the right-hand triangle. Its hypotenuse is the side `c` we want, and its legs are readable off the coordinates:

```
   vertical leg    =  a sin C
   horizontal leg  =  b − a cos C
```

### Step 3: The algebra

Apply Pythagoras and expand:

```
   c²  =  (b − a cos C)²  +  (a sin C)²

       =  b² − 2ab cos C + a² cos²C  +  a² sin²C

       =  b² − 2ab cos C + a² (cos²C + sin²C)
```

The last bracket is Concept 01's Pythagorean identity, worth exactly 1:

```
   c²  =  a² + b² − 2ab cos C
```

That is the **law of cosines**, and nothing entered it but Pythagoras, the unit-circle definitions of sine and cosine, and `sin² + cos² = 1`.

One objection: if C is obtuse the foot falls *outside* segment CA. But beyond 90° the cosine is negative, so `b − a cos C` comes out *larger* than `b` — exactly right for a foot on the far side. We never asked whether `cos C` was positive, so we owe no second case.

> ### Math!
> ```
>    c² = a² + b² − 2ab·cos C
> ```
> Read out loud as **"c squared equals a squared plus b squared, minus two a b cosine C."** `C` is the angle *between* sides `a` and `b`. The pairing is rigid: the side on the left and the angle inside the cosine must be **opposite each other**. Every other version is this one relabeled, so `a² = b² + c² − 2bc·cos A` needs no separate proof.

### Step 4: Pythagoras is the special case

Set `C = 90°`. On the unit circle the point at 90° is `(0, 1)`, so `cos 90° = 0` exactly and the third term disappears:

```
   c² = a² + b² − 2ab·(0) = a² + b²
```

Pythagoras, recovered without a scratch. That is the point of this concept: **the law of cosines is not a different theorem, it is Pythagoras plus a correction for the corner not being square.** Read `−2ab cos C` as the correction:

* **Under 90°** — corner pinched shut, cosine positive, the term subtracts, and `c` comes out **shorter** than Pythagoras predicts.
* **Exactly 90°** — no correction.
* **Over 90°** — corner levered open, cosine negative, subtracting a negative *adds*, and `c` comes out **longer**.

Check it on the arm. A square elbow would place the gripper at

```
   √(0.90² + 0.60²) = √1.17 = 1.0817 m
```

Our target sits at `r = 1.0000` m — closer, so the elbow must be pinched tighter than 90°. Step 6 says by how much.

### Step 5: The law of sines, and the one job it does

The law of cosines wants three sides, or two sides and the angle between them. Sometimes you hold instead **an angle and the side across from it**. Drop a perpendicular `h` from vertex C onto side `c`. It is a leg of two right triangles at once: in the one containing A the hypotenuse is `b`, so `h = b sin A`; in the one containing B it is `a`, so `h = a sin B`. Same segment, so:

```
   b sin A = a sin B      →      a / sin A  =  b / sin B
```

Repeat from another vertex and the third ratio joins:

> ### Math!
> ```
>    a / sin A  =  b / sin B  =  c / sin C
> ```
> Read out loud as **"a over sine A equals b over sine B equals c over sine C."** Each side divided by the sine of the angle opposite it gives the same number for all three pairs — on the arm's triangle in Step 6, 1.0126 every time.

Here is what it buys. Two cameras 2.00 m apart both see the same game piece: the left measures 70° between the baseline and its line of sight, the right 50°. Angles sum to 180°, so the angle at the piece is 60°, and the range from the left camera — the side opposite the 50° vertex — falls straight out:

```
   range = 2.00 × sin 50° / sin 60° = 2.00 × 0.76604 / 0.86603 = 1.769 m
```

Two bearings and a baseline give a position: **triangulation**, and why the law of sines exists.

It has one trap. Given two sides and an angle *not* between them, `sin B = b sin A / a` has two valid answers, because sine is positive on both sides of 90° — `sin 40° = sin 140°`. That **ambiguous case** is why the rest of this concept uses the law of cosines: cosine is one-to-one across `0°` to `180°`, positive below 90° and negative above, so an angle recovered from a cosine is unique.

### Step 6: Solving the arm — the elbow angle

The triangle is shoulder, elbow, target, with sides `L1 = 0.90`, `L2 = 0.60` and `r = √(0.80² + 0.60²) = 1.0000` m. The interior angle at the elbow — call it `φ` — sits between the two known sides, with `r` opposite. Exactly the law of cosines' shape:

```
   r² = L1² + L2² − 2·L1·L2·cos φ
```

Everything but `φ` is known, so rearrange for the cosine:

```
   cos φ = (L1² + L2² − r²) / (2·L1·L2)
         = (0.81 + 0.36 − 1.00) / (2 × 0.90 × 0.60)
         = 0.17 / 1.08
         = 0.15741

   φ = arccos(0.15741) = 80.94°
```

Under 90°, as Step 4 predicted. But `φ` is the triangle's *interior* angle, not the number a motor wants. An elbow motor is zeroed with the arm straight out, so `θ2` measures the bend away from straight, and straight means an interior angle of 180°:

```
   θ2 = 180° − φ = 180° − 80.94° = 99.06°
```

### Step 7: The shoulder angle, in two pieces

The shoulder angle splits into a direction and a lift. The **direction** is `β = atan2(0.60, 0.80) = 36.87°`, Concept 04's four-quadrant heading, which keeps this correct when the target is behind or below the shoulder. The **lift** is the triangle's interior angle at the shoulder, `α`, between the first link and the line to the target. It sits opposite `L2`, so law of cosines again:

```
   cos α = (L1² + r² − L2²) / (2·L1·r)
         = (0.81 + 1.00 − 0.36) / (2 × 0.90 × 1.00)
         = 1.45 / 1.80
         = 0.80556

   α = arccos(0.80556) = 36.34°
```

Sanity check: `80.94° + 36.34° + 62.72° = 180.00°`, the third angle from a third use of the same formula — the triangle closes. So one solution is `θ1 = β + α = 73.21°` with `θ2 = −99.06°`. Through Section 1's forward equations:

```
   elbow   = (0.90 cos θ1, 0.90 sin θ1)                = (0.2600, 0.8616)
   gripper = elbow + (0.60 cos(θ1 + θ2), 0.60 sin(θ1 + θ2)) = (0.8000, 0.6000)
```

The gripper lands on the target. (Degrees are rounded; at full precision it closes exactly.) The inverse problem is solved — except that the sign on `θ2` was never forced, which is Step 9.

### Step 8: Reachability, and why the failure is a NaN

Read the elbow formula as software. A cosine can never leave `−1 … +1`, but `r` is a driver's choice. Push it to each limit:

```
   cos φ = −1  →  φ = 180°, links straight  →  r² = (L1 + L2)²  →  r = 1.50 m
   cos φ = +1  →  φ =   0°, links folded    →  r² = (L1 − L2)²  →  r = 0.30 m
```

Nothing farther than the first is reachable, and nothing nearer than the second, because the forearm cannot retract past the shoulder segment. The reachable set is an **annulus** — outer radius `L1 + L2`, dead hole of radius `|L1 − L2|` that equal links would close. Those are the **triangle inequality**, so algebra and geometry agree.

<div style="text-align: center; margin: 20px 0;">
  <svg width="380" height="390" viewBox="0 0 360 370" style="max-width: 100%; height: auto;" role="img" aria-label="A shaded ring around the shoulder showing the reachable region between an inner radius of 0.30 meters and an outer radius of 1.50 meters, with an unreachable target outside the ring and the clamped straight-arm solution touching the outer rim on the way to it.">
    <path d="M 20 195 A 150 150 0 1 0 320 195 A 150 150 0 1 0 20 195 Z M 140 195 A 30 30 0 1 0 200 195 A 30 30 0 1 0 140 195 Z" fill="#38bdf8" fill-opacity="0.1" fill-rule="evenodd" stroke="none" />
    <circle cx="170" cy="195" r="150" fill="none" stroke="#38bdf8" stroke-width="2" />
    <circle cx="170" cy="195" r="30" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="5,4" />
    <line x1="170" y1="195" x2="300" y2="105" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.5" stroke-dasharray="6,4" />
    <line x1="170" y1="195" x2="244" y2="143.77" stroke="#38bdf8" stroke-width="6" stroke-linecap="round" />
    <line x1="244" y1="143.77" x2="293.33" y2="109.62" stroke="#4ade80" stroke-width="6" stroke-linecap="round" />
    <circle cx="170" cy="195" r="7" fill="#fbbf24" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.5" />
    <circle cx="244" cy="143.77" r="6" fill="#fbbf24" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.5" />
    <circle cx="293.33" cy="109.62" r="6" fill="#4ade80" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="300" cy="105" r="6" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" />
    <text x="176" y="212" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">shoulder</text>
    <text x="132" y="252" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="bold">0.30 m</text>
    <text x="60" y="60" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">outer limit 1.50 m</text>
    <text x="196" y="288" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">reachable ring</text>
    <text x="192" y="88" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="bold">commanded r = 1.581 m</text>
    <text x="216" y="130" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">clamped tip</text>
    <text x="8" y="360" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">Links 0.90 and 0.60. The clamped arm is straight, aimed at the target, and stops 0.081 m short.</text>
  </svg>
</div>

Now the bug. Command a target at `(1.30, 0.90)`, so `r = √(1.69 + 0.81) = 1.5811` m:

```
   cos φ argument = (0.81 + 0.36 − 2.50) / 1.08 = −1.2315
```

Java's `Math.acos` of anything outside `−1 … +1` returns **NaN** — not an exception, so it propagates silently into your setpoint, your PID controller and your motor output, and the arm freezes or does something spectacular with no stack trace. It surfaces mid-match, not on the bench, because reaching an inch too far is not a condition you tested.

**Clamp the cosine argument to `−1 … +1` before calling `acos`.** That is not papering over the problem, it is the geometrically correct answer. Clamping to `−1` gives `φ = 180°`, and the shoulder's `α` clamps to `0°` in the same breath, leaving `θ1 = β`: the arm goes straight, aimed at the unreachable target, reaching as far along that line as it can — stopping at `(1.2333, 0.8538)`, `0.081` m short. Report that shortfall so the operator sees it.

### Step 9: Elbow-up, elbow-down, and why you must choose

`φ = 80.94°` came back as one unambiguous number, so the triangle's *shape* is pinned down. But a shape is not a placement: it can be laid onto the plane two ways — elbow above the shoulder-to-target line, or mirrored below.

<div style="text-align: center; margin: 20px 0;">
  <svg width="400" height="250" viewBox="0 0 400 240" style="max-width: 100%; height: auto;" role="img" aria-label="Two arm configurations reaching the same target point, one with the elbow above the shoulder-to-target line and one with it mirrored below, joined by a dashed mirror line.">
    <line x1="55" y1="195" x2="235" y2="60" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" stroke-dasharray="6,4" />
    <text x="200" y="52" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">mirror line (shoulder to target)</text>
    <line x1="55" y1="195" x2="94.01" y2="65.76" stroke="#38bdf8" stroke-width="6" stroke-linecap="round" />
    <line x1="94.01" y1="65.76" x2="175" y2="105" stroke="#4ade80" stroke-width="6" stroke-linecap="round" />
    <line x1="55" y1="195" x2="189.99" y2="193.74" stroke="#38bdf8" stroke-width="6" stroke-linecap="round" stroke-opacity="0.45" />
    <line x1="189.99" y1="193.74" x2="175" y2="105" stroke="#4ade80" stroke-width="6" stroke-linecap="round" stroke-opacity="0.45" />
    <circle cx="55" cy="195" r="7" fill="#fbbf24" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.5" />
    <circle cx="94.01" cy="65.76" r="6" fill="#fbbf24" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.5" />
    <circle cx="189.99" cy="193.74" r="6" fill="#fbbf24" fill-opacity="0.5" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <circle cx="175" cy="105" r="6" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" />
    <text x="14" y="214" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">shoulder</text>
    <text x="183" y="98" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">target</text>
    <text x="100" y="58" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">elbow-up</text>
    <text x="198" y="212" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">elbow-down</text>
    <text x="252" y="96" fill="currentColor" fill-opacity="0.75" font-family="sans-serif" font-size="11" font-weight="bold">elbow-up</text>
    <text x="252" y="114" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">θ1 = +73.21°</text>
    <text x="252" y="130" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">θ2 = −99.06°</text>
    <text x="252" y="158" fill="currentColor" fill-opacity="0.75" font-family="sans-serif" font-size="11" font-weight="bold">elbow-down</text>
    <text x="252" y="176" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">θ1 = +0.53°</text>
    <text x="252" y="192" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">θ2 = +99.06°</text>
    <text x="8" y="232" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">Same gripper point (0.80, 0.60). Same |θ2|. Opposite signs.</text>
  </svg>
</div>

The fork is a missing sign: `+99.06°` and `−99.06°` share a cosine, so both satisfy the equation. **The cosine fixed the magnitude of the bend and said nothing about its direction.** The shoulder follows: bend one way and the first link swings to `β + α`, the other way and it swings to `β − α`. The second solution checks out just as exactly:

```
   elbow   = (0.90 cos θ1, 0.90 sin θ1)                = (0.9000, 0.0084)
   gripper = elbow + (0.60 cos(θ1 + θ2), 0.60 sin(θ1 + θ2)) = (0.8000, 0.6000)
```

> ### Math!
> ```
>    θ2 = ±(180° − φ)
> ```
> Read out loud as **"theta-two equals plus or minus one hundred eighty degrees minus phi."** That `±` is the entire elbow ambiguity in one symbol. `arccos` only ever hands back the value between `0°` and `180°`, because a function returns one number — so the sign is yours to choose, never the formula's to supply.

Neither is preferable *mathematically*, which is why a mechanism must choose **deliberately, in code, and stick to it**. Elbow-up here tucks the arm high and close; elbow-down throws the first link nearly flat, putting the elbow 0.90 m past the shoulder — likely outside the frame perimeter, an inspection failure before it is a collision.

And **never let the branch flip mid-motion**: the two poses are far apart in joint space even when their gripper positions are millimeters apart, so a sign flip slams both joints across their full range at speed.

---

## 3. Solving It in Code (Java & WPILib)

### First Principles (Java)

```java
// Link lengths in meters. These are mechanism constants, never variables.
final double L1 = 0.90;   // shoulder segment
final double L2 = 0.60;   // forearm segment

// Target, expressed in the shoulder's own frame: x out, y up.
double tx = 0.80, ty = 0.60;

double r = Math.hypot(tx, ty);   // 1.0000 m

// Law of cosines at the elbow. The interior triangle angle phi is opposite r.
//   r^2 = L1^2 + L2^2 - 2*L1*L2*cos(phi)
double cosPhi = (L1 * L1 + L2 * L2 - r * r) / (2.0 * L1 * L2);   // 0.15741

// A cosine cannot leave [-1, +1]. An out-of-reach target makes it, and
// Math.acos then returns NaN, which spreads silently into every setpoint.
cosPhi = Math.max(-1.0, Math.min(1.0, cosPhi));

double phi = Math.acos(cosPhi);                 // 1.4127 rad = 80.94 deg
double elbowMagnitude = Math.PI - phi;          // 1.7289 rad = 99.06 deg

// Law of cosines again at the shoulder, for the lift above the line to the target.
double cosAlpha = (L1 * L1 + r * r - L2 * L2) / (2.0 * L1 * r);  // 0.80556
cosAlpha = Math.max(-1.0, Math.min(1.0, cosAlpha));
double alpha = Math.acos(cosAlpha);             // 0.6342 rad = 36.34 deg

// Four-quadrant direction to the target (Concept 04).
double beta = Math.atan2(ty, tx);               // 0.6435 rad = 36.87 deg

// The two mirror-image solutions. Choose ONE and stay on it.
double elbowUpShoulder = beta + alpha,  elbowUpElbow   = -elbowMagnitude;
double elbowDnShoulder = beta - alpha,  elbowDnElbow   =  elbowMagnitude;

System.out.printf("elbow-up   theta1 %+.2f  theta2 %+.2f%n",
                  Math.toDegrees(elbowUpShoulder), Math.toDegrees(elbowUpElbow));
System.out.printf("elbow-down theta1 %+.2f  theta2 %+.2f%n",
                  Math.toDegrees(elbowDnShoulder), Math.toDegrees(elbowDnElbow));
// elbow-up   theta1 +73.21  theta2 -99.06
// elbow-down theta1  +0.53  theta2 +99.06
```

Always test inverse kinematics by running the answer back through forward kinematics. Two lines, and it catches every sign error:

```java
double t1 = elbowUpShoulder, t2 = elbowUpElbow;
double gx = L1 * Math.cos(t1) + L2 * Math.cos(t1 + t2);   // 0.8000
double gy = L1 * Math.sin(t1) + L2 * Math.sin(t1 + t2);   // 0.6000
```

### In a Robot Project (Java & WPILib)

**WPILib has no arm inverse-kinematics class.** `SwerveDriveKinematics` and `DifferentialDriveKinematics` cover drivetrains; nothing solves a jointed arm. So the production tier is not a library call but the same mathematics in a small, well-named utility, built from the pieces WPILib *does* give you: `MathUtil.clamp` for the guard, `Rotation2d` for angles that never lose their units, `Translation2d` for the target.

```java
import edu.wpi.first.math.MathUtil;
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.math.geometry.Translation2d;

/** Inverse kinematics for a planar two-link arm. */
public final class TwoLinkArmKinematics {
  public enum Elbow { UP, DOWN }

  /** Shoulder and elbow joint angles, plus whether the target had to be clamped. */
  public record ArmAngles(Rotation2d shoulder, Rotation2d elbow, boolean clamped) {}

  private final double l1, l2;

  public TwoLinkArmKinematics(double l1Meters, double l2Meters) {
    this.l1 = l1Meters;
    this.l2 = l2Meters;
  }

  public double maxReach()  { return l1 + l2; }
  public double minReach()  { return Math.abs(l1 - l2); }

  /** Target is in the shoulder frame: +x away from the robot, +y up. */
  public ArmAngles toAngles(Translation2d target, Elbow branch) {
    double r = target.getNorm();
    boolean clamped = r > maxReach() || r < minReach();

    // MathUtil.clamp is the guard: without it an unreachable target
    // makes Math.acos return NaN, which propagates into the setpoint.
    double cosPhi   = MathUtil.clamp((l1 * l1 + l2 * l2 - r * r) / (2 * l1 * l2), -1, 1);
    double cosAlpha = MathUtil.clamp((l1 * l1 + r * r - l2 * l2) / (2 * l1 * r),  -1, 1);

    Rotation2d bend  = Rotation2d.fromRadians(Math.PI - Math.acos(cosPhi));
    Rotation2d lift  = Rotation2d.fromRadians(Math.acos(cosAlpha));
    Rotation2d aim   = new Rotation2d(target.getX(), target.getY());   // atan2 inside

    return branch == Elbow.UP
        ? new ArmAngles(aim.plus(lift),  bend.unaryMinus(), clamped)
        : new ArmAngles(aim.minus(lift), bend,              clamped);
  }

  /** Forward kinematics, for verifying the above in a unit test. */
  public Translation2d toTip(Rotation2d shoulder, Rotation2d elbow) {
    Rotation2d far = shoulder.plus(elbow);
    return new Translation2d(l1 * shoulder.getCos() + l2 * far.getCos(),
                             l1 * shoulder.getSin() + l2 * far.getSin());
  }
}
```

Called with `new Translation2d(0.80, 0.60)` and `Elbow.UP` it returns `73.21°` and `−99.06°` — the same numbers as the from-scratch tier, because it is the same arithmetic — and `toTip` on that pair returns `(0.800, 0.600)`, the assertion your unit test should make. The one input to watch is `r = 0`: `new Rotation2d(0, 0)` gives `0°` rather than throwing, so the arm folds and points down-field.

---

## 4. Bridge to Real Systems

### Robot manipulators, from FRC to industrial arms

Everything above is the standard analytic solution for a **planar 2R manipulator**, one of the few arm geometries solvable in closed form at all. Past a few joints there is no formula and controllers switch to numerical solvers — but the properties derived here survive: a workspace bounded by maximum and minimum reach, solutions in discrete branches, and branch-switching mid-trajectory as the classic way to wreck a mechanism.

The elbow fork has a name there. Configurations where branches meet are **singularities**, and here they sit on Step 8's two rims: at full extension and full fold, `α = 0` and the solutions collapse into one. Near a rim a tiny change in target demands a large change in joint angle, which is why arm code stays a margin inside the annulus.

### Trilateration: the same triangle, solved for position

**Trilateration** is how GPS works: a receiver measures its distance to satellites whose positions are known, each distance defines a sphere, and the receiver sits where the spheres intersect — this same manoeuvre in three dimensions. Closer to home, ultrasonic and time-of-flight sensors report ranges rather than bearings, and two at a known separation pin a target to a point by exactly the Step 6 computation, as Checkpoint 2 works through. Ranges take cosines, bearings take sines, and both are this triangle.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1

An arm has links `L1 = 0.70` m and `L2 = 0.50` m. Find its reachable ring, decide whether a target 1.30 m out is reachable, and say what the code should command if not.

**Solution:**

1. **The ring**, from Step 8's two limits:

   ```
   outer = L1 + L2   = 0.70 + 0.50 = 1.20 m
   inner = |L1 − L2| = 0.70 − 0.50 = 0.20 m
   ```
2. **Test it.** 1.30 lies outside that ring. Confirm as the code will:

   ```
   cos φ = (0.49 + 0.25 − 1.69) / (2 × 0.70 × 0.50) = −0.95 / 0.70 = −1.357
   ```
3. **Unclamped.** `Math.acos(−1.357)` returns NaN, silently contaminating the shoulder angle, the setpoint and the motor output.
4. **Clamped.** `cos φ` clamps to `−1`, giving `φ = 180°` and `θ2 = 0°`, arm straight. The shoulder's cosine clamps too:

   ```
   cos α = (0.49 + 1.69 − 0.25) / (2 × 0.70 × 1.30) = 1.060   →   clamps to +1   →   α = 0°
   ```

   so `θ1 = β`. The arm points straight at the target and stops 0.10 m short, the best it can physically do.

---

### Checkpoint 2

A robot at `(2.0, 3.0)` and a teammate at `(6.0, 3.0)` both range the same game piece: the first measures 3.5 m, the second 2.5 m. Find the angle at the first robot between the lines to its teammate and to the piece, then the piece's field position (larger-Y solution).

**Solution:**

1. **The triangle.** All three sides are known — baseline 4.0 m, ranges 3.5 and 2.5 m. Three sides is the law of cosines' other input mode.
2. **At the first robot.** Its angle `A` lies between the sides 4.0 and 3.5, and opposite it is the teammate's range, 2.5:

   ```
   2.5² = 4.0² + 3.5² − 2 × 4.0 × 3.5 × cos A
   6.25 = 16.00 + 12.25 − 28.00 cos A
   cos A = 22.00 / 28.00 = 0.78571      →      A = 38.21°
   ```
3. **Guard it, as code would.** `0.78571` is inside `−1 … +1`, so the three lengths really do close into a triangle. Ranges of 3.5 and 0.4 would not, meaning the sensors disagree.
4. **To a field position.** The baseline runs along `+X`, so the bearing is 38.21° and the piece is 3.5 m along it:

   ```
   (2.0 + 3.5 cos 38.21°, 3.0 + 3.5 sin 38.21°) = (4.750, 5.165)
   ```
5. **Verify.** Its distance to the teammate is `√(1.5625 + 4.6872) = 2.500` m, matching the second range.

---

### Deep Dive 1

Step 9 forbade flipping branches mid-motion, but said nothing about how to *change* branch when you genuinely must — stowed elbow-down to an elbow-up scoring pose, say. Work out what the gripper does if you command the new angles and let both motors drive straight there, and where on that path the arm is most extended. Then design a safer route through the branch-change point, and decide whether the folded or the extended rim is the better crossing.

### Deep Dive 2

Real arms cannot use their whole annulus. Suppose the shoulder is limited to `0°` through `120°`, the elbow to `−140°` through `0°`, and the gripper must never dip below the floor line. Sketch the part of the ring that survives all three. Then extend Section 3's code to report whether each joint angle is inside its limit and try elbow-down when elbow-up is not — and decide what to do when both branches fail on a target inside the annulus.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../05_concept_angle_wrapping_swerve/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 05: Angle Wrapping</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../07_concept_3d_rotations_quaternions/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 07: 3D Rotations & Quaternions →</a></div>
</div>
