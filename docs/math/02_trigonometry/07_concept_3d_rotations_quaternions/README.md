# Concept 07: 3D Rotations, Gimbal Lock & Quaternions

> **▶ Interactive Demo: [Gimbal Lock & Quaternion Explorer](demo.html)**
>
> Drive roll, pitch and yaw on a wireframe robot, swap the order the turns are applied in, and watch the quaternion update live. Push pitch toward 90° and watch the roll and yaw axes collapse onto each other.

<iframe src="demo.html" width="100%" height="660" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Field Is Not Flat

Every concept so far has needed exactly one angle: heading. A navX reports it, Concept 02 rotates a joystick command by it, Concept 04 recovers it with `atan2`, Concept 05 wraps it. One number, because the carpet is flat.

Now drive up a ramp. The nose lifts 20 degrees and heading does not change — it cannot, having only ever measured a turn about the vertical. Yet a camera bolted to the robot now points 20 degrees into the air.

<div style="text-align: center; margin: 20px 0;">
  <svg width="400" height="215" viewBox="0 0 400 215" style="max-width: 100%; height: auto;" role="img" aria-label="Two panels. On the left a robot seen from above on flat carpet with a heading arrow forty-five degrees from down-field. On the right the same robot seen from the side sitting on a twenty-degree ramp, its whole body tilted twenty degrees.">
    <rect x="8" y="10" width="176" height="180" rx="8" fill="none" stroke="currentColor" stroke-opacity="0.12" stroke-width="1" />
    <rect x="196" y="10" width="196" height="180" rx="8" fill="none" stroke="currentColor" stroke-opacity="0.12" stroke-width="1" />
    <text x="18" y="30" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">seen from above: flat carpet</text>
    <line x1="85" y1="120" x2="160" y2="120" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.5" stroke-dasharray="5,4" />
    <text x="128" y="136" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">down-field</text>
    <g transform="rotate(-45 85 120)">
      <rect x="63" y="98" width="44" height="44" rx="5" fill="#38bdf8" fill-opacity="0.14" stroke="#38bdf8" stroke-width="2" />
    </g>
    <line x1="85" y1="120" x2="127.43" y2="77.57" stroke="#fbbf24" stroke-width="3" />
    <polygon points="131,74 120.5,79.5 125.5,84.5" fill="#fbbf24" />
    <path d="M 119 120 A 34 34 0 0 0 109.04 95.96" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="106" y="116" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">45°</text>
    <text x="18" y="172" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="10">one number, yaw, says everything</text>
    <text x="206" y="30" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">seen from the side: a 20° ramp</text>
    <line x1="200" y1="170" x2="384" y2="170" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <line x1="215" y1="170" x2="365" y2="115.4" stroke="currentColor" stroke-opacity="0.55" stroke-width="2.5" />
    <path d="M 255 170 A 40 40 0 0 0 252.59 156.32" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="258" y="164" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">20°</text>
    <line x1="300" y1="139.06" x2="300" y2="84" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" stroke-dasharray="5,4" />
    <text x="268" y="78" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">world up</text>
    <g transform="rotate(-20 300 139.06)">
      <rect x="274" y="111.06" width="52" height="20" rx="4" fill="#38bdf8" fill-opacity="0.14" stroke="#38bdf8" stroke-width="2" />
      <circle cx="286" cy="131.06" r="8" fill="none" stroke="#38bdf8" stroke-opacity="0.7" stroke-width="2" />
      <circle cx="314" cy="131.06" r="8" fill="none" stroke="#38bdf8" stroke-opacity="0.7" stroke-width="2" />
    </g>
    <line x1="300" y1="139.06" x2="320.52" y2="82.68" stroke="#4ade80" stroke-width="2.5" />
    <text x="322" y="94" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">robot up</text>
    <text x="206" y="186" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="10">yaw is unchanged, yet the orientation is not</text>
  </svg>
</div>

The gap opens everywhere: a turret that both spins and elevates has two independent axes, and an AprilTag hangs on a wall at a specific attitude — which is why WPILib returns a tag's location as a `Pose3d`. The obvious answer, one angle per axis, is broken in a diagnosable way.

---

## 2. Building the Math: From Three Angles to Four Numbers

### Step 1: One angle per axis

In 3D there are three perpendicular axes, so the natural guess is three numbers. Fix a frame on the robot — **X** out the nose, **Y** out the left side, **Z** straight up — and name a turn about each.

* **Roll** — about X, the nose axis. The robot leans onto one side's wheels.
* **Pitch** — about Y. The nose goes up or down; the ramp above is 20 degrees of pitch.
* **Yaw** — about Z, the vertical. Heading, and all Concepts 01 through 05 needed.

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="230" viewBox="0 0 340 230" style="max-width: 100%; height: auto;" role="img" aria-label="A three-dimensional axis triad drawn in isometric projection. The X axis goes to the lower left and is labeled the roll axis, the Y axis goes to the lower right and is labeled the pitch axis, and the Z axis goes straight up and is labeled the yaw axis.">
    <line x1="170" y1="130" x2="109.9" y2="164.7" stroke="#fbbf24" stroke-width="3" />
    <polygon points="105,167.5 116.5,166 113,159.5" fill="#fbbf24" />
    <line x1="170" y1="130" x2="230.1" y2="164.7" stroke="#4ade80" stroke-width="3" />
    <polygon points="235,167.5 223.5,166 227,159.5" fill="#4ade80" />
    <line x1="170" y1="130" x2="170" y2="60.6" stroke="#38bdf8" stroke-width="3" />
    <polygon points="170,55 165,65 175,65" fill="#38bdf8" />
    <circle cx="170" cy="130" r="4" fill="currentColor" fill-opacity="0.7" />
    <path d="M 128 152 A 16 30 -30 1 1 132 172" fill="none" stroke="#fbbf24" stroke-opacity="0.75" stroke-width="2" />
    <polygon points="133,175 128.5,166 136.5,166.5" fill="#fbbf24" fill-opacity="0.75" />
    <path d="M 212 152 A 16 30 30 1 0 208 172" fill="none" stroke="#4ade80" stroke-opacity="0.75" stroke-width="2" />
    <polygon points="207,175 211.5,166 203.5,166.5" fill="#4ade80" fill-opacity="0.75" />
    <path d="M 140 80 A 30 13 0 1 0 200 80" fill="none" stroke="#38bdf8" stroke-opacity="0.75" stroke-width="2" />
    <polygon points="203,79 194,74 194,84" fill="#38bdf8" fill-opacity="0.75" />
    <text x="46" y="184" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">X: nose — roll axis</text>
    <text x="238" y="184" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">Y: left — pitch axis</text>
    <text x="182" y="52" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">Z: up — yaw axis</text>
    <text x="24" y="214" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">Three perpendicular axes, one angle each. This is what a dashboard shows you.</text>
  </svg>
</div>

These are the **Euler angles**: readable, and what every IMU dashboard shows. Nothing below says stop *reading* them — it says stop *storing* orientation in them.

### Step 2: The order is part of the answer

Concept 02 ended on a warning. In 2D, rotating by α then β is one rotation by `α + β`, and `α + β = β + α`, so order cannot matter. In 3D that argument collapses: a rotation is not a number added to a number.

Try it with a real book, laid flat, cover up, top edge pointing away from you. **Yaw, then pitch:** spin it 90° counter-clockwise on the table, then tip it 90° away from you. **Reset and swap:** tip it away first, then spin it about the vertical. The two end up visibly different — track the top edge, which started along **+X**:

$$
\begin{aligned}
\text{yaw 90°, then pitch 90°:} \quad +X &\longrightarrow +Y \\[4pt]
\text{pitch 90°, then yaw 90°:} \quad +X &\longrightarrow -Z
\end{aligned}
$$

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="230" viewBox="0 0 340 230" style="max-width: 100%; height: auto;" role="img" aria-label="An isometric axis triad. A dashed gray arrow marks the starting direction along positive X. A green arrow along positive Y marks the result of yawing then pitching, and a rose arrow along negative Z marks the result of pitching then yawing.">
    <line x1="170" y1="110" x2="113.43" y2="142.66" stroke="currentColor" stroke-opacity="0.22" stroke-width="1.5" />
    <line x1="170" y1="110" x2="226.57" y2="142.66" stroke="currentColor" stroke-opacity="0.22" stroke-width="1.5" />
    <line x1="170" y1="110" x2="170" y2="44.68" stroke="currentColor" stroke-opacity="0.22" stroke-width="1.5" />
    <line x1="170" y1="110" x2="170" y2="175.32" stroke="currentColor" stroke-opacity="0.22" stroke-width="1.5" />
    <text x="166" y="38" fill="currentColor" fill-opacity="0.45" font-family="sans-serif" font-size="10">+Z (up)</text>
    <line x1="170" y1="110" x2="113.43" y2="142.66" stroke="currentColor" stroke-opacity="0.5" stroke-width="2.5" stroke-dasharray="5,4" />
    <polygon points="109,145.2 120,143 116.5,137" fill="currentColor" fill-opacity="0.5" />
    <text x="16" y="160" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10" font-weight="bold">start: +X</text>
    <line x1="170" y1="110" x2="226.57" y2="142.66" stroke="#4ade80" stroke-width="3.5" />
    <polygon points="231,145.2 220,143 223.5,137" fill="#4ade80" />
    <text x="234" y="150" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">+Y</text>
    <text x="196" y="172" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">yaw 90 then pitch 90</text>
    <line x1="170" y1="110" x2="170" y2="175.32" stroke="#f43f5e" stroke-width="3.5" />
    <polygon points="170,181 165,171 175,171" fill="#f43f5e" />
    <text x="146" y="196" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="bold">−Z</text>
    <text x="14" y="212" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="bold">pitch 90 then yaw 90</text>
    <circle cx="170" cy="110" r="4" fill="currentColor" fill-opacity="0.7" />
    <text x="14" y="26" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">Same two turns, swapped order. The nose lands 90° apart.</text>
  </svg>
</div>

So **"roll 30, pitch 20, yaw 45" is not an orientation** — it is three numbers waiting for a convention: which axis turns first, and whether the turns are about fixed world axes or the body's own moving axes. Libraries disagree. WPILib's `Rotation3d(roll, pitch, yaw)` is *extrinsic* — roll about fixed X, then pitch about Y, then yaw about Z — where aerospace usually means body-axis yaw, pitch, roll. Cross the two and the answer is wrong but plausible.

> ### Math!
> Write `R(θ)` for a rotation by θ, and a product for applying one then another. In 2D `R(α)R(β) = R(β)R(α)`; in 3D `R₁R₂ ≠ R₂R₁`, which is what **non-commutative** means. Read `R₁R₂` as **"R-one composed with R-two"** — and the rightmost factor is applied *first*.

### Step 3: Gimbal lock, derived

The next problem is fatal. Picture a two-axis turret, read the aerospace way: yaw about the vertical, then pitch about the new side-to-side axis, then roll about the nose. With the barrel horizontal these are three different motions.

Now elevate the barrel through **90 degrees of pitch**, until it points straight up. (A right-hand turn about +Y tips the nose *down*, so "straight up" is a pitch of −90°.) The nose axis is now the vertical — the line the yaw stage turns about. **Roll and yaw have become the same rotation.**

<div style="text-align: center; margin: 20px 0;">
  <svg width="380" height="215" viewBox="0 0 380 215" style="max-width: 100%; height: auto;" role="img" aria-label="Two panels. On the left, at zero pitch, the amber roll axis points to the lower left and the purple dashed yaw axis points straight up, and they are ninety degrees apart in space. On the right, at ninety degrees of pitch, both the roll axis and the yaw axis lie along the same vertical line and are zero degrees apart.">
    <rect x="8" y="10" width="176" height="150" rx="8" fill="none" stroke="currentColor" stroke-opacity="0.12" stroke-width="1" />
    <rect x="196" y="10" width="176" height="150" rx="8" fill="none" stroke="currentColor" stroke-opacity="0.12" stroke-width="1" />
    <line x1="100" y1="140" x2="100" y2="82.8" stroke="#c084fc" stroke-width="3" stroke-dasharray="6,4" />
    <polygon points="100,77 95,87 105,87" fill="#c084fc" />
    <line x1="100" y1="140" x2="50.5" y2="168.6" stroke="#fbbf24" stroke-width="3.5" />
    <polygon points="46,171 57,169 53.5,163" fill="#fbbf24" />
    <circle cx="100" cy="140" r="4" fill="currentColor" fill-opacity="0.7" />
    <text x="106" y="74" fill="#c084fc" font-family="sans-serif" font-size="10" font-weight="bold">yaw axis</text>
    <text x="14" y="186" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="bold">roll axis (the nose)</text>
    <text x="18" y="34" fill="currentColor" fill-opacity="0.7" font-family="sans-serif" font-size="11" font-weight="bold">pitch = 0°</text>
    <text x="18" y="204" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="10">two axes, 90° apart: three independent controls</text>
    <line x1="288" y1="140" x2="288" y2="82.8" stroke="#fbbf24" stroke-width="7" />
    <line x1="288" y1="140" x2="288" y2="82.8" stroke="#c084fc" stroke-width="3" stroke-dasharray="6,4" />
    <polygon points="288,77 283,87 293,87" fill="#c084fc" />
    <circle cx="288" cy="140" r="4" fill="currentColor" fill-opacity="0.7" />
    <text x="296" y="100" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="bold">roll axis</text>
    <text x="296" y="114" fill="#c084fc" font-family="sans-serif" font-size="10" font-weight="bold">yaw axis</text>
    <text x="220" y="152" fill="currentColor" fill-opacity="0.45" font-family="sans-serif" font-size="10">(same line)</text>
    <text x="206" y="34" fill="currentColor" fill-opacity="0.7" font-family="sans-serif" font-size="11" font-weight="bold">pitch = −90° (nose straight up)</text>
    <text x="206" y="204" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="10">one axis, 0° apart: only two controls remain</text>
  </svg>
</div>

A roll of φ about a vertical nose *is* a yaw of φ, so the pair only produces `yaw + roll` about the vertical:

```
   yaw    pitch   roll     resulting orientation
   ------------------------------------------------
    0°    -90°      0°     identical
   30°    -90°    -30°     identical
   45°    -90°    -45°     identical

   30°    -90°      0°     identical
    0°    -90°     30°     identical
```

Three dials, two degrees of freedom. The encoding is many-to-one — infinitely many `(yaw, roll)` pairs name that orientation, so converting *back* has no unique answer. This is **gimbal lock**, after the three-ring mechanism whose rings become coplanar.

**The damage is the neighborhood, not the exact singularity.** Elevate to 89.9 degrees instead, so the barrel points 0.1 degrees off vertical, and sweep yaw through 90 degrees. The nose travels a circle of angular radius 0.1 degrees, and two points 90 degrees apart on it differ by

$$
\sqrt{2} \times 0.1° = 0.141°
$$

of actual direction. Read that backwards: **a 0.141-degree nudge of the barrel demands a 90-degree jump in reported yaw.** Millidegree IMU noise becomes yaw swings of tens of degrees per loop cycle, and a controller sees a huge error from nothing. Point an arm straight up and a naive Euler-angle controller thrashes.

### Step 4: Euler's rotation theorem

**Any orientation of a rigid body about a fixed point, however you got there, is a single rotation by some angle about some single axis.** This is **Euler's rotation theorem**, and it is the key idea of this concept.

Test it on the book. A rotation of **120 degrees about the diagonal** `(1, 1, 1)/√3` sends `+X → +Y`, `+Y → +Z`, `+Z → +X` — what yaw-then-pitch did. The reverse order is a different single rotation: 120 degrees about `(−1, 1, 1)/√3`.

Why must it hold? A rotation preserves lengths and fixes the origin, so it maps the unit sphere onto itself, and such a map either turns the sphere about an axis or reflects it. Reflection is out — it would turn a right hand into a left one. What survives is a turn, and a turn has an axis: the two points that did not move.

So orientation is **a direction plus an amount**: an axis, 3 numbers, and an angle, 1 more. No order to get wrong, and no configuration where controls collide.

### Step 5: Quaternions encode axis-angle

Axis-angle is right but awkward: composing two pairs is a mess, and the axis is undefined at zero angle. The **quaternion** fixes both, and is what your IMU is really computing — four numbers, from the axis `n̂` and angle θ:

$$
\begin{aligned}
w &= \cos\!\left(\frac{\theta}{2}\right) \\[6pt]
(x,\ y,\ z) &= \hat{n} \cdot \sin\!\left(\frac{\theta}{2}\right)
\end{aligned}
$$

Every ingredient is from Concept 01: a cosine, a sine, and a scaled unit vector.

**Why the half?** Because of how a quaternion is *applied*. A lone quaternion product does not send 3D vectors to 3D vectors while preserving lengths; what works is the two-sided sandwich `q v q⁻¹`. Since `q` appears on both sides, the angle inside it is used **twice** — store the full θ and you get a turn of 2θ, store θ/2 and the two applications combine into exactly θ.

Since the half-angle runs 0 to 180 degrees as θ runs 0 to 360, `q` and `−q` name the *same* orientation: a log will occasionally show all four components flip sign with the robot still, and nothing is wrong.

> ### Math!
> `(n̂, θ)` is the **axis-angle** representation, read **"a rotation of theta about the axis n-hat"**; as with Concept 02's `î` and `ĵ`, the hat means length 1. `q = (w, x, y, z)` is read **"the quaternion w, x, y, z"**, from *quaternio*, Latin for a set of four — Hamilton's 1843 extension of the complex numbers, as the complex numbers extend the reals. You need none of that algebra, only that four numbers of length 1 encode an axis and an angle.

### Step 6: The constraint is Concept 01's identity

Not every four numbers is a rotation. It has to be a **unit** quaternion:

$$
w^2 + x^2 + y^2 + z^2 = 1
$$

It falls out of the definition, using `n̂`'s own unit length `nx² + ny² + nz² = 1`:

$$
\begin{aligned}
w^2 + x^2 + y^2 + z^2 &= \cos^2\!\left(\tfrac{\theta}{2}\right) + \left(n_x^2 + n_y^2 + n_z^2\right)\sin^2\!\left(\tfrac{\theta}{2}\right) \\[4pt]
&= \cos^2\!\left(\tfrac{\theta}{2}\right) + \sin^2\!\left(\tfrac{\theta}{2}\right) = 1
\end{aligned}
$$

The last line is Concept 01's `sin² + cos² = 1` — Pythagoras on a hypotenuse of 1 — at the half-angle. It proved there that splitting a speed preserves the speed, and in Concept 02 that a 2D rotation preserves length. Same job here: the unit constraint keeps the rotation **rigid**, and no Euler triple offers a self-check like it.

### Step 7: The book experiment, in quaternions

Yaw 90 degrees turns about `(0, 0, 1)` with half-angle 45 degrees, and `cos 45° = sin 45° = 0.70711`:

$$
q_{\text{yaw}} = (0.70711,\ 0,\ 0,\ 0.70711) \qquad q_{\text{pitch}} = (0.70711,\ 0,\ 0.70711,\ 0)
$$

Multiply them in the two orders:

```
   yaw then pitch:   q = ( 0.5,  0.5, 0.5, 0.5)   ->  120° about ( 1, 1, 1)/sqrt(3)
   pitch then yaw:   q = ( 0.5, -0.5, 0.5, 0.5)   ->  120° about (-1, 1, 1)/sqrt(3)
```

Both satisfy `0.5² × 4 = 1`, so both are legal rotations, and both are turns of `2 × arccos(0.5) = 120°`. They differ in one sign — the difference between the nose pointing left and pointing at the floor. Concept 02's non-commutativity, made arithmetic.

### Step 8: What this buys a team

* **No gimbal lock, anywhere.** Every unit quaternion is an ordinary point on the unit sphere in four dimensions; the barrel straight up is `(0.70711, 0, −0.70711, 0)`, four unremarkable numbers. The singularity was never in the rotation, only in the *encoding*.
* **Composition is multiplication.** "This rotation, then that one" is one quaternion product — sixteen multiplies, twelve adds, no trigonometry. Concept 03's field → robot → camera chain is the same in 3D.
* **Drift is cheap to repair.** Products accumulate floating-point error until the four squares stop summing to 1; the repair is one square root and four divisions. Three Euler angles have no invariant to check.
* **Interpolation works.** Geometry Concept 03 warned that angles cannot be blended naively — halfway between 350° and 10° comes out 180°, exactly backwards — and it returns in 3D: averaging roll, pitch and yaw separately lurches through orientations neither endpoint was near. Blending quaternions along the shortest arc of the 4D unit sphere gives a smooth turn about one axis instead: **SLERP**.

**The honest caveat.** Nobody looks at `(0.90984, 0.06645, −0.16043, 0.37687)` and pictures a robot; Euler angles are far better for a dashboard or a log read at 2 a.m. So: **store and compute in quaternions, convert to Euler angles for humans, and never convert back.**

---

## 3. Solving It in Code (Java & WPILib)

### First Principles (Java)

```java
// A unit quaternion from an axis-angle pair. The axis must have length 1.
static double[] fromAxisAngle(double nx, double ny, double nz, double angleRad) {
    double len = Math.sqrt(nx * nx + ny * ny + nz * nz);
    nx /= len; ny /= len; nz /= len;              // make the axis a unit vector
    double half = angleRad / 2.0;                 // the sandwich uses q twice
    double s = Math.sin(half);
    return new double[] { Math.cos(half), nx * s, ny * s, nz * s };
}

// Compose: apply b first, then a. Sixteen multiplies, no trig.
static double[] multiply(double[] a, double[] b) {
    return new double[] {
        a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3],
        a[0]*b[1] + a[1]*b[0] + a[2]*b[3] - a[3]*b[2],
        a[0]*b[2] - a[1]*b[3] + a[2]*b[0] + a[3]*b[1],
        a[0]*b[3] + a[1]*b[2] - a[2]*b[1] + a[3]*b[0]
    };
}

static double norm(double[] q) {
    return Math.sqrt(q[0]*q[0] + q[1]*q[1] + q[2]*q[2] + q[3]*q[3]);
}

// Step 7, checked by hand.
double[] yaw90   = fromAxisAngle(0, 0, 1, Math.toRadians(90));  // (0.70711, 0, 0, 0.70711)
double[] pitch90 = fromAxisAngle(0, 1, 0, Math.toRadians(90));  // (0.70711, 0, 0.70711, 0)

double[] yawThenPitch = multiply(pitch90, yaw90);   // ( 0.5,  0.5, 0.5, 0.5)
double[] pitchThenYaw = multiply(yaw90, pitch90);   // ( 0.5, -0.5, 0.5, 0.5)

System.out.println(norm(yawThenPitch));   // 1.0  <- still a legal rotation
System.out.println(norm(pitchThenYaw));   // 1.0  <- also legal, and NOT the same one
```

Reading the axis and angle back is the definition in reverse: `w` gives the angle, and dividing the other three by `sin(θ/2)` gives the axis.

```java
// Recover (axis, angle) from a unit quaternion. Round-trips fromAxisAngle exactly.
static double[] toAxisAngle(double[] q) {
    double w = Math.max(-1.0, Math.min(1.0, q[0]));   // clamp against drift
    double angle = 2.0 * Math.acos(w);
    double s = Math.sqrt(1.0 - w * w);                // this is sin(angle / 2)
    if (s < 1e-9) {
        return new double[] { 0, 0, 1, 0 };           // no rotation: axis is arbitrary
    }
    return new double[] { q[1] / s, q[2] / s, q[3] / s, angle };
}

double[] back = toAxisAngle(yawThenPitch);
// axis (0.57735, 0.57735, 0.57735) = (1,1,1)/sqrt(3),  angle 2.0944 rad = 120.000 deg
```

That `1e-9` guard is the only special case in the file, and it is not a singularity: a zero rotation has no distinguished axis. Euler-angle code needs a branch whenever pitch nears ±90 degrees, with no correct answer inside it.

### In a Robot Project (Java & WPILib)

```java
import edu.wpi.first.math.geometry.Pose3d;
import edu.wpi.first.math.geometry.Quaternion;
import edu.wpi.first.math.geometry.Rotation3d;
import edu.wpi.first.math.geometry.Translation3d;
import edu.wpi.first.math.VecBuilder;

// 1. From roll, pitch and yaw -- the readable route, and what an IMU hands you.
//    WPILib documents these as EXTRINSIC: roll about fixed X, then pitch about
//    fixed Y, then yaw about fixed Z. Another library's triple may not mean this.
Rotation3d onTheRamp = new Rotation3d(
    Math.toRadians(0.0),     // roll
    Math.toRadians(-20.0),   // pitch -- nose 20 degrees UP the ramp; see Step 3
    Math.toRadians(45.0));   // yaw

// 2. From an axis and an angle -- Euler's rotation theorem, spelled out.
Rotation3d spinUp = new Rotation3d(VecBuilder.fill(0, 0, 1), Math.toRadians(90));

// 3. From a quaternion -- what a navX or Pigeon 2 reports natively.
Rotation3d fromImu = new Rotation3d(new Quaternion(0.70711, 0, 0, 0.70711));
```

All three constructors do the same thing internally: **`Rotation3d` stores a quaternion and nothing else**, as Concept 01's `Rotation2d` stores a cosine and a sine rather than an angle. Euler angles are computed on demand, never stored.

```java
Quaternion q = onTheRamp.getQuaternion();
System.out.printf("w %.5f  x %.5f  y %.5f  z %.5f%n",
                  q.getW(), q.getX(), q.getY(), q.getZ());
// w 0.90984  x 0.06645  y -0.16043  z 0.37687

double sumOfSquares = q.getW()*q.getW() + q.getX()*q.getX()
                    + q.getY()*q.getY() + q.getZ()*q.getZ();   // 1.00000

// Euler's theorem, from the library: one axis, one angle.
var axis         = onTheRamp.getAxis();                   // (0.1601, -0.3866, 0.9082)
double angleDeg  = Math.toDegrees(onTheRamp.getAngle());  // 49.0325

// And back to human-readable numbers, for the dashboard only.
double pitchDeg = Math.toDegrees(onTheRamp.getY());       // -20.0
double yawDeg   = Math.toDegrees(onTheRamp.getZ());       // 45.0
```

A pitch of −20 plus a yaw of 45 is a **single rotation of 49.03 degrees about the axis (0.1601, −0.3866, 0.9082)**. Two turns in, one turn out, as Step 4 promised; the from-scratch tier agrees, reproducing `(0.90984, 0.06645, −0.16043, 0.37687)` from that axis and angle. And none of this is academic — an AprilTag's location is a `Pose3d`:

```java
// Position in three numbers, orientation in a Rotation3d that holds a quaternion.
Pose3d tagPose = new Pose3d(new Translation3d(4.20, 1.83, 1.45), onTheRamp);

// Composition is a quaternion product under the hood -- Step 8, second paragraph.
Rotation3d combined = onTheRamp.rotateBy(spinUp);

// Rotation3d.times(scalar) scales a rotation along its own single axis, which is
// what makes interpolate() a true SLERP rather than a three-angle average.
Rotation3d halfway = onTheRamp.interpolate(spinUp, 0.5);
```

---

## 4. Bridge to Graphics, Games & Machine Learning

**Every 3D engine runs on this.** Unity stores a rotation only as a `Quaternion`; `transform.eulerAngles` is a view computed on demand, and Unity's own documentation warns against using it as storage. Unreal, Godot, Blender and glTF all store orientation as four numbers. Character animation is the reason: blending two keyframed poses is a SLERP, sixty times a second, on every joint of every skeleton.

**Orientation is a live problem in machine learning too, and the representation is the difficulty.** A network predicting an object's pose from an image must emit a rotation, and three Euler angles train badly. The cause is the discontinuity Concept 05 fixed for a single angle, now unavoidable: the map to Euler triples has points where a tiny change in the true orientation forces a large change in the target numbers, and near gimbal lock the target is not unique. A regression loss cannot fit a function with a jump in it, so the network hedges toward the average of both sides.

Predicting a quaternion is what most pose-estimation networks did instead: four outputs normalized to length 1, Step 6's constraint imposed as a network layer. It is still imperfect — `q` and `−q` are the same rotation, so the target is ambiguous unless a sign is chosen consistently — and the standard fix now is a **6D representation**, predicting two vectors and orthogonalizing them into a frame.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1

A robot is level and facing straight down-field: no rotation at all. Write its quaternion. Then write the one for a robot yawed 180 degrees, and confirm from the numbers alone that it is a half turn about the vertical.

**Solution:**

1. **No rotation** is θ = 0. The half-angle is 0, so `w = cos 0° = 1` and `sin 0° = 0` kills the axis: the **identity quaternion** is `(1, 0, 0, 0)`, with `1² = 1`. ✓ Its axis is undefined, correctly — the `1e-9` branch in `toAxisAngle`.
2. **Yawed 180 degrees** is θ = 180° about `n̂ = (0, 0, 1)`, half-angle 90°, so `w = cos 90° = 0` and `(x, y, z) = (0, 0, 1) × sin 90°`. That is `(0, 0, 0, 1)`, and `1² = 1`. ✓
3. **Read it back.** `θ = 2 × arccos(0) = 180°` and `sin(θ/2) = 1`, so the axis is `(0, 0, 1)` — straight up.

---

### Checkpoint 2

A shooter's barrel points straight up: pitch −90 degrees. Software commands yaw 40, roll 0; a moment later, yaw 0, roll 40. The mechanism does not move. Explain why, and say what a controller comparing the two yaw readings would do.

**Solution:**

1. **The axes.** At −90 degrees of pitch the nose has been tipped onto the vertical, so the roll axis and the yaw axis are the same line.
2. **So the two commands are the same rotation.** A roll of 40 about a vertical nose *is* a yaw of 40, and only the sum `yaw + roll` reaches the hardware — Step 3's table shows the same collapse for `(30, −30)`.
3. **What the controller sees.** Yaw feedback dropped from 40 to 0 while the mechanism sat still — a 40-degree error from nothing. A proportional controller answers with a large output, slamming a stationary mechanism.
4. **Why reality is worse.** Near 90 degrees the encoding is violently sensitive rather than merely degenerate: at 89.9 degrees, `0.141°` of real motion swings yaw through 90 degrees, and noise alone produces that. The fix is not a harder filter — it is to stop storing orientation as three angles.

---

### Deep Dive 1

Step 5 asserted the half-angle without proving it. Check the simplest case by hand: let `q` be a rotation of θ about Z, so `q = (cos(θ/2), 0, 0, sin(θ/2))`, and let `v` be `(1, 0, 0)` written as `(0, 1, 0, 0)`. Work out `q v q⁻¹` with the multiplication rule from the code section, remembering that a unit quaternion's inverse negates `x`, `y` and `z`. The result is `(0, cos θ, sin θ, 0)` — Concept 02's 2D rotation applied to `î`. Say where the two half-angles combined, and predict what the full θ would have given.

### Deep Dive 2

Step 8 claimed SLERP blends orientations correctly and averaging Euler angles does not. Build the counterexample: A is yaw 170 degrees, B is yaw −170 degrees, roll and pitch zero. Average each angle at `t = 0.25`, `0.5` and `0.75`, describe the path the nose takes, and compare it with Geometry Concept 03's answer for `lerp(350, 10, 0.5)`. Then convert both to quaternions and work out what goes wrong if a SLERP implementation does *not* check the sign of their dot product first, recalling that `q` and `−q` are the same orientation.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../06_concept_law_of_cosines/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 06: Law of Cosines</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../../03_linear_algebra/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 3: Linear Algebra →</a></div>
</div>
