# Concept 01: Right Triangles & the Unit Circle

> **▶ Interactive Demo: [Unit Circle & Right Triangle Explorer](demo.html)**
>
> Drag the wheel around the circle and set its speed. Watch the triangle redraw, the signs flip quadrant by quadrant, and `sin²θ + cos²θ` hold at 1.000.

<iframe src="demo.html" width="100%" height="620" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: A Wheel Turned at an Angle

A wheel is pointed 30 degrees off straight down-field, spinning fast enough to move at 4.0 m/s. How much of that 4.0 m/s is carrying the robot **down-field**, and how much is carrying it **sideways**?

<div style="text-align: center; margin: 20px 0;">
  <svg width="360" height="240" viewBox="0 0 340 226" style="max-width: 100%; height: auto;" role="img" aria-label="A wheel seen from above, turned thirty degrees off the down-field axis, with its 4.0 metres per second velocity arrow resolved by dashed lines into an unknown down-field component and an unknown sideways component.">
    <circle cx="140" cy="130" r="34" fill="none" stroke="currentColor" stroke-opacity="0.16" stroke-width="1.5" stroke-dasharray="3,4" />
    <line x1="50" y1="130" x2="272" y2="130" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <line x1="140" y1="42" x2="140" y2="200" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <text x="242" y="146" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">down-field</text>
    <g transform="rotate(-30 140 130)">
      <rect x="113" y="122" width="54" height="16" rx="4" fill="currentColor" fill-opacity="0.13" stroke="currentColor" stroke-opacity="0.65" stroke-width="2" />
      <line x1="127" y1="123" x2="127" y2="137" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
      <line x1="140" y1="123" x2="140" y2="137" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
      <line x1="153" y1="123" x2="153" y2="137" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    </g>
    <path d="M 174 130 A 34 34 0 0 0 169.4 113" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="178" y="124" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">θ = 30°</text>
    <line x1="140" y1="130" x2="213" y2="87.9" stroke="#fbbf24" stroke-width="3" />
    <polygon points="218,85 210.1,95.3 205.1,86.7" fill="#fbbf24" />
    <text x="148" y="98" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">v = 4.0 m/s</text>
    <line x1="140" y1="130" x2="218" y2="130" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,4" />
    <line x1="218" y1="130" x2="218" y2="85" stroke="#4ade80" stroke-width="2.5" stroke-dasharray="4,4" />
    <rect x="208" y="120" width="10" height="10" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <text x="150" y="146" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">down-field = ?</text>
    <text x="224" y="110" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">sideways = ?</text>
    <circle cx="140" cy="130" r="4" fill="currentColor" fill-opacity="0.7" />
    <text x="16" y="216" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">The wheel, seen from above. Known: the angle θ and the speed v. Wanted: the two legs.</text>
  </svg>
</div>

The picture already contains a right triangle: the 4.0 m/s is its long slanted side, and the two components are its legs. Everything about it is fixed by the wheel's angle, and turning that angle into those two numbers is the rest of this concept.

A wheel that can be pointed anywhere and driven at any speed is called a **swerve module** — four sit under a typical robot, and this module returns to one repeatedly: Concept 02 builds field-oriented drive on these components, Concept 04 recovers a module angle with `atan2`, Concept 05 handles the 180° flip.

---

## 2. Building the Math: From a Triangle to a Circle

### Step 1: Naming the sides — and why the names are not fixed

Drop a perpendicular from the tip of that velocity arrow to the down-field axis and you get a **right triangle**: one angle exactly 90°, two acute. Pick a non-right angle, call it θ, and name the sides relative to *that choice*:

* **Hypotenuse** — opposite the right angle. The longest side, and the only name independent of your choice.
* **Opposite** — the side that does not touch θ.
* **Adjacent** — the remaining side: it touches θ and is not the hypotenuse.

<div style="text-align: center; margin: 20px 0;">
  <svg width="420" height="220" viewBox="0 0 400 212" style="max-width: 100%; height: auto;" role="img" aria-label="The same right triangle drawn twice. On the left the angle is chosen at the lower-left vertex; on the right it is chosen at the top vertex, and the opposite and adjacent labels have swapped sides.">
    <line x1="20" y1="160" x2="116" y2="160" stroke="#38bdf8" stroke-width="3" />
    <line x1="116" y1="160" x2="116" y2="88" stroke="#4ade80" stroke-width="3" />
    <line x1="20" y1="160" x2="116" y2="88" stroke="#fbbf24" stroke-width="3" />
    <rect x="106" y="150" width="10" height="10" fill="none" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.5" />
    <path d="M 46 160 A 26 26 0 0 0 40.8 144.4" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="49" y="153" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">θ</text>
    <text x="40" y="176" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">adjacent</text>
    <text x="122" y="128" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">opposite</text>
    <text x="30" y="146" transform="rotate(-36.87 30 146)" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">hypotenuse</text>
    <text x="14" y="200" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">angle chosen at the left vertex</text>
    <line x1="220" y1="160" x2="316" y2="160" stroke="#4ade80" stroke-width="3" />
    <line x1="316" y1="160" x2="316" y2="88" stroke="#38bdf8" stroke-width="3" />
    <line x1="220" y1="160" x2="316" y2="88" stroke="#fbbf24" stroke-width="3" />
    <rect x="306" y="150" width="10" height="10" fill="none" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.5" />
    <path d="M 316 112 A 24 24 0 0 1 296.8 102.4" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="292" y="122" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">φ</text>
    <text x="240" y="176" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">opposite</text>
    <text x="322" y="128" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">adjacent</text>
    <text x="230" y="146" transform="rotate(-36.87 230 146)" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">hypotenuse</text>
    <text x="214" y="200" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">angle chosen at the top vertex</text>
  </svg>
</div>

Both pictures show the *same triangle*: only the chosen angle changed, and the blue and green labels traded places. This is trigonometry's commonest confusion — "opposite" and "adjacent" describe a side *relative to a chosen angle*, not the side itself. Name your angle before writing a ratio.

### Step 2: Why the ratios ignore the triangle's size

This observation makes trigonometry possible, and it is almost always skipped. Scale a triangle by `k`: opposite becomes `k · opposite`, hypotenuse becomes `k · hypotenuse`. Form the ratio:

$$
\frac{k \cdot \text{opposite}}{k \cdot \text{hypotenuse}} = \frac{\text{opposite}}{\text{hypotenuse}}
$$

The `k` cancels: **the ratio is untouched by scaling.**

But we want more — that *any* two right triangles sharing the angle θ give the same ratio. The three angles of a triangle sum to 180°, as you can confirm by tearing the corners off a paper triangle and laying them along a ruler. So if two right triangles both contain 90° and θ, the third is forced to `180° − 90° − θ`. All three match, making the triangles **similar** — so one *is* a scaled copy of the other.

Together: **the ratio between two named sides depends on θ and nothing else** — which is what earns them permanent names.

### Step 3: SOH-CAH-TOA

Three ratios get names:

$$
\begin{aligned}
\sin\theta &= \frac{\text{opposite}}{\text{hypotenuse}} \\[4pt]
\cos\theta &= \frac{\text{adjacent}}{\text{hypotenuse}} \\[4pt]
\tan\theta &= \frac{\text{opposite}}{\text{adjacent}}
\end{aligned}
$$

Generations have memorised them as **SOH-CAH-TOA** — Sine is Opposite over Hypotenuse, Cosine is Adjacent over Hypotenuse, Tangent is Opposite over Adjacent. A mnemonic, but a good one.

Try it on Geometry Concept 01's 3-4-5 triangle, scaled to sides 90, 120 and 150. At the left vertex the opposite is 90, the adjacent 120:

$$
\begin{aligned}
\sin\theta &= \frac{90}{150} = 0.600 \\[4pt]
\cos\theta &= \frac{120}{150} = 0.800 \\[4pt]
\tan\theta &= \frac{90}{120} = 0.750
\end{aligned}
$$

Stand at the *other* acute vertex, φ, and the two swap: `sin φ = 0.800`, `cos φ = 0.600`. The sine of one acute angle is the cosine of the other — the "co" marks the **co**mplementary angle, the one completing 90°.

> ### Math!
> `sin θ` is read out loud as **"sine of theta"**, `cos θ` as **"cosine of theta"**, `tan θ` as **"tangent of theta"**. These are *functions*: `sin` eats an angle and returns a number. It is **not** `sin` times `θ`, and cannot be cancelled from both sides. And `sin²θ` means `(sin θ)²` — sine first, then square — not `sin(θ²)`.

### Step 4: The hypotenuse-1 collapse

Use that scaling freedom aggressively: divide every side of a right triangle by its own hypotenuse. The hypotenuse becomes 1, the ratios are unchanged, and the definitions now say:

$$
\begin{aligned}
\sin\theta &= \frac{\text{opposite}}{1} = \text{opposite} \\[4pt]
\cos\theta &= \frac{\text{adjacent}}{1} = \text{adjacent}
\end{aligned}
$$

The ratios have stopped being ratios: **they are now the side lengths themselves.**

Run it backwards and the opening problem is solved. If the hypotenuse is a speed `v` rather than 1, scaling up gives `adjacent = v · cos θ` and `opposite = v · sin θ`. A wheel doing 4.0 m/s at 30° splits into `4.0 · cos 30° = 3.464` m/s down-field and `4.0 · sin 30° = 2.000` m/s sideways.

### Step 5: The circle, and escaping the triangle's 90° ceiling

Pin that triangle so θ sits at the origin and the adjacent leg lies along the positive X-axis. Its far tip lands at `(cos θ, sin θ)`, always 1 unit from the origin because the hypotenuse is 1. Sweep θ and the tip traces a circle of radius 1: the **unit circle**.

A right triangle spends 90° of its 180° budget on the right angle, so each acute angle is under 90° — no right triangle has a 150° angle. But a **point at 150° on a circle** is perfectly ordinary. So the circle becomes the definition:

$$
\begin{aligned}
\cos\theta &= \text{the x-coordinate of the point at angle } \theta \text{ on the unit circle} \\[4pt]
\sin\theta &= \text{the y-coordinate of that same point}
\end{aligned}
$$

Between 0° and 90° this agrees with SOH-CAH-TOA, where the point sits at a first-quadrant triangle's corner. Beyond it the circle sails on alone: an **extension**, not a replacement.

<div style="text-align: center; margin: 20px 0;">
  <svg width="360" height="340" viewBox="0 0 340 320" style="max-width: 100%; height: auto;" role="img" aria-label="A unit circle with a point at 150 degrees, its reference triangle dropped to the negative x-axis, and the sign of cosine and sine marked in each quadrant.">
    <circle cx="170" cy="160" r="120" fill="none" stroke="currentColor" stroke-opacity="0.3" stroke-width="2" />
    <line x1="30" y1="160" x2="310" y2="160" stroke="currentColor" stroke-opacity="0.45" stroke-width="1.5" />
    <line x1="170" y1="30" x2="170" y2="290" stroke="currentColor" stroke-opacity="0.45" stroke-width="1.5" />
    <text x="292" y="176" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">1</text>
    <text x="40" y="176" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">−1</text>
    <text x="176" y="46" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">1</text>
    <text x="176" y="284" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">−1</text>
    <path d="M 240 160 A 70 70 0 0 0 109.4 125" fill="none" stroke="#c084fc" stroke-width="2.5" />
    <text x="182" y="98" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">θ = 150°</text>
    <path d="M 130 160 A 40 40 0 0 1 135.4 140" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <text x="96" y="153" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">30°</text>
    <line x1="170" y1="160" x2="66" y2="100" stroke="#fbbf24" stroke-width="3" />
    <line x1="170" y1="160" x2="66" y2="160" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5,4" />
    <line x1="66" y1="160" x2="66" y2="100" stroke="#4ade80" stroke-width="2.5" stroke-dasharray="5,4" />
    <rect x="66" y="150" width="10" height="10" fill="none" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.5" />
    <circle cx="66" cy="100" r="6" fill="#fbbf24" stroke="#ffffff" stroke-width="1.5" />
    <text x="72" y="134" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">sin = +0.500</text>
    <text x="78" y="176" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="bold">cos = −0.866</text>
    <text x="96" y="72" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">II: cos −</text>
    <text x="96" y="85" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">    sin +</text>
    <text x="238" y="72" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">I: cos +</text>
    <text x="238" y="85" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">   sin +</text>
    <text x="96" y="238" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">III: cos −</text>
    <text x="96" y="251" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">     sin −</text>
    <text x="238" y="238" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">IV: cos +</text>
    <text x="238" y="251" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">    sin −</text>
    <text x="16" y="308" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">θ = 150°  →  (cos θ, sin θ) = (−0.866, +0.500)</text>
  </svg>
</div>

To *evaluate* `cos 150°`, drop a perpendicular to the X-axis. It, the axis and the radius form a right triangle whose angle at the origin is `180° − 150° = 30°` — the **reference angle** — with legs `cos 30° = 0.866` and `sin 30° = 0.500`. The signs come off the picture: the point is left of the vertical axis and above the horizontal one, so `cos 150° = −0.866` and `sin 150° = +0.500`. Nothing to memorise beyond which side of which axis:

```
   Quadrant     angle range      cos      sin      tan
   ----------------------------------------------------
   I              0° – 90°        +        +        +
   II            90° – 180°       −        +        −
   III          180° – 270°       −        −        +
   IV           270° – 360°       +        −        −
```

θ may also pass 360° or go negative: walking right around the rim returns you to the same point, so `cos(θ + 360°) = cos θ` and the functions are **periodic**. A heading of 370° and one of 10° command identical wheel angles, and subtracting headings to compare them is a trap Concept 05 cleans up.

> ### Math!
> $$
> \cos(\theta + 2\pi k) = \cos\theta \qquad \text{for any whole number } k
> $$
> Read out loud as **"cosine of theta plus two pi k equals cosine of theta, for any integer k."** The `k` is a lap counter: whole turns change the angle you *wrote down*, not the point you *landed on*. `2π` is the **period**.

### Step 6: Radians, and why 360 is the strange number

Where did 360 come from? Babylonian base-60 arithmetic, a 360-day year, and the fact that 360 divides evenly by 2, 3, 4, 5, 6, 8, 9, 10 and 12. Good reasons for a calendar; none a fact about circles. The circle offers its own unit for free: walk along the rim from the positive X-axis to the point at angle θ, and **the distance you walked is the angle**. That measure is the **radian**.

<div style="text-align: center; margin: 20px 0;">
  <svg width="320" height="200" viewBox="0 0 300 195" style="max-width: 100%; height: auto;" role="img" aria-label="A unit circle wedge in which the arc along the rim has the same length as the radius, defining one radian.">
    <path d="M 180 150 A 100 100 0 0 0 134 65.9" fill="none" stroke="#4ade80" stroke-width="5" />
    <circle cx="80" cy="150" r="100" fill="none" stroke="currentColor" stroke-opacity="0.2" stroke-width="1.5" />
    <line x1="80" y1="150" x2="180" y2="150" stroke="#fbbf24" stroke-width="3" />
    <line x1="80" y1="150" x2="134" y2="65.9" stroke="#fbbf24" stroke-width="3" />
    <path d="M 110 150 A 30 30 0 0 0 96.2 124.7" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="112" y="140" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">θ = 1 rad</text>
    <text x="106" y="166" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">radius = 1</text>
    <text x="182" y="104" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">arc length = 1</text>
    <text x="8" y="186" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">Walk a distance of 1 along the rim. The angle you swept is 1 radian ≈ 57.2958°.</text>
  </svg>
</div>

One radian is the angle whose arc, on a circle of radius 1, has length 1. A full lap is the circumference `2πr`, so a full turn is `2π ≈ 6.28318` radians; half a turn `π`, a quarter turn `π/2`. Setting `360° = 2π rad` gives `180° = π rad` and both conversions:

$$
\begin{aligned}
\text{radians} &= \text{degrees} \times \frac{\pi}{180} \\[4pt]
\text{degrees} &= \text{radians} \times \frac{180}{\pi}
\end{aligned}
$$

Check them: `30° × π/180 ≈ 0.5236` rad, and `2.0 rad × 180/π ≈ 114.59°`. Software uses radians because the definition buys `arc length = radius × angle` with no conversion factor.

> ### Math!
> $$
> s = r \cdot \theta \qquad (\theta \text{ in radians})
> $$
> Read out loud as **"s equals r theta"** — arc length equals radius times angle. On a 4-inch wheel (radius 0.0508 m) one rotation is `θ = 2π`, so it rolls `0.0508 × 6.28318 = 0.3192` m. Feed degrees in and you are wrong by about 57×.

**And now the bug.** Java's `Math.sin` and `Math.cos` take **radians**. Gyros — NavX, Pigeon, ADIS — report **degrees**, as does every human on your drive team. `Math.sin(30.0)` when you meant 30 degrees does not crash: it returns the sine of 30 *radians*, `−0.988`. That is a plausible number between −1 and 1, so nothing complains and the wheel simply points the wrong way. Convert with `Math.toRadians` and `Math.toDegrees` at every boundary, and put the unit in the variable name.

### Step 7: The identity that comes free — sin² + cos² = 1

The point `(cos θ, sin θ)` is by construction exactly 1 unit from the origin. Geometry Concept 01 proved the Pythagorean theorem by area rearrangement and turned it into the distance formula. Apply that formula to `(0, 0)` and our point:

$$
\text{distance} = \sqrt{(\cos\theta - 0)^2 + (\sin\theta - 0)^2} = \sqrt{\cos^2\theta + \sin^2\theta} = 1
$$

Square both sides:

$$
\sin^2\theta + \cos^2\theta = 1
$$

That is the **Pythagorean identity**, and nothing new went into it: it is Pythagoras applied to a triangle whose hypotenuse happens to be 1. Check it at 150°: `(−0.866)² + (0.500)² = 0.750 + 0.250 = 1.000`. The sign vanishes under squaring, so it holds in every quadrant with no case split.

Decompose a speed `v` into `(v cos θ, v sin θ)` and ask how fast the robot is going:

$$
\sqrt{(v \cos\theta)^2 + (v \sin\theta)^2} = \sqrt{v^2 (\cos^2\theta + \sin^2\theta)} = \sqrt{v^2} = v
$$

**Splitting a speed into components never changes the total speed.**

### Step 8: Tangent is slope, and slope has a known failure

Divide sine by cosine and see what survives:

$$
\frac{\sin\theta}{\cos\theta} = \frac{\dfrac{\text{opposite}}{\text{hypotenuse}}}{\dfrac{\text{adjacent}}{\text{hypotenuse}}} = \frac{\text{opposite}}{\text{adjacent}} = \tan\theta
$$

The hypotenuse cancels and the third ratio reappears. But `opposite / adjacent` is rise over run: `tan θ` **is the slope** of a line through the origin at angle θ.

So tangent inherits slope's disease. At θ = 90° the cosine is 0, the division blows up, and `tan 90°` does not exist: `tan 89° = 57.29`, `tan 89.9° = 572.96`, `tan 89.99° = 5729.6`. This is exactly the objection Geometry Concept 02 raised against describing a line by its slope, and vertical lines are not rare on a field.

The unit circle is immune because it never divides — the point at 90° is `(0, 1)`, ordinary as any other. That is why robotics code stores a heading as a `(cos, sin)` pair, and why Concept 04 uses `atan2`.

---

## 3. Solving It in Code (Java & WPILib)

### First Principles (Java)

```java
// One wheel, turned 30 degrees off straight down-field, spinning fast
// enough to move at 4.0 m/s.
double wheelSpeedMps     = 4.0;    // meters per second (the hypotenuse)
double wheelAngleDegrees = 30.0;   // counter-clockwise from down-field

// Java trig takes RADIANS. Convert at the boundary, once, explicitly.
double wheelAngleRadians = Math.toRadians(wheelAngleDegrees);   // 0.5236 rad

// SOH-CAH-TOA, scaled up from a hypotenuse of 1 to a hypotenuse of 4.0:
//   adjacent = hypotenuse * cos(theta)  -> the down-field component
//   opposite = hypotenuse * sin(theta)  -> the sideways   component
double downfieldMps = wheelSpeedMps * Math.cos(wheelAngleRadians);   // 3.464 m/s
double sidewaysMps  = wheelSpeedMps * Math.sin(wheelAngleRadians);   // 2.000 m/s

// sin^2 + cos^2 = 1 promises the split preserved the wheel's speed.
double recovered = Math.hypot(downfieldMps, sidewaysMps);            // 4.000 m/s

System.out.printf("down-field %.3f  sideways %.3f  total %.3f%n",
                  downfieldMps, sidewaysMps, recovered);
```

Past 90° needs no special handling; the library implements the circle definition, signs included:

```java
for (int deg = 0; deg <= 360; deg += 45) {
    double r = Math.toRadians(deg);
    System.out.printf("%4d deg -> cos %+.3f  sin %+.3f  identity %.6f%n",
                      deg, Math.cos(r), Math.sin(r),
                      Math.sin(r) * Math.sin(r) + Math.cos(r) * Math.cos(r));
}
// 150 deg -> cos -0.866  sin +0.500  identity 1.000000
// 270 deg -> cos -0.000  sin -1.000  identity 1.000000
```

The bug, for the record — neither line errors:

```java
double right = Math.sin(Math.toRadians(30.0));   // +0.500  <- 30 degrees
double wrong = Math.sin(30.0);                   // -0.988  <- 30 RADIANS
```

### In a Robot Project (Java & WPILib)

```java
import edu.wpi.first.math.geometry.Rotation2d;

// Build the wheel's angle from degrees; the class converts and caches it.
Rotation2d wheelAngle = Rotation2d.fromDegrees(30.0);

double downfieldMps = wheelSpeedMps * wheelAngle.getCos();   // 3.464 m/s
double sidewaysMps  = wheelSpeedMps * wheelAngle.getSin();   // 2.000 m/s

double rad = wheelAngle.getRadians();   // 0.5236
double deg = wheelAngle.getDegrees();   // 30.0

// Straight from an absolute steering encoder, which reports degrees:
Rotation2d measured = Rotation2d.fromDegrees(steerEncoder.getPositionDegrees());

// Or straight from a pair of components, with no trigonometry called at all:
// this normalises (x, y) to length 1 and keeps the pair.
Rotation2d fromComponents = new Rotation2d(downfieldMps, sidewaysMps);
```

Both tiers produce the same numbers, 3.464 and 2.000. WPILib's `SwerveModuleState` stores exactly the polar pair this concept starts from: a speed in meters per second and a `Rotation2d`. And notice that `Rotation2d` **does not store the angle** — it stores the cosine and sine, normalised so `cos² + sin² = 1`, reconstructing the angle only when asked. So `getCos()` and `getSin()` are free in a 20 ms loop, building one from components needs no trig, and the stored pair always lies on the unit circle: Step 7's identity, enforced by a constructor.

---

## 4. Bridge to Machine Learning & Modern Autonomy

### Sinusoidal positional encodings: giving a Transformer a sense of order

A Transformer's attention mechanism is **permutation-invariant**: shuffle a sentence and the model sees the identical bag of tokens, so order must be injected deliberately. Appending the position index 0, 1, 2, … fails, because the magnitude grows without bound and token 4,000 dwarfs every learned feature beside it.

The original Transformer paper solved this with the unit circle. Each position `pos` gets a vector of length `d`, filled in pairs:

$$
\begin{aligned}
PE_{(pos,\ 2i)}   &= \sin\!\left(\frac{pos}{10000^{\,2i/d}}\right) \\[4pt]
PE_{(pos,\ 2i+1)} &= \cos\!\left(\frac{pos}{10000^{\,2i/d}}\right)
\end{aligned}
$$

Pair `i` places the position on its own unit circle at its own rate. Pair 0 turns fastest, a lap every `2π ≈ 6.3` tokens; the last takes about `62,832` tokens per lap, the rates between spaced geometrically.

The result is a set of clock hands: no single one gives the position, but read all `d/2` at once and the combination is unique over any length — as hour, minute and second hands pin down a moment none identifies alone.

Two properties come straight from this concept. Sine and cosine never leave `[−1, 1]`, so position 4,000 encodes to the same size as position 4. And each frequency contributes a **pair** rather than a lone sine because `cos² + sin² = 1` then makes every pair contribute identical length at every position: no position is louder than another, only its *direction* varies. Step 7's identity as a design constraint inside a language model.

### Fourier features: why coordinate networks need a circle to see detail

Give a small network a coordinate `(x, y)` and ask for the colour there, or the density there in a 3D scene — the NeRF setup. Feed it raw coordinates and the output is a blurry smear. The cause has a name, **spectral bias**: ReLU networks are biased toward smooth, low-frequency functions, and detail is high-frequency.

The fix is to feed *angles* instead — replace `x` with a bank of sine and cosine pairs at geometrically spaced frequencies:

$$
\gamma(x) = \left[\ \sin(2^{0}\pi x),\ \cos(2^{0}\pi x),\ \sin(2^{1}\pi x),\ \cos(2^{1}\pi x),\ \ldots,\ \sin(2^{L-1}\pi x),\ \cos(2^{L-1}\pi x)\ \right]
$$

This is the hypotenuse-1 collapse applied at many scales at once. Each frequency wraps the coordinate onto its own unit circle, and the fast ones lap across a sliver of the scene, so two nearby points land far apart there. NeRF uses `L = 10`, one lap per 1/512 of the scene at the top. Same layers, same optimiser — only the input changes, and mush becomes geometry. The same trick encodes "hour of day" as `(cos(2π·h/24), sin(2π·h/24))`, so midnight sits beside 11 p.m.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1

A wheel is turned to 220° counter-clockwise from down-field and driven at 2.5 m/s. Find its down-field and sideways components, convert 220° to radians, and verify the split preserved the speed.

**Solution:**

1. **Quadrant.** 220° lies between 180° and 270° — Quadrant III, so cosine and sine are both negative.
2. **Reference angle.** The nearest half-axis is the negative one at 180°: `220° − 180° = 40°`.
3. **Ratios, signs attached.** `cos 40° = 0.766` and `sin 40° = 0.643`, so `cos 220° = −0.766`, `sin 220° = −0.643`.
4. **Scale by the speed.** down-field `= 2.5 × (−0.766) = −1.915` m/s, sideways `= 2.5 × (−0.643) = −1.607` m/s — the wheel is pushing backwards and to the right.
5. **Convert.** `220 × π/180 = 3.840` rad.
6. **Verify.** `(−1.915)² + (−1.607)² = 3.667 + 2.582 = 6.249`, and `√6.249 = 2.500` m/s.

---

### Checkpoint 2

A camera sits 0.60 m above the carpet, tilted 25° upward, and centres an AprilTag whose middle is 1.45 m up. How far away is the tag along the ground? Then say what happens if the camera is remounted pointing straight up.

**Solution:**

1. **The triangle.** The line of sight is the hypotenuse; the rise is `1.45 − 0.60 = 0.85` m; the ground distance `d` is wanted.
2. **Name the sides relative to the 25° angle at the camera.** The rise is across the triangle from it, so **opposite**; the ground distance touches it and is not the hypotenuse, so **adjacent**.
3. **Pick the ratio using those two.** Opposite over adjacent is tangent: `tan 25° = 0.85 / d`.
4. **Solve.** `d = 0.85 / tan 25° = 0.85 / 0.4663 = 1.823` m.
5. **Straight up.** `tan 90°` is undefined, so the formula returns nothing — correct, not glitchy. A camera aimed at the ceiling looks parallel to the wall and never reaches a wall tag: Step 8's failure as physical impossibility.

---

### Deep Dive 1

A wheel cannot turn instantly. Commanded to a new angle, it spends several loop cycles swinging toward it while already spinning — so for that moment it pushes in the wrong direction. A widely used fix scales the commanded speed by `cos(commanded angle − measured angle)`. Work out why the cosine of the error is exactly the right factor, by asking how much of the intended push lies along the direction the wheel actually points. Then evaluate it at errors of 0°, 30°, 90° and 180°, say what the wheel does in each case, and decide whether an implementation should keep the negative value at 180° or clamp it to zero.

### Deep Dive 2

Radians earn their keep in `s = rθ`. Take a 4-inch wheel (radius 0.0508 m) behind a 6.75:1 reduction, driven by a motor whose encoder reports rotations. Derive the meters travelled per motor rotation, and state where the `2π` enters. Then test a claim you meet constantly in control code: for small angles **in radians**, `sin θ ≈ θ`. Evaluate both sides at 0.05, 0.10, 0.20 and 0.40 rad, find where the error crosses 1%, and check what happens if it is handed degrees.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../../01_geometry/05_concept_polygons_zones/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 05: Polygons & Zones</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../02_concept_rotating_vectors/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Rotating a Vector →</a></div>
</div>
