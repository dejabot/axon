# Concept 07: 3D Rotations, Gimbal Lock & Quaternions

> **▶ Interactive Demo: [Gimbal Lock & Quaternion Explorer](demo.html)**
>
> Drive roll, pitch and yaw on a wireframe robot, watch the quaternion update live, and swap the order the three turns are applied in to see identical numbers produce different orientations. Push pitch to 90° and watch the roll and yaw axes collapse onto each other.

<iframe src="demo.html" width="100%" height="660" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Field Is Not Flat

Every concept so far has needed exactly one angle. A navX or a Pigeon reports the robot's heading, Concept 02 rotates a joystick command by it, Concept 04 recovers it with `atan2`, Concept 05 wraps it into range. One number, because the carpet is flat.

Now drive up a ramp. The nose lifts 20 degrees and the heading number does not change at all — it cannot, because heading only ever measured a turn about the vertical. Yet the orientation is plainly different: a camera bolted to the robot now points 20 degrees into the air.

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

The gap opens everywhere once you look. A turret that both spins and elevates has two independent axes. An AprilTag is a flat square hanging on a wall in a specific 3D attitude — WPILib returns its location as a `Pose3d`, not a `Pose2d`, precisely because two numbers of position and one of heading cannot say where a wall tag is or where a camera is looking.

So we need a way to say "this rigid body is oriented like *this*" in three dimensions. The obvious answer is broken in a specific, diagnosable way, and this concept is that failure and its fix.

---

## 2. Building the Math: From Three Angles to Four Numbers

### Step 1: The obvious first answer — one angle per axis

In 2D there was one axis to spin about. In 3D there are three perpendicular ones, so the natural guess is three numbers. Fix a frame on the robot — **X** out the nose, **Y** out the left side, **Z** straight up — and name a turn about each.

* **Roll** — about X, the nose axis. The robot leans onto one side's wheels.
* **Pitch** — about Y, the side-to-side axis. The nose goes up or down; the ramp above is 20 degrees of pitch.
* **Yaw** — about Z, the vertical. This is heading, the only one Concepts 01 through 05 needed.

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="230" viewBox="0 0 340 230" style="max-width: 100%; height: auto;" role="img" aria-label="A three-dimensional axis triad drawn in isometric projection. The X axis goes to the lower left and is labelled the roll axis, the Y axis goes to the lower right and is labelled the pitch axis, and the Z axis goes straight up and is labelled the yaw axis.">
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

These three are the **Euler angles**, and they are genuinely good: readable — "pitched up 20, yawed 45" is a sentence a human can picture — and what every IMU dashboard puts on screen. Nothing below says stop *reading* roll, pitch and yaw. It says stop *storing* orientation in them.

### Step 2: The order is part of the answer

Concept 02 ended on a warning. In 2D, rotating by α and then β is a single rotation by `α + β`, and since `α + β = β + α` the order cannot matter. Addition is commutative, so 2D rotation is commutative. Airtight — in 2D.

In 3D it collapses, because a 3D rotation is not a number added to a number. The experiment takes ten seconds with a real book. Lay one flat, spine on your left, front cover up, top edge pointing away from you.

1. **Yaw first.** Spin it 90 degrees counter-clockwise on the table, so the top edge points left. Then **pitch**: tip it 90 degrees away from you about the table's left-right axis. It ends up standing on what was its bottom edge, cover facing you.
2. **Reset, pitch first.** Tip it 90 degrees away from you — it stands upright, cover facing you, top edge at the ceiling. Then **yaw** 90 degrees counter-clockwise about the table's vertical. It ends up on its spine, cover facing left.

Two visibly different books. Pin it down by tracking one direction, the top edge, which started along **+X**:

$$
\begin{aligned}
\text{yaw 90°, then pitch 90°:} \quad +X &\longrightarrow +Y \\[4pt]
\text{pitch 90°, then yaw 90°:} \quad +X &\longrightarrow -Z
\end{aligned}
$$

One ends up pointing left, the other at the floor: 90 degrees apart. Not a rounding disagreement — a different physical orientation.

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="230" viewBox="0 0 340 230" style="max-width: 100%; height: auto;" role="img" aria-label="An isometric axis triad. A dashed grey arrow marks the starting direction along positive X. A green arrow along positive Y marks the result of yawing then pitching, and a rose arrow along negative Z marks the result of pitching then yawing.">
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

So **"roll 30, pitch 20, yaw 45" is not an orientation.** It is three numbers waiting for a convention: which axis turns first, and whether each turn is about the fixed world axes or about the body's own axes as they move. That is twelve sequences times two, and libraries genuinely disagree. Aerospace usually applies yaw, then pitch, then roll about the body; WPILib's `Rotation3d(roll, pitch, yaw)` documents itself as *extrinsic* — roll about the fixed X, then pitch about the fixed Y, then yaw about the fixed Z. Feed one library's triple into another's constructor and you get a wrong answer that looks plausible.

> ### Math!
> Write `R(θ)` for a rotation by θ, and write applying one and then another as a product. In 2D, `R(α)R(β) = R(β)R(α)`. In 3D, `R₁R₂ ≠ R₂R₁` in general, and the word for that is **non-commutative**. Read `R₁R₂` out loud as **"R-one composed with R-two"**. Almost everywhere the rightmost factor is applied *first*, so `R₁R₂` means "do R₂, then do R₁" — reading that backwards is the commonest 3D transform bug.

### Step 3: Gimbal lock — when two of your three controls become one

Order dependence is annoying. The next problem is fatal.

Take the aerospace reading — yaw about the vertical, then pitch about the new side-to-side axis, then roll about the nose — and picture a two-axis turret. With the barrel horizontal, the three are obviously different motions: yaw sweeps the barrel across the field, roll spins it about its own length and moves the aim point not at all.

Now elevate the barrel through **90 degrees of pitch**, until it points straight up. (A right-hand turn about +Y tips the nose *down*, so "straight up" is a pitch of −90° — a sign convention worth knowing, because WPILib uses this frame.) The nose axis is now the vertical axis, the same physical line the yaw stage turns about. Roll is a spin about the barrel; the barrel is vertical; yaw is a spin about the vertical. **They are the same rotation.**

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

Check it. Hold pitch at −90 degrees and ask what the pair (yaw, roll) produces. Because the nose axis has become the vertical, a roll of φ *is* a yaw of φ, so the pair only ever produces a turn of `yaw + roll` about the vertical:

```
   yaw    pitch   roll     resulting orientation
   ------------------------------------------------
    0°    -90°      0°     identical
   30°    -90°    -30°     identical
   45°    -90°    -45°     identical

   30°    -90°      0°     identical
    0°    -90°     30°     identical
```

Three dials, two degrees of freedom. One whole axis of control has vanished, and the encoding is now many-to-one: infinitely many `(yaw, roll)` pairs name the same orientation, so converting *back* to angles has no unique answer. This is **gimbal lock**, named for the mechanical version — a three-ring gimbal in which two rings become coplanar and the inner mass can no longer be commanded about the lost axis.

**The real damage is not the exact singularity; it is the neighborhood around it.** Elevate the barrel to 89.9 degrees, so it points 0.1 degrees off vertical, and sweep yaw through a full 90 degrees. The nose moves along a tiny circle of angular radius 0.1 degrees, and two points on that circle 90 degrees apart in yaw are separated by

$$
\sqrt{2} \times 0.1° = 0.141°
$$

of actual physical direction. Read that backwards: **a 0.141-degree nudge of the barrel demands a 90-degree jump in the reported yaw.** Millidegree sensor noise, which every IMU has, becomes yaw readings that swing tens of degrees between loop cycles. A controller holding yaw to a setpoint sees an enormous error appear from nothing and commands full output to chase it. Point an arm straight up and a naive Euler-angle controller does not fail gracefully — it thrashes.

### Step 4: Euler's rotation theorem — every rotation is one turn about one axis

The escape is one surprising fact. **Any orientation of a rigid body about a fixed point, however you got there, is achievable as a single rotation by some angle about some single axis.** No sequence, no order, no three-stage assembly — one axis, one angle. This is **Euler's rotation theorem**, and it is the key idea of this concept.

Test it on the book. Yaw 90 then pitch 90 looked like two turns about two axes; Euler's theorem says one suffices, and it does. A rotation of **120 degrees about the diagonal axis** `(1, 1, 1)/√3` sends `+X → +Y`, `+Y → +Z`, `+Z → +X` — exactly what the two turns did. Reverse the order and you get a different single rotation: 120 degrees about `(−1, 1, 1)/√3`.

Why must the theorem hold? A rotation keeps the origin fixed and preserves all lengths and angles, so it maps the unit sphere onto itself. Every such map either turns the sphere about some axis or reflects it, and a reflection turns a right hand into a left hand — impossible for a rigid body that was moved rather than mirrored. What survives is a turn, and a turn has an axis: the two points on the sphere that did not move.

So orientation is not three sequenced angles. It is **a direction plus an amount** — an axis, 3 numbers, and an angle, 1 more. There is no order to get wrong, because there is only one turn, and no configuration where two controls collide, because there is only one axis.

> ### Math!
> The pair is written `(n̂, θ)` and called the **axis-angle** representation. `n̂` is read **"n-hat"**, and as with Concept 02's `î` and `ĵ` the hat means the vector has length 1 — direction only. Read the pair out loud as **"a rotation of theta about the axis n-hat."** Note that `(n̂, θ)` and `(−n̂, −θ)` are the same physical turn: reverse the axis and reverse the angle and you have turned the same way.

### Step 5: Quaternions — packing the axis and the angle into four numbers

Axis-angle is the right idea but awkward to compute with: composing two pairs into one is a mess, and the axis is undefined at zero angle. The **quaternion** fixes both, and it is what your IMU is really computing whether or not it shows you.

A unit quaternion is four numbers, `(w, x, y, z)`, built from the axis-angle pair:

$$
\begin{aligned}
w &= \cos\!\left(\frac{\theta}{2}\right) \\[6pt]
(x,\ y,\ z) &= \hat{n} \cdot \sin\!\left(\frac{\theta}{2}\right)
\end{aligned}
$$

Every ingredient is from Concept 01: a cosine, a sine, and a unit vector scaled by a number. `w` is a scalar; `(x, y, z)` points along the rotation axis, with a length that grows with the angle.

**Why the half?** Because of how a quaternion is *applied*. Rotating a vector `v` is not a single multiplication — a lone quaternion product does not send 3D vectors to 3D vectors while preserving lengths. The construction that works is a two-sided sandwich: multiply by `q` on the left and by its inverse on the right, `q v q⁻¹`. Because `q` appears on both sides, whatever angle is stored inside it gets used **twice**. Store the full θ and you get a rotation of 2θ; store θ/2 and the two applications combine into exactly θ. The half is not a mystery, it is bookkeeping for a formula that touches `q` twice. You never need to grind that algebra by hand — the library does it — but knowing why the half is there stops it looking arbitrary.

One consequence to carry: since the half-angle runs 0 to 180 degrees as θ runs 0 to 360, `q` and `−q` name the *same* orientation. Negating all four components flips the axis and adds a full turn, landing you where you started. A log will occasionally show every component flip sign with the robot perfectly still, and nothing is wrong.

> ### Math!
> `q = (w, x, y, z)` is read **"the quaternion w, x, y, z."** The name is from *quaternio*, Latin for a set of four. Quaternions extend the complex numbers the way the complex numbers extend the reals, and William Rowan Hamilton wrote the algebra down in 1843, a century before there was a computer to run it on. You do not need that algebra here. You need that four numbers constrained to length 1 encode an axis and an angle, and that libraries multiply them for you.

### Step 6: The constraint is Concept 01's identity, one dimension up

Not every four numbers is a rotation. It has to be a **unit** quaternion:

$$
w^2 + x^2 + y^2 + z^2 = 1
$$

That is not an extra rule bolted on; it falls out of the definition. Substitute, using the fact that `n̂` has length 1 so `nx² + ny² + nz² = 1`:

$$
\begin{aligned}
w^2 + x^2 + y^2 + z^2 &= \cos^2\!\left(\tfrac{\theta}{2}\right) + \left(n_x^2 + n_y^2 + n_z^2\right)\sin^2\!\left(\tfrac{\theta}{2}\right) \\[4pt]
&= \cos^2\!\left(\tfrac{\theta}{2}\right) + \sin^2\!\left(\tfrac{\theta}{2}\right) \\[4pt]
&= 1
\end{aligned}
$$

The last line is `sin² + cos² = 1` from Concept 01 — Pythagoras on a hypotenuse of 1 — evaluated at the half-angle. Concept 01 used it to show that splitting a speed into components does not change the speed; Concept 02 used it to show a 2D rotation preserves length. It does the same job here: the unit constraint is exactly what makes the rotation **rigid**, unable to stretch or squash what it is applied to.

It is also a free self-check, which three Euler angles do not offer. Sum the four squares; if the answer has drifted from 1, your orientation has drifted from being a rotation, and the repair is to divide all four by their own root-sum-of-squares.

### Step 7: The book experiment, in quaternions

Run Step 2's two orderings through the encoding. Yaw 90 degrees is a turn about `(0, 0, 1)`, half-angle 45 degrees, and `cos 45° = sin 45° = 0.70711`:

$$
q_{\text{yaw}} = (0.70711,\ 0,\ 0,\ 0.70711) \qquad q_{\text{pitch}} = (0.70711,\ 0,\ 0.70711,\ 0)
$$

Multiply them in the two orders:

```
   yaw then pitch:   q = ( 0.5,  0.5, 0.5, 0.5)   ->  120° about ( 1, 1, 1)/sqrt(3)
   pitch then yaw:   q = ( 0.5, -0.5, 0.5, 0.5)   ->  120° about (-1, 1, 1)/sqrt(3)
```

Both satisfy `0.5² × 4 = 1`, so both are legal rotations, and both are turns of `2 × arccos(0.5) = 120°`. They differ in the sign of one component — and that single sign is the difference between the nose pointing left and the nose pointing at the floor. Concept 02's non-commutativity, made arithmetic.

### Step 8: What this actually buys a team

**No gimbal lock, anywhere.** Every unit quaternion is an ordinary point on the unit sphere in four dimensions, and none is special. The barrel straight up is `(0.70711, 0, −0.70711, 0)`, four unremarkable numbers with no more noise sensitivity than any others. The singularity was never in the rotation; it was in the three-angle *encoding*, and the encoding is gone.

**Composition is multiplication.** "Apply this rotation, then that one" is one quaternion product: sixteen multiplies and twelve adds, no trigonometry in the inner loop. Chaining field → robot → camera → tag, which Concept 03 built in 2D as rotate-then-translate, is the same chain in 3D with quaternion products doing the rotating.

**Drift is cheap to repair.** Every product adds a little floating-point error, and after thousands of loop cycles the four squares no longer sum to 1. The repair is one square root and four divisions. Three Euler angles have no invariant to check, so there is nothing to notice and nothing to fix.

**Interpolation works.** Geometry Concept 03 warned that angles cannot be blended naively — halfway between 350° and 10° comes out 180°, exactly backwards — and fixed it in 1D by wrapping the difference into range, which is Concept 05's job. The same problem returns in 3D: averaging two orientations' roll, pitch and yaw separately gives a path that lurches and can pass through orientations neither endpoint was near. Blending quaternions instead, along the shortest arc of the 4D unit sphere, gives a smooth constant-rate turn about a single axis. That operation is **SLERP**, spherical linear interpolation.

**And the honest caveat.** A quaternion is not intuitive. Nobody looks at `(0.90984, −0.06645, 0.16043, 0.37687)` and pictures a robot, and roll, pitch and yaw are far better for a dashboard or a log you have to read at 2 a.m. The rule is not "quaternions are better" — it is **store and compute in quaternions, convert to Euler angles at the moment you show a human, and never convert back.**

---

## 3. Solving It in Code (Java & WPILib)

### First Principles (Java)

Build a quaternion from an axis and an angle, compose two, and check the constraint.

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

Reading the axis and angle back is the definition run in reverse: `w = cos(θ/2)` gives the angle, and dividing the other three by `sin(θ/2)` gives the axis.

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

That `1e-9` guard is the only special case in the file, and it is not a singularity — a zero rotation genuinely has no distinguished axis, so any unit vector is correct. Euler-angle code needs a branch every time pitch approaches ±90 degrees, and has no correct answer to give inside it.

### In a Robot Project (Java & WPILib)

WPILib's `Rotation3d` accepts all three descriptions and stores exactly one of them.

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
    Math.toRadians(20.0),    // pitch -- the 20 degree ramp
    Math.toRadians(45.0));   // yaw

// 2. From an axis and an angle -- Euler's rotation theorem, spelled out.
Rotation3d spinUp = new Rotation3d(VecBuilder.fill(0, 0, 1), Math.toRadians(90));

// 3. From a quaternion -- what a navX or Pigeon 2 reports natively.
Rotation3d fromImu = new Rotation3d(new Quaternion(0.70711, 0, 0, 0.70711));
```

All three do the same thing internally: **`Rotation3d` stores a quaternion and nothing else**, exactly as Concept 01's `Rotation2d` stores a cosine and a sine rather than an angle. Roll, pitch and yaw are computed on demand, never stored.

```java
Quaternion q = onTheRamp.getQuaternion();
System.out.printf("w %.5f  x %.5f  y %.5f  z %.5f%n",
                  q.getW(), q.getX(), q.getY(), q.getZ());
// w 0.90984  x -0.06645  y 0.16043  z 0.37687

double sumOfSquares = q.getW()*q.getW() + q.getX()*q.getX()
                    + q.getY()*q.getY() + q.getZ()*q.getZ();   // 1.00000

// Euler's theorem, from the library: one axis, one angle.
var axis         = onTheRamp.getAxis();                   // (-0.1601, 0.3866, 0.9082)
double angleDeg  = Math.toDegrees(onTheRamp.getAngle());  // 49.0325

// And back to human-readable numbers, for the dashboard only.
double pitchDeg = Math.toDegrees(onTheRamp.getY());       // 20.0
double yawDeg   = Math.toDegrees(onTheRamp.getZ());       // 45.0
```

Pitch 20 plus yaw 45 is a **single rotation of 49.03 degrees about the axis (−0.1601, 0.3866, 0.9082)** — mostly vertical, tipped over. Two turns in, one turn out, exactly as Step 4 promised. The from-scratch tier agrees: feed that axis and angle to `fromAxisAngle` and it reproduces `(0.90984, −0.06645, 0.16043, 0.37687)` component for component.

None of this is academic — an AprilTag's location comes back as a `Pose3d`, and so does the camera-to-tag observation:

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

**Every 3D engine runs on this.** Unity's `Quaternion` is the only type it stores a rotation in; `transform.eulerAngles` is a view computed on demand, and Unity's own documentation warns against using it as storage. Unreal, Godot, Blender and glTF — the format most 3D assets ship in — all store orientation as four numbers. Character animation is the reason: blending two keyframed poses is a SLERP, sixty times a second, on every joint of every skeleton in the scene, and Euler angles would make limbs take the long way round exactly as a naively blended turret does.

**Orientation is also a live problem in machine learning, and the representation is the whole difficulty.** A network predicting an object's pose from an image has to emit a rotation, and emitting three Euler angles trains badly. The reason is the discontinuity Concept 05 fixed for a single angle, now unavoidable: the map from orientations to Euler triples has points where a tiny change in the true orientation forces a large change in the target numbers, and near gimbal lock the target is not even unique. A regression loss cannot reconcile that — the network is asked to fit a function with a jump in it, and hedges by predicting the average of both sides, which is wrong everywhere.

Predicting a quaternion is a large improvement, and is what most pose-estimation networks did first: the four outputs are normalized to length 1, which is Step 6's constraint imposed as a network layer. It is still imperfect, because `q` and `−q` are the same rotation, so the target is ambiguous unless a sign is chosen consistently. The current standard fix is a **6D representation** — predict two vectors and orthogonalize them into a frame — which removes that ambiguity too. The lesson generalizes past robotics: when a quantity lives on a curved space, the coordinates you pick for it are not neutral bookkeeping, and picking badly makes a solvable learning problem hard.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1

A robot is level and facing straight down-field: no rotation at all. Write its quaternion. Then write the quaternion for a robot yawed 180 degrees, and confirm from the four numbers alone that it is a half turn about the vertical.

**Solution:**

1. **No rotation** means θ = 0 about any axis. The half-angle is 0, so `w = cos 0° = 1`, and `sin 0° = 0` kills the axis: `(x, y, z) = (0, 0, 0)`.
2. The **identity quaternion** is `(1, 0, 0, 0)`, and `1² + 0 + 0 + 0 = 1`. ✓ The axis is undefined, correctly — a zero rotation has no distinguished axis, which is the `1e-9` branch in `toAxisAngle`.
3. **Yawed 180 degrees** is θ = 180° about `n̂ = (0, 0, 1)`. The half-angle is 90°, so `w = cos 90° = 0` and `(x, y, z) = (0, 0, 1) × sin 90° = (0, 0, 1)`.
4. The quaternion is `(0, 0, 0, 1)`, and `0 + 0 + 0 + 1² = 1`. ✓
5. **Read it back.** `θ = 2 × arccos(0) = 180°`, and `sin(θ/2) = 1`, so the axis is `(0, 0, 1)` — straight up. A half turn about the vertical, recovered from the numbers alone.

---

### Checkpoint 2

A shooter is elevated until its barrel points straight up — a pitch of −90 degrees in the frame of Step 1. Software commands yaw 40 degrees, roll 0. A moment later it commands yaw 0, roll 40. The mechanism does not move. Explain why, and say what a controller comparing those two yaw readings would do.

**Solution:**

1. **Identify the axes.** At −90 degrees of pitch the nose axis has been tipped onto the vertical, so the roll axis and the yaw axis are the same line.
2. **The two commands are therefore the same rotation.** A roll of 40 about a vertical nose *is* a yaw of 40. Only the sum `yaw + roll` reaches the hardware, and the split between them is unobservable — Step 3's table shows the same collapse for `(30, −30)` against `(0, 0)`.
3. **What the controller sees.** Its yaw feedback dropped from 40 to 0 while the mechanism sat perfectly still: a 40-degree error appearing in one loop cycle from nothing. A proportional controller answers with a large output and slams a stationary mechanism.
4. **Why reality is worse.** Nothing sits at exactly 90 degrees; it sits near it, where the encoding is not degenerate but is violently sensitive. At 89.9 degrees, `√2 × 0.1° = 0.141°` of real motion swings the yaw reading through 90 degrees, and noise alone produces that. The fix is not to filter yaw harder — it is to stop storing orientation as three angles.

---

### Deep Dive 1

Step 5 asserted the half-angle without proving it. Check the simplest case by hand: let `q` be a rotation of θ about Z, so `q = (cos(θ/2), 0, 0, sin(θ/2))`, and let `v` be `(1, 0, 0)` written as the quaternion `(0, 1, 0, 0)`. Work out `q v q⁻¹` with the multiplication rule from the code section, remembering that the inverse of a unit quaternion negates `x`, `y` and `z`. Show that the result is `(0, cos θ, sin θ, 0)` — the vector `(cos θ, sin θ, 0)`, which is exactly Concept 02's 2D rotation applied to `î`. Then say precisely where the two half-angles combined into one full angle, and predict what you would get if the full θ had been stored instead.

### Deep Dive 2

Step 8 claimed SLERP blends orientations correctly and averaging Euler angles does not. Build the counterexample: orientation A is roll 0, pitch 0, yaw 170 degrees, and orientation B is roll 0, pitch 0, yaw −170 degrees — 20 degrees apart. Blend by averaging each angle at `t = 0.25`, `0.5` and `0.75`, describe the path the nose takes, compare it with Geometry Concept 03's answer for `lerp(350, 10, 0.5)`, and name the shared root cause. Then convert both to quaternions and work out what goes wrong if a SLERP implementation does *not* check whether the two have a negative dot product first — recall from Step 5 that `q` and `−q` are the same orientation, and decide which arc the interpolation takes in each case.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../06_concept_law_of_cosines/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 06: Law of Cosines</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../../03_linear_algebra/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 3: Linear Algebra →</a></div>
</div>
