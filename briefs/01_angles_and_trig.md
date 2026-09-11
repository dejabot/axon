# Brief: Lesson 1, Angles and Trig Ratios

Design record for `docs/lessons/01_angles_and_trig/`. The author writes `README.md` and the demo author writes `demo.html` from this brief. Every number below was recomputed by script; do not change a number without recomputing it.

## Audience and voice

Readers are a Team 766 mentor relearning this from scratch and high-school students meeting it for the first time. Assume nothing beyond arithmetic and square roots. Write plain, direct American English. No em-dashes, no emoji, no ASCII art, no jokes. Define every term the first time it appears, in general, not just in context. Show every algebra step that is not a single substitution. The lesson is a 30 to 45 minute read; write what the material needs and stop. Around 2,000 words of prose is typical. Do not pad and do not compress.

Say "PID", never "gains", if the topic ever comes up. It should not in this lesson.

## Shape, in this order

1. Title, then two lines: `**Builds on:** arithmetic and square roots.` and `**Leads to:** [Lesson 2, Vectors](../02_vectors/).`
2. **What we are trying to do.** The problem, in general robotics terms first, then the concrete instance.
3. **The picture.** Figure 1.
4. **Intuition.** Plain language, no symbols.
5. **The theory, from first principles.** Each idea introduced at the moment the problem needs it. Ends by solving the opening problem with numbers.
6. **Try it.** The embedded demo.
7. **In code.** Three tiers: plain Java with WPILib Units, WPILib geometry, then the team's own code.
8. **Recap** and one **re-derive prompt**.

Nothing else gets a section. No "design space", no "edge cases and bugs", no machine-learning bridge, no checkpoint quizzes. Two short worked examples beyond the opening problem live inside the theory where noted.

## The problem

General form: a mobile robot has a sensor that reports which way it is facing (a gyro) and encoders that report how fast it is driving forward. We want to know where it is on the floor. That is a later lesson (Lesson 6). The first step, and the whole of this lesson, is one moment of that motion.

Concrete instance: the robot faces 30° to the left of straight down-field and drives forward at 2.0 m/s. After one second, how far down-field has it gone, and how far sideways?

Frame convention, stated once in the theory when angles are introduced, as a choice not a fact: down-field is the positive x direction, left when facing down-field is positive y, and angles are measured counter-clockwise from down-field. This is WPILib's field convention and what the team's gyro reports.

After stating the problem, list in a short paragraph or bullet list what the lesson will cover to solve it: describing a direction with an angle and a sign convention; degrees and radians; the three ratios of a right triangle and why they depend on the angle alone; the unit circle so any heading works; the identity that guarantees the split loses no speed; velocity as a quantity with a direction and displacement as velocity times time.

## Verified numbers

| Quantity | Value |
|---|---|
| cos 30°, sin 30°, tan 30° | 0.866, 0.500, 0.577 |
| 30° in radians | 0.5236 |
| 1 radian in degrees | 57.2958 |
| Down-field speed, 2.0 m/s at 30° | 1.732 m/s |
| Sideways speed (to the left) | 1.000 m/s |
| Position after 1.0 s | (1.732, 1.000) m |
| Distance traveled after 1.0 s | 2.000 m, and √(1.732² + 1.000²) = √(3.000 + 1.000) = 2.000 |
| Shooter example: 12 m/s at 55° above horizontal | forward 6.883 m/s, up 9.830 m/s, √(6.883² + 9.830²) = 12.000 |
| cos 55°, sin 55° | 0.5736, 0.8192 (four decimals, so a reader who multiplies gets the printed products) |
| Third-quadrant example: 220°, 1.5 m/s | cos 220° = −0.766, sin 220° = −0.643, reference angle 40°, components −1.149 m/s and −0.964 m/s, 220° = 3.840 rad |
| 3-4-5 triangle scaled to 90, 120, 150 | sin = 0.600, cos = 0.800, tan = 0.750 |
| tan near 90° | tan 89° = 57.29, tan 89.9° = 572.96, tan 89.99° = 5729.6 |

## Intuition

Walking diagonally across a parking lot: part of every step goes north and part goes east. Turn further toward east and you trade north-progress for east-progress. The trade is set by the angle you walk at, not by how fast you walk. Fast or slow, at the same angle the same fraction of your motion goes north. That last sentence is the whole lesson: once we know the fraction for an angle, we multiply by the speed and we are done.

## The theory, step by step

Each step says why the problem needs it before introducing it.

**Step 1. Saying which way.** To use the gyro's number we need to agree what it means. Define an angle as an amount of turn, a full turn as 360 degrees (a convention inherited from Babylonian astronomy, not a fact about circles). State the frame convention above. So "30° to the left of down-field" is heading +30°, and a robot facing straight down-field is at 0°.

**Step 2. The triangle already in the picture.** The velocity arrow, its shadow on the down-field axis, and the vertical from the arrow tip form a right triangle. Define right triangle, hypotenuse, and the two legs. Name the legs relative to the chosen angle: opposite (does not touch the angle) and adjacent (touches it and is not the hypotenuse). Show with Figure 2 that choosing the other acute angle swaps the two names. The down-field component is the adjacent leg and the sideways component is the opposite leg. Our problem is: given the hypotenuse (2.0 m/s) and the angle (30°), find the two legs.

**Step 3. Why the fraction depends on the angle alone.** This is the load-bearing step. Scale a triangle by any factor k: every side is multiplied by k, so in the ratio opposite/hypotenuse the k cancels. Then: the three angles of any triangle add to 180° (say how to convince yourself: tear the corners off a paper triangle and lay them along a straight edge). Two right triangles that share one acute angle therefore share all three angles, and triangles with the same angles are scaled copies of each other (define "similar"). So the ratio of any two sides is fixed by the angle and nothing else. This is exactly the parking-lot intuition, now proved. Use the 90, 120, 150 triangle for a numeric check.

**Step 4. Naming the ratios.** Because the ratios depend only on the angle, they earn names as functions of the angle: sine is opposite over hypotenuse, cosine is adjacent over hypotenuse, tangent is opposite over adjacent. Mention SOH-CAH-TOA as the mnemonic. Include a "Math!" callout (a blockquote headed `### Math!`) giving the notation `sin θ`, `cos θ`, `tan θ`, how to read each aloud, that these are functions of the angle and not products, and that `sin²θ` means `(sin θ)²`. Tangent, for this problem, is "sideways meters per down-field meter": at 30°, 0.577 m sideways for every 1 m down-field. Say that Lesson 2 uses tangent's inverse to get an angle back from two components.

**Step 5. Solving the opening problem, first pass.** Rearrange: adjacent = hypotenuse × cos θ, opposite = hypotenuse × sin θ. Down-field speed = 2.0 × cos 30° = 2.0 × 0.866 = 1.732 m/s. Sideways = 2.0 × 0.500 = 1.000 m/s. State that a calculator or library supplies cos 30° and sin 30°; where those numbers come from is the next two steps.

**Step 6. Every heading, not just the ones in a triangle.** A right triangle's other angles are each under 90°, so Steps 2 to 5 only cover headings between 0° and 90°. A robot can face anywhere. Divide every side of the triangle by its hypotenuse so the hypotenuse becomes 1; the ratios are unchanged (Step 3) and now the legs *are* cos θ and sin θ. Put the angle at the origin: the far corner of the triangle sits at (cos θ, sin θ), always 1 unit from the origin. Sweep θ and that corner traces the unit circle. Define cos θ and sin θ for any angle as the x and y coordinates of the point at angle θ on the unit circle. Between 0° and 90° this is the same as before; beyond it, it is the definition. Use Figure 3 at 220°: reference angle 40°, cos 220° = −0.766, sin 220° = −0.643, signs read from which side of each axis the point sits. Give the quadrant sign table as a small Markdown table. Work the third example: at 220° and 1.5 m/s the robot is moving −1.149 m/s down-field (so, up-field) and −0.964 m/s sideways (to the right). Note that 220° and −140° and 580° all land on the same point, so cos and sin repeat every 360°; Lesson 3 deals with what that means for comparing headings.

**Step 7. Radians.** The library the code will call takes angles in radians, so we need the unit. On a circle of radius 1, measure an angle by the distance walked along the rim. Figure 4. A full turn is the circumference 2π, half a turn is π, a quarter is π/2. Conversions: radians = degrees × π/180, degrees = radians × 180/π. 30° = 0.5236 rad; 1 rad = 57.2958°. "Math!" callout for `s = r θ` with θ in radians, read aloud, and the one-sentence reason radians matter beyond this lesson: with radians, arc length equals radius times angle with no conversion factor, which is how a wheel encoder's rotations become meters rolled (this appears in the team code in Step 9).

**Step 8. Did the split lose any speed?** We claimed the two components account for all 2.0 m/s. Check it. First derive Pythagoras, because we assume nothing: Figure 5, the area rearrangement. A square of side a + b holds four copies of a right triangle with legs a and b either around a tilted square of side c, or regrouped to leave two squares of sides a and b. Same big square, same four triangles, so c² = a² + b². Then apply it to the unit-circle point (cos θ, sin θ), which is 1 from the origin: cos²θ + sin²θ = 1. Multiply through by v²: (v cos θ)² + (v sin θ)² = v². Numerically: 1.732² + 1.000² = 3.000 + 1.000 = 4.000, and √4.000 = 2.000 m/s. The split lost nothing.

**Step 9. Finish the problem.** Displacement is velocity times time when velocity is constant (define displacement: change of position, with a direction). Over 1.0 s: 1.732 m down-field and 1.000 m to the left, so the robot is at (1.732, 1.000) m relative to where it started, 2.000 m from it along its heading. Then the second worked example, one paragraph: the same split pointed upward instead of sideways. A ball leaves a shooter at 12 m/s, 55° above horizontal: forward 12 × 0.5736 = 6.883 m/s, up 12 × 0.8192 = 9.830 m/s, and √(6.883² + 9.830²) = 12.000. Lesson 5 starts from exactly these two numbers.

## Figures

All inline SVG, `style="max-width: 100%; height: auto;"`, with `role="img"` and an `aria-label`. Structural strokes use `currentColor` at reduced opacity so they render on both themes. Colored elements use these hex values, which read on both themes: blue `#38bdf8` for the down-field leg, green `#4ade80` for the sideways leg, amber `#fbbf24` for the hypotenuse or velocity arrow, purple `#c084fc` for the angle arc. Text at `font-family="sans-serif"`. Every coordinate below is computed; draw them as given so the geometry matches the labels.

**Figure 1, the problem.** viewBox `0 0 380 230`. Robot center at (150, 170). Faint field grid or a faint down-field axis through the center and a faint vertical axis. Scale 60 px per m/s. Velocity arrow from (150, 170) to (253.9, 110.0), amber, width 3, arrowhead at the tip, label "2.0 m/s". Robot body: a 44 by 36 rounded rectangle centered on (150, 170) with `transform="rotate(-30 150 170)"`, a short tick at its front. Down-field leg dashed blue from (150, 170) to (253.9, 170), labeled "down-field = ?". Sideways leg dashed green from (253.9, 170) to (253.9, 110.0), labeled "sideways = ?". Right-angle marker, a 10 by 10 square, at (243.9, 160). Angle arc purple radius 34: path `M 184 170 A 34 34 0 0 0 179.4 153.0`, labeled "30°". Caption line inside the SVG at the bottom: "The robot from above. Known: heading 30°, speed 2.0 m/s. Wanted: the two legs."

**Figure 2, naming the sides.** viewBox `0 0 400 212`. Same 3-4-5 triangle twice. Left copy: vertices (20, 160), (116, 160), (116, 88); right angle at (116, 160); angle chosen at (20, 160), which is 36.87°, arc radius 26 `M 46 160 A 26 26 0 0 0 40.8 144.4`. Legs: bottom (20,160)-(116,160) blue labeled "adjacent", vertical (116,160)-(116,88) green labeled "opposite", hypotenuse amber labeled "hypotenuse". Right copy shifted by +200 in x, with the angle chosen at the top vertex (316, 88) and the labels swapped: bottom leg green "opposite", vertical leg blue "adjacent". Captions under each: "angle chosen at the left vertex" and "angle chosen at the top vertex".

**Figure 3, the unit circle at 220°.** viewBox `0 0 340 320`. Circle center (170, 160), radius 120, faint. Axes through the center. Tick labels 1 and −1 at the axis ends. The point at 220°: (78.1, 237.1), amber dot radius 6. Radius line from center to the point, amber. Reference triangle: dashed blue from (170, 160) to (78.1, 160), dashed green from (78.1, 160) to (78.1, 237.1), right-angle marker at (78.1, 160) drawn toward the interior. Angle arc purple radius 50 from (220, 160) counter-clockwise on screen through the top to the point direction: path `M 220 160 A 50 50 0 1 0 131.7 192.1`, label "220°". Small reference-angle arc at the center between the negative x-axis and the radius, label "40°". Labels "cos = −0.766" under the blue leg and "sin = −0.643" beside the green leg. Quadrant sign labels in each quadrant: I cos + sin +, II cos − sin +, III cos − sin −, IV cos + sin −. Caption: "θ = 220°: the point is (−0.766, −0.643)".

**Figure 4, one radian.** viewBox `0 0 300 195`. Circle center (80, 150) radius 100, faint. Two radii, amber: to (180, 150) and to (134.0, 65.9). Arc on the rim between them, green, width 5: `M 180 150 A 100 100 0 0 0 134.0 65.9`. Small purple angle arc radius 30 near the center: `M 110 150 A 30 30 0 0 0 96.2 124.7`, label "1 rad". Labels "radius = 1" on the horizontal radius and "arc length = 1" by the green arc. Caption: "Walk 1 unit along the rim of a unit circle: that turn is 1 radian, about 57.3°."

**Figure 5, Pythagoras by rearrangement.** viewBox `0 0 360 190`. Two squares of side 140, legs a = 60 and b = 80 so c = 100. Left square from (20, 20) to (160, 160): four right triangles at the corners, each with legs 60 and 80, drawn as polygons (20,20)-(80,20)-(20,100); (160,20)-(80,20)-(160,80); (160,160)-(160,80)-(100,160); (20,160)-(20,100)-(100,160); the tilted inner square (80,20)-(160,80)-(100,160)-(20,100) labeled "c²". Right square from (200, 20) to (340, 160): square (200,20)-(260,80) labeled "a²", square (260,80)-(340,160) labeled "b²", the two remaining 60 by 80 rectangles each split by a diagonal into two of the same triangles: (260,20)-(340,80) with diagonal (260,80)-(340,20), and (200,80)-(260,160) with diagonal (200,160)-(260,80). Triangles filled with the amber color at low opacity, squares with blue at low opacity. Caption: "Same square, same four triangles: c² = a² + b²."

## Demo, embedded after the theory

Embed with `<iframe src="demo.html" width="100%" height="640" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>` preceded by a one-line invitation to drag the heading and watch the two legs and the ghost robot move. The demo spec is in its own section below.

## Code

Signpost each tier with an `###` heading. Numbers in comments must match the table. Say once, after the first tier, that all three tiers produce the same 1.732 and 1.000.

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

Explain in prose: the typed quantities carry their units, so a heading in degrees cannot be handed to `Math.cos` by accident; `heading.in(Radians)` is the one place the conversion happens.

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

Explain: `Rotation2d` stores the angle and caches its cosine and sine, so `getCos()` and `getSin()` cost nothing in a loop that runs fifty times a second. `new Translation2d(distance, angle)` is exactly Step 5, and Lesson 2 names the result a vector.

### Tier 3, the team's code

Quote from `src/main/java/com/team766/localization/Odometry.java` in the `robots` repo (link: https://github.com/Team766/robots/blob/main/src/main/java/com/team766/localization/Odometry.java). Two excerpts:

```java
currentWheelRotation[i] =
        Rotation2d.fromDegrees(gyro.getAngle()).plus(moduleList[i].getSteerAngle());
```

```java
Translation2d wheelMotion =
        new Translation2d(deltaX, deltaY).rotateBy(prevWheelRotation[i]);
```

Explain: each wheel on the robot can be steered, so a wheel's direction on the field is the robot's heading from the gyro plus how far that wheel is turned relative to the robot. `deltaX` is how far the wheel rolled since the last loop, which comes from the wheel's turns times its circumference 2πr (Step 7's arc length, with 2π radians per turn). For a wheel that rolled straight, `deltaY` is zero, and rotating the point `(deltaX, 0)` to the wheel's direction gives exactly `(deltaX · cos θ, deltaX · sin θ)`: this lesson's split, once per wheel, fifty times a second. Lesson 3 covers what `rotateBy` does when `deltaY` is not zero, and Lesson 6 covers adding these steps up into a position. Do not paste more of the file than these two excerpts.

## Recap and re-derive prompt

Recap in four or five sentences what the reader can now do: turn a heading and a speed into down-field and sideways parts for any heading, convert between degrees and radians, and check that the parts account for the whole.

Re-derive prompt, for the spaced pass a week later, from a blank page: (1) show why the ratio of two sides of a right triangle depends on the angle alone; (2) starting from the unit circle, get cos²θ + sin²θ = 1 from Pythagoras; (3) a robot at heading 220° driving at 1.5 m/s: find both components and check them.

## Conventions the author must follow

- Display math in `$$…$$`, inline symbols as Unicode in prose (θ, ², √, −). Never author `\(…\)` or `\[…\]`; kramdown strips the backslashes. Never leave an unpaired `$`. Subscripts outside math delimiters use brackets.
- Inside `aligned` blocks, separate rows with `\cr`, never `\\`: kramdown eats one backslash, so `\\[4pt]` reaches KaTeX as `\[4pt]` and the rows silently merge.
- No `{{` or `{%` anywhere; Jekyll's Liquid would break the build.
- Headings: `##` for the numbered sections, `###` inside them.
- A "Math!" callout is a blockquote whose first line is `> ### Math!`.
- Links: relative. The demo is `demo.html`. Lesson 2 is `../02_vectors/`.
- End the page with the same prev/next footer pattern the site uses: a flex `<div>` with a link back to `../` labeled "Lessons" in the middle, nothing on the left for Lesson 1, and "Lesson 2: Vectors →" on the right pointing at `../02_vectors/`.

## Demo spec (`demo.html`)

Self-contained; no CDN, no external libraries. In `<head>`: `<script src="../../assets/theme.js"></script>` then `<link rel="stylesheet" href="../../assets/axon.css">`. `<html lang="en" data-theme="dark">`.

Layout, top to bottom: a `.canvas-container` with `position: relative; overflow: hidden; height: 400px` holding an absolutely positioned canvas that fills it (`inset: 0; width: 100%; height: 100%; touch-action: none`). The canvas must never size its own container. Then a controls row, then a telemetry row. Use `var(--panel)`, `var(--line)`, `var(--ink)`, `var(--muted)`, `var(--accent)`, `var(--accent-green)`, `var(--accent-amber)`, `var(--accent-purple)` for colors; read them with `getComputedStyle(document.documentElement)` at paint time so the canvas follows the theme. Repaint on the `axon-theme-changed` window event, on resize (`ResizeObserver` on the container, device-pixel-ratio aware), and on every input change.

Scene: the floor from above. Origin (the robot's start) at about 30% of the width from the left and vertically centered. Down-field is +x to the right, +y is up on screen (left of the robot). Scale chosen so 5 m/s fits; a faint 1 m grid with the down-field axis slightly stronger. Draw:
- the robot at the origin as a rounded square rotated to the heading with a tick at its front;
- the velocity arrow (amber) of length speed × scale at the heading;
- the down-field leg (blue, dashed) from the origin along x, and the sideways leg (green, dashed) from the tip of the down-field leg up to the arrow tip, with a right-angle marker;
- the angle arc (purple) from the +x axis to the heading with the degrees label;
- a ghost robot, semi-transparent, at (v cos θ · t, v sin θ · t) with a faint straight line from the origin to it, labeled with the elapsed time;
- optional, behind a checkbox "Show unit circle": a circle of radius 1 m/s around the origin and the point (cos θ, sin θ) on it, so the reader sees the hypotenuse-1 triangle inside the real one.

Controls: a heading slider from −180 to 360 in steps of 1, default 30; a speed slider 0 to 5 m/s step 0.1, default 2.0; a time slider 0 to 2.0 s step 0.1, default 1.0; the unit-circle checkbox; a "Reset" button restoring 30°, 2.0 m/s, 1.0 s. Dragging on the canvas (pointer events, mouse and touch) sets the heading from the drag point relative to the origin; the slider follows.

Telemetry, monospace, each with a small uppercase label: heading in degrees (one decimal), heading in radians (four decimals), quadrant (I to IV, or "axis" when on one), cos θ, sin θ, tan θ (four decimals; show "undefined" within 0.05° of ±90°), sin²θ + cos²θ (six decimals, should read 1.000000), down-field speed and sideways speed (three decimals, m/s), position after t seconds as (x, y) in meters, and distance from the start (three decimals), which must equal speed × time.

Defaults must reproduce the lesson's numbers exactly: 30.0°, 0.5236 rad, cos 0.8660, sin 0.5000, tan 0.5774, down-field 1.732 m/s, sideways 1.000 m/s, position (1.732, 1.000) m, distance 2.000 m.

Before finishing, extract the inline script to a temporary file and run `node --check` on it, and confirm the page has no reference to any external host.
