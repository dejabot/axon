# Concept 01: Coordinates, Poses & Pythagorean Distance

> **▶ Interactive Demo: [2D Field Distance Visualizer](demo.html)**
>
> Drag the robot and the target anywhere on the field. Watch the right triangle redraw itself and every distance measure update live.

<iframe src="demo.html" width="100%" height="520" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Where Is the Robot?

Stand at the corner of an FRC playing field and look down its length. The field is a rectangle roughly 16.54 meters long and 8.21 meters wide. To let software talk about locations on that rectangle, we nail down three arbitrary but permanent choices:

* One corner of the carpet is declared the **origin**, the point named `(0, 0)`.
* The long direction away from that corner is the **X-axis**, increasing to 16.54.
* The short direction is the **Y-axis**, increasing to 8.21.

Nothing about the field forces those choices. They are a convention, and the only thing that matters is that every subsystem on the robot agrees on the same one. The moment your odometry believes the origin is in the blue-alliance corner and your vision code believes it is in the red-alliance corner, every number the two exchange is wrong by the length of the field.

<div style="text-align: center; margin: 20px 0;">
  <svg width="360" height="200" viewBox="0 0 360 200" style="max-width: 100%; height: auto;" role="img" aria-label="A field rectangle with an origin at the lower left, a robot, a target, and the right triangle connecting them.">
    <rect x="30" y="20" width="300" height="150" fill="none" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" rx="4" />
    <line x1="30" y1="170" x2="335" y2="170" stroke="currentColor" stroke-opacity="0.55" stroke-width="2" />
    <line x1="30" y1="170" x2="30" y2="15" stroke="currentColor" stroke-opacity="0.55" stroke-width="2" />
    <text x="300" y="188" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">X (16.54 m)</text>
    <text x="36" y="16" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="11">Y (8.21 m)</text>
    <circle cx="30" cy="170" r="4" fill="#38bdf8" />
    <text x="38" y="164" fill="#38bdf8" font-family="sans-serif" font-size="11">(0, 0)</text>
    <line x1="85" y1="134" x2="248" y2="134" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5,4" />
    <line x1="248" y1="134" x2="248" y2="61" stroke="#4ade80" stroke-width="2" stroke-dasharray="5,4" />
    <line x1="85" y1="134" x2="248" y2="61" stroke="#fbbf24" stroke-width="3" />
    <text x="150" y="150" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="12">Δx = 9.0</text>
    <text x="254" y="102" fill="#4ade80" font-family="sans-serif" font-weight="bold" font-size="12">Δy = 4.0</text>
    <text x="132" y="88" fill="#fbbf24" font-family="sans-serif" font-weight="bold" font-size="12">d = ?</text>
    <rect x="73" y="122" width="24" height="24" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" rx="3" />
    <text x="52" y="164" fill="#38bdf8" font-family="sans-serif" font-weight="bold" font-size="11">Robot (3, 2)</text>
    <circle cx="248" cy="61" r="7" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" />
    <text x="230" y="48" fill="#f43f5e" font-family="sans-serif" font-weight="bold" font-size="11">Target (12, 6)</text>
  </svg>
</div>

With the convention fixed, put the robot at `(3.0, 2.0)` and a scoring target at `(12.0, 6.0)`. Two of the three questions a shooter needs are easy:

1. How far East must the game piece travel? `Δx = 12.0 − 3.0 = 9.0` meters.
2. How far North must it travel? `Δy = 6.0 − 2.0 = 4.0` meters.
3. How far is the target **in a straight line**? That one is not subtraction, and answering it properly is the rest of this concept.

---

## 2. Building the Math: From a Number Line to a Distance Formula

### Step 1: Distance in one dimension

Forget the field for a second and think about an elevator carriage on a vertical rail. Its state is a single number: height in meters. If it sits at `h₁ = 0.4` and you command it to `h₂ = 1.1`, the travel distance is `1.1 − 0.4 = 0.7` meters.

But if you command it back down, the subtraction gives `0.4 − 1.1 = −0.7`. The carriage did not travel negative seven-tenths of a meter; it travelled seven-tenths of a meter downward. Distance is a length, and lengths are never negative. So in one dimension:

```
   distance = |h₂ − h₁|
```

The bars mean **absolute value**: throw away the sign, keep the size. This distinction between a *displacement* (signed, carries direction) and a *distance* (unsigned, just magnitude) is going to reappear in every axon of this curriculum.

> ### Math!
> `|x|` is read out loud as **"the absolute value of x"**, or informally "the size of x". It is defined piecewise: `|x| = x` when `x ≥ 0`, and `|x| = −x` when `x < 0`. The second branch surprises people — negating a negative number produces a positive one, which is exactly the point.

### Step 2: Why the diagonal is not just addition

Back on the field. A tempting first guess is that the straight-line distance is `Δx + Δy = 9.0 + 4.0 = 13.0` meters. That is the distance a robot would travel if it drove East to the target's column and *then* North to the target's row — an L-shaped path. But a game piece flying through the air, or a swerve drive moving diagonally, cuts the corner. The straight line must be shorter than 13.0. How much shorter?

The three segments — the horizontal run, the vertical run, and the diagonal — form a **right triangle**: a triangle in which two sides meet at 90 degrees. The two sides that meet at the right angle are the **legs** (here `Δx` and `Δy`), and the side opposite the right angle is the **hypotenuse** (here `d`). The relationship we need is the Pythagorean theorem, and we are going to prove it rather than assert it.

### Step 3: Proving the Pythagorean theorem

Take a square whose side length is `a + b`, where `a` and `b` are the two leg lengths. Its total area is `(a + b)²`.

Now place four copies of our right triangle inside it, one tucked into each corner, each rotated a quarter turn from the last. The four hypotenuses turn out to enclose a tilted square in the middle, whose side length is `c`.

<div style="text-align: center; margin: 20px 0;">
  <svg width="240" height="240" viewBox="0 0 220 220" style="max-width: 100%; height: auto;" role="img" aria-label="A large square of side a plus b containing four right triangles around a tilted inner square of side c.">
    <rect x="20" y="20" width="160" height="160" fill="none" stroke="currentColor" stroke-opacity="0.5" stroke-width="2" />
    <polygon points="80,20 180,80 120,180 20,120" fill="rgba(251, 191, 36, 0.18)" stroke="#fbbf24" stroke-width="2" />
    <polygon points="20,20 80,20 20,120" fill="rgba(56, 189, 248, 0.22)" stroke="#38bdf8" stroke-width="1.5" />
    <polygon points="180,20 80,20 180,80" fill="rgba(56, 189, 248, 0.22)" stroke="#38bdf8" stroke-width="1.5" />
    <polygon points="180,180 180,80 120,180" fill="rgba(56, 189, 248, 0.22)" stroke="#38bdf8" stroke-width="1.5" />
    <polygon points="20,180 120,180 20,120" fill="rgba(56, 189, 248, 0.22)" stroke="#38bdf8" stroke-width="1.5" />
    <text x="45" y="15" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">a</text>
    <text x="125" y="15" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">b</text>
    <text x="188" y="55" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">a</text>
    <text x="188" y="135" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">b</text>
    <text x="95" y="105" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">c²</text>
    <text x="118" y="45" fill="currentColor" fill-opacity="0.65" font-family="sans-serif" font-size="11">c</text>
  </svg>
</div>

Now count the same area two different ways.

* **Counting from the outside:** the big square has area `(a + b)²`. Expanding that product gives `a² + 2ab + b²`.
* **Counting from the inside:** the big square is exactly four triangles plus the tilted square. Each triangle has area `½ab`, so four of them contribute `4 · ½ab = 2ab`. The tilted square contributes `c²`. Total: `2ab + c²`.

Both counts describe the identical region, so they must be equal:

```
   a² + 2ab + b²  =  2ab + c²
```

Subtract `2ab` from both sides, and the cross terms vanish:

```
   a² + b² = c²
```

That is the Pythagorean theorem, and nothing went into it except "area is area". No black box.

### Step 4: The distance formula

Our triangle's legs are `Δx` and `Δy`, and its hypotenuse is the distance `d` we want. Substituting into `a² + b² = c²`:

```
   d² = (Δx)² + (Δy)²
   d  = √( (x₂ − x₁)² + (y₂ − y₁)² )
```

Notice that the squaring quietly solved the sign problem from Step 1 for us. `(−9.0)²` and `(9.0)²` are both 81, so it no longer matters which point you call "first". We never need absolute value bars here — squaring already discards the sign.

For our robot and target: `d = √(9.0² + 4.0²) = √(81 + 16) = √97 ≈ 9.85` meters. Compare that to the L-shaped path's 13.0 meters. Cutting the corner saves over three meters, which in a 15-second autonomous period is the difference between scoring and not.

> ### Math!
> Written formally, a point is a **vector** and the distance between two of them is the length of their difference:
>
> ```
>    d(p, q) = ‖p − q‖₂ = √( Σᵢ (pᵢ − qᵢ)² )
> ```
>
> Read this out loud as **"the distance from p to q equals the norm of p minus q, which is the square root of the sum over i of p-sub-i minus q-sub-i, squared."** The double bars `‖ ‖` mean **norm**, the general word for "length of a vector". The subscript `₂` marks it as the **L2 norm**, because everything inside is raised to the power 2. The capital sigma `Σ` means **sum**, and the `i` underneath is a counter that walks through the coordinates — `i = 1` for x, `i = 2` for y, and onward for as many dimensions as you have. Written this way, the formula does not care whether you hand it 2 coordinates or 2,048.

### Step 5: Squared distance, and why you should usually stop early

Suppose autonomous code must pick the nearest of six game pieces. The obvious loop computes six square roots and keeps the smallest. But square roots are comparatively expensive, and here they are pure waste.

The reason is that squaring is **monotonic** for non-negative numbers: if `d₁ < d₂` then `d₁² < d₂²`, and vice versa. Taking the square root never reorders the list. So you can compare `d²` values directly and skip the square root entirely, calling it once at the very end if you actually need a distance in meters rather than a ranking.

The same trick appears whenever you compare a distance to a fixed threshold. Instead of `if (distance(a, b) < 0.5)`, write `if (squaredDistance(a, b) < 0.25)`. Square the threshold once at compile time instead of taking a square root every loop iteration, 50 times a second.

### Step 6: Position is not enough — the pose

Knowing the robot is at `(3.0, 2.0)` still leaves a question unanswered: which way is it pointing? A robot at the perfect scoring position with its shooter aimed at its own driver station scores nothing.

So we track a third number, the **heading** `θ`, measured counter-clockwise from the positive X-axis. Bundle all three together and you have a **pose**:

```
   pose = (x, y, θ)
```

Two numbers of position plus one of orientation gives a planar robot three **degrees of freedom** — three independent quantities you can change. Every odometry system, every path follower, and every auto-alignment routine in this curriculum tracks the robot's state as exactly this triple.

> ### Math!
> The set of all `(x, y, θ)` poses has a formal name: **SE(2)**, the special Euclidean group in 2 dimensions, read "S-E-two". "Euclidean" because it preserves distances, "special" because it excludes mirror reflections — a robot cannot turn into its own mirror image. Its 3D cousin `SE(3)` carries three position numbers and three rotation numbers, and shows up when the trig axon reaches quaternions.

---

## 3. Solving It in Code (Java & WPILib)

### First-Principles Java

```java
// Field positions in meters, using the same origin convention everywhere.
double robotX  =  3.0, robotY = 2.0;
double targetX = 12.0, targetY = 6.0;

// Signed displacements: these carry direction.
double dx = targetX - robotX;   // 12.0 - 3.0 = +9.0 m (East)
double dy = targetY - robotY;   //  6.0 - 2.0 = +4.0 m (North)

// Unsigned distance: the hypotenuse. Squaring erased the signs for us.
double distance = Math.hypot(dx, dy);   // 9.85 m

// Ranking without square roots: compare squared distances instead.
double squaredDistance = dx * dx + dy * dy;   // 97.0
boolean withinRange = squaredDistance < 10.0 * 10.0;   // no sqrt needed

System.out.printf("Distance %.2f m, in range: %b%n", distance, withinRange);
```

Prefer `Math.hypot(dx, dy)` over `Math.sqrt(dx * dx + dy * dy)` when you need the actual distance. It computes the same value but rescales internally so that squaring a very large or very tiny coordinate cannot overflow or underflow the intermediate result.

### Production WPILib Equivalent

```java
import edu.wpi.first.math.geometry.Pose2d;
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.math.geometry.Translation2d;

Translation2d robot  = new Translation2d(3.0, 2.0);
Translation2d target = new Translation2d(12.0, 6.0);

double distance = robot.getDistance(target);   // 9.85 m
double norm     = robot.getNorm();             // distance from the origin

// A full pose bundles position and heading together.
Pose2d robotPose = new Pose2d(3.0, 2.0, Rotation2d.fromDegrees(45.0));
Translation2d midpoint = robot.plus(target).div(2.0);   // (7.5, 4.0)
```

`Translation2d` is a position or a displacement; `Pose2d` adds the heading. Keeping them as distinct types is deliberate — it makes the compiler reject the common mistake of handing a bare position to something that needs an orientation too.

---

## 4. Bridge to Machine Learning & Modern Autonomy

The distance formula you just derived is the workhorse of machine learning, where it measures similarity rather than meters.

A neural network represents an image, a word, or a sentence as an **embedding**: a list of numbers, often 768 or 1,536 of them, that is a point in a very high-dimensional space. The formula generalizes without modification — the `Σᵢ` in the Math! sidebar simply runs over more coordinates. Two photographs of the same game piece land close together in that space; a photograph of a game piece and one of a referee land far apart. **k-nearest-neighbours** classification does nothing more than compute these distances and take a vote among the closest `k` points.

The squared-distance trick from Step 5 matters enormously at that scale: vector databases serving billions of embeddings rank by squared distance precisely because the ordering is identical and the square root is wasted work, exactly as it was for the six game pieces.

Mean squared error, the loss function that trains a huge fraction of all regression models, is literally the squared L2 distance between what the network predicted and what was true, averaged over the training examples. When the machine learning axon derives gradient descent, the surface it descends is built from this formula.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1
Your robot sits at `(1.0, 1.0)`. An AprilTag on the field wall is at `(4.0, 5.0)`. Find the straight-line distance, and also find the midpoint you would use as a staging waypoint.

**Solution:**
1. `Δx = 4.0 − 1.0 = 3.0` and `Δy = 5.0 − 1.0 = 4.0`.
2. `d = √(3.0² + 4.0²) = √(9 + 16) = √25 = 5.0` meters. This is the 3-4-5 triangle, the smallest right triangle with whole-number sides.
3. The midpoint averages each coordinate independently: `((1.0 + 4.0)/2, (1.0 + 5.0)/2) = (2.5, 3.0)`.

---

### Checkpoint 2
An autonomous routine must reject any game piece farther than 3.0 meters away. A teammate writes `if (Math.sqrt(dx * dx + dy * dy) > 3.0) skip();` inside a loop that runs 50 times per second over 12 candidate pieces. Rewrite it to give identical results with no square roots, and explain why the results are identical.

**Solution:**
```java
if (dx * dx + dy * dy > 9.0) skip();   // 3.0 squared, computed once
```
Squaring is monotonic on non-negative numbers, so `d > 3.0` is true in exactly the cases where `d² > 9.0` is true. The comparison never changes its answer, and 600 square roots per second disappear. The one thing you must not do is forget to square the threshold — comparing `d²` against an unsquared `3.0` would silently reject everything beyond 1.73 meters.

---

### Deep Dive 1
The field origin convention is arbitrary, but FRC alliances are mirror images. Investigate how WPILib's `AllianceFlipUtil`-style helpers convert a blue-alliance path into a red-alliance path. Does mirroring change the *distance* between two points? Does it change the *heading* `θ`? Work out what happens to the pose `(3.0, 2.0, 30°)` under both a horizontal mirror and a 180-degree rotation of the field, and explain why modern game manuals prefer the rotational convention.

### Deep Dive 2
This concept treated the field as flat. A charge station ramp is not. Extend the distance formula to three dimensions by applying the Pythagorean theorem twice — once in the XY plane, then again using that result and `Δz` as the legs of a second right triangle. Sketch the argument, then consider: if your shooter needs the *ground* distance to a target that is 2.5 meters up on a wall, which of the three distances you now have is the one it should use?

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1: Geometry</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Math Axon Home</a></div>
  <div><a href="../02_concept_lines_intersections/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Lines & Intersections →</a></div>
</div>
