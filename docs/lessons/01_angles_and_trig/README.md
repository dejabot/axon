# Lesson 1: Angles and Trig Ratios

**Builds on:** arithmetic and square roots.

**Leads to:** [Lesson 2, Vectors](../02_vectors/).

---

## What we are trying to do

A mobile robot carries two kinds of sensor that between them ought to say where it is. A **gyro** reports which way the robot is facing. **Encoders** on the wheels report how fast it is driving forward. Neither one reports a position. Turning a stream of headings and speeds into a position on the floor is called odometry, and that is Lesson 6.

The first step, and the whole of this lesson, is one moment of that motion. Freeze the robot at a single instant: it faces some direction and moves at some speed. Where is that motion taking it?

The concrete instance we will solve: the robot faces 30° to the left of straight down-field and drives forward at 2.0 m/s. After one second, how far down-field has it gone, and how far sideways?

To answer that we need, in this order:

- how to describe a direction with an angle, and a sign convention that fixes what the angle means;
- degrees and radians, the two units angles come in;
- the three ratios of a right triangle, and why they depend on the angle alone;
- the unit circle, which extends those ratios to any heading, not just the ones that fit inside a triangle;
- the identity that guarantees the split loses no speed;
- velocity as a quantity with a direction, and displacement as velocity times time.

---

## The picture

<div style="text-align: center; margin: 20px 0;">
  <svg width="400" height="242" viewBox="0 0 380 230" style="max-width: 100%; height: auto;" role="img" aria-label="A robot seen from above, facing thirty degrees to the left of down-field, with a two meters per second velocity arrow split by dashed lines into an unknown down-field leg and an unknown sideways leg.">
    <line x1="40" y1="170" x2="350" y2="170" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <line x1="150" y1="40" x2="150" y2="210" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <text x="296" y="186" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">+x down-field</text>
    <text x="156" y="52" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">+y left</text>
    <g transform="rotate(-30 150 170)">
      <rect x="128" y="152" width="44" height="36" rx="6" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-opacity="0.6" stroke-width="2" />
      <line x1="166" y1="156" x2="166" y2="184" stroke="currentColor" stroke-opacity="0.55" stroke-width="2.5" />
    </g>
    <path d="M 184 170 A 34 34 0 0 0 179.4 153.0" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="190" y="164" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">30°</text>
    <line x1="150" y1="170" x2="253.9" y2="110.0" stroke="#fbbf24" stroke-width="3" />
    <polygon points="253.9,110.0 246.0,120.3 241.0,111.7" fill="#fbbf24" />
    <text x="186" y="124" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">2.0 m/s</text>
    <line x1="150" y1="170" x2="253.9" y2="170" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,4" />
    <line x1="253.9" y1="170" x2="253.9" y2="110.0" stroke="#4ade80" stroke-width="2.5" stroke-dasharray="4,4" />
    <rect x="243.9" y="160" width="10" height="10" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <text x="176" y="190" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">down-field = ?</text>
    <text x="258" y="142" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">sideways = ?</text>
    <circle cx="150" cy="170" r="3.5" fill="currentColor" fill-opacity="0.7" />
    <text x="8" y="222" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="9">The robot from above. Known: heading 30°, speed 2.0 m/s. Wanted: the two legs.</text>
  </svg>
</div>

The amber arrow is what the robot is doing; the two dashed lines are the answer we want. Notice that they close into a triangle with a square corner in it. That triangle is the subject of this lesson.

---

## Intuition

Walk diagonally across a parking lot, heading somewhere between north and east. Part of every step goes north and part of it goes east. There is no such thing as a step that goes diagonally without going partly north.

Turn a little further toward east and you give up some north-progress and gain some east-progress. Turn all the way to east and the north part is gone. The trade between the two is set entirely by the angle you walk at, and not at all by how fast you walk.

That last point deserves a sentence of its own. Fast or slow, at the same angle, the same fraction of your motion goes north. So the useful thing to know about an angle is a pair of fractions: what fraction of the motion goes north, and what fraction goes east. That is the whole lesson. Once we have the two fractions for an angle, we multiply each by the speed and we are done.

---

## The theory, from first principles

### Step 1. Saying which way

The gyro hands us a number, and "30°" on its own does not say 30° from what, or turned which way. So we fix both.

An **angle** is an amount of turn. We measure it in **degrees**, where a full turn back to the starting direction is 360 degrees, written 360°. There is nothing special about 360: it is a convention inherited from Babylonian astronomy, kept because 360 divides evenly by so many numbers. Later in this lesson we meet a second unit that most software prefers.

We also pick a frame: a direction that counts as zero, and a rotational direction that counts as positive. This is a choice, not a fact, and different teams and different software make different choices. Ours is WPILib's field convention, which is what the team's gyro reports:

- **down-field** is the positive x direction;
- **left**, when you are facing down-field, is the positive y direction;
- angles are measured **counter-clockwise** from down-field, seen from above.

So a robot facing straight down-field has heading 0°, and our robot has heading +30°. From here on we call that number θ, the Greek letter theta, which is the traditional name for an angle.

### Step 2. The triangle already in the picture

In Figure 1, the velocity arrow, the dashed blue line that is its shadow on the down-field axis, and the dashed green line dropping from its tip form a closed three-sided shape.

A **right triangle** is a triangle with one angle of exactly 90°, called a right angle and marked in figures by a small square. The other two angles are each less than 90°. The side opposite the right angle, always the longest, is the **hypotenuse**; the other two are the **legs**.

The legs get names, but the names depend on which of the two non-right angles you mean. Pick one and call it θ. The **opposite** leg is the one that does not touch θ. The **adjacent** leg is the one that touches θ and is not the hypotenuse. So "hypotenuse" is fixed by the triangle, while "opposite" and "adjacent" are fixed by your choice of angle, and choosing the other non-right angle swaps them.

<div style="text-align: center; margin: 20px 0;">
  <svg width="420" height="222" viewBox="0 0 400 212" style="max-width: 100%; height: auto;" role="img" aria-label="The same right triangle drawn twice. On the left the angle is chosen at the lower-left vertex, so the horizontal leg is adjacent and the vertical leg is opposite. On the right the angle is chosen at the top vertex and the two labels have swapped.">
    <line x1="20" y1="160" x2="116" y2="160" stroke="#38bdf8" stroke-width="3" />
    <line x1="116" y1="160" x2="116" y2="88" stroke="#4ade80" stroke-width="3" />
    <line x1="20" y1="160" x2="116" y2="88" stroke="#fbbf24" stroke-width="3" />
    <rect x="106" y="150" width="10" height="10" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <path d="M 46 160 A 26 26 0 0 0 40.8 144.4" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="50" y="154" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">θ</text>
    <text x="36" y="176" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">adjacent</text>
    <text x="122" y="128" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">opposite</text>
    <text x="12" y="112" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="bold">hypotenuse</text>
    <text x="10" y="196" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">angle chosen at the left vertex</text>
    <line x1="220" y1="160" x2="316" y2="160" stroke="#4ade80" stroke-width="3" />
    <line x1="316" y1="160" x2="316" y2="88" stroke="#38bdf8" stroke-width="3" />
    <line x1="220" y1="160" x2="316" y2="88" stroke="#fbbf24" stroke-width="3" />
    <rect x="306" y="150" width="10" height="10" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <path d="M 316 114 A 26 26 0 0 1 295.2 103.6" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="300" y="120" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">θ</text>
    <text x="236" y="176" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">opposite</text>
    <text x="322" y="128" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">adjacent</text>
    <text x="212" y="112" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="bold">hypotenuse</text>
    <text x="210" y="196" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">angle chosen at the top vertex</text>
  </svg>
</div>

In our picture, θ sits at the robot, the corner where the velocity arrow and the down-field axis meet. So the down-field component is the adjacent leg, the sideways component is the opposite leg, and the speed is the hypotenuse. The problem now has a clean statement: given the hypotenuse, 2.0 m/s, and the angle, 30°, find the two legs.

### Step 3. Why the fraction depends on the angle alone

This is the step everything else rests on: the parking-lot claim that the trade between forward and sideways is set by the angle and not by the speed. Here is why it is true.

First, scaling. Take any right triangle and multiply every side by the same number k, keeping the angles the same. You get a bigger or smaller copy of the same shape. Now look at a ratio of two of its sides, say the opposite leg divided by the hypotenuse:

$$\frac{k \times \text{opposite}}{k \times \text{hypotenuse}} = \frac{\text{opposite}}{\text{hypotenuse}}$$

The k cancels top and bottom, so the ratio survives scaling untouched.

Second, angles. The three angles of any triangle add up to 180°. To convince yourself rather than take it on faith, cut a triangle out of paper, tear off its three corners, and lay them side by side with their points touching: they fill a straight line, and a straight line is a half turn, which is 180°.

Now take two right triangles that share one of their non-right angles, say both have a 30° in them. Each has a 90°, so each has a third angle of 180° − 90° − 30° = 60°. All three angles match. Two triangles with all three angles equal are called **similar**, and similar triangles are scaled copies of one another: one is the other blown up or shrunk by some factor k.

Put the two facts together. Any two right triangles with the same acute angle are scaled copies, and scaling does not change a ratio of sides. Therefore the ratio of any two sides of a right triangle is fixed by the angle and by nothing else. Not by size, and not by speed.

A numeric check. A right triangle with legs 90 and 120 and hypotenuse 150 is the familiar 3-4-5 shape scaled up by 30. Taking the angle at the corner touching the side of length 120:

$$
\begin{aligned}
\frac{\text{opposite}}{\text{hypotenuse}} &= \frac{90}{150} = 0.600 \cr
\frac{\text{adjacent}}{\text{hypotenuse}} &= \frac{120}{150} = 0.800 \cr
\frac{\text{opposite}}{\text{adjacent}} &= \frac{90}{120} = 0.750
\end{aligned}
$$

Halve every side to 45, 60 and 75 and the ratios come out 45/75 = 0.600, 60/75 = 0.800 and 45/60 = 0.750. Unchanged, as promised.

### Step 4. Naming the ratios

Because each ratio depends only on the angle, each ratio is a **function** of the angle: feed in an angle, get back one fixed number. All three of them are used often enough to have names.

$$
\begin{aligned}
\sin \theta &= \frac{\text{opposite}}{\text{hypotenuse}} \cr
\cos \theta &= \frac{\text{adjacent}}{\text{hypotenuse}} \cr
\tan \theta &= \frac{\text{opposite}}{\text{adjacent}}
\end{aligned}
$$

The standard mnemonic is SOH-CAH-TOA: Sine is Opposite over Hypotenuse, Cosine is Adjacent over Hypotenuse, Tangent is Opposite over Adjacent.

> ### Math!
>
> `sin θ` is read "sine theta", `cos θ` is "cosine theta", `tan θ` is "tangent theta". The name and the angle are written next to each other with no symbol between them, which looks like multiplication but is not. `sin θ` does not mean "sin times θ"; it means "the sine function applied to the angle θ", and on its own `sin` is not a number at all. Some writers add brackets, `sin(θ)`, and that means the same thing. One more piece of shorthand you will meet in Step 8: `sin²θ` means `(sin θ)²`, that is, take the sine first and then square the result. It does not mean the sine of θ².

For our problem, tangent has a plain reading: sideways meters per down-field meter. At 30° it is 0.577, so the robot slides 0.577 m sideways for every 1 m it makes down-field. Tangent has no upper limit. As the heading approaches 90°, straight sideways, down-field progress approaches zero and the ratio runs away: tan 89° = 57.29, tan 89.9° = 572.96, tan 89.99° = 5729.6. At exactly 90° it is undefined, which is correct rather than broken, since a robot going straight sideways makes no down-field progress to divide by.

Tangent also runs backwards: given the two components, its inverse recovers the angle. That is how Lesson 2 turns a pair of numbers back into a heading.

### Step 5. Solving the opening problem, first pass

We know the hypotenuse and want the legs, so multiply both sides of each definition by the hypotenuse:

$$\text{adjacent} = \text{hypotenuse} \times \cos \theta \qquad \text{opposite} = \text{hypotenuse} \times \sin \theta$$

Those are the parking lot's two fractions, now with names. Put in our numbers, with the hypotenuse being the speed 2.0 m/s and θ being 30°:

$$\text{down-field} = 2.0 \times \cos 30° = 2.0 \times 0.866 = 1.732 \text{ m/s}$$

$$\text{sideways} = 2.0 \times \sin 30° = 2.0 \times 0.500 = 1.000 \text{ m/s}$$

A calculator or a software library supplies the two numbers 0.866 and 0.500. Where those numbers come from, and how to get them for a heading that will not fit inside a right triangle at all, is the next two steps.

### Step 6. Every heading, not just the ones in a triangle

The non-right angles of a right triangle are each under 90°, so everything from Step 2 onward covers only headings between 0° and 90°. A robot can face anywhere, including backwards.

Fix it by shrinking the triangle to a standard size. Divide every side by the hypotenuse. By Step 3 the ratios do not change, but the hypotenuse becomes hypotenuse/hypotenuse = 1, and the two legs become

$$\frac{\text{adjacent}}{\text{hypotenuse}} = \cos \theta \qquad \frac{\text{opposite}}{\text{hypotenuse}} = \sin \theta$$

In a triangle whose hypotenuse is 1, the legs are no longer proportional to the ratios. They **are** the ratios.

Now place that triangle on a grid, with θ at the origin and the adjacent leg along the positive x axis. The tip of the hypotenuse sits at the point (cos θ, sin θ), always exactly 1 unit from the origin. Sweep θ around and that point traces a circle of radius 1 centered on the origin: the **unit circle**.

This gives us the definition we were missing. For any angle at all, cos θ and sin θ are the x and y coordinates of the point you reach by starting at (1, 0) and turning counter-clockwise by θ around the unit circle. Between 0° and 90° this agrees with the triangle ratios. Beyond 90° there is no triangle to appeal to, and this is simply the definition.

<div style="text-align: center; margin: 20px 0;">
  <svg width="360" height="340" viewBox="0 0 340 320" style="max-width: 100%; height: auto;" role="img" aria-label="The unit circle with the point at two hundred and twenty degrees in the third quadrant, its reference triangle drawn with dashed legs, the reference angle of forty degrees marked at the center, and the sign of cosine and sine labeled in each quadrant.">
    <circle cx="170" cy="160" r="120" fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.5" />
    <line x1="40" y1="160" x2="300" y2="160" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.5" />
    <line x1="170" y1="30" x2="170" y2="290" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.5" />
    <text x="294" y="153" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">1</text>
    <text x="40" y="153" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">−1</text>
    <text x="176" y="44" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">1</text>
    <text x="176" y="290" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="10">−1</text>
    <text x="236" y="60" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="9.5">I: cos + sin +</text>
    <text x="14" y="60" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="9.5">II: cos − sin +</text>
    <text x="14" y="268" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="9.5">III: cos − sin −</text>
    <text x="232" y="268" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="9.5">IV: cos + sin −</text>
    <path d="M 220 160 A 50 50 0 1 0 131.7 192.1" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="180" y="100" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">220°</text>
    <path d="M 144 160 A 26 26 0 0 0 150.1 176.7" fill="none" stroke="#c084fc" stroke-width="2" stroke-opacity="0.8" />
    <text x="134" y="176" text-anchor="middle" fill="#c084fc" font-family="sans-serif" font-size="9.5" font-weight="bold">40°</text>
    <line x1="170" y1="160" x2="78.1" y2="160" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,4" />
    <line x1="78.1" y1="160" x2="78.1" y2="237.1" stroke="#4ade80" stroke-width="2.5" stroke-dasharray="4,4" />
    <rect x="78.1" y="160" width="10" height="10" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <line x1="170" y1="160" x2="78.1" y2="237.1" stroke="#fbbf24" stroke-width="3" />
    <circle cx="78.1" cy="237.1" r="6" fill="#fbbf24" />
    <text x="89" y="176" fill="#38bdf8" font-family="sans-serif" font-size="9.5" font-weight="bold">cos =</text>
    <text x="89" y="189" fill="#38bdf8" font-family="sans-serif" font-size="9.5" font-weight="bold">−0.766</text>
    <text x="6" y="205" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">sin = −0.643</text>
    <circle cx="170" cy="160" r="3.5" fill="currentColor" fill-opacity="0.7" />
    <text x="12" y="312" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">θ = 220°: the point is (−0.766, −0.643)</text>
  </svg>
</div>

Take θ = 220°, drawn above. Turning counter-clockwise by 220° from the positive x axis puts the point down and to the left of the origin, in the third of the four quarters of the plane. Those quarters are called **quadrants**, numbered I to IV counter-clockwise starting from the upper right.

To read off the numbers, drop a perpendicular from the point to the x axis. That makes a right triangle again, and the angle it makes at the origin, between the radius and the nearest part of the x axis, is 220° − 180° = 40°. This is called the **reference angle**. The triangle's legs have lengths cos 40° = 0.766 and sin 40° = 0.643. The signs come from which side of each axis the point sits on: left of the vertical axis, so its x coordinate is negative, and below the horizontal axis, so its y coordinate is negative. Hence cos 220° = −0.766 and sin 220° = −0.643.

The same reading works in every quadrant, and it always comes down to this table:

| Quadrant | Angles | cos θ | sin θ |
|---|---|---|---|
| I | 0° to 90° | + | + |
| II | 90° to 180° | − | + |
| III | 180° to 270° | − | − |
| IV | 270° to 360° | + | − |

Now the worked example. The robot is at heading 220°, driving at 1.5 m/s. Step 5's formulas do not change at all:

$$\text{down-field} = 1.5 \times \cos 220° = 1.5 \times (-0.766) = -1.149 \text{ m/s}$$

$$\text{sideways} = 1.5 \times \sin 220° = 1.5 \times (-0.643) = -0.964 \text{ m/s}$$

Both are negative. Under our sign convention, negative down-field means up-field, back toward our own end, and negative sideways means to the right, which is exactly what a heading of 220° should mean. The formulas needed no special case; the unit circle handled the signs.

One more property falls straight out of the picture. A full 360° brings you back to the same point on the circle, so 220°, 220° − 360° = −140°, and 220° + 360° = 580° all name the same direction and all give the same cosine and sine. The functions repeat every 360°. That is convenient here and a nuisance later, because one heading then has infinitely many numerical names. Lesson 3 deals with what that costs you when comparing two headings.

### Step 7. Radians

We are about to hand these angles to software, and the library functions that compute sines and cosines do not take degrees. They take radians.

Go back to the unit circle. Instead of measuring an angle by what fraction of an arbitrary 360 it is, measure it by the distance you walk along the rim while turning. That distance is the angle in **radians**.

<div style="text-align: center; margin: 20px 0;">
  <svg width="320" height="208" viewBox="0 0 300 195" style="max-width: 100%; height: auto;" role="img" aria-label="A circle of radius one with two radii drawn, and the arc between them highlighted. The arc has length one and the angle between the radii is one radian, about fifty-seven point three degrees.">
    <circle cx="80" cy="150" r="100" fill="none" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <path d="M 180 150 A 100 100 0 0 0 134.0 65.9" fill="none" stroke="#4ade80" stroke-width="5" />
    <line x1="80" y1="150" x2="180" y2="150" stroke="#fbbf24" stroke-width="2.5" />
    <line x1="80" y1="150" x2="134.0" y2="65.9" stroke="#fbbf24" stroke-width="2.5" />
    <path d="M 110 150 A 30 30 0 0 0 96.2 124.7" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="114" y="134" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">1 rad</text>
    <text x="98" y="166" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">radius = 1</text>
    <text x="176" y="100" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold">arc length = 1</text>
    <circle cx="80" cy="150" r="3.5" fill="currentColor" fill-opacity="0.7" />
    <text x="10" y="176" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">Walk 1 unit along the rim of a unit circle:</text>
    <text x="10" y="190" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">that turn is 1 radian, about 57.3°.</text>
  </svg>
</div>

Walking all the way around a circle of radius 1 covers its circumference, 2π, roughly 6.283. So a full turn is 2π radians, a half turn is π radians, and a quarter turn is π/2 radians. Setting the two units for a full turn equal, 360° = 2π rad, gives the conversions:

$$\text{radians} = \text{degrees} \times \frac{\pi}{180} \qquad \text{degrees} = \text{radians} \times \frac{180}{\pi}$$

So our heading 30° is 30 × π/180 = 0.5236 rad, the heading 220° from the last example is 220 × π/180 = 3.840 rad, and 1 rad is 1 × 180/π = 57.2958°.

> ### Math!
>
> On a circle of radius r rather than 1, an angle θ cuts off an arc whose length s is given by `s = r θ`, read "s equals r theta", and the θ must be in radians. This is the reason radians are worth the trouble: with them, arc length is just radius times angle, with no conversion factor stuck in front. With degrees you would have to write `s = r θ π / 180` every time. That single clean formula is how a wheel encoder's count of rotations turns into meters rolled across the floor, which you will see in the team's code in Step 9.

### Step 8. Did the split lose any speed?

We claimed the two components account for all of the robot's 2.0 m/s. That deserves a check, because if the split leaked speed then every position we computed downstream would drift.

The check needs one classical result, and since we are assuming nothing, here is where it comes from. Draw a square of side a + b, where a and b are the two legs of our right triangle, and fit four copies of that triangle inside it in two different arrangements.

<div style="text-align: center; margin: 20px 0;">
  <svg width="380" height="200" viewBox="0 0 360 190" style="max-width: 100%; height: auto;" role="img" aria-label="Two squares of the same size. In the left one, four copies of a right triangle sit in the corners and leave a tilted square of side c in the middle. In the right one, the same four triangles are regrouped to leave two squares of sides a and b.">
    <polygon points="80,20 160,80 100,160 20,100" fill="#38bdf8" fill-opacity="0.18" />
    <polygon points="20,20 80,20 20,100" fill="#fbbf24" fill-opacity="0.3" />
    <polygon points="160,20 80,20 160,80" fill="#fbbf24" fill-opacity="0.3" />
    <polygon points="160,160 160,80 100,160" fill="#fbbf24" fill-opacity="0.3" />
    <polygon points="20,160 20,100 100,160" fill="#fbbf24" fill-opacity="0.3" />
    <polygon points="80,20 160,80 100,160 20,100" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <rect x="20" y="20" width="140" height="140" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="2" />
    <text x="82" y="96" fill="currentColor" fill-opacity="0.85" font-family="sans-serif" font-size="13" font-weight="bold">c²</text>
    <text x="46" y="15" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">a</text>
    <text x="116" y="15" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">b</text>
    <text x="126" y="46" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">c</text>
    <rect x="200" y="20" width="60" height="60" fill="#38bdf8" fill-opacity="0.18" />
    <rect x="260" y="80" width="80" height="80" fill="#38bdf8" fill-opacity="0.18" />
    <polygon points="260,20 340,20 260,80" fill="#fbbf24" fill-opacity="0.3" />
    <polygon points="340,20 340,80 260,80" fill="#fbbf24" fill-opacity="0.3" />
    <polygon points="200,80 260,80 200,160" fill="#fbbf24" fill-opacity="0.3" />
    <polygon points="260,80 260,160 200,160" fill="#fbbf24" fill-opacity="0.3" />
    <line x1="260" y1="80" x2="340" y2="20" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <line x1="200" y1="160" x2="260" y2="80" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <rect x="200" y="20" width="60" height="60" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <rect x="260" y="80" width="80" height="80" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="1.5" />
    <rect x="200" y="20" width="140" height="140" fill="none" stroke="currentColor" stroke-opacity="0.55" stroke-width="2" />
    <text x="224" y="56" fill="currentColor" fill-opacity="0.85" font-family="sans-serif" font-size="13" font-weight="bold">a²</text>
    <text x="292" y="126" fill="currentColor" fill-opacity="0.85" font-family="sans-serif" font-size="13" font-weight="bold">b²</text>
    <text x="12" y="182" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10.5">Same square, same four triangles: c² = a² + b².</text>
  </svg>
</div>

On the left, the four triangles sit in the corners and the space they leave in the middle is a tilted square whose side is the hypotenuse c, so the leftover area is c². On the right, the same four triangles are regrouped into two rectangles, and the space they leave is two squares, of sides a and b, so the leftover area is a² + b². The outer square is the same in both pictures and the four triangles have the same total area in both, so the leftovers are equal:

$$c^2 = a^2 + b^2$$

That is the Pythagorean theorem, and it is now ours rather than borrowed.

Apply it to the unit circle. The point at angle θ is cos θ across and sin θ up from the origin, with the radius as hypotenuse, and the radius is 1. So:

$$\cos^2\theta + \sin^2\theta = 1$$

This holds for every angle in every quadrant, because squaring wipes out the signs. Now scale it back up to a real speed v by multiplying both sides by v²:

$$(v \cos \theta)^2 + (v \sin \theta)^2 = v^2$$

The left side is exactly our two components, squared and added. Check it with our numbers:

$$1.732^2 + 1.000^2 = 3.000 + 1.000 = 4.000 \qquad \sqrt{4.000} = 2.000 \text{ m/s}$$

The two parts recombine to the full 2.0 m/s. The split lost nothing.

### Step 9. Finish the problem

We have the robot's **velocity**, a speed together with a direction, split into 1.732 m/s down-field and 1.000 m/s to the left. The question asked for distances after one second.

**Displacement** is the change of position, and like velocity it carries a direction. When velocity is constant, displacement is velocity times elapsed time. Our robot holds its heading and speed for 1.0 s, so:

$$\Delta x = 1.732 \times 1.0 = 1.732 \text{ m} \qquad \Delta y = 1.000 \times 1.0 = 1.000 \text{ m}$$

After one second the robot is at (1.732, 1.000) m relative to where it started: 1.732 m down-field and 1.000 m to the left. The straight-line distance from the start is

$$\sqrt{1.732^2 + 1.000^2} = \sqrt{3.000 + 1.000} = 2.000 \text{ m}$$

which is 2.0 m/s for 1.0 s, as it must be. That is the opening problem, solved.

The same split works when the second direction is up instead of sideways. A ball leaves a shooter at 12 m/s, aimed 55° above the horizontal. Here cos 55° = 0.5736 and sin 55° = 0.8192, so the ball moves forward at 12 × 0.5736 = 6.883 m/s and upward at 12 × 0.8192 = 9.830 m/s, and the check holds: √(6.883² + 9.830²) = 12.000. Nothing about the method cared that the plane was vertical rather than horizontal. Lesson 5, on how a ball flies, starts from exactly those two numbers.

---

## Try it

Drag the heading around and watch the two dashed legs and the ghost robot move with it.

<iframe src="demo.html" width="100%" height="640" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## In code

### Tier 1, plain Java with WPILib Units

```java
import static edu.wpi.first.units.Units.*;
import edu.wpi.first.units.measure.Angle;
import edu.wpi.first.units.measure.Distance;
import edu.wpi.first.units.measure.LinearVelocity;
import edu.wpi.first.units.measure.Time;

Angle heading = Degrees.of(30.0);
LinearVelocity speed = MetersPerSecond.of(2.0);
Time elapsed = Seconds.of(1.0);

// Math.cos and Math.sin take radians. The Units library does the conversion.
double cosHeading = Math.cos(heading.in(Radians));   // 0.866
double sinHeading = Math.sin(heading.in(Radians));   // 0.500

LinearVelocity downField = speed.times(cosHeading);  // 1.732 m/s
LinearVelocity sideways  = speed.times(sinHeading);  // 1.000 m/s

Distance dx = downField.times(elapsed);              // 1.732 m
Distance dy = sideways.times(elapsed);               // 1.000 m

System.out.printf("down-field %.3f m, sideways %.3f m%n", dx.in(Meters), dy.in(Meters));
```

This is Step 5 typed out line for line. The point of the `Angle`, `LinearVelocity`, `Distance` and `Time` types is that each quantity carries its unit with it, so a heading measured in degrees cannot be handed to `Math.cos` by accident: the compiler will not let an `Angle` stand where a `double` is wanted. The one place the conversion happens is `heading.in(Radians)`, which is visible, deliberate, and easy to find later. All three tiers produce the same 1.732 and 1.000.

### Tier 2, WPILib geometry

```java
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.math.geometry.Translation2d;

Rotation2d heading = new Rotation2d(Degrees.of(30.0));   // or Rotation2d.fromDegrees(30.0)
double speedMps = 2.0;

double downFieldMps = speedMps * heading.getCos();   // 1.732
double sidewaysMps  = speedMps * heading.getSin();   // 1.000

// The same split in one call: a length pointed along a direction.
Translation2d velocity = new Translation2d(speedMps, heading);   // (1.732, 1.000)
Translation2d afterOneSecond = velocity.times(1.0);              // (1.732, 1.000) m
```

`Rotation2d` is WPILib's type for an angle. It stores the angle and caches its cosine and sine at construction, so `getCos()` and `getSin()` are reads of a stored number. That matters in a loop that runs fifty times a second: nothing recomputes a trig function it already has. The constructor `new Translation2d(distance, angle)` is Step 5 packaged as one call, taking a length and a direction and handing back the pair of components. Lesson 2 gives that pair its proper name, a vector.

### Tier 3, the team's code

These two lines are from [`Odometry.java`](https://github.com/Team766/robots/blob/main/src/main/java/com/team766/localization/Odometry.java) in the team's `robots` repository.

```java
currentWheelRotation[i] =
        Rotation2d.fromDegrees(gyro.getAngle()).plus(moduleList[i].getSteerAngle());
```

```java
Translation2d wheelMotion =
        new Translation2d(deltaX, deltaY).rotateBy(prevWheelRotation[i]);
```

Each wheel on this robot can be steered independently, so a wheel does not necessarily point where the robot points. Its direction on the field is the robot's heading, read from the gyro, plus how far that wheel is turned relative to the robot, read from its steering sensor. That is the first line.

In the second line, `deltaX` is how far that wheel rolled since the last loop. It comes from the wheel's number of turns times its circumference, 2πr: each full turn is 2π radians, so this is Step 7's arc length s = rθ with the angle in radians. For a wheel that rolled straight ahead, `deltaY` is zero, so the point being rotated is `(deltaX, 0)`, and turning it to the wheel's field direction gives exactly `(deltaX · cos θ, deltaX · sin θ)`. That is this lesson's split, once per wheel, fifty times a second, on a real robot. Lesson 3 covers what `rotateBy` does when `deltaY` is not zero, and Lesson 6 covers adding these little steps up into a position on the field.

---

## Recap

You can now turn a heading and a speed into a down-field part and a sideways part, using cosine for the leg along the heading's axis and sine for the leg across it. You know why those two fractions depend on the angle and not on the speed: right triangles sharing an acute angle are scaled copies, and scaling cancels out of a ratio. You can do it for any heading, not just the ones under 90°, by reading cos θ and sin θ off the unit circle and taking the signs from the quadrant. You can convert between degrees and radians in either direction, and you know why the library wants radians. And you can check your own work, because cos²θ + sin²θ = 1 guarantees the two parts recombine to the whole speed.

### Re-derive it from a blank page

Come back to this in about a week, take a blank sheet, and do these three without looking:

1. Show why the ratio of two sides of a right triangle depends on the angle alone.
2. Starting from the unit circle and Pythagoras, get cos²θ + sin²θ = 1.
3. A robot at heading 220° is driving at 1.5 m/s. Find both components, and check them.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Lessons</a></div>
  <div><a href="../02_vectors/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Lesson 2: Vectors →</a></div>
</div>
