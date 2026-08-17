# Concept 05: Polygons, Areas & Field Zones

> **▶ Interactive Demo: [Zone Membership & Shoelace Area Visualizer](demo.html)**
>
> Drag the zone's vertices and the robot. Watch the ray-casting crossings count up, the shoelace terms accumulate, and the inside/outside verdict flip.

<iframe src="demo.html" width="100%" height="580" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: Zones Are Not Rectangles

FRC games are built around regions of the carpet that mean something. A launching zone that scores you extra points, a protected area you are penalised for entering, a starting box you must be fully inside when autonomous begins, an amplified region that changes what a game piece is worth.

Concept 04 could handle these only if they were rectangles. They rarely are. Field regions are marked by tape lines running at angles, they get cut off by the diagonal of an alliance station, and they are often five- or six-sided. Approximating a slanted zone with an axis-aligned box either claims territory you do not have or gives away territory you do.

<div style="text-align: center; margin: 20px 0;">
  <svg width="360" height="200" viewBox="0 0 360 200" style="max-width: 100%; height: auto;" role="img" aria-label="A five-sided field zone with a robot inside it and a rectangle poorly approximating the same zone.">
    <polygon points="60,160 110,40 230,30 290,110 200,175" fill="rgba(74,222,128,0.14)" stroke="#4ade80" stroke-width="2.5" />
    <rect x="60" y="30" width="230" height="145" fill="none" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="6,4" />
    <text x="238" y="192" fill="#f43f5e" font-family="sans-serif" font-size="10">bounding box overclaims</text>
    <circle cx="165" cy="105" r="7" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />
    <text x="120" y="126" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">robot: inside?</text>
    <circle cx="270" cy="55" r="6" fill="#fbbf24" stroke="#ffffff" stroke-width="1.5" />
    <text x="278" y="48" fill="#fbbf24" font-family="sans-serif" font-size="10">in box, outside zone</text>
  </svg>
</div>

Two questions follow, and both are answered with the cross product from Concept 02. Is a given point inside the zone? And how much area does the zone cover?

---

## 2. Building the Math

### Step 1: What a polygon is

A **polygon** is an ordered list of vertices. The order is the whole substance of the definition — the same five points listed in a different order describe a different shape. Edges run between consecutive vertices, and one final edge closes the loop from the last vertex back to the first.

```
   vertices:  v[0], v[1], v[2], …, v[n−1]
   edges:     v[0]→v[1], v[1]→v[2], …, v[n−2]→v[n−1], v[n−1]→v[0]
```

That closing edge is forgotten constantly, and the resulting bug is distinctive: the shape behaves correctly except along one boundary, where points leak in or out. Any loop over the edges of a polygon should be written so the wrap-around is structural rather than a special case appended at the end. The standard idiom uses modular arithmetic on the index: edge `i` runs from `v[i]` to `v[(i + 1) % n]`, which for the last edge wraps back to `v[0]` automatically.

A polygon is **convex** if it has no dents — every interior angle is at most 180 degrees, and a segment between any two interior points stays inside. It is **concave** otherwise. This matters because convex polygons admit a much cheaper membership test.

Concept 02 already gave us a way to tell the difference. Walk the vertices in order and compute the orientation of each consecutive triple. If every turn goes the same way, the shape is convex; if the sign flips somewhere, you have found a dent.

$$
\text{convex} \iff \operatorname{cross}(v[i+1] - v[i],\ v[i+2] - v[i+1]) \quad \text{has the same sign for every } i
$$

### Step 2: Inside a convex zone — the same side of everything

For a convex polygon whose vertices are listed counter-clockwise, the interior is exactly the set of points lying to the **left of every edge**.

That claim is easier to believe than to prove, and the picture carries it. Each edge, extended into an infinite line, cuts the plane in two. For a convex shape the polygon lies entirely within the left half of each of those cuts, so the interior is what all the left halves have in common. Take any one edge and step across it and you have left the shape.

Since Concept 02's orientation test reports which side a point is on, the membership test is a loop of cross products:

$$
\text{inside} \iff \operatorname{orient}(v[i], v[i+1], P) \geq 0 \quad \text{for every edge } i
$$

One negative result and you can stop immediately — the point is out. No division, no square roots, no trigonometry, and an early exit on most queries. For the convex zones that make up most of a field, this is the test to use.

> ### Math!
> The region carved out by a set of "stay on this side" constraints is called a **convex polytope**, and each individual constraint is a **half-plane**. Written formally, each edge contributes an inequality of the form `aₓ·x + a_y·y + b ≥ 0`, where `aₓ` and `a_y` are two numbers fixed by that edge, and the polygon is the set of points satisfying all of them at once. Read `⋂` as "intersection of": the polygon is `⋂ᵢ Hᵢ`, the intersection of its half-planes. This is exactly the shape of a **linear programming** feasible region, and it will reappear when the machine learning axon looks at what a ReLU network does to its input space.

### Step 3: Inside any zone — counting crossings

Concave zones break the previous test, because a point can be to the right of an edge and still be comfortably inside the shape. The general answer is one of the most satisfying results in computational geometry.

Pick your point `P` and fire a ray from it in any fixed direction — conventionally straight along positive X, since that makes the arithmetic easiest. Count how many polygon edges the ray crosses. If the count is **odd**, `P` is inside. If it is **even**, `P` is outside.

<div style="text-align: center; margin: 20px 0;">
  <svg width="370" height="180" viewBox="0 0 370 180" style="max-width: 100%; height: auto;" role="img" aria-label="A concave polygon with two horizontal rays, one crossing an odd number of edges from an inside point and one crossing an even number from an outside point.">
    <polygon points="55,150 55,35 180,35 180,95 240,95 240,35 320,35 320,150" fill="rgba(74,222,128,0.12)" stroke="#4ade80" stroke-width="2.5" />
    <line x1="90" y1="120" x2="365" y2="120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5,4" />
    <circle cx="90" cy="120" r="6" fill="#38bdf8" />
    <circle cx="320" cy="120" r="5" fill="#fbbf24" />
    <text x="330" y="115" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="bold">1 crossing → inside</text>
    <line x1="210" y1="65" x2="365" y2="65" stroke="#c084fc" stroke-width="2" stroke-dasharray="5,4" />
    <circle cx="210" cy="65" r="6" fill="#c084fc" />
    <circle cx="240" cy="65" r="5" fill="#fbbf24" />
    <circle cx="320" cy="65" r="5" fill="#fbbf24" />
    <text x="330" y="60" fill="#c084fc" font-family="sans-serif" font-size="10" font-weight="bold">2 → outside</text>
  </svg>
</div>

The proof is a parity argument, and it takes one sentence. Start infinitely far away along the ray, where you are certainly outside. Walk back toward `P`. Every time you cross an edge you pass from outside to inside or from inside to outside — the state flips, every single time, with no exceptions. So the state when you arrive at `P` depends only on how many flips happened: an odd number leaves you inside, an even number leaves you outside.

This is the **crossing number** or **even-odd** rule, and it works for any simple polygon, convex or not, however many dents it has.

To implement it, take each edge from `v[i]` to `v[j]` and ask whether it crosses the horizontal ray heading in `+X` from `P`:

1. **Does the edge span the ray's height at all?** It does when one endpoint is above `P.y` and the other is not. Written as `(v[i].y > P.y) ≠ (v[j].y > P.y)`, using a strict comparison on both sides.
2. **Does it cross to the right of P rather than the left?** Find the edge's x at height `P.y` by interpolating, and compare it to `P.x`.

That first condition deserves attention, because it is where naive implementations break. A ray passing exactly through a vertex touches two edges at once, and counting both, or neither, gives the wrong parity — producing a point that reports "outside" while sitting visibly inside the zone. The strict-on-one-side comparison written above is a **half-open rule**: each edge owns its lower endpoint and disowns its upper one. A vertex shared by two edges is then counted exactly once, and the ambiguity disappears rather than being patched.

### Step 4: The area of a zone

Rectangles have area width times height. General polygons need something better, and the cross product supplies it.

Start with a triangle with one corner at the origin and the other two at `u` and `v`. From Concept 02, `|cross(u, v)|` is the area of the parallelogram those two vectors span, and a triangle is half a parallelogram. So the triangle's area is `½|cross(u, v)|`.

Now fan the whole polygon into triangles from the origin: origin to `v[0]` to `v[1]`, then origin to `v[1]` to `v[2]`, and so on around the loop. Summing the signed cross products gives the **shoelace formula**:

$$
\begin{aligned}
\text{Area} &= \frac{1}{2} \cdot \left\lvert \sum_i \operatorname{cross}(v[i], v[i+1]) \right\rvert \\
&= \frac{1}{2} \cdot \left\lvert \sum_i \left( x[i] \cdot y[i+1] - x[i+1] \cdot y[i] \right) \right\rvert
\end{aligned}
$$

The elegance is in the word *signed*. If the origin sits outside the polygon, some of those triangles stick out beyond the shape and should not be counted. They are not counted — because those triangles are traversed in the opposite rotational direction, their cross products come out negative, and they subtract exactly the excess that the other triangles overcounted. The formula needs no special handling for where you put the origin, and none for concave shapes.

The sign of the sum before you take the absolute value is useful on its own: positive means the vertices were listed counter-clockwise, negative means clockwise. Since Step 2's convex test assumed counter-clockwise ordering, running the shoelace sum first is a cheap way to detect a zone definition that was typed in backwards.

> ### Math!
> It is called the shoelace formula because of how it is written by hand: list the coordinates in a column, repeat the first vertex at the bottom, then multiply diagonally down-right and down-left, crossing over like lacing a shoe. Down-right products are added, down-left products subtracted. It is also known as the **surveyor's formula**, having been used to compute land parcel areas from boundary measurements long before it was used for anything on a computer.

### Step 5: Choosing a test

Three tools now overlap, and picking between them is a judgement about cost and shape.

```
   bounding box (Concept 04)   4 comparisons     rectangles only, or as a first filter
   convex half-planes          n cross products  convex zones, early exit, no division
   ray casting                 n edge tests      any simple polygon, handles dents
```

The standard arrangement uses them together. Precompute each zone's bounding box once. On every query, test the box first — it rejects the overwhelming majority of points in four comparisons — and only run the exact polygon test on the survivors. The exact test is never skipped, so nothing is approximated; it is just rarely reached.

### A caution about the robot's size

Everything above tests a **point** against a zone. Robots are boxes, and game rules are usually written about the robot, not its centre. "Fully inside the starting zone" means all four bumper corners are inside; "has entered the protected area" may mean any part of it has.

The point test is still the primitive. To ask whether the robot is fully inside, test all four corners and require every answer to be yes. To ask whether it has touched the zone at all, test the corners and also check whether any bumper edge crosses any zone edge — because a large robot can straddle a small zone with every corner outside it. That crossing check is precisely the segment intersection from Concept 02, run over each pair of edges.

---

## 3. Solving It in Code (Java & WPILib)

### First-Principles Java

```java
import edu.wpi.first.math.geometry.Translation2d;
import java.util.List;

public class Zone {
    private final List<Translation2d> vertices;   // in order; the loop closes implicitly

    public Zone(List<Translation2d> vertices) {
        this.vertices = List.copyOf(vertices);
    }

    /** Crossing-number test. Works for convex and concave zones alike. */
    public boolean contains(Translation2d p) {
        boolean inside = false;
        int n = vertices.size();
        for (int i = 0, j = n - 1; i < n; j = i++) {     // j trails i, wrapping at the end
            Translation2d a = vertices.get(i);
            Translation2d b = vertices.get(j);

            // Half-open rule: each edge owns its lower endpoint, so a ray through a
            // shared vertex is counted once rather than twice or not at all.
            boolean straddles = (a.getY() > p.getY()) != (b.getY() > p.getY());
            if (!straddles) continue;

            // X where this edge sits at height p.y; count only crossings to the right.
            double t = (p.getY() - a.getY()) / (b.getY() - a.getY());
            double crossingX = a.getX() + t * (b.getX() - a.getX());
            if (p.getX() < crossingX) inside = !inside;
        }
        return inside;
    }

    /** Shoelace area. The sign of the raw sum reveals the winding direction. */
    public double signedArea() {
        double sum = 0.0;
        int n = vertices.size();
        for (int i = 0; i < n; i++) {
            Translation2d a = vertices.get(i);
            Translation2d b = vertices.get((i + 1) % n);   // wraps to v0 on the last edge
            sum += a.getX() * b.getY() - b.getX() * a.getY();
        }
        return sum / 2.0;
    }

    public double area() { return Math.abs(signedArea()); }

    public boolean isCounterClockwise() { return signedArea() > 0; }
}
```

```java
Zone launchZone = new Zone(List.of(
    new Translation2d(2.0, 1.0),
    new Translation2d(6.5, 1.0),
    new Translation2d(7.5, 4.0),
    new Translation2d(3.0, 5.0)));

System.out.printf("area %.2f m², ccw %b%n", launchZone.area(), launchZone.isCounterClockwise());
System.out.println(launchZone.contains(new Translation2d(4.0, 3.0)));   // true

// Rules are about the robot, not its centre: require all four bumper corners inside.
boolean fullyInside = robotCorners.stream().allMatch(launchZone::contains);
```

### Production WPILib Equivalent

WPILib's geometry package covers points, poses and simple shapes, but it has no general polygon type — zone definitions are game-specific and change every season, so they live in your own code. Two conventions make that code much easier to trust.

Define every zone once, in a single constants file, with vertices listed counter-clockwise and a comment naming the field drawing they came from. Then assert the winding at construction with `signedArea() > 0`, so a zone typed in backwards fails loudly at startup instead of silently reporting every point as outside during a match.

---

## 4. Bridge to Machine Learning & Modern Autonomy

The half-plane picture from Step 2 is what a neural network with ReLU activations actually builds.

Each ReLU unit computes a weighted sum and clips it at zero. Whether it is active or clipped depends on which side of a hyperplane the input falls on — Step 2's constraint, in as many dimensions as the layer has inputs. A whole layer of such units carves the input space into regions, and each region is the intersection of the half-planes corresponding to which units are firing. That intersection is a **convex polytope**, exactly the object in the Math! sidebar.

The consequence is worth sitting with: inside any one of those regions the network is perfectly linear, because the active units are fixed and the clipped ones contribute nothing. A deep ReLU network is therefore a **piecewise-linear function** — a plane sliced into polytopes, each carrying its own linear map. Training does not smooth this out; it moves the cuts. When the machine learning axon shows a decision boundary bending to separate two clusters, the bend is made of flat pieces, and counting them is a standard way to measure a network's expressive capacity.

The shoelace formula has a direct second life in computer vision. **Instance segmentation** models such as Mask R-CNN and the polygon-output detectors used for aerial and document imagery report objects as vertex lists rather than boxes, precisely because a box overclaims for anything slanted — the same complaint that opened this concept. Scoring those predictions needs polygon area for the intersection-over-union of Concept 04, and that area comes from the shoelace sum. Training-data pipelines lean on the crossing-number test too: deciding which labelled region a click or a pixel belongs to is Step 3, run millions of times.

The autonomy link is more direct still. Ray casting is how an occupancy grid decides which cells a sensor beam passed through, and the even-odd rule is how a planner decides whether a candidate waypoint sits inside a keep-out region before it wastes time expanding it.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1
A zone has vertices `(0, 0)`, `(4, 0)`, `(4, 3)`, `(0, 3)` listed in that order. Compute its area with the shoelace formula and confirm the winding direction.

**Solution:**
Apply `Σ (x[i] · y[i+1] − x[i+1] · y[i])` around the loop, remembering the closing edge from `(0,3)` back to `(0,0)`:
1. `(0,0)→(4,0)`: `0·0 − 4·0 = 0`
2. `(4,0)→(4,3)`: `4·3 − 4·0 = 12`
3. `(4,3)→(0,3)`: `4·3 − 0·3 = 12`
4. `(0,3)→(0,0)`: `0·0 − 0·3 = 0`
Sum is `24`, so `signedArea = 24/2 = +12`. The area is 12 m², which checks out against width times height for this 4 by 3 rectangle, and the positive sign confirms counter-clockwise ordering.

---

### Checkpoint 2
A team defines their protected zone but lists the vertices clockwise. They use the Step 2 convex test with the condition `orient(...) ≥ 0` on every edge. What happens during a match, and what are two ways to fix it?

**Solution:**
Every point in the field reports as **outside**. With clockwise ordering the interior lies to the *right* of every edge, so `orient` returns negative for interior points and the `≥ 0` condition fails on the very first edge. The zone effectively does not exist, and any penalty avoidance or scoring bonus keyed to it never triggers.

Two fixes:
1. Reverse the vertex list so the winding is counter-clockwise, and assert `signedArea() > 0` at construction so this cannot recur silently.
2. Make the test winding-agnostic: require all orientation results to share *a* sign rather than specifically the positive one — that is, accept if all are `≥ 0` or all are `≤ 0`.

The first is better. Ambiguity about winding tends to leak into other code, and pinning the convention down once is cheaper than defending against both everywhere.

---

### Deep Dive 1
Step 3's half-open rule resolves rays passing through vertices. Construct the failure it prevents: take a simple diamond-shaped zone, choose a query point whose horizontal ray passes exactly through one of its vertices, and hand-trace the crossing count both with and without the strict comparison on one side. Then investigate the **winding number** algorithm as an alternative to even-odd, and work out how the two differ for a self-intersecting polygon — a figure-eight is the clarifying case.

### Deep Dive 2
This concept assumed zones are static. In many games they are not: a region activates for a few seconds, or its boundary is defined relative to a movable field element. Design a `Zone` that can be transformed, and work out what each operation costs — translating a polygon means moving every vertex, so decide whether to transform the zone or instead transform the query point into the zone's own frame and leave the polygon untouched. The trigonometry module's coordinate-frame concept is the tool for the second approach; argue which is cheaper when one zone is tested against many points each cycle.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../04_concept_bounding_boxes/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 04: Bounding Boxes</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 1 Overview</a></div>
  <div><a href="../../02_trigonometry/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Module 2: Trigonometry →</a></div>
</div>
