# Concept 04: Inverse Trig & 4-Quadrant Heading with atan2

> **▶ Interactive Demo: [atan vs. atan2 Explorer](demo.html)**
>
> Drag the target through all four quadrants. Watch `atan(y/x)` and `atan2(y, x)` agree in Quadrant I, then part company by exactly 180° — and watch `atan` fail outright when x reaches 0.

<iframe src="demo.html" width="100%" height="640" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Getting the Angle Back

Concept 01 took a wheel pointed 30° off down-field, driven at 4.0 m/s, and split it into **3.464 m/s down-field** and **2.000 m/s sideways**. One angle and one speed in; two components out.

This concept runs that arrow backwards. A path follower does not think in wheel angles — it computes where the robot should be heading and hands you exactly those two numbers: so many m/s down-field, so many m/s sideways. But the wheel has two physical motors, one that spins it and one that points it, so it needs a **speed and an angle**. The speed is Module 1's distance formula and costs nothing:

```
   speed = √( 3.464² + 2.000² ) = √( 12.000 + 4.000 ) = √16.000 = 4.000 m/s
```

The angle is the problem, and it is the whole of this concept.

<div style="text-align: center; margin: 20px 0;">
  <svg width="360" height="240" viewBox="0 0 340 226" style="max-width: 100%; height: auto;" role="img" aria-label="A wheel seen from above with its two velocity components known — 3.464 metres per second down-field and 2.000 metres per second sideways — and the angle of the resulting arrow marked as unknown.">
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
    <text x="178" y="124" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">θ = ?</text>
    <line x1="140" y1="130" x2="212.8" y2="88" stroke="#fbbf24" stroke-width="3" stroke-opacity="0.55" />
    <circle cx="212.8" cy="88" r="5" fill="#fbbf24" />
    <line x1="140" y1="130" x2="212.8" y2="130" stroke="#38bdf8" stroke-width="3" />
    <line x1="212.8" y1="130" x2="212.8" y2="88" stroke="#4ade80" stroke-width="3" />
    <rect x="202.8" y="120" width="10" height="10" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <text x="146" y="146" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">down-field = 3.464</text>
    <text x="219" y="112" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">sideways</text>
    <text x="219" y="124" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">= 2.000</text>
    <circle cx="140" cy="130" r="4" fill="currentColor" fill-opacity="0.7" />
    <text x="16" y="216" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">Concept 01 knew θ and wanted the legs. Here the legs are known and θ is wanted.</text>
  </svg>
</div>

The same question has a second face you will meet more often. Your robot sits at `(2.0, 1.0)` and a scoring target at `(5.0, 5.0)`; subtracting, as Module 1 does for distance, gives `(3.0, 4.0)` — three metres down-field, four to the left. Which way does the turret point? Again: two components known, one angle wanted.

That is the inverse of everything Concept 01 did, and the tool for it has a name most people get wrong the first three times.

---

## 2. Building the Math: Inverting a Function That Repeats

### Step 1: What inverting a trig function has to mean

`sin 30° = 0.500`. Running that backwards means asking: **what is the angle whose sine is 0.500?**

Look at what the sine function actually does over a long stretch of angles. Concept 01 established that `sin θ` is the y-coordinate of the point at angle θ on the unit circle, so as θ sweeps round and round, the sine rises to 1, falls to −1 and comes back, forever. Draw a horizontal line at height 0.500 and it does not cross the curve once. It crosses infinitely often.

<div style="text-align: center; margin: 20px 0;">
  <svg width="470" height="215" viewBox="0 0 460 210" style="max-width: 100%; height: auto;" role="img" aria-label="The sine curve plotted from minus 420 to plus 420 degrees, with a horizontal line at 0.5 crossing it at minus 330, minus 210, 30, 150 and 390 degrees. The stretch from minus 90 to plus 90 degrees is highlighted as the principal branch.">
    <rect x="190.4" y="45" width="79.2" height="125" fill="#c084fc" fill-opacity="0.1" />
    <line x1="40" y1="105" x2="425" y2="105" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <line x1="230" y1="42" x2="230" y2="172" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <text x="71.6" y="120" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="9" text-anchor="middle">−360°</text>
    <text x="150.8" y="120" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="9" text-anchor="middle">−180°</text>
    <text x="309.2" y="120" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="9" text-anchor="middle">180°</text>
    <text x="388.4" y="120" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="9" text-anchor="middle">360°</text>
    <text x="236" y="54" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="9">+1</text>
    <text x="236" y="164" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="9">−1</text>
    <polyline points="45.2,152.6 49.6,147.1 54.0,140.4 58.4,132.5 62.8,123.8 67.2,114.6 71.6,105.0 76.0,95.4 80.4,86.2 84.8,77.5 89.2,69.6 93.6,62.9 98.0,57.4 102.4,53.3 106.8,50.8 111.2,50.0 115.6,50.8 120.0,53.3 124.4,57.4 128.8,62.9 133.2,69.6 137.6,77.5 142.0,86.2 146.4,95.4 150.8,105.0 155.2,114.6 159.6,123.8 164.0,132.5 168.4,140.4 172.8,147.1 177.2,152.6 181.6,156.7 186.0,159.2 190.4,160.0 194.8,159.2 199.2,156.7 203.6,152.6 208.0,147.1 212.4,140.4 216.8,132.5 221.2,123.8 225.6,114.6 230.0,105.0 234.4,95.4 238.8,86.2 243.2,77.5 247.6,69.6 252.0,62.9 256.4,57.4 260.8,53.3 265.2,50.8 269.6,50.0 274.0,50.8 278.4,53.3 282.8,57.4 287.2,62.9 291.6,69.6 296.0,77.5 300.4,86.2 304.8,95.4 309.2,105.0 313.6,114.6 318.0,123.8 322.4,132.5 326.8,140.4 331.2,147.1 335.6,152.6 340.0,156.7 344.4,159.2 348.8,160.0 353.2,159.2 357.6,156.7 362.0,152.6 366.4,147.1 370.8,140.4 375.2,132.5 379.6,123.8 384.0,114.6 388.4,105.0 392.8,95.4 397.2,86.2 401.6,77.5 406.0,69.6 410.4,62.9 414.8,57.4" fill="none" stroke="currentColor" stroke-opacity="0.45" stroke-width="2" />
    <polyline points="190.4,160.0 193.7,159.5 197.0,158.1 200.3,155.8 203.6,152.6 206.9,148.6 210.2,143.9 213.5,138.5 216.8,132.5 220.1,126.0 223.4,119.2 226.7,112.2 230.0,105.0 233.3,97.8 236.6,90.8 239.9,84.0 243.2,77.5 246.5,71.5 249.8,66.1 253.1,61.4 256.4,57.4 259.7,54.2 263.0,51.9 266.3,50.5 269.6,50.0" fill="none" stroke="#c084fc" stroke-width="3.5" />
    <line x1="40" y1="77.5" x2="425" y2="77.5" stroke="#f43f5e" stroke-width="2" stroke-dasharray="5,4" />
    <text x="428" y="81" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="bold">0.5</text>
    <circle cx="84.8" cy="77.5" r="4.5" fill="#f43f5e" />
    <circle cx="137.6" cy="77.5" r="4.5" fill="#f43f5e" />
    <circle cx="243.2" cy="77.5" r="4.5" fill="#4ade80" />
    <circle cx="296.0" cy="77.5" r="4.5" fill="#f43f5e" />
    <circle cx="401.6" cy="77.5" r="4.5" fill="#f43f5e" />
    <text x="84.8" y="70" fill="#f43f5e" font-family="sans-serif" font-size="9" text-anchor="middle">−330°</text>
    <text x="137.6" y="70" fill="#f43f5e" font-family="sans-serif" font-size="9" text-anchor="middle">−210°</text>
    <text x="243.2" y="70" fill="#4ade80" font-family="sans-serif" font-size="9" text-anchor="middle">30°</text>
    <text x="296.0" y="70" fill="#f43f5e" font-family="sans-serif" font-size="9" text-anchor="middle">150°</text>
    <text x="401.6" y="70" fill="#f43f5e" font-family="sans-serif" font-size="9" text-anchor="middle">390°</text>
    <text x="230" y="188" fill="#c084fc" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">the −90°…+90° window: each height hit exactly once</text>
    <text x="14" y="204" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">"The angle whose sine is 0.5" has infinitely many answers. asin returns the green one.</text>
  </svg>
</div>

Reading off the crossings: 30°, 150°, 390°, 510°, and going the other way −210°, −330°, and on forever in both directions. Two families, `30° + 360k` and `150° + 360k`, for every whole number k.

So the honest answer to "the angle whose sine is 0.5" is *there is no such angle; there are infinitely many*. But a **function** must return exactly one value for each input — that is what makes it a function. The inverse therefore cannot answer the question as asked. It answers a narrower one: **of all the angles whose sine is 0.5, the one lying inside a window we agree on in advance.** That agreed window is the **principal range**, and picking it is not a detail — it is the entire reason the inverse exists at all.

> ### Math!
> ```
>    sin⁻¹ x   =   arcsin x   =   asin x        (three spellings, one function)
> ```
> Read out loud as **"the angle whose sine is x"** — "arcsine of x" is the shorter version. The `⁻¹` marks a **function inverse**, not a reciprocal: `sin⁻¹(0.5)` is 30°, whereas `1 / sin(0.5)` is a completely different and unrelated number. This clash of notation is unfortunate and permanent. Java sidesteps it entirely and calls them `Math.asin`, `Math.acos` and `Math.atan`.

### Step 2: Choosing the three windows

A window has to satisfy two demands. It must be narrow enough that the function hits each output **only once** inside it, or we are back to two answers. And it must be wide enough to reach **every possible output**, or some legal inputs would have no answer at all.

* **Sine.** From −90° to +90° the sine climbs steadily from −1 up to +1, passing through each height exactly once — the purple stretch in the figure. Narrower and you lose values; wider and 150° sneaks in beside 30°. So `asin` returns an angle in **[−90°, +90°]**.
* **Cosine.** The same window fails for cosine: `cos(−60°) = cos(+60°) = 0.500`, two answers already. Cosine is symmetric about 0°, so any window containing 0° in its interior is doomed. Slide it: from 0° to 180° cosine falls steadily from +1 to −1, once through. So `acos` returns an angle in **[0°, 180°]**.
* **Tangent.** Concept 01 showed `tan θ` is the slope of the line at angle θ, and that it blows up at ±90°. Between those two poles the slope sweeps from arbitrarily steep downhill to arbitrarily steep uphill, taking every real number exactly once. So `atan` accepts **any** number and returns an angle in **(−90°, +90°)**, endpoints excluded because no finite slope is vertical.

> ### Math!
> ```
>    asin :  [−1, +1]  →  [ −90°, +90° ]
>    acos :  [−1, +1]  →  [   0°, 180° ]
>    atan :  any number →  ( −90°, +90° )
> ```
> Read the first line out loud as **"arcsine takes a number between −1 and 1 and returns an angle between −90 and +90 degrees."** Square brackets include the endpoint, round brackets exclude it — so `asin(1) = 90°` exactly, while `atan` approaches ±90° and never arrives. Java's versions return **radians**: `Math.asin(0.5)` is `0.5236`, not `30`. Wrap them in `Math.toDegrees` at the boundary, exactly as Concept 01 insisted.

Hold on to one consequence, because everything that goes wrong from here comes out of it: **`atan` can only ever return an angle in the right half of the plane**, quadrants I and IV. Its entire output range is −90° to +90°. Nothing you feed it will make it point left.

### Step 3: The inverse tangent, and why it looks like it works

Back to the wheel. We have the two legs, so the ratio we want is opposite over adjacent — sideways over down-field — and Concept 01's SOH-CAH-TOA says that ratio is the tangent:

```
   tan θ  =  sideways / down-field  =  2.000 / 3.464  =  0.5774
   θ      =  atan(0.5774)           =  30.0°
```

Correct. And this is the trap, because it is correct every single time you try it on a wheel pushing forwards and to the left, which is what you naturally try first.

### Step 4: The first failure — two opposite directions, one answer

Take the turret problem, and give it two targets. Both are 5 m away, using the 3-4-5 triangle from Geometry Concept 01:

* **Target A** at `(x, y) = (3, 4)` — ahead and to the left.
* **Target B** at `(x, y) = (−3, −4)` — behind and to the right. The exact opposite direction.

Form the ratio each time:

```
   Target A:   y / x  =  (+4) / (+3)  =  +1.3333
   Target B:   y / x  =  (−4) / (−3)  =  +1.3333
```

**The same number.** Not close — identical, because the two minus signs cancel in the division. So `atan` cannot help but return the same angle for both:

```
   atan(+1.3333)  =  53.13°       for A  — correct
   atan(+1.3333)  =  53.13°       for B  — the true heading is −126.87°
```

<div style="text-align: center; margin: 20px 0;">
  <svg width="380" height="250" viewBox="0 0 380 250" style="max-width: 100%; height: auto;" role="img" aria-label="Two targets five metres from the robot: A at plus three plus four, and B at minus three minus four, in exactly opposite directions. A red dashed arrow shows the inverse tangent aiming toward A even when the target is B.">
    <line x1="50" y1="125" x2="330" y2="125" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <line x1="180" y1="25" x2="180" y2="225" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <text x="304" y="140" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">x (down-field)</text>
    <text x="186" y="36" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">y (left)</text>
    <line x1="180" y1="125" x2="240" y2="45" stroke="#38bdf8" stroke-width="3" />
    <circle cx="240" cy="45" r="6" fill="#38bdf8" />
    <text x="250" y="42" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">A (+3, +4)</text>
    <text x="250" y="55" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">true +53.13°</text>
    <line x1="180" y1="125" x2="120" y2="205" stroke="#4ade80" stroke-width="3" />
    <circle cx="120" cy="205" r="6" fill="#4ade80" />
    <text x="30" y="222" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">B (−3, −4)</text>
    <text x="30" y="235" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">true −126.87°</text>
    <path d="M 220 125 A 40 40 0 0 0 204 93" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="222" y="112" fill="#c084fc" font-family="sans-serif" font-size="10" font-weight="bold">53.13°</text>
    <path d="M 236 125 A 56 56 0 0 1 146.4 169.8" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="196" y="188" fill="#c084fc" font-family="sans-serif" font-size="10" font-weight="bold">−126.87°</text>
    <line x1="180" y1="125" x2="246" y2="37" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,5" />
    <polygon points="251,30 243,41 238,34" fill="#f43f5e" />
    <text x="86" y="60" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">atan(+1.3333) = 53.13°</text>
    <text x="86" y="74" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">— where the turret goes</text>
    <text x="86" y="88" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">for BOTH targets</text>
    <circle cx="180" cy="125" r="4.5" fill="currentColor" fill-opacity="0.7" />
    <text x="14" y="246" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">Negating both components leaves y/x untouched, so atan cannot tell A from B.</text>
  </svg>
</div>

A robot aiming with `atan` would fire at empty space **exactly 180° from the target**. Not off by a bit, not noisy: reversed. Drive a swerve module with it and the wheel pushes precisely backwards.

And notice this is not a defect in `atan`. `atan` was handed the number `+1.3333` and returned the only angle in its range whose tangent is `+1.3333`. The information was destroyed *before* the call. There were four possible sign pairs going in — `(+,+)`, `(−,+)`, `(−,−)`, `(+,−)` — and the division emits only two possible ratio signs, positive and negative. Two directions per ratio, and the ratio itself does not remember which. Restated geometrically: **negating both x and y rotates the target 180° about the robot and leaves `y/x` unchanged**, so no function of `y/x` alone can ever distinguish a direction from its opposite.

### Step 5: The second failure — x = 0

Now point the wheel straight sideways: down-field `0.0`, sideways `4.0`. Nothing exotic — that is a pure strafe, one of the most-commanded motions there is. The ratio is

```
   y / x  =  4.0 / 0.0        undefined
```

Division by zero. In Java, `double` arithmetic will not throw here — it quietly produces `Infinity`, and `Math.atan(Infinity)` happens to return exactly `+90°`, which is the right answer. That accident is worse than a crash, because it teaches you the code is fine. Three things it hides:

* If the components arrive as **integers** — raw encoder counts, pixel offsets from a camera — `dy / dx` throws `ArithmeticException` and the robot code dies mid-match.
* If the components are **both zero**, `0.0 / 0.0` is `NaN`. `Math.atan(NaN)` is `NaN`, and `NaN` fails every comparison silently, so your clamps and safety checks all pass it straight through into a motor command.
* You are computing the commonest sideways heading on the field by relying on infinity arithmetic to bail you out. That is not a design; it is a coincidence you inherited.

### Step 6: atan2 — stop dividing

Both failures have one cause: we destroyed information by dividing before we asked the question. The fix is to **stop dividing** and hand the function both components separately, so it can look at their signs itself.

That function is `atan2`.

> ### Math!
> ```
>    θ = atan2(y, x)
> ```
> Read out loud as **"theta equals a-tan-two of y and x"**. Its defining property is exactly the undoing of Concept 01: for any point other than the origin, with `r = √(x² + y²)`, `atan2(y, x)` is the one angle θ in the range `(−180°, +180°]` satisfying
> ```
>    x = r · cos θ        and        y = r · sin θ
> ```
> Concept 01 went θ → `(x, y)`. This goes `(x, y)` → θ. The half-open range means −180° is not a legal answer and +180° is; pointing straight backwards reports `+180°`.

You can build it yourself out of `atan`, and doing so is the point — there is no magic inside. Two steps:

**1. Get the size of the turn, ignoring direction.** Feed `atan` the ratio of the *magnitudes*:

```
   a = atan( |y| / |x| )        always between 0° and 90°
```

This is Concept 01's **reference angle** — the acute angle between the ray and the horizontal axis.

**2. Place it in the correct quadrant using the two signs.** The signs are still in your hand, because you never divided them away:

```
   sign of x   sign of y   quadrant   θ = atan2(y, x)     for (±3, ±4), a = 53.13°
   ----------------------------------------------------------------------------
       +           +          I             a                    +53.13°
       −           +          II         180° − a                +126.87°
       −           −          III        a − 180°                −126.87°
       +           −          IV           − a                   −53.13°
```

Four distinct answers from the same reference angle, all four targets 5 m away, and no two of them confusable.

<div style="text-align: center; margin: 20px 0;">
  <svg width="400" height="300" viewBox="0 0 400 300" style="max-width: 100%; height: auto;" role="img" aria-label="Four targets at plus or minus three and plus or minus four, one in each quadrant, all five metres from the robot. Their atan2 angles are 53.13, 126.87, minus 126.87 and minus 53.13 degrees, with arcs drawn at four different radii.">
    <line x1="50" y1="140" x2="350" y2="140" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <line x1="190" y1="25" x2="190" y2="258" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <text x="316" y="155" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">x</text>
    <text x="197" y="36" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">y</text>
    <line x1="190" y1="140" x2="250" y2="60" stroke="#38bdf8" stroke-width="2.5" />
    <circle cx="250" cy="60" r="6" fill="#38bdf8" />
    <text x="258" y="56" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">(+3, +4)</text>
    <text x="258" y="70" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">+53.13°</text>
    <line x1="190" y1="140" x2="130" y2="60" stroke="#4ade80" stroke-width="2.5" />
    <circle cx="130" cy="60" r="6" fill="#4ade80" />
    <text x="58" y="56" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">(−3, +4)</text>
    <text x="58" y="70" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">+126.87°</text>
    <line x1="190" y1="140" x2="130" y2="220" stroke="#fbbf24" stroke-width="2.5" />
    <circle cx="130" cy="220" r="6" fill="#fbbf24" />
    <text x="58" y="238" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">(−3, −4)</text>
    <text x="58" y="252" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">−126.87°</text>
    <line x1="190" y1="140" x2="250" y2="220" stroke="#f43f5e" stroke-width="2.5" />
    <circle cx="250" cy="220" r="6" fill="#f43f5e" />
    <text x="258" y="238" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">(+3, −4)</text>
    <text x="258" y="252" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">−53.13°</text>
    <path d="M 224 140 A 34 34 0 0 0 210.4 112.8" fill="none" stroke="#c084fc" stroke-width="2" />
    <path d="M 240 140 A 50 50 0 0 0 160 100" fill="none" stroke="#c084fc" stroke-width="2" />
    <path d="M 256 140 A 66 66 0 0 1 150.4 192.8" fill="none" stroke="#c084fc" stroke-width="2" />
    <path d="M 272 140 A 82 82 0 0 1 239.2 205.6" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="226" y="128" fill="#c084fc" font-family="sans-serif" font-size="9" font-weight="bold">I</text>
    <text x="196" y="94" fill="#c084fc" font-family="sans-serif" font-size="9" font-weight="bold">II</text>
    <text x="192" y="212" fill="#c084fc" font-family="sans-serif" font-size="9" font-weight="bold">III</text>
    <text x="266" y="176" fill="#c084fc" font-family="sans-serif" font-size="9" font-weight="bold">IV</text>
    <circle cx="190" cy="140" r="4.5" fill="currentColor" fill-opacity="0.7" />
    <text x="14" y="288" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">One reference angle a = 53.13°, four sign pairs, four distinct headings. Arcs above the axis run counter-clockwise (positive); below it, clockwise (negative).</text>
  </svg>
</div>

The axes need no special pleading — they fall straight out of the same rule. `x > 0, y = 0` gives `0°`; `x = 0, y > 0` gives `+90°`; `x < 0, y = 0` gives `+180°`; `x = 0, y < 0` gives `−90°`. The pure strafe that broke Step 5 is `atan2(4.0, 0.0) = +90.0°`, computed with no division and no special case, because the magnitude ratio `|y| / |x|` is only reached when `x` is nonzero — the sign table handles the axes on its own.

This is Concept 01's Step 5 running in reverse. There, you found the reference angle and read the signs off the picture to *evaluate* `cos 150°`. Here you read the signs off the components to *recover* the angle. Same table, opposite direction.

### Step 7: The argument order is backwards, and it is a real bug

`atan2` takes **y first**. The reason is that it is standing in for `tan θ = y / x`, and the numerator is written first — but almost nobody guesses it, because every coordinate pair you have ever written puts x first.

Swapping the arguments does not crash and does not produce anything obviously silly. It **mirrors the heading about the 45° diagonal**, because for a first-quadrant point the two reference angles are complementary:

```
   atan2(4, 3) = 53.13°           atan2(3, 4) = 36.87°           53.13 + 36.87 = 90
```

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="195" viewBox="0 0 300 195" style="max-width: 100%; height: auto;" role="img" aria-label="Two rays from the origin at 53.13 degrees and 36.87 degrees, mirror images about a dashed 45 degree line, showing that swapping the arguments of atan2 reflects the heading.">
    <line x1="40" y1="155" x2="280" y2="155" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <line x1="60" y1="175" x2="60" y2="35" stroke="currentColor" stroke-opacity="0.4" stroke-width="1.5" />
    <line x1="60" y1="155" x2="151.9" y2="63.1" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.5" stroke-dasharray="5,4" />
    <text x="156" y="60" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">45° mirror</text>
    <line x1="60" y1="155" x2="138" y2="51" stroke="#38bdf8" stroke-width="3" />
    <circle cx="138" cy="51" r="5.5" fill="#38bdf8" />
    <text x="86" y="42" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">atan2(4, 3) = 53.13°</text>
    <line x1="60" y1="155" x2="164" y2="77" stroke="#f43f5e" stroke-width="3" />
    <circle cx="164" cy="77" r="5.5" fill="#f43f5e" />
    <text x="172" y="98" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">atan2(3, 4) = 36.87°</text>
    <text x="172" y="112" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">(arguments swapped)</text>
    <circle cx="60" cy="155" r="4.5" fill="currentColor" fill-opacity="0.7" />
    <text x="14" y="186" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">A swapped call reflects the heading about 45°, so a 45° test passes and hides it.</text>
  </svg>
</div>

Which means a robot tested by driving it diagonally forward-left — at or near 45°, the natural thing to try — behaves *perfectly*, because 45° is a fixed point of the mirror. The bug only surfaces later, off the diagonal, under a match load. Write the order out in a comment every time.

Worse, WPILib's `Rotation2d` constructor takes `(x, y)` — the opposite order — so a single Java file can legitimately contain both conventions. Both are correct. Neither is guessable.

### Step 8: atan2(0, 0)

The origin has no direction. There is genuinely no angle to return, because every angle satisfies `0 = r cos θ` when `r = 0`. Java's `Math.atan2(0.0, 0.0)` returns `0.0` by convention rather than erroring — which means a **zero velocity command silently reads as "point straight down-field"**, and the wheels snap to 0° for no reason at the end of every path.

The fix is a magnitude check before the call, not after:

```
   if √(x² + y²) < ε        keep the previous commanded angle
   else                     θ = atan2(y, x)
```

Holding the last angle is the right behaviour for a swerve module: a stopped wheel should stay where it is pointed, ready for the next command.

### Step 9: The loop closes

Feed the opening problem back in. `atan2(2.000, 3.464) = 30.0°`, and the speed was already `4.000` m/s — exactly the pair Concept 01 started from. The two concepts are inverses, and now you can go both ways.

For the turret: the difference `(3.0, 4.0)` gives `atan2(4.0, 3.0) = +53.13°` measured **in the field frame**. Concept 03 warned that a turret does not live in the field frame — if the robot is itself facing 20°, the turret must go to `53.13° − 20° = 33.13°` relative to the chassis. Subtracting two angles can push the result outside ±180°, and repairing that is Concept 05's job.

---

## 3. Solving It in Code (Java & WPILib)

### First Principles (Java)

```java
// The inverse of Concept 01: two components in, angle and speed out.
double downfieldMps = 3.4641;   // meters per second
double sidewaysMps  = 2.0000;   // meters per second

double speedMps  = Math.hypot(downfieldMps, sidewaysMps);          // 4.0000 m/s
double angleDeg  = Math.toDegrees(Math.atan2(sidewaysMps, downfieldMps));
System.out.printf("speed %.4f  angle %.2f deg%n", speedMps, angleDeg);
// speed 4.0000  angle 30.00 deg   <- exactly what Concept 01 started from
```

Building `atan2` by hand from `atan`, so nothing is hidden — this is the sign table from Step 6, line for line:

```java
/** Same contract as Math.atan2: returns radians in (-PI, PI]. */
static double atan2FromScratch(double y, double x) {
    if (x == 0.0 && y == 0.0) return 0.0;                 // no direction exists
    if (x == 0.0) return (y > 0) ? Math.PI / 2 : -Math.PI / 2;
    if (y == 0.0) return (x > 0) ? 0.0 : Math.PI;

    double a = Math.atan(Math.abs(y) / Math.abs(x));      // reference angle, 0..PI/2
    if (x > 0 && y > 0) return a;                         // quadrant I
    if (x < 0 && y > 0) return Math.PI - a;               // quadrant II
    if (x < 0 && y < 0) return a - Math.PI;               // quadrant III
    return -a;                                            // quadrant IV
}
```

Run both against the four targets and watch `atan` collapse the plane in half:

```java
double[] xs = {  3.0, -3.0, -3.0,  3.0,  0.0,  0.0 };
double[] ys = {  4.0,  4.0, -4.0, -4.0,  4.0,  0.0 };
for (int i = 0; i < xs.length; i++) {
    double x = xs[i], y = ys[i];
    double naive = Math.toDegrees(Math.atan(y / x));          // one argument
    double good  = Math.toDegrees(Math.atan2(y, x));          // two arguments
    double mine  = Math.toDegrees(atan2FromScratch(y, x));
    System.out.printf("(%+.0f,%+.0f)  atan %8.2f   atan2 %8.2f   mine %8.2f%n",
                      x, y, naive, good, mine);
}
// (+3,+4)  atan    53.13   atan2    53.13   mine    53.13
// (-3,+4)  atan   -53.13   atan2   126.87   mine   126.87    <- 180 deg out
// (-3,-4)  atan    53.13   atan2  -126.87   mine  -126.87    <- 180 deg out
// (+3,-4)  atan   -53.13   atan2   -53.13   mine   -53.13
// (+0,+4)  atan    90.00   atan2    90.00   mine    90.00    <- 4.0/0.0 = Infinity
// (+0,+0)  atan      NaN   atan2     0.00   mine     0.00    <- 0.0/0.0 = NaN
```

The hand-built version agrees with `Math.atan2` on every row, which is the point: `atan2` is `atan` plus a sign table, and you have just written the sign table.

### In a Robot Project (Java & WPILib)

```java
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.math.geometry.Translation2d;

// The Rotation2d(x, y) constructor calls atan2 internally and normalises the
// pair to length 1. Note the argument order: (x, y), NOT atan2's (y, x).
Rotation2d wheelAngle = new Rotation2d(3.4641, 2.0000);
double deg = wheelAngle.getDegrees();                    // 30.00  <- same as above

// Bearing to a target, straight from a position difference.
Translation2d robot  = new Translation2d(2.0, 1.0);
Translation2d target = new Translation2d(5.0, 5.0);
Translation2d delta  = target.minus(robot);              // (3.0, 4.0)

double range   = delta.getNorm();                        // 5.00 m
Rotation2d bearing = delta.getAngle();                   // 53.13 deg, field frame

// Turret command is relative to the chassis, so subtract the robot's heading.
Rotation2d turret = bearing.minus(robotPose.getRotation());   // 33.13 deg at heading 20

// The (0, 0) guard from Step 8, which no library will apply for you.
// lastTurret is a field, holding whatever was commanded on the previous loop.
if (delta.getNorm() > 1e-6) {
    lastTurret = turret;
}
turretSubsystem.setSetpoint(lastTurret);
```

Both tiers produce the same numbers — `30.00°` for the wheel, `53.13°` and `5.00` m for the target — because `Rotation2d(x, y)` and `Translation2d.getAngle()` are `Math.atan2` with a different argument order and a normalisation bolted on.

---

## 4. Bridge to Real Systems

### Every heading a robot computes

`atan2` is the single most-called trig function in a drivetrain. `SwerveDriveKinematics` turns a chassis velocity into four module states, and the last thing it does for each wheel is convert that wheel's two velocity components into a `Rotation2d` — an `atan2` per module, fifty times a second. Vision code turns an AprilTag's position relative to the camera into a bearing. `Translation2d.getAngle()`, `Rotation2d(x, y)`, `Transform2d.getTranslation().getAngle()` — every one of them is this function wearing a WPILib name.

The reason the library never stores a bare angle is Step 5 and Step 8 combined. `Rotation2d` holds the `(cos, sin)` pair, calls `atan2` once at construction, and hands back the angle only when something asks. No division, no `Infinity`, no quadrant to lose.

### Cartesian to polar, and the phase of a signal

Outside robotics, the same operation is called **converting Cartesian coordinates to polar**: a point `(x, y)` becomes a magnitude `r = √(x² + y²)` and an angle `θ = atan2(y, x)`. The magnitude is Module 1's distance formula; the angle is this concept. That pair shows up wherever two orthogonal measurements have to become "how big, and which way".

Signal processing leans on it hardest. A discrete Fourier transform reports each frequency bin as two numbers, a real part and an imaginary part, and the two questions asked of a bin are *how much of this frequency is present* and *where in its cycle did it start*. The first is the magnitude; the second is the **phase**, computed as `atan2(imaginary, real)` — which is exactly what NumPy's `numpy.angle` calls. The failure mode is identical to the turret's: use the ratio instead of the pair and a signal is reported half a cycle out of step, which in radar interferometry or beamforming puts a target on the wrong side of the antenna.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1

The robot is at field position `(6.0, 2.0)` and an AprilTag is at `(2.0, 5.0)`. Find the range and the field-frame bearing to the tag. Then say what `atan(dy / dx)` would have returned, and how far wrong the turret would end up.

**Solution:**

1. **Difference.** `dx = 2.0 − 6.0 = −4.0`, `dy = 5.0 − 2.0 = +3.0`. Behind the robot's down-field axis and to the left.
2. **Range.** `√((−4.0)² + (3.0)²) = √(16.0 + 9.0) = √25.0 = 5.0` m — a 3-4-5 triangle again.
3. **Reference angle.** `a = atan(|3.0| / |−4.0|) = atan(0.7500) = 36.87°`.
4. **Quadrant.** `x < 0`, `y > 0`, so Quadrant II, and the table says `θ = 180° − a = 180° − 36.87° = 143.13°`.
5. **What atan gives.** `dy / dx = 3.0 / (−4.0) = −0.7500`, and `atan(−0.7500) = −36.87°`. `atan` can only answer in the right half-plane, so it reports a heading forward and to the right.
6. **How wrong.** `143.13° − (−36.87°) = 180.00°` — exactly reversed, as it must be, since `(−4, +3)` and `(+4, −3)` share the ratio `−0.75`.

---

### Checkpoint 2

A wheel is commanded to `down-field = 0.0`, `sideways = −2.5` m/s — a pure strafe to the right. Work out what `atan(y / x)` does in Java, what `atan2` gives, and what happens one loop later when the command becomes `(0.0, 0.0)`.

**Solution:**

1. **The naive ratio.** `−2.5 / 0.0` is not an exception for Java `double`s; it evaluates to `−Infinity`. `Math.atan(Double.NEGATIVE_INFINITY)` returns `−π/2`, so `Math.toDegrees` gives `−90.0°` — which is the correct heading, obtained entirely by luck. Change the components to `int`s and the same expression throws `ArithmeticException`.
2. **atan2.** `Math.atan2(−2.5, 0.0) = −π/2 = −90.0°`. Step 6's axis rule, no division performed, no coincidence involved.
3. **The stop command.** `0.0 / 0.0` is `NaN`, so the naive path produces `NaN` degrees, and `NaN` fails every comparison — including any `if (angle > limit)` guard — so it reaches the motor controller unchallenged.
4. **atan2 at the origin.** `Math.atan2(0.0, 0.0)` returns `0.0`, so the wheel would snap from −90° round to 0° the instant the robot stops. Correct behaviour is Step 8's guard: `if (Math.hypot(x, y) < 1e-6) keep the previous angle`, leaving the wheel at −90°.

---

### Deep Dive 1

`atan2` is not the only way to recover an angle from components. Try building the same thing out of `acos` instead: given `(x, y)` and `r = √(x² + y²)`, the cosine of the heading is `x / r`, so `acos(x / r)` is a candidate. Work out for which points it is correct and for which it is wrong, using the fact that `acos` returns `0°` to `180°`. Then find the one-line sign patch that repairs it, and test your repaired version against `Math.atan2` on the four targets `(±3, ±4)`. Finally, argue which of the two constructions you would trust when `r` is very small, and why.

### Deep Dive 2

Step 7 claimed a swapped `atan2(x, y)` reflects the heading about the 45° line, so a 45° test passes. Find **every** heading that survives the swap unchanged — there is one more besides 45°, and the sign table tells you where. Then design the smallest set of test targets that is guaranteed to catch a swapped call, and explain why testing "straight ahead" alone is not enough on its own to be convincing. For extra bite: Microsoft Excel's `ATAN2` takes its arguments as `(x, y)`, the reverse of Java, Python, C and JavaScript. Work out what happens to a scouting spreadsheet that copies a heading formula out of robot code, and which cells would look right.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../03_concept_coordinate_frames/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 03: Coordinate Frames</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../05_concept_angle_wrapping_swerve/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 05: Angle Wrapping →</a></div>
</div>
