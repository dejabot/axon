# Concept 02: Rotating a Vector

> **▶ Interactive Demo: [Rotation & Field-Oriented Drive Visualizer](demo.html)**
>
> Spin the robot's heading and watch the same joystick push turn into completely different wheel commands. Toggle between the driver's view and the robot's view of the identical motion.

<iframe src="demo.html" width="100%" height="560" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Robot Is Not Facing Forward

A driver stands behind the alliance wall holding a gamepad. They push the left stick straight away from their body, meaning: *go to the far end of the field*. That instruction lives in the **field frame**, and in field coordinates it means "increase X".

But the robot's motors have never heard of the field. A swerve drive accepts a forward speed and a strafe speed measured relative to **its own chassis** — where its own front bumper is pointing. And at this instant the robot happens to be spun 40 degrees counter-clockwise, because it just finished picking up a game piece.

Send the stick values straight through to the motors and the robot drives 40 degrees off course, diagonally into the wall. Every driver who has ever fought a robot that "goes the wrong way when it's turned around" has met this problem. The fix is called **field-oriented drive**, and it is one operation: rotate the command vector from the field frame into the robot frame.

<div style="text-align: center; margin: 20px 0;">
  <svg width="380" height="200" viewBox="0 0 380 200" style="max-width: 100%; height: auto;" role="img" aria-label="A robot rotated forty degrees, showing the driver's intended field-frame direction versus the robot's own forward axis.">
    <line x1="30" y1="160" x2="350" y2="160" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <line x1="30" y1="160" x2="30" y2="25" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <text x="320" y="177" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="11">Field X</text>
    <text x="36" y="34" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="11">Field Y</text>
    <g transform="translate(170,100)">
      <g transform="rotate(-40)">
        <rect x="-32" y="-32" width="64" height="64" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="2" rx="6" />
        <line x1="0" y1="0" x2="86" y2="0" stroke="#c084fc" stroke-width="3" />
        <polygon points="86,0 76,-6 76,6" fill="#c084fc" />
        <text x="52" y="-12" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">robot forward</text>
      </g>
      <line x1="0" y1="0" x2="110" y2="0" stroke="#fbbf24" stroke-width="3" stroke-dasharray="6,4" />
      <polygon points="110,0 100,-6 100,6" fill="#fbbf24" />
      <text x="60" y="26" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">driver wants this way</text>
      <path d="M 44 0 A 44 44 0 0 0 33.7 -28.3" fill="none" stroke="#4ade80" stroke-width="2" />
      <text x="46" y="-30" fill="#4ade80" font-family="sans-serif" font-size="12" font-weight="bold">θ = 40°</text>
    </g>
  </svg>
</div>

To build that operation we need to answer a smaller question first: **when a vector is rotated by an angle θ, what are its new coordinates?**

---

## 2. Building the Math: What Rotation Does to Coordinates

### Step 1: The trigonometry we actually need

Start with a plain right triangle. Pick one of its non-right angles and call it θ. The three sides get names relative to that choice: the side touching θ that is not the hypotenuse is the **adjacent** side, the side across from θ is the **opposite** side, and the long side facing the right angle is the **hypotenuse**.

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="170" viewBox="0 0 300 170" style="max-width: 100%; height: auto;" role="img" aria-label="A right triangle labeled with opposite, adjacent and hypotenuse relative to the angle theta.">
    <polygon points="40,140 240,140 240,40" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="2" />
    <rect x="222" y="122" width="18" height="18" fill="none" stroke="currentColor" stroke-opacity="0.5" stroke-width="1.5" />
    <path d="M 80 140 A 40 40 0 0 0 71.5 115.5" fill="none" stroke="#4ade80" stroke-width="2" />
    <text x="84" y="132" fill="#4ade80" font-family="sans-serif" font-size="13" font-weight="bold">θ</text>
    <text x="120" y="158" fill="currentColor" fill-opacity="0.75" font-family="sans-serif" font-size="12">adjacent</text>
    <text x="248" y="95" fill="currentColor" fill-opacity="0.75" font-family="sans-serif" font-size="12">opposite</text>
    <text x="105" y="82" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold">hypotenuse</text>
  </svg>
</div>

The ratios between those sides depend only on θ, never on how big you draw the triangle — scale the triangle up and both sides grow by the same factor, leaving the ratio untouched. Three of those ratios get names, remembered by the mnemonic **SOH-CAH-TOA**:

$$
\begin{aligned}
\text{SOH:} \quad \sin\theta &= \frac{\text{Opposite}}{\text{Hypotenuse}} \\[4pt]
\text{CAH:} \quad \cos\theta &= \frac{\text{Adjacent}}{\text{Hypotenuse}} \\[4pt]
\text{TOA:} \quad \tan\theta &= \frac{\text{Opposite}}{\text{Adjacent}}
\end{aligned}
$$

Now shrink the hypotenuse to exactly 1. Dividing by 1 changes nothing, so the two ratios collapse into something much easier to hold in your head: the adjacent side simply *is* `cos θ`, and the opposite side simply *is* `sin θ`. Drawn on a circle of radius 1 centered at the origin — the **unit circle** — a point at angle θ sits at coordinates `(cos θ, sin θ)`.

That last sentence is the entire foundation of what follows. It also extends the definition past the right triangle: a right triangle cannot have a 150-degree angle, but a point on a circle can sit at 150 degrees perfectly well, and its coordinates are still called `(cos 150°, sin 150°)`. The circle is the general definition; the triangle is the special case.

### Step 2: Track only the basis vectors

Here is the trick that makes rotation easy. Instead of asking what happens to some arbitrary point, ask what happens to two very specific ones:

* `î` (read "i-hat"), the unit vector pointing along X, at coordinates `(1, 0)`.
* `ĵ` (read "j-hat"), the unit vector pointing along Y, at coordinates `(0, 1)`.

These two are the **basis vectors**, and every other vector is built from them. The vector `(3, 2)` is literally `3` steps along `î` plus `2` steps along `ĵ`.

Now rotate the whole plane counter-clockwise by θ.

**Where does `î` go?** It started on the unit circle at angle 0. Rotating by θ leaves it on the unit circle at angle θ. By Step 1, it lands at `(cos θ, sin θ)`.

**Where does `ĵ` go?** It started on the unit circle at angle 90°, so it lands at angle `θ + 90°`, at coordinates `(cos(θ + 90°), sin(θ + 90°))`. You do not need to memorize the angle-addition identities to simplify this — just look at the picture. A vector 90 degrees counter-clockwise from `(cos θ, sin θ)` is `(−sin θ, cos θ)`: rotating any vector a quarter turn counter-clockwise swaps its two components and negates the new first one. So `ĵ` lands at `(−sin θ, cos θ)`.

<div style="text-align: center; margin: 20px 0;">
  <svg width="300" height="240" viewBox="0 0 300 240" style="max-width: 100%; height: auto;" role="img" aria-label="The unit circle showing i-hat rotating to cos theta sin theta and j-hat rotating to minus sin theta cos theta.">
    <circle cx="150" cy="130" r="85" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="1.5" />
    <line x1="45" y1="130" x2="255" y2="130" stroke="currentColor" stroke-opacity="0.3" stroke-width="1" />
    <line x1="150" y1="235" x2="150" y2="25" stroke="currentColor" stroke-opacity="0.3" stroke-width="1" />
    <line x1="150" y1="130" x2="235" y2="130" stroke="currentColor" stroke-opacity="0.45" stroke-width="2" stroke-dasharray="4,3" />
    <line x1="150" y1="130" x2="150" y2="45" stroke="currentColor" stroke-opacity="0.45" stroke-width="2" stroke-dasharray="4,3" />
    <text x="238" y="126" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="12" font-weight="bold">î</text>
    <text x="132" y="42" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="12" font-weight="bold">ĵ</text>
    <line x1="150" y1="130" x2="215" y2="75" stroke="#38bdf8" stroke-width="3" />
    <polygon points="215,75 204,77 209,86" fill="#38bdf8" />
    <text x="196" y="66" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">(cos θ, sin θ)</text>
    <line x1="150" y1="130" x2="95" y2="65" stroke="#4ade80" stroke-width="3" />
    <polygon points="95,65 99,76 106,69" fill="#4ade80" />
    <text x="20" y="56" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">(−sin θ, cos θ)</text>
    <path d="M 196 130 A 46 46 0 0 0 182 97" fill="none" stroke="#fbbf24" stroke-width="2" />
    <text x="192" y="112" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold">θ</text>
  </svg>
</div>

### Step 3: Assemble the general rule

Rotation is **linear**, which means two things: rotating a scaled vector is the same as scaling the rotated vector, and rotating a sum is the same as summing the rotations. Both are obvious once said aloud — spinning a picture does not change how many times one arrow fits into another, and it does not change how two arrows join tip to tail.

So take any vector `v = (x, y)`, write it as `x·î + y·ĵ`, and rotate:

$$
\begin{aligned}
R(v) &= R(x \cdot \hat{\imath} + y \cdot \hat{\jmath}) \\[4pt]
     &= x \cdot R(\hat{\imath}) + y \cdot R(\hat{\jmath}) && \text{(linearity)} \\[4pt]
     &= x \cdot (\cos\theta,\ \sin\theta) + y \cdot (-\sin\theta,\ \cos\theta) && \text{(Step 2)}
\end{aligned}
$$

Adding those two scaled vectors component by component gives the result:

$$
\begin{aligned}
x' &= x \cdot \cos\theta - y \cdot \sin\theta \\[4pt]
y' &= x \cdot \sin\theta + y \cdot \cos\theta
\end{aligned}
$$

Two lines of arithmetic, and everything else in this concept is a consequence of them.

**Sanity check it.** Set θ = 0: `cos 0 = 1`, `sin 0 = 0`, so `x' = x` and `y' = y`. Rotating by nothing changes nothing. Now set θ = 90°: `cos 90° = 0`, `sin 90° = 1`, giving `x' = −y` and `y' = x`. Feed in `(1, 0)` and you get `(0, 1)` — X really did swing round to Y. The formula behaves.

> ### Math!
> The prime mark in `x'` and `y'` is read **"x-prime"** and **"y-prime"**. It is not a derivative here — it simply means "the new version of", and it is the standard way to name a transformed copy of something without inventing a fresh letter.
>
> Notice what the four coefficients in those two equations are. Reading down the columns, `(cos θ, sin θ)` is exactly where `î` landed, and `(−sin θ, cos θ)` is exactly where `ĵ` landed. That is not a coincidence, and it generalizes: these four numbers are usually packed into a single object called a **matrix**, and the fact that its columns are the images of the basis vectors turns out to be true of every matrix, not just this one. The linear algebra module derives what that object is and how to multiply by it. For now the two scalar equations are all you need, and computing them by hand is worth doing — it makes the abstraction land properly when it arrives.

### Step 4: Rotation preserves length

A rotation should not stretch anything. Let us confirm the formula agrees, by computing the new squared length:

$$
{x'}^2 + {y'}^2 = (x \cos\theta - y \sin\theta)^2 + (x \sin\theta + y \cos\theta)^2
$$

Expand both squares:

$$
\begin{aligned}
&= x^2 \cos^2\theta - 2xy \cos\theta \sin\theta + y^2 \sin^2\theta \\[4pt]
&\phantom{=} + x^2 \sin^2\theta + 2xy \sin\theta \cos\theta + y^2 \cos^2\theta
\end{aligned}
$$

The two middle terms are identical apart from sign, so they cancel. Grouping what remains:

$$
= x^2 (\cos^2\theta + \sin^2\theta) + y^2 (\sin^2\theta + \cos^2\theta)
$$

And `cos²θ + sin²θ = 1` — which is just the Pythagorean theorem from Concept 01 applied to a triangle with hypotenuse 1. So:

$$
{x'}^2 + {y'}^2 = x^2 + y^2
$$

Length out equals length in, for every angle and every vector. A transformation that preserves all distances is called **rigid**, and rigid is exactly what you want when the thing being transformed is a physical robot.

### Step 5: Undoing a rotation is free

To rotate back, rotate by `−θ`. Two facts about the unit circle make this cheap: `cos(−θ) = cos θ` (a point and its mirror image below the X-axis share the same x-coordinate) while `sin(−θ) = −sin θ` (their y-coordinates are opposite). Substituting those into our two equations:

$$
\begin{aligned}
x' &= \phantom{-} x \cdot \cos\theta + y \cdot \sin\theta \\[4pt]
y' &= -x \cdot \sin\theta + y \cdot \cos\theta
\end{aligned}
$$

Compare the coefficients with the forward rotation from Step 3. They are the same four numbers — `cos θ`, `sin θ`, `−sin θ`, `cos θ` — merely rearranged. Undoing a rotation costs you nothing beyond flipping one sign. There is no division, no square root, and nothing that can lose precision.

That is worth appreciating, because "undo this transformation" is usually an expensive and numerically delicate operation. For rotations it is almost free, and the reason will become sharp in the linear algebra module: the rearrangement you just spotted has a name, and rotations belong to a special family of transformations for which reversing is only ever a relabeling.

### Step 6: Rotations compose by adding angles

Rotate by β, then by α. Physically the result must be a single rotation by `α + β` — there is no other outcome a turn followed by a turn could have.

Now do it algebraically. Take `î = (1, 0)`, rotate it by β to get `(cos β, sin β)`, then feed that result back through the Step 3 equations with angle α:

$$
\begin{aligned}
x'' &= \cos\beta \cdot \cos\alpha - \sin\beta \cdot \sin\alpha \\[4pt]
y'' &= \cos\beta \cdot \sin\alpha + \sin\beta \cdot \cos\alpha
\end{aligned}
$$

But we already know where a single rotation by `α + β` sends `î`: to `(cos(α + β), sin(α + β))`. Both routes must land on the same point, so the expressions must be equal. You have just derived the angle-addition identities from geometry, rather than memorizing them:

$$
\begin{aligned}
\cos(\alpha + \beta) &= \cos\alpha \cos\beta - \sin\alpha \sin\beta \\[4pt]
\sin(\alpha + \beta) &= \sin\alpha \cos\beta + \cos\alpha \sin\beta
\end{aligned}
$$

One caution: in 2D we get lucky, because `α + β = β + α`, so the order you apply two rotations in cannot matter. That luck runs out in three dimensions. Turn a book 90 degrees to the right and then 90 degrees forward, then reset and do it in the opposite order — the book ends up in two visibly different orientations. Concept 07 returns to this when 3D rotations and quaternions arrive, and it is the root of gimbal lock.

### Step 7: Rotating about a point that is not the origin

The formula spins everything around `(0, 0)`. To pivot about some other center `c` — say a swerve module's location, or the robot's center of mass — use the standard three-step sandwich: subtract `c` to move the pivot to the origin, rotate, then add `c` back.

$$
v_{\text{rotated}} = R(\theta) \cdot (v - c) + c
$$

Getting the order wrong here is one of the most common geometry bugs in robot code, and it fails in a distinctive way: the object rotates correctly but also swings around the field on a large arc, because you rotated its position vector along with its shape.

### A note on sign conventions

Everything above assumes θ grows **counter-clockwise** and that Y points up. That is the WPILib convention and the mathematical norm. Screen graphics traditionally put Y pointing *down*, which silently flips the direction of every rotation. When a visualizer spins the wrong way, this is almost always why — and it is why the companion demo negates its angle before handing it to the canvas.

---

## 3. Solving It in Code (Java & WPILib)

### First-Principles Java

```java
// Rotate a vector counter-clockwise by theta, about the origin.
static double[] rotate(double x, double y, double thetaRadians) {
    double c = Math.cos(thetaRadians);
    double s = Math.sin(thetaRadians);
    return new double[] { x * c - y * s,      // x' = x cos - y sin
                          x * s + y * c };    // y' = x sin + y cos
}

// Field-oriented drive: the driver's field-frame command, expressed in robot terms.
double fieldVx = 3.0;    // driver pushes 3.0 m/s toward the far end of the field
double fieldVy = 0.0;
double headingRadians = Math.toRadians(40.0);   // gyro says the robot is turned 40 deg

// Rotate by NEGATIVE heading: we are going from the field frame into the robot frame.
double[] robotFrame = rotate(fieldVx, fieldVy, -headingRadians);

System.out.printf("forward %.2f m/s, strafe %.2f m/s%n", robotFrame[0], robotFrame[1]);
// forward 2.30 m/s, strafe -1.93 m/s
```

The minus sign on the heading is the part worth pausing on. The robot is rotated `+40°` relative to the field, so the field is rotated `−40°` relative to the robot. Transforming a vector *into* a frame uses the opposite sign from rotating a vector *within* a frame. Concept 03 makes this precise; for now, the sanity check is that the robot must steer to its own right (a negative strafe) to compensate for having been turned to the left.

### Production WPILib Equivalent

```java
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.math.geometry.Translation2d;
import edu.wpi.first.math.kinematics.ChassisSpeeds;

Rotation2d heading = Rotation2d.fromDegrees(40.0);

// Rotation2d caches cos and sin at construction, so repeated use costs no trig calls.
Translation2d fieldCommand = new Translation2d(3.0, 0.0);
Translation2d robotCommand = fieldCommand.rotateBy(heading.unaryMinus());

// Rotations compose by adding angles - exactly Step 6.
Rotation2d combined = heading.plus(Rotation2d.fromDegrees(15.0));   // 55 degrees

// In practice the whole field-oriented conversion is one library call:
ChassisSpeeds speeds =
    ChassisSpeeds.fromFieldRelativeSpeeds(3.0, 0.0, 0.0, heading);
```

`Rotation2d` stores `cos θ` and `sin θ` rather than θ itself. That is a direct consequence of Step 3: the sine and cosine are the only things the rotation formula ever asks for, so computing them once at construction removes trigonometry from the 50 Hz control loop entirely.

---

## 4. Bridge to Machine Learning & Modern Autonomy

The two equations you just derived are, unmodified, the mechanism behind **Rotary Position Embeddings (RoPE)** — the position-encoding scheme used in Llama, Mistral, Qwen and most other current large language models.

A transformer processes all tokens in parallel, so on its own it cannot tell "the robot hit the wall" from "the wall hit the robot". It needs position information injected. RoPE does this by taking each token's embedding vector, chopping its hundreds of dimensions into consecutive pairs, and treating every pair as a little 2D vector — then rotating pair number `k` of the token at position `m` by the angle `m · θₖ`. That is precisely `R(θ)` from Step 3, applied a few hundred times per token.

Two properties derived above are exactly why this works rather than wrecking the model. **Length preservation (Step 4)** means the rotation cannot inflate or shrink any embedding, so attention scores stay numerically well behaved no matter how long the context grows. **Composition by angle addition (Step 6)** is the deeper one: when attention compares a token at position `m` with a token at position `n`, the two rotations combine into a single rotation by `(m − n)·θₖ`. The absolute positions cancel and only the *relative* distance survives. A model trained on short documents can therefore generalize to longer ones, because it only ever learned about gaps between tokens, never about absolute slots.

The length-preserving property from Step 4 shows up again in how networks are initialized. Transformations that neither amplify nor attenuate the signal passing through them are a standard choice for initializing deep and recurrent networks, precisely because a transformation that stretches even slightly, applied across fifty layers, compounds into gradients that explode or vanish. Rotations are the archetype of a transformation that does neither, and the linear algebra module gives this family its proper name.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1
Rotate the vector `(4, 0)` counter-clockwise by 90 degrees using the formula, then again by another 90 degrees. Confirm the length is unchanged at each stage.

**Solution:**
At θ = 90°, `cos θ = 0` and `sin θ = 1`.
1. First rotation: `x' = 4·0 − 0·1 = 0`, `y' = 4·1 + 0·0 = 4`. The result is `(0, 4)`, length `√(0 + 16) = 4`. ✓
2. Second rotation, applied to `(0, 4)`: `x' = 0·0 − 4·1 = −4`, `y' = 0·1 + 4·0 = 0`. The result is `(−4, 0)`, length 4. ✓
Two 90-degree turns produced a 180-degree turn, which negated both components — agreeing with Step 6, since `R(90°)·R(90°) = R(180°)`.

---

### Checkpoint 2
A teammate writes field-oriented drive as `rotate(fieldVx, fieldVy, +heading)` instead of `−heading`. The robot is turned 90 degrees counter-clockwise and the driver pushes straight down-field, commanding `(3.0, 0.0)`. What does the robot actually do, and what should it have done?

**Solution:**
* Correct, with `−90°`: `x' = 3·cos(−90°) − 0·sin(−90°) = 0`, `y' = 3·sin(−90°) + 0 = −3`. The command is "strafe 3 m/s to my right", which for a robot turned a quarter turn to the left does send it down-field. ✓
* The bug, with `+90°`: `x' = 0`, `y' = +3`. The robot strafes to its *left* at 3 m/s — a 180-degree error, driving it directly away from the intended direction. The sign error is invisible when the heading is 0 and worst when the robot is sideways, which is why it typically survives testing and fails in a match.

---

### Deep Dive 1
Step 4 proved rotation preserves length. Investigate what else it preserves: take two vectors, rotate both by the same θ, and work out whether the angle *between* them changes. Then take a triangle with known area, rotate all three of its corners, and compute the new area using the shoelace formula from Geometry Concept 05. Does rotation change area? Does it change the *sign* of the shoelace sum — that is, can a rotation turn a shape into its mirror image? Argue why not from the geometry alone. The linear algebra module formalises what you will discover under the name "determinant".

### Deep Dive 2
Step 6 noted that 2D rotations commute but 3D rotations do not. Test this physically: take a book, rotate it 90 degrees about the vertical axis and then 90 degrees about the horizontal axis, and note the final orientation. Reset and perform the two rotations in the opposite order. Then research why this non-commutativity leads to **gimbal lock** in Euler-angle systems, and why quaternions are the standard fix in robot IMUs and 3D graphics.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../01_concept_unit_circle_ratios/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 01: Unit Circle & Ratios</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../03_concept_coordinate_frames/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 03: Coordinate Frames →</a></div>
</div>
