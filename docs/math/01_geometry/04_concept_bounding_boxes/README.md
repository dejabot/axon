# Concept 04: Bounding Boxes, Overlap & Collision

> **▶ Interactive Demo: [Collision & IoU Sandbox](demo.html)**
>
> Drag the robot and the obstacle. Watch the per-axis interval tests pass and fail independently, see the overlap rectangle appear, and read the Intersection-over-Union score update live.

<iframe src="demo.html" width="100%" height="580" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Robot Is Not a Dot

Concept 01 treated the robot as a point at `(x, y)`, and Concept 02 treated its path as an infinitely thin line. Neither is true. A competition robot is a box roughly 0.9 metres on a side once its bumpers are on, and those bumpers are what actually make contact with the world.

This changes the question. A path planner that only checks whether the robot's *centre* clears an obstacle will happily drive 45 centimetres of bumper straight through a field element. What we need is a test between two regions of space, not two points — and we need it to be cheap, because it will run against every obstacle on the field, fifty times a second, for the entire match.

<div style="text-align: center; margin: 20px 0;">
  <svg width="380" height="190" viewBox="0 0 380 190" style="max-width: 100%; height: auto;" role="img" aria-label="A robot bounding box approaching an obstacle bounding box, with their X and Y intervals projected onto the axes.">
    <rect x="55" y="55" width="85" height="85" fill="rgba(56,189,248,0.16)" stroke="#38bdf8" stroke-width="2" rx="4" />
    <text x="76" y="103" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">robot</text>
    <rect x="185" y="35" width="105" height="90" fill="rgba(244,63,94,0.16)" stroke="#f43f5e" stroke-width="2" rx="4" />
    <text x="205" y="85" fill="#f43f5e" font-family="sans-serif" font-size="12" font-weight="bold">obstacle</text>
    <line x1="55" y1="165" x2="140" y2="165" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" />
    <line x1="185" y1="165" x2="290" y2="165" stroke="#f43f5e" stroke-width="4" stroke-linecap="round" />
    <text x="120" y="182" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">gap on X — separated</text>
    <line x1="25" y1="55" x2="25" y2="140" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" />
    <line x1="12" y1="35" x2="12" y2="125" stroke="#f43f5e" stroke-width="4" stroke-linecap="round" />
    <text x="300" y="150" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">Y intervals</text>
    <text x="300" y="164" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">do overlap</text>
  </svg>
</div>

The picture above already contains the answer, and the rest of this concept is about seeing why. Look at the two shadows cast onto the X-axis: they do not touch. That single observation is enough to declare the boxes disjoint, no matter what happens on Y.

---

## 2. Building the Math

### Step 1: Collapse the problem to one dimension

Before doing anything in 2D, solve the easy case. Two intervals on a number line, `[a₁, a₂]` and `[b₁, b₂]`. When do they overlap?

Trying to characterize overlap directly is fiddly — there are several arrangements to enumerate, one interval inside the other, partial overlap from the left, from the right. The trick is to describe the **opposite** condition, because separation has only two arrangements:

$$
\begin{aligned}
\text{they are separated} \iff\ & a_2 < b_1 \quad \text{(A finishes before B starts)} \\
\text{or}\ & b_2 < a_1 \quad \text{(B finishes before A starts)}
\end{aligned}
$$

Overlap is simply "not separated". Negating an *or* turns it into an *and*, and negating each comparison flips it:

$$
\text{they overlap} \iff a_2 \geq b_1 \quad \text{and} \quad b_2 \geq a_1
$$

Two comparisons. That is the whole 1D test, and every arrangement is covered without enumerating any of them.

> ### Math!
> Turning "not (P or Q)" into "(not P) and (not Q)" is **De Morgan's law**, and it is one of the most useful moves in all of applied logic. Its partner runs the other way: "not (P and Q)" becomes "(not P) or (not Q)". Read the symbol `¬` as "not". Whenever a condition is awkward to state directly, try stating its negation and applying De Morgan — collision detection, error handling and database queries are all full of conditions that are far clearer inside-out.

### Step 2: Lift it to two dimensions

An **axis-aligned bounding box**, or AABB, is a rectangle whose sides run parallel to the coordinate axes. That restriction is what makes it cheap, and it means the box is completely described by two intervals: an X-interval `[minX, maxX]` and a Y-interval `[minY, maxY]`. A point is inside the box exactly when its x lies in the first interval *and* its y lies in the second.

So when do two boxes share at least one point? Such a shared point would need an x in both X-intervals and a y in both Y-intervals. Conversely, if the X-intervals share some value and the Y-intervals share some value, you can pair them up to construct a point lying in both boxes. The two directions together give:

$$
\text{boxes overlap} \iff \text{X-intervals overlap} \quad \text{and} \quad \text{Y-intervals overlap}
$$

Written out, four comparisons:

```
   A.maxX ≥ B.minX   and   A.minX ≤ B.maxX
   A.maxY ≥ B.minY   and   A.minY ≤ B.maxY
```

Note the shape of this result: to prove the boxes are **disjoint** you only need to find **one** axis where the shadows fail to meet. Finding a single such axis is enough; you can stop early and skip the rest of the test. That idea — project both shapes onto a candidate axis and look for a gap — is the **separating axis theorem**, and for axis-aligned boxes the only two candidate axes are X and Y. For rotated shapes there are more axes to try, which is why rotated collision is more expensive, and which is why it waits until you have rotation matrices in hand.

### Step 3: Build the robot's box from its pose

Robot poses are given as a centre. Bumper dimensions are given as a total width and length. Converting between them uses **half-extents** — half the width and half the length:

$$
\begin{aligned}
\text{hx} &= \frac{\text{width}}{2} \\
\text{hy} &= \frac{\text{length}}{2} \\[6pt]
\text{minX} &= \text{cx} - \text{hx} & \qquad \text{maxX} &= \text{cx} + \text{hx} \\
\text{minY} &= \text{cy} - \text{hy} & \qquad \text{maxY} &= \text{cy} + \text{hy}
\end{aligned}
$$

A 0.9 by 0.9 metre robot centred at `(3.0, 2.0)` therefore occupies `x ∈ [2.55, 3.45]` and `y ∈ [1.55, 2.45]`. Its centre being 0.5 metres from a wall means its bumper is only 0.05 metres from that wall, which is the entire reason this concept exists.

### Step 4: Inflate the obstacle instead of growing the robot

Here is a reframing that pays for itself many times over. Rather than testing box-against-box, **grow the obstacle by the robot's half-extents and test the robot's centre point against the grown obstacle.**

Why is that the same test? The boxes touch exactly when the gap between their centres has closed to `hx_A + hx_B` on X and `hy_A + hy_B` on Y. Moving those two amounts from the robot onto the obstacle changes neither total, so the moment of contact is identical. The robot has become a point, and the obstacle has absorbed its size:

```
   inflated.minX = obstacle.minX − hx_robot        inflated.maxX = obstacle.maxX + hx_robot
   inflated.minY = obstacle.minY − hy_robot        inflated.maxY = obstacle.maxY + hy_robot
```

<div style="text-align: center; margin: 20px 0;">
  <svg width="330" height="180" viewBox="0 0 330 180" style="max-width: 100%; height: auto;" role="img" aria-label="An obstacle box surrounded by a larger dashed inflated box, with the robot reduced to a single point.">
    <rect x="95" y="45" width="90" height="80" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="6,4" rx="4" />
    <rect x="125" y="70" width="60" height="55" fill="rgba(244,63,94,0.18)" stroke="#f43f5e" stroke-width="2" rx="3" />
    <text x="132" y="103" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">obstacle</text>
    <text x="196" y="42" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">inflated by robot half-extents</text>
    <circle cx="70" cy="140" r="5" fill="#38bdf8" />
    <text x="20" y="162" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">robot centre (a point)</text>
  </svg>
</div>

This is the two-dimensional case of a **Minkowski sum**, and it is how serious path planners think. Once every obstacle has been inflated once, at the start of planning, the robot is a dimensionless point for the rest of the search — so line-of-sight checks between waypoints become the segment tests from Concept 02, run against inflated rectangles, with no robot geometry to carry around. The space you are planning in stops being the physical field and becomes **configuration space**.

Inflation is also where the safety margin belongs. Add a few extra centimetres beyond the true half-extents and every downstream query inherits the buffer automatically, instead of each call site remembering to apply its own.

### Step 5: How much are they overlapping?

A boolean is a poor output. "Blocked" gives a planner nothing to work with, while "overlapping by 3 centimetres on Y" tells it which way to nudge.

The overlap region of two AABBs is itself an AABB, and its bounds come from taking the *inner* edges on each side:

```
   overlap.minX = max(A.minX, B.minX)        overlap.maxX = min(A.maxX, B.maxX)
   overlap.minY = max(A.minY, B.minY)        overlap.maxY = min(A.maxY, B.maxY)
```

Take a moment with the `max` of the mins: the overlap starts wherever the later of the two boxes starts. Symmetrically it ends at the earlier of the two ends. If the boxes are disjoint this computation produces a rectangle with a negative width or height, which is the same information the Step 2 test gives, arriving as a number instead of a boolean.

The overlap widths on each axis are the **penetration depths**. The smaller of the two is the cheapest direction to escape, which is exactly what a physics engine uses to push two intersecting objects apart.

### Step 6: Intersection over Union

Sometimes the question is not "do these overlap" but "how well do these two boxes agree". The standard score is **Intersection over Union**:

$$
\text{IoU} = \frac{\text{area(intersection)}}{\text{area(union)}}
$$

The intersection area comes straight from Step 5, clamping negatives to zero:

```
   interArea = max(0, overlap.maxX − overlap.minX) · max(0, overlap.maxY − overlap.minY)
```

The union needs one moment of care. Adding the two areas double-counts the shared region, so subtract it back off exactly once:

$$
\text{unionArea} = \text{areaA} + \text{areaB} - \text{interArea}
$$

IoU runs from 0 for boxes that do not touch, to 1 for boxes that coincide exactly. Work a case through. Box A spans `x ∈ [1, 3]`, `y ∈ [1, 3]`, so `areaA = 4`. Box B spans `x ∈ [2, 5]`, `y ∈ [2, 4]`, so `areaB = 6`. The overlap is `x ∈ [max(1,2), min(3,5)] = [2, 3]` and `y ∈ [max(1,2), min(3,4)] = [2, 3]`, an area of `1 · 1 = 1`. Then `unionArea = 4 + 6 − 1 = 9`, and `IoU = 1/9 ≈ 0.111` — a poor match, as the numbers should say for boxes sharing only a corner.

### Step 7: The gap between two frames

Collision tests run at discrete instants, typically once every 20 milliseconds. In between, the robot teleports.

At 4 metres per second, a 20 millisecond tick moves the robot 8 centimetres. Test the box at the start of the tick and again at the end, and you have said nothing about the 8 centimetres in between. If an obstacle is thinner than the step — a bar, a wall edge, another robot's bumper caught at a glancing angle — both tests can report "clear" while the robot passes straight through. This is **tunneling**, and it gets worse exactly when it matters most, at high speed.

The cheap and conservative fix is a **swept bounding box**: build one AABB enclosing both the start pose and the end pose, and test that.

```
   swept.minX = min(start.minX, end.minX)        swept.maxX = max(start.maxX, end.maxX)
   swept.minY = min(start.minY, end.minY)        swept.maxY = max(start.maxY, end.maxY)
```

The swept box can never miss a collision the true motion would have had, because it contains the entire motion. It can report collisions that would not really happen — a diagonal move produces a swept box covering corners the robot never visits — so it is conservative in the safe direction. For a robot, refusing a path that was marginally passable is a far better failure than driving through a wall.

### What AABBs cannot do

An axis-aligned box around a robot turned 45 degrees is about 40 percent larger in area than the robot itself, and all of that excess is phantom obstacle. The box says "blocked" for gaps the robot would fit through diagonally.

The fix is an **oriented bounding box**, which rotates with the robot, and testing those requires projecting both shapes onto four candidate axes rather than two. That needs the rotation machinery from the trigonometry module, so it waits until then. The practical pattern in real code is to use both: an AABB test first as a cheap rejection filter, and the exact oriented test only for the few candidates that survive it.

---

## 3. Solving It in Code (Java & WPILib)

### First-Principles Java

```java
/** An axis-aligned bounding box, stored as the two intervals it is made of. */
public record Box(double minX, double minY, double maxX, double maxY) {

    /** Build a box from a robot centre and its full bumper dimensions. */
    public static Box fromCenter(double cx, double cy, double width, double length) {
        return new Box(cx - width / 2, cy - length / 2,
                       cx + width / 2, cy + length / 2);
    }

    /** Overlap on BOTH axes. One separating axis is enough to prove disjoint. */
    public boolean overlaps(Box other) {
        if (maxX < other.minX || other.maxX < minX) return false;   // separated on X
        if (maxY < other.minY || other.maxY < minY) return false;   // separated on Y
        return true;
    }

    /** Grow by the robot's half-extents plus a safety margin (Minkowski inflation). */
    public Box inflate(double hx, double hy, double margin) {
        return new Box(minX - hx - margin, minY - hy - margin,
                       maxX + hx + margin, maxY + hy + margin);
    }

    public boolean contains(double px, double py) {
        return px >= minX && px <= maxX && py >= minY && py <= maxY;
    }

    public double area() {
        return Math.max(0, maxX - minX) * Math.max(0, maxY - minY);
    }

    /** Overlap rectangle. Returns zero area when the boxes are disjoint. */
    public Box intersection(Box other) {
        return new Box(Math.max(minX, other.minX), Math.max(minY, other.minY),
                       Math.min(maxX, other.maxX), Math.min(maxY, other.maxY));
    }

    public double iou(Box other) {
        double inter = intersection(other).area();
        double union = area() + other.area() - inter;
        return union <= 0 ? 0.0 : inter / union;
    }

    /** Conservative swept box covering the whole move from this pose to the next. */
    public Box sweptTo(Box end) {
        return new Box(Math.min(minX, end.minX), Math.min(minY, end.minY),
                       Math.max(maxX, end.maxX), Math.max(maxY, end.maxY));
    }
}
```

```java
Box robotNow  = Box.fromCenter(3.00, 2.00, 0.9, 0.9);
Box robotNext = Box.fromCenter(3.08, 2.00, 0.9, 0.9);   // 20 ms later at 4 m/s
Box barrier   = new Box(3.40, 1.00, 3.60, 3.00);        // a thin 20 cm bar

System.out.println(robotNow.overlaps(barrier));              // false
System.out.println(robotNext.overlaps(barrier));             // false
System.out.println(robotNow.sweptTo(robotNext).overlaps(barrier));   // true

// Planning against a point robot: inflate once, then query centres forever.
Box inflated = barrier.inflate(0.45, 0.45, 0.10);
System.out.println(inflated.contains(3.08, 2.00));           // true
```

Note what the first two lines print. Both instantaneous tests say the path is clear; only the swept test catches the bar. That is tunneling reproduced in eight lines.

### Production WPILib Equivalent

Recent WPILib releases ship geometry primitives — `Translation2d` for points and `Rectangle2d` for axis-aligned regions, with containment and intersection helpers — and using them is preferable to hand-rolled doubles because the types stop you from transposing an X and a Y. Check the version your project targets before depending on any specific class, since this area of the library has grown recently.

What no library will decide for you is the policy: how much margin to inflate by, whether a grazing touch counts, and whether your loop tests instantaneous poses or swept ones. Those are the choices that determine whether the robot works, and they belong in your own well-named, unit-tested utility class.

---

## 4. Bridge to Machine Learning & Modern Autonomy

Intersection over Union is not a robotics side-note that happens to resemble a machine learning idea. It is *the* metric of object detection, and Step 6 is the whole of it.

A detector such as YOLO or a Faster R-CNN outputs boxes with confidence scores. Evaluating it means matching predicted boxes against human-labelled ground-truth boxes, and the match rule is IoU against a threshold — a prediction with IoU ≥ 0.5 against a ground-truth box counts as a hit, anything less counts as a miss plus a false alarm. Sweeping that threshold from 0.5 to 0.95 and averaging produces **mean Average Precision**, the number reported in essentially every detection paper.

The same arithmetic runs inside the model, twice more. **Non-maximum suppression** cleans up the dozens of overlapping boxes a detector fires at a single object: sort by confidence, keep the best, and delete every remaining box whose IoU with it exceeds a threshold — Step 6 executed thousands of times per frame. And during training, IoU-based losses such as GIoU and DIoU supply the gradient that pulls predicted boxes onto their targets, chosen over naive corner-coordinate error precisely because IoU is invariant to the scale of the object.

For an FRC team the loop closes tightly: a vision coprocessor detects a game piece and reports a pixel-space bounding box, non-maximum suppression having already used this arithmetic to pick one box per piece. Your code converts that box to a field position, and then the collision arithmetic from this same concept decides whether the robot can reach it. Same four comparisons, two very different jobs.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1
Robot box A spans `x ∈ [1.0, 2.0]`, `y ∈ [1.0, 2.0]`. Obstacle B spans `x ∈ [2.5, 3.5]`, `y ∈ [1.0, 2.0]`. Do they collide? Then compute their IoU.

**Solution:**
1. Y-intervals: `A.maxY (2.0) ≥ B.minY (1.0)` ✓ and `B.maxY (2.0) ≥ A.minY (1.0)` ✓ — they overlap on Y.
2. X-intervals: `A.maxX (2.0) ≥ B.minX (2.5)`? No — 2.0 < 2.5. The test fails, so X is a **separating axis** and the boxes are disjoint. A 0.5 metre gap remains.
3. IoU: the intersection rectangle would be `x ∈ [2.5, 2.0]`, a negative width, clamped to zero area. With `interArea = 0`, `IoU = 0 / (1 + 1 − 0) = 0`.
Overlap on one axis is never enough — that is exactly what the second half of the test is for.

---

### Checkpoint 2
Your 0.9 by 0.9 metre robot must pass through a gap between two field elements. The gap runs from `x = 4.00` to `x = 5.30`. Using inflation, decide whether the robot's centre has any legal x-values, and say how much lateral tolerance the driver has.

**Solution:**
1. The robot's half-extent is `hx = 0.45`.
2. Inflate each side of the gap inward by `0.45`. The legal band for the robot's *centre* is `x ∈ [4.00 + 0.45, 5.30 − 0.45] = [4.45, 4.85]`.
3. The band is non-empty and 0.40 metres wide, so the robot fits with 20 centimetres of slack either side of the gap's centre line at `x = 4.65`.
4. With a 0.10 metre safety margin the band shrinks to `[4.55, 4.75]`, still 0.20 metres wide. Had the gap been 0.9 metres exactly, the band would have collapsed to a single point — geometrically a fit, practically an impossibility.

---

### Deep Dive 1
Step 7's swept box is conservative: it reports collisions that the true motion would avoid. Quantify the cost. For a robot moving diagonally across a field at 4 m/s, compute the swept box area over one 20 ms tick and compare it to the area the robot actually sweeps. Then investigate **conservative advancement** and **speculative contacts** as alternatives, and work out at what speed the swept box becomes too pessimistic to plan with.

### Deep Dive 2
This concept closed by noting that an AABB around a robot rotated 45 degrees overstates its footprint. Compute exactly how much: for a square of side `s` rotated by 45 degrees, work out the side length of the smallest axis-aligned box containing it, and express the wasted area as a percentage. Then sketch how the separating-axis idea from Step 2 generalizes to rotated boxes — how many candidate axes are needed, and where do they come from? Return to this after the trigonometry module supplies rotation matrices.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../03_concept_linear_interpolation/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 03: Linear Interpolation</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="../05_concept_polygons_zones/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 05: Polygons & Zones →</a></div>
</div>
