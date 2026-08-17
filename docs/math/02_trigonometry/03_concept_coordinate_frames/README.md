# Concept 03: Coordinate Frames (Field, Robot & Camera)

> **▶ Interactive Demo: [Frame Transform Explorer](demo.html)**
>
> Drag the robot, spin its heading, drag the target. Read the target's position in the field frame and in the robot frame at the same time — and switch on the naive-addition overlay to watch the wrong answer drift away from the right one as soon as the heading leaves zero.

<iframe src="demo.html" width="100%" height="660" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);"></iframe>

---

## 1. The Real-World Problem: The Camera Only Knows About Itself

A camera on the robot spots a game piece and reports one thing: **1.5 metres ahead of me, 0.4 metres to my right.**

That is all a camera can ever say. It has no gyro, no odometry and no idea where the field's corner is. Meanwhile the path planner that has to drive to that piece speaks only **field** coordinates — metres from a fixed corner of the carpet, the same numbers an autonomous routine was written against last night.

So we need a translation between two ways of naming the same physical spot. Throughout this concept:

* The **field frame** has its origin at a corner of the carpet, X pointing down-field, Y pointing left as you look down-field, and angles measured counter-clockwise from the X-axis. This is WPILib's convention.
* The **robot frame** has its origin at the centre of the drive base, x pointing out of the front bumper, y pointing out of the robot's left side. Same handedness, carried around by the robot.

Say the gyro and odometry put the robot at field `(5.00, 3.00)`. The camera's sighting, written in the robot frame, is `(1.5, −0.4)` — 1.5 forward, and 0.4 in the *negative* left direction, which is 0.4 to the right.

The obvious move is to add them: `(5.00 + 1.5, 3.00 − 0.4) = (6.50, 2.60)`. Every instinct says this is right, and it is easy to check.

**At heading 0°, it is right.** The robot's nose points down-field, so "1.5 m ahead" really is "1.5 m further along field X", and "0.4 m right" really is "0.4 m in field −Y". Adding the two coordinate pairs gives `(6.50, 2.60)`, and if you walk out on the carpet with a tape measure, that is where the piece is.

**At heading 90°, it is badly wrong.** Now the robot's nose points along field +Y. "1.5 m ahead" has become "1.5 m further along field **Y**", and "0.4 m to my right" has become "0.4 m along field **+X**". The piece is actually at `(5.00 + 0.4, 3.00 + 1.5) = (5.40, 4.50)`. Addition still cheerfully returns `(6.50, 2.60)`.

Those two points are `√((6.50 − 5.40)² + (2.60 − 4.50)²) = √(1.21 + 3.61) = √4.82 = 2.20` metres apart. A robot sent to the addition answer arrives more than two metres from the piece — most of a robot length past it and well off to the side.

<div style="text-align: center; margin: 20px 0;">
  <svg width="480" height="240" viewBox="0 0 460 234" style="max-width: 100%; height: auto;" role="img" aria-label="Two field panels. On the left the robot faces down-field at heading zero and the naive sum lands on the true game piece position. On the right the robot is turned ninety degrees, the true piece has moved up and left, and the naive sum is left stranded two point two metres away.">
    <g>
      <rect x="16" y="70" width="192" height="120" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
      <circle cx="16" cy="190" r="3" fill="currentColor" fill-opacity="0.6" />
      <text x="10" y="203" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="9">field (0,0)</text>
      <rect x="125" y="107" width="22" height="22" rx="3" fill="#38bdf8" fill-opacity="0.18" stroke="#38bdf8" stroke-width="2" />
      <line x1="136" y1="118" x2="166" y2="118" stroke="#38bdf8" stroke-width="2" />
      <polygon points="170,118 161,114 161,122" fill="#38bdf8" />
      <line x1="136" y1="118" x2="136" y2="88" stroke="#4ade80" stroke-width="2" />
      <polygon points="136,84 132,93 140,93" fill="#4ade80" />
      <line x1="136" y1="118" x2="172" y2="118" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3" />
      <line x1="172" y1="118" x2="172" y2="127.6" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3" />
      <circle cx="172" cy="127.6" r="6" fill="#4ade80" />
      <text x="120" y="150" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">piece (6.50, 2.60)</text>
      <text x="16" y="206" fill="currentColor" fill-opacity="0.75" font-family="sans-serif" font-size="11" font-weight="bold">heading 0°  —  addition happens to work</text>
    </g>
    <g transform="translate(240,0)">
      <rect x="16" y="70" width="192" height="120" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
      <circle cx="16" cy="190" r="3" fill="currentColor" fill-opacity="0.6" />
      <text x="10" y="203" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="9">field (0,0)</text>
      <rect x="125" y="107" width="22" height="22" rx="3" fill="#38bdf8" fill-opacity="0.18" stroke="#38bdf8" stroke-width="2" />
      <line x1="136" y1="118" x2="136" y2="88" stroke="#38bdf8" stroke-width="2" />
      <polygon points="136,84 132,93 140,93" fill="#38bdf8" />
      <line x1="136" y1="118" x2="106" y2="118" stroke="#4ade80" stroke-width="2" />
      <polygon points="102,118 111,114 111,122" fill="#4ade80" />
      <line x1="136" y1="118" x2="136" y2="82" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3" />
      <line x1="136" y1="82" x2="145.6" y2="82" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3" />
      <circle cx="145.6" cy="82" r="6" fill="#4ade80" />
      <text x="152" y="78" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">true (5.40, 4.50)</text>
      <line x1="145.6" y1="82" x2="172" y2="127.6" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3" />
      <text x="150" y="112" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="bold">2.20 m</text>
      <line x1="166" y1="121.6" x2="178" y2="133.6" stroke="#f43f5e" stroke-width="2.5" />
      <line x1="178" y1="121.6" x2="166" y2="133.6" stroke="#f43f5e" stroke-width="2.5" />
      <text x="106" y="150" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="bold">addition says (6.50, 2.60)</text>
      <text x="16" y="206" fill="currentColor" fill-opacity="0.75" font-family="sans-serif" font-size="11" font-weight="bold">heading 90°  —  addition is 2.20 m out</text>
    </g>
    <text x="16" y="228" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">Same robot position, same camera reading. Only the heading changed. Blue = robot forward, green = robot left.</text>
  </svg>
</div>

Notice what makes this bug so nasty. It is not a crash and not an obviously silly number — `(6.50, 2.60)` is a perfectly plausible spot on the carpet. And it is *exactly correct* whenever the robot happens to be square to the field, which is precisely the condition under which people test things in the shop. It only fails in a match, at speed, after a turn.

The rest of this concept fixes it properly, and by the end you will also be able to run the transform backwards — given a target's known field position, work out where the robot should look for it.

---

## 2. Building the Math: A Frame Is Just Two Directions and a Point

### Step 1: What "1.5 metres ahead" actually means

Strip the sentence down. When the camera says the piece is at `(1.5, −0.4)` in the robot frame, it is giving you a set of walking directions:

> Stand at the robot's origin. Walk 1.5 metres along whatever direction the robot calls **forward**. Then walk 0.4 metres along whatever direction the robot calls **right**.

Every quantity in that instruction is already known in field terms — except the two direction words. So the whole problem reduces to one question: **in field coordinates, which way is the robot's forward, and which way is its left?**

That question Concept 02 already answered. The robot's forward axis is a unit vector, and its heading θ is by definition the angle that unit vector makes with the field's X-axis. A unit vector at angle θ sits at `(cos θ, sin θ)` on the unit circle. The robot's left axis is a quarter turn counter-clockwise from that, and Concept 02 Step 2 showed a quarter turn sends `(cos θ, sin θ)` to `(−sin θ, cos θ)`.

```
   robot forward, in field coordinates  =  ( cos θ,  sin θ )
   robot left,    in field coordinates  =  (−sin θ,  cos θ )
```

These are exactly the images of `î` and `ĵ` from Concept 02. Nothing new has been introduced — the robot's own axes, seen from the stands, *are* the rotated basis vectors.

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="250" viewBox="0 0 340 250" style="max-width: 100%; height: auto;" role="img" aria-label="A robot origin with its forward axis drawn at thirty-five degrees above the field X direction and its left axis a quarter turn beyond it, and a dashed path walking one point five metres along forward then zero point four metres along right to reach the game piece.">
    <line x1="40" y1="200" x2="310" y2="200" stroke="currentColor" stroke-opacity="0.28" stroke-width="1.5" stroke-dasharray="5,4" />
    <line x1="110" y1="240" x2="110" y2="60" stroke="currentColor" stroke-opacity="0.28" stroke-width="1.5" stroke-dasharray="5,4" />
    <text x="264" y="214" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">field X direction</text>
    <text x="116" y="70" fill="currentColor" fill-opacity="0.5" font-family="sans-serif" font-size="10">field Y direction</text>
    <path d="M 150 200 A 40 40 0 0 0 142.77 177.06" fill="none" stroke="#c084fc" stroke-width="2" />
    <text x="152" y="188" fill="#c084fc" font-family="sans-serif" font-size="12" font-weight="bold">θ = 35°</text>
    <line x1="110" y1="200" x2="175.5" y2="154.1" stroke="#38bdf8" stroke-width="3" />
    <polygon points="179.6,151.2 168.8,152.6 172.4,157.8" fill="#38bdf8" />
    <text x="184" y="146" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="bold">forward = (0.819, 0.574)</text>
    <line x1="110" y1="200" x2="64.1" y2="134.5" stroke="#4ade80" stroke-width="3" />
    <polygon points="61.2,130.4 62.6,141.2 67.8,137.6" fill="#4ade80" />
    <text x="4" y="124" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">left = (−0.574, 0.819)</text>
    <line x1="110" y1="200" x2="208.3" y2="131.2" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="5,4" />
    <line x1="208.3" y1="131.2" x2="226.65" y2="157.4" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="5,4" />
    <text x="120" y="168" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="bold">1.5 m along forward</text>
    <text x="214" y="124" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="bold">0.4 m along right</text>
    <circle cx="226.65" cy="157.4" r="6" fill="#fbbf24" />
    <circle cx="110" cy="200" r="4.5" fill="currentColor" fill-opacity="0.75" />
    <text x="16" y="216" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">robot origin, at field (5.00, 3.00)</text>
    <text x="16" y="240" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">Unit arrows are 1 m long. The dashed path is the camera's reading, walked out in the field.</text>
  </svg>
</div>

### Step 2: Walk the directions, then start from the right place

A walk of `a` metres along forward plus `b` metres along left, written in field coordinates, is just those two direction vectors scaled and added:

```
   a · ( cos θ, sin θ )  +  b · (−sin θ, cos θ )
     = ( a·cos θ − b·sin θ ,  a·sin θ + b·cos θ )
```

That is Concept 02's rotation, arriving on its own rather than being imposed. The walk has an offset *shape* in the field, but it still starts at the origin. To finish, start it where the robot actually is — add the robot's field position `(rx, ry)`:

```
   field_x = rx + ( a·cos θ − b·sin θ )
   field_y = ry + ( a·sin θ + b·cos θ )
```

**Rotate the local offset by the heading, then translate by the robot's position.** A rotation followed by a translation is called a **rigid transform**: Concept 02 Step 4 proved rotation preserves length, and sliding everything by a fixed amount obviously does too, so distances between transformed points come out unchanged. That is the right property for a physical robot, which does not stretch.

Run our numbers at heading 35°, with `a = 1.5`, `b = −0.4`, `cos 35° = 0.81915`, `sin 35° = 0.57358`:

```
   rotated_x = 1.5(0.81915) − (−0.4)(0.57358) = 1.22873 + 0.22943 =  1.4582
   rotated_y = 1.5(0.57358) + (−0.4)(0.81915) = 0.86037 − 0.32766 =  0.5327

   field_x = 5.00 + 1.4582 = 6.458
   field_y = 3.00 + 0.5327 = 3.533
```

Check the rotation did not stretch anything: `√(1.4582² + 0.5327²) = √2.4101 = 1.5524`, and the original offset had length `√(1.5² + 0.4²) = √2.41 = 1.5524`. Identical, as Step 4 of Concept 02 promised.

And set θ = 0 to see the naive version reappear as a special case: `cos 0 = 1`, `sin 0 = 0`, so `field_x = rx + a` and `field_y = ry + b`. Plain addition is not a *different* rule — it is this rule with the heading quietly assumed away.

> ### Math!
> A transform is worth naming by the two frames it connects. Write the one we just built as **field ← robot**, read out loud as **"field from robot"**. It eats a point written in robot coordinates and hands back the same point written in field coordinates.
>
> The arrow points the way the *data* flows, and the label nearest the arrow is the frame the data arrives in. A transform is completely described by three numbers — the child frame's origin and heading as seen from the parent frame — so people usually write it as a **pose**, the triple `(x, y, θ)`. Our robot's pose is `(5.00, 3.00, 35°)`, read out loud as **"the pose of the robot in the field frame"**. Every rigid transform in this concept is one of these triples, and every one of them means: rotate by θ, then translate by `(x, y)`.

### Step 3: Why the order is rotate-then-translate and not the reverse

"Rotate then translate" is two operations, and swapping them gives a different answer. This is worth doing once with real numbers, because the reversed version is a common bug and it does not look like one in code.

Take the same sighting at heading 35°. Translate first — add the robot's position to the raw local offset — and you get `(5.00 + 1.5, 3.00 − 0.4) = (6.50, 2.60)`. Now rotate *that* by 35°:

```
   x' = 6.50(0.81915) − 2.60(0.57358) = 5.32449 − 1.49130 = 3.833
   y' = 6.50(0.57358) + 2.60(0.81915) = 3.72824 + 2.12979 = 5.858
```

The answer is `(3.833, 5.858)` instead of `(6.458, 3.533)` — 3.51 m away, on the far side of the field from where the piece is.

The reason is easy to see once you look at what got rotated. In the wrong order, the robot's *own field position* went through the rotation too. `(5.00, 3.00)` rotated by 35° is `(2.375, 5.325)`, so the calculation quietly picked the robot up and swung it around the **field origin** — a corner of the carpet twenty feet away — before measuring anything. Both points are the same distance from that corner (`√(5² + 3²) = 5.831` m for the robot, `√(2.375² + 5.325²) = 5.831` m for the ghost), which is the signature of a rotation about the wrong centre.

<div style="text-align: center; margin: 20px 0;">
  <svg width="320" height="250" viewBox="0 0 320 250" style="max-width: 100%; height: auto;" role="img" aria-label="A field showing the robot at five three with heading thirty-five degrees, the correct piece position just ahead of it, and a ghost robot swung thirty-five degrees around the field origin with the wrong-order answer beside it.">
    <rect x="20" y="28" width="234" height="182" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <circle cx="20" cy="210" r="3.5" fill="currentColor" fill-opacity="0.7" />
    <text x="14" y="223" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="9">field origin</text>
    <path d="M 150 132 A 151.6 151.6 0 0 0 81.79 71.56" fill="none" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4,4" />
    <rect x="70.8" y="60.6" width="22" height="22" rx="3" fill="#f43f5e" fill-opacity="0.10" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3" />
    <text x="26" y="56" fill="#f43f5e" font-family="sans-serif" font-size="9">robot, flung round the origin</text>
    <circle cx="119.7" cy="57.7" r="6" fill="#f43f5e" />
    <text x="126" y="50" fill="#f43f5e" font-family="sans-serif" font-size="10" font-weight="bold">(3.833, 5.858)</text>
    <text x="126" y="62" fill="#f43f5e" font-family="sans-serif" font-size="9">translate, then rotate</text>
    <rect x="139" y="121" width="22" height="22" rx="3" fill="#38bdf8" fill-opacity="0.18" stroke="#38bdf8" stroke-width="2" />
    <line x1="150" y1="132" x2="174.6" y2="114.8" stroke="#38bdf8" stroke-width="2" />
    <polygon points="178.9,111.8 168.4,114.6 172.7,120.7" fill="#38bdf8" />
    <text x="96" y="152" fill="#38bdf8" font-family="sans-serif" font-size="9">robot (5.00, 3.00), 35°</text>
    <circle cx="187.9" cy="118.1" r="6" fill="#4ade80" />
    <text x="196" y="114" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">(6.458, 3.533)</text>
    <text x="196" y="126" fill="#4ade80" font-family="sans-serif" font-size="9">rotate, then translate</text>
    <text x="16" y="240" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">Translating first lets the robot's own position ride through the rotation. Error: 3.51 m.</text>
  </svg>
</div>

The rule to remember: **the rotation must act only on quantities measured in the robot frame.** The moment a field-frame number is inside the thing being rotated, you are spinning the field about its own corner.

### Step 4: Chaining — field ← robot ← camera

A camera is never at the robot's centre. Ours is mounted 0.30 m forward and 0.10 m to the left of the drive-base centre, and yawed 20° to the left so it can watch the intake lane. So the camera has its own frame, and its reading `(1.5, −0.4)` is in *camera* coordinates, not robot coordinates.

The fix is not a new idea, only the same one applied twice. The camera's pose in the robot frame is `(0.30, 0.10, 20°)`, so **robot ← camera** is rotate by 20°, then translate by `(0.30, 0.10)`:

```
   x = 1.5(0.93969) − (−0.4)(0.34202) = 1.40954 + 0.13681 = 1.5463
   y = 1.5(0.34202) + (−0.4)(0.93969) = 0.51303 − 0.37588 = 0.1372

   in robot coordinates: (0.30 + 1.5463, 0.10 + 0.1372) = (1.8463, 0.2372)
```

Now feed that through **field ← robot**, which is what Step 2 built, at heading 35°:

```
   x = 1.8463(0.81915) − 0.2372(0.57358) = 1.51244 − 0.13603 = 1.3764
   y = 1.8463(0.57358) + 0.2372(0.81915) = 1.05902 + 0.19426 = 1.2533

   in field coordinates: (5.00 + 1.3764, 3.00 + 1.2533) = (6.376, 4.253)
```

<div style="text-align: center; margin: 20px 0;">
  <svg width="340" height="260" viewBox="0 0 340 260" style="max-width: 100%; height: auto;" role="img" aria-label="A zoomed view of the robot at field five three with heading thirty-five degrees, the camera mounted up and to the left of centre pointing at fifty-five degrees, and the sighting line running out to the game piece at six point three seven six comma four point two five three.">
    <line x1="60" y1="180" x2="78.84" y2="154.6" stroke="#c084fc" stroke-width="2.5" />
    <circle cx="60" cy="180" r="5" fill="currentColor" fill-opacity="0.75" />
    <line x1="60" y1="180" x2="96.86" y2="154.19" stroke="#38bdf8" stroke-width="2.5" />
    <polygon points="101,151.3 90.2,152.6 93.9,157.8" fill="#38bdf8" />
    <text x="26" y="196" fill="#38bdf8" font-family="sans-serif" font-size="9" font-weight="bold">robot (5.00, 3.00), 35°</text>
    <circle cx="78.84" cy="154.6" r="4.5" fill="#c084fc" />
    <line x1="78.84" y1="154.6" x2="101.78" y2="121.83" stroke="#c084fc" stroke-width="2.5" />
    <polygon points="105.1,117.1 96.1,123.3 101.9,127.4" fill="#c084fc" />
    <text x="8" y="146" fill="#c084fc" font-family="sans-serif" font-size="9" font-weight="bold">camera (5.188, 3.254), 55°</text>
    <line x1="78.84" y1="154.6" x2="197.64" y2="54.67" stroke="#fbbf24" stroke-width="2" stroke-dasharray="5,4" />
    <text x="112" y="128" fill="#fbbf24" font-family="sans-serif" font-size="9" font-weight="bold">sighting (1.5, −0.4)</text>
    <text x="112" y="140" fill="#fbbf24" font-family="sans-serif" font-size="9" font-weight="bold">in the camera frame</text>
    <circle cx="197.64" cy="54.67" r="6.5" fill="#4ade80" />
    <text x="206" y="52" fill="#4ade80" font-family="sans-serif" font-size="10" font-weight="bold">piece (6.376, 4.253)</text>
    <text x="16" y="222" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">Purple: the camera mount, 0.30 m forward and 0.10 m left of centre, yawed 20°.</text>
    <text x="16" y="240" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">Scale: 100 px per metre. All three arrows are drawn at their stated field angles.</text>
  </svg>
</div>

There is a shortcut hiding here, and confirming it is a good check on everything so far. Instead of hopping frame by frame, collapse **field ← robot** and **robot ← camera** into a single transform first. Its rotation is `35° + 20° = 55°` — rotations compose by adding angles, which is Concept 02 Step 6. Its translation is the camera's position expressed in the field, which is the camera's robot-frame offset put through **field ← robot**:

```
   x = 0.30(0.81915) − 0.10(0.57358) = 0.24575 − 0.05736 = 0.1884
   y = 0.30(0.57358) + 0.10(0.81915) = 0.17207 + 0.08192 = 0.2540

   camera pose in the field: (5.188, 3.254, 55°)
```

Apply that single transform to the raw sighting, with `cos 55° = 0.57358` and `sin 55° = 0.81915`:

```
   x = 1.5(0.57358) − (−0.4)(0.81915) = 0.86036 + 0.32766 = 1.1880
   y = 1.5(0.81915) + (−0.4)(0.57358) = 1.22873 − 0.22943 = 0.9993

   field: (5.188 + 1.188, 3.254 + 0.999) = (6.376, 4.253)
```

The same answer to every digit. Two transforms applied in sequence are always equivalent to one composed transform, so a chain of any length collapses to a single pose — which is exactly why robot code can afford to describe every sensor by its own little mounting pose and let the library do the bookkeeping.

> ### Math!
> The chaining rule is easiest to read when you write the frame labels out:
>
> ```
>    (field ← robot) ∘ (robot ← camera)  =  (field ← camera)
> ```
>
> Read out loud as **"field-from-robot composed with robot-from-camera equals field-from-camera."** The `∘` is read "composed with", or just "after". The two inner `robot` labels sit next to each other and cancel, exactly like units cancelling in a physics calculation.
>
> That cancellation is a genuine debugging tool. If your labels do not meet — if you find yourself writing `(field ← robot) ∘ (camera ← tag)` — the composition is meaningless and you have found the bug before running the code. Line the labels up first, then write the arithmetic.

### Step 5: Running it backwards, and the trap in doing so

The other direction comes up constantly: an AprilTag's field position is published in the game manual, and you want to know where the robot should expect to see it. That is **robot ← field**, the inverse of what we built.

Here is the trap. The forward transform is "rotate by θ, then add `(rx, ry)`", so it is tempting to write the inverse as "rotate by −θ, then subtract `(rx, ry)`" — negate both parts and be done. **That is wrong**, and the reason is that reversing a two-step process reverses the *order* of the steps as well as each step. You put socks on before shoes; undoing that is shoes off before socks off, not socks off before shoes off.

Derive it instead. We know what the forward transform claims, for the local coordinates `(a, b)` we are looking for:

```
   fx = rx + ( a·cos θ − b·sin θ )
   fy = ry + ( a·sin θ + b·cos θ )
```

Move the robot's position to the left and name the difference `(dx, dy) = (fx − rx, fy − ry)`:

```
   dx = a·cos θ − b·sin θ
   dy = a·sin θ + b·cos θ
```

Two equations, two unknowns. Multiply the first by `cos θ`, the second by `sin θ`, and add:

```
   dx·cos θ + dy·sin θ = a·cos²θ − b·sin θ cos θ + a·sin²θ + b·sin θ cos θ
                       = a·(cos²θ + sin²θ)
                       = a
```

The two `b` terms cancel outright, and `cos²θ + sin²θ = 1` is the Pythagorean identity from Concept 01. Do the mirror image — multiply the first by `−sin θ`, the second by `cos θ`, and add — and the `a` terms cancel the same way, leaving `b`. So:

```
   a = ( fx − rx)·cos θ + (fy − ry)·sin θ
   b = −(fx − rx)·sin θ + (fy − ry)·cos θ
```

Those coefficients are exactly Concept 02 Step 5's rotation by `−θ`, applied to the difference. In words: **subtract first, then un-rotate.** The subtraction happens in the field frame, where both positions are known; the rotation happens afterwards, on a quantity that is already a pure offset.

Work it. The robot is still at `(5.00, 3.00, 35°)`; a tag sits at field `(8.00, 4.00)`. The difference is `(3.00, 1.00)`:

```
   a =  3.00(0.81915) + 1.00(0.57358) = 2.45746 + 0.57358 =  3.031
   b = −3.00(0.57358) + 1.00(0.81915) = −1.72073 + 0.81915 = −0.902
```

The tag is 3.03 m ahead of the robot and 0.90 m to its right. Sanity-check with a length: the field-frame difference has length `√(3² + 1²) = 3.162`, and `√(3.031² + 0.902²) = √9.9999 = 3.162`. A frame change can never alter how far away something is, so this check catches almost every sign error for free.

<div style="text-align: center; margin: 20px 0;">
  <svg width="320" height="240" viewBox="0 0 320 240" style="max-width: 100%; height: auto;" role="img" aria-label="A field with the robot at five three heading thirty-five degrees and a tag at eight four. The difference vector between them is decomposed into three point zero three metres along the robot's forward axis and zero point nine metres along its right axis.">
    <rect x="20" y="54" width="234" height="156" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5" />
    <circle cx="20" cy="210" r="3.5" fill="currentColor" fill-opacity="0.7" />
    <text x="14" y="223" fill="currentColor" fill-opacity="0.55" font-family="sans-serif" font-size="9">field origin</text>
    <line x1="150" y1="132" x2="192.6" y2="102.2" stroke="#38bdf8" stroke-width="2" />
    <polygon points="196.9,99.2 186.4,102.1 190.7,108.2" fill="#38bdf8" />
    <text x="150" y="96" fill="#38bdf8" font-family="sans-serif" font-size="9" font-weight="bold">forward</text>
    <line x1="150" y1="132" x2="167.9" y2="157.56" stroke="#4ade80" stroke-width="2" />
    <polygon points="170.5,161.3 168.8,150.6 163.6,154.2" fill="#4ade80" />
    <text x="172" y="170" fill="#4ade80" font-family="sans-serif" font-size="9" font-weight="bold">right</text>
    <rect x="139" y="121" width="22" height="22" rx="3" fill="#38bdf8" fill-opacity="0.18" stroke="#38bdf8" stroke-width="2" />
    <text x="86" y="150" fill="currentColor" fill-opacity="0.7" font-family="sans-serif" font-size="9">robot (5.00, 3.00), 35°</text>
    <line x1="150" y1="132" x2="228" y2="106" stroke="#c084fc" stroke-width="2.5" />
    <text x="152" y="122" fill="#c084fc" font-family="sans-serif" font-size="9" font-weight="bold">Δ = (3.00, 1.00)</text>
    <line x1="150" y1="132" x2="214.56" y2="86.8" stroke="#fbbf24" stroke-width="2" stroke-dasharray="5,4" />
    <line x1="214.56" y1="86.8" x2="228" y2="106" stroke="#fbbf24" stroke-width="2" stroke-dasharray="5,4" />
    <text x="192" y="80" fill="#fbbf24" font-family="sans-serif" font-size="9" font-weight="bold">3.03 m ahead</text>
    <text x="232" y="98" fill="#fbbf24" font-family="sans-serif" font-size="9" font-weight="bold">0.90 m right</text>
    <circle cx="228" cy="106" r="6" fill="#f43f5e" />
    <text x="196" y="126" fill="#f43f5e" font-family="sans-serif" font-size="9" font-weight="bold">tag (8.00, 4.00)</text>
    <text x="16" y="236" fill="currentColor" fill-opacity="0.6" font-family="sans-serif" font-size="10">Subtract in the field frame, then un-rotate the difference by 35°. Scale: 26 px per metre.</text>
  </svg>
</div>

Now the version that swaps the order — un-rotate the tag's field position first, then subtract the robot's position:

```
   x =  8.00(0.81915) + 4.00(0.57358) = 6.55322 + 2.29430 = 8.848
   y = −8.00(0.57358) + 4.00(0.81915) = −4.58861 + 3.27661 = −1.312

   minus the robot position: (8.848 − 5.00, −1.312 − 3.00) = (3.848, −4.312)
```

`(3.848, −4.312)` instead of `(3.031, −0.902)` — off by 3.51 m, and note it fails the length check immediately: `√(3.848² + 4.312²) = 5.78`, not 3.162. It has moved the tag further away than it really is.

That 3.51 m is the same error as the wrong-order forward transform in Step 3, and for the same reason: in both cases the robot's own field position `(5.00, 3.00)` got rotated when it should not have. Getting either order backwards commits the identical sin — mixing a field-frame quantity into a rotation that belongs to the robot.

### Step 6: The rule for which direction takes −θ

You should not have to memorise which way the minus sign goes. Here is the rule that generates it.

**Every transform is written once, in one direction: the child frame's pose as seen from the parent.** The robot's pose `(5.00, 3.00, 35°)` is written in the field's terms; the camera's pose `(0.30, 0.10, 20°)` is written in the robot's terms. That direction — child to parent, robot to field — is the one you were given, so it is the one that uses the angle as written.

```
   Child → parent  (robot to field):   rotate by +θ,  then  ADD    the child's position
   Parent → child  (field to robot):   SUBTRACT the child's position,  then  rotate by −θ
```

Reversing direction does two things at once, and it always does both: the sign of θ flips, **and** the translation swaps sides of the rotation. If you find yourself changing only one of them, you have written one of the two bugs above.

One more distinction that saves real debugging time. Everything so far has been about **points** — physical spots on the carpet, which have a location. A **direction** — a velocity, a heading offset, the vector from the robot to a target — has no location, so translating it is meaningless. Directions rotate only. That is why Concept 02's field-oriented drive multiplied by `−heading` with no subtraction anywhere: a driver's stick command is a velocity, not a place. Ask "does this thing have a position, or only a direction?" before writing the transform, and the presence or absence of the translation answers itself.

And if what you actually want is the *angle* to steer toward that target rather than its coordinates — you need to turn `(3.031, −0.902)` back into an angle, which requires care about quadrants. That is `atan2`, and it is Concept 04.

---

## 3. Solving It in Code (Java & WPILib)

### First Principles (Java)

```java
// A rigid transform: rotate by theta, THEN translate by (tx, ty).
// Every frame change in this concept is one of these.
static double[] toParent(double a, double b, double tx, double ty, double theta) {
    double c = Math.cos(theta), s = Math.sin(theta);
    return new double[] { tx + (a * c - b * s),      // rotate first...
                          ty + (a * s + b * c) };    // ...then translate
}

// The inverse: SUBTRACT first, then un-rotate by -theta.
// Not "negate both parts" - reversing two steps also reverses their order.
static double[] toChild(double fx, double fy, double tx, double ty, double theta) {
    double c = Math.cos(theta), s = Math.sin(theta);
    double dx = fx - tx, dy = fy - ty;               // subtract first...
    return new double[] {  dx * c + dy * s,          // ...then rotate by -theta
                          -dx * s + dy * c };
}

double robotX = 5.00, robotY = 3.00;
double heading = Math.toRadians(35.0);               // from the gyro

// Camera mounted 0.30 m forward, 0.10 m left, yawed 20 deg left.
double camX = 0.30, camY = 0.10;
double camYaw = Math.toRadians(20.0);

// The camera reports the piece 1.5 m ahead of itself, 0.4 m to its right.
double[] inRobot = toParent(1.5, -0.4, camX, camY, camYaw);
// inRobot = { 1.8463, 0.2372 }

double[] inField = toParent(inRobot[0], inRobot[1], robotX, robotY, heading);
// inField = { 6.376, 4.253 }

// Backwards: a tag at field (8.00, 4.00), seen from the robot.
double[] tagInRobot = toChild(8.00, 4.00, robotX, robotY, heading);
// tagInRobot = { 3.031, -0.902 }  ->  3.03 m ahead, 0.90 m to the right

// The check that catches sign errors for free: a frame change
// cannot alter a distance.
double before = Math.hypot(8.00 - robotX, 4.00 - robotY);   // 3.162
double after  = Math.hypot(tagInRobot[0], tagInRobot[1]);   // 3.162
```

The two wrong versions, for the record — neither throws, and both are correct at heading 0:

```java
// BUG 1: translate before rotating. Spins the robot's own field
// position about the corner of the carpet.
double c = Math.cos(heading), s = Math.sin(heading);
double bx = (robotX + 1.5), by = (robotY - 0.4);
double[] wrong1 = { bx * c - by * s, bx * s + by * c };   // { 3.833, 5.858 }

// BUG 2: un-rotate before subtracting, going the other way.
double[] wrong2 = { 8.00 * c + 4.00 * s - robotX,
                   -8.00 * s + 4.00 * c - robotY };      // { 3.848, -4.312 }
```

### In a Robot Project (Java & WPILib)

```java
import edu.wpi.first.math.geometry.Pose2d;
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.math.geometry.Transform2d;
import edu.wpi.first.math.geometry.Translation2d;

Pose2d robotPose = new Pose2d(5.00, 3.00, Rotation2d.fromDegrees(35.0));

// A Transform2d is exactly the (x, y, theta) triple from the Math! sidebar:
// a child frame's pose expressed in its parent's terms.
Transform2d robotToCamera = new Transform2d(new Translation2d(0.30, 0.10),
                                            Rotation2d.fromDegrees(20.0));
Transform2d cameraToPiece = new Transform2d(new Translation2d(1.5, -0.4),
                                            new Rotation2d());

// Pose2d.plus(Transform2d) IS rotate-then-translate. It rotates the
// transform's translation by the pose's heading, adds it to the pose's
// position, and adds the two headings. Step 2 and Step 4, in one call.
Pose2d cameraPose = robotPose.plus(robotToCamera);   // (5.188, 3.254, 55.0 deg)
Pose2d piecePose  = cameraPose.plus(cameraToPiece);  // (6.376, 4.253, 55.0 deg)

// Composition: chaining two transforms first gives the same answer.
Pose2d sameAnswer = robotPose.plus(robotToCamera.plus(cameraToPiece));

// Just the translation part, when the target has no meaningful heading:
Translation2d local = new Translation2d(1.5, -0.4);
Translation2d onField = robotPose.getTranslation()
                                 .plus(local.rotateBy(robotPose.getRotation()));
// (6.458, 3.533) - the Step 2 answer, with the camera mount ignored.

// The inverse. relativeTo does subtract-then-un-rotate, not negate-both.
Pose2d tagPose = new Pose2d(8.00, 4.00, new Rotation2d());
Pose2d tagFromRobot = tagPose.relativeTo(robotPose);   // (3.031, -0.902, -35 deg)
```

Every number here matches the from-scratch tier digit for digit: `(1.8463, 0.2372)` in the robot frame, `(6.376, 4.253)` on the field, `(3.031, −0.902)` coming back. `Pose2d.plus(Transform2d)` is not a different rule from Step 2 — it *is* Step 2, and `relativeTo` is Step 5. Note also that `Translation2d.rotateBy` only rotates, with no translation anywhere: a `Translation2d` used as an offset is a direction, and directions do not translate.

Two practical notes. `Pose2d.plus` takes a `Transform2d`, never another `Pose2d` — the type system is enforcing the frame-label discipline from the Math! sidebar, refusing to let you add two poses that both live in the field frame. And `Rotation2d` stores `cos θ` and `sin θ` rather than θ, so every one of these calls is multiplication and addition only, with no trigonometry inside the 20 ms loop.

---

## 4. Bridge to Real Systems

### Robotics: AprilTag pose estimation, running the chain in reverse

A vision coprocessor running PhotonVision or a Limelight does not see a robot pose. It sees a tag in an image and solves for **camera ← tag**: the tag's position and orientation relative to the lens. Turning that into "where is my robot on the field" is this concept's chain, inverted end to end.

The field layout file (`AprilTagFieldLayout`, published with the game manual) gives **field ← tag** for every tag: tag 7 is at a surveyed spot, facing a surveyed direction. The vision solve gives **camera ← tag**, which must be inverted to **tag ← camera**. The mounting measurements give **robot ← camera**, which is inverted to **camera ← robot**. Line the labels up:

```
   (field ← tag) ∘ (tag ← camera) ∘ (camera ← robot)  =  (field ← robot)
```

Every inner pair cancels, and out drops the robot's field pose — which is fed to `SwerveDrivePoseEstimator.addVisionMeasurement`, where it is blended with wheel odometry. That estimator is why a robot can drive a scripted path for fifteen seconds without accumulating enough wheel slip to miss a scoring location.

Two things go wrong in exactly the ways derived above. A camera mount measured to the wrong sign — 0.10 m left recorded as 0.10 m right — produces a pose error that is zero when the robot faces down-field and grows with heading, the Step 3 signature. And a team that inverts a transform by negating both parts gets a pose estimate that is correct at the field origin and wrong everywhere else, which is the Step 5 signature. Both survive a shop test on a stationary robot.

### Machine learning: bird's-eye-view perception in autonomous driving

The same chain is the backbone of modern camera-only driving stacks. A car with six surround cameras produces six image-plane detections per frame, each in the frame of the lens that saw it, none of them comparable to any other. Before a planner can reason about anything, all six must be expressed in one frame.

Datasets encode this literally. In nuScenes, every sensor sample carries a `calibrated_sensor` record — the fixed sensor-to-ego transform, a mounting pose exactly like our `robotToCamera` — and an `ego_pose` record giving ego-to-global at that instant, exactly like our `robotPose`. Detections are annotated in global coordinates, and every training and evaluation script composes the two to move between them.

Architectures like Lift-Splat-Shoot and BEVFormer make the transform part of the network. Each camera's image features are lifted into 3D, transformed into the shared ego frame using that camera's known extrinsic pose, and splatted onto a single bird's-eye-view grid on which the detection head then runs. The consequence is worth stating plainly: the network never has to learn where the cameras are bolted. Mounting geometry is supplied as an exact transform, so the learned weights spend their capacity on recognising vehicles instead of on memorising a rig.

The inverse direction does real work too. Temporal fusion — using the last few frames to stabilise a detection, or to estimate how fast another car is moving — needs the previous timestep's BEV grid expressed in the *current* ego frame. The car has moved and turned in between, so this is subtract-then-un-rotate on every cell of the grid, our Step 5 applied at scale. And the failure mode is the familiar one: a stale extrinsic calibration, or an ego pose off by a degree of yaw, and detections land metres from the vehicles they describe. Calibration drift is a routine maintenance item on these fleets for precisely this reason.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1

A robot sits at field `(2.00, 6.00)` with heading 120°. A rear distance sensor reports a wall 0.8 m directly behind the robot — robot-frame coordinates `(−0.8, 0.0)`. Where is that wall on the field? How far is the naive-addition answer from the truth, and why is that distance what it is?

**Solution:**

1. **The transform.** Rotate the local offset by 120°, then translate. `cos 120° = −0.5`, `sin 120° = 0.86603`.
2. **Rotate.** `x = (−0.8)(−0.5) − (0.0)(0.86603) = 0.400`, and `y = (−0.8)(0.86603) + (0.0)(−0.5) = −0.693`.
3. **Translate.** `(2.00 + 0.400, 6.00 − 0.693) = (2.400, 5.307)`.
4. **Check the length.** `√(0.400² + 0.693²) = √(0.160 + 0.480) = √0.640 = 0.800`, matching the sensor reading. The rotation did not stretch anything.
5. **Naive addition** gives `(2.00 − 0.8, 6.00 + 0.0) = (1.200, 6.000)`, which is `√((2.400 − 1.200)² + (5.307 − 6.000)²) = √(1.440 + 0.480) = √1.920 = 1.386` m away.
6. **Why that distance.** Both answers are 0.8 m from the robot — one along field −X, one along the robot's actual backward direction, and those two directions differ by exactly 120°. The gap between them is the chord of a 120° arc on a circle of radius 0.8, and a robot sent to the wrong wall position would be over a metre out on an obstacle only 0.8 m away.

---

### Checkpoint 2

A robot is at field `(3.00, 1.00)` with heading `−40°` — turned 40° clockwise, to its own right. A tag sits at field `(6.00, 1.00)`, straight down-field of the robot. Where is the tag in the robot frame? Then compute what "un-rotate first, subtract second" would have returned, and say how you would have caught it without knowing the right answer.

**Solution:**

1. **Subtract first.** `Δ = (6.00 − 3.00, 1.00 − 1.00) = (3.00, 0.00)`.
2. **Then un-rotate by −θ**, with `θ = −40°`, so `cos θ = 0.76604` and `sin θ = −0.64279`.
3. `a = 3.00(0.76604) + 0.00(−0.64279) = 2.298` and `b = −3.00(−0.64279) + 0.00(0.76604) = 1.928`.
4. **Result:** `(2.298, 1.928)` — 2.30 m ahead of the robot, 1.93 m to its **left**. That is the right sense: the robot is turned to its right, so something straight down-field appears off to its left.
5. **The wrong order.** Un-rotating `(6.00, 1.00)` gives `x = 6.00(0.76604) + 1.00(−0.64279) = 3.953` and `y = −6.00(−0.64279) + 1.00(0.76604) = 4.623`. Subtracting the robot position leaves `(0.953, 3.623)`.
6. **Catching it.** The tag is `√(3² + 0²) = 3.000` m from the robot, and a frame change cannot alter a distance. The correct answer gives `√(2.298² + 1.928²) = √9.000 = 3.000`. The wrong one gives `√(0.953² + 3.623²) = 3.746`. One length check, no known answer needed, and it flags the bug at any heading except 0°.

---

### Deep Dive 1

A camera's own optical convention is not WPILib's. Computer-vision libraries conventionally put +Z out of the lens, +X to the image right and +Y *down* the image; WPILib's robot frame puts +x forward, +y left and +z up. Work out the relabelling that connects them, and confirm it is a pure axis permutation with sign flips rather than a rotation by any angle. Then argue why an axis-permutation mistake is so much harder to spot than a heading error: what does a swapped-sign Y axis do to a detection directly ahead, and what does it do to one off to the side? Finally, look at how `Transform3d` and `Rotation3d` let you write the mount once and stop thinking about it.

### Deep Dive 2

Two tags are visible at once, and inverting each chain independently gives two estimates of the robot's field pose that differ by 4 cm and 1.5°. Averaging the two translations is straightforward. Averaging the two *headings* is not — try it with headings of 179° and −179° and see what the arithmetic mean claims. Work out what has gone wrong, then design a fix using the fact that `Rotation2d` stores a `(cos, sin)` pair rather than an angle. Concept 05 attacks the underlying wraparound problem head-on, and Module 5 gives the principled way to weight two disagreeing measurements instead of averaging them blindly.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../02_concept_rotating_vectors/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 02: Rotating a Vector</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 2 Overview</a></div>
  <div><a href="../04_concept_atan2_heading/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 04: 4-Quadrant atan2 →</a></div>
</div>
