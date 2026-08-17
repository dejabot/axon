# Concept 01: Measuring Errors with Loss Functions (MSE & MAE)

> **▶ Interactive Demo: [Loss Landscape & Residual Visualizer](demo.html)**
>
> Drag the prediction line and drag individual data points. Watch the residuals, MSE, MAE and RMSE respond — and watch what happens to each when you drag one point far away.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 16px 0; background: var(--panel, #141923);" title="Loss Functions Interactive Visualizer"></iframe>

---

## 1. The Real-World Problem: Is the Shooter Getting Better?

You are calibrating a shooter flywheel. The model takes a distance to the goal and predicts the RPM needed; you fire test shots and record where the game piece actually lands. Five shots produce five results:

```
   target (m)   landed (m)   residual
      2.0          2.2         +0.2
      3.0          2.9         −0.1
      4.0          5.0         +1.0
      5.0          4.8         −0.2
      6.0          6.1         +0.1
```

Now you change a constant in the model and fire five more shots. Did it improve?

You cannot answer that by staring at ten numbers, and you certainly cannot automate it. To tune anything — by hand or by gradient descent — you need to collapse all of the misses into **one number** that goes down when the model gets better. That number is the **loss**.

Choosing how to collapse them is not a detail. Two reasonable choices, both used constantly in practice, disagree about which of two models is better, disagree about what a "typical" shot looks like, and behave completely differently when one sensor reading is garbage.

---

## 2. Building the Math

### Step 1: The residual, and why you cannot just add them up

For each shot `i`, the **residual** is the signed difference between what the model predicted and what actually happened:

$$
\text{residual} = \text{prediction} - \text{actual}
$$

Signed, so it carries direction: positive means the shot went long, negative means short. That sign is genuinely useful information — it tells you which way to adjust.

But it makes the residual useless as a score. Add up the five residuals above:

$$
+0.2 - 0.1 + 1.0 - 0.2 + 0.1 = +1.0
$$

Now imagine a much worse model that misses by `+5.0` on one shot and `−5.0` on another. Its residuals sum to `0.0` — a perfect score, from a model that missed by five meters twice. Positive and negative errors cancel, and cancelation is exactly what a score must not do.

The fix is to strip the sign before summing. There are two natural ways to strip a sign, and they lead to the two loss functions in this concept's title.

### Step 2: Two ways to discard a sign

**Take the absolute value.** Average those, and you get **Mean Absolute Error**:

$$
\text{MAE} = \frac{1}{N} \cdot \sum_i \left| \hat{y}_i - y_i \right|
$$

**Square it.** Squaring also kills the sign, since a negative times a negative is positive. Average those and you get **Mean Squared Error**:

$$
\text{MSE} = \frac{1}{N} \cdot \sum_i (\hat{y}_i - y_i)^2
$$

> ### Math!
> Read `MSE = (1/N) · Σ (ŷᵢ − yᵢ)²` out loud as **"M-S-E equals one over N, times the sum over i of y-hat-sub-i minus y-sub-i, all squared."**
>
> * `yᵢ` — "y sub i" — the true value for sample `i`.
> * `ŷᵢ` — "y **hat** sub i" — the model's prediction. The hat is the near-universal convention for "estimated", and you will meet it everywhere in statistics and machine learning.
> * `Σ` — capital sigma — "the sum of". The `i` underneath counts through the samples.
> * `N` — how many samples. Dividing by it turns a total into an average, so the loss does not grow simply because you collected more data.

For our five shots: `MAE = (0.2 + 0.1 + 1.0 + 0.2 + 0.1)/5 = 0.32` meters, while `MSE = (0.04 + 0.01 + 1.00 + 0.04 + 0.01)/5 = 0.22`.

Two different numbers for the same five shots. Neither is wrong. They are answering different questions.

### Step 3: The units are not the same, and RMSE fixes it

Look closely at that MSE of `0.22`. Point two two of *what*?

The residuals were in meters. Squaring them produced meters squared, and averaging kept it that way. So MSE is `0.22 m²` — an area, for a quantity that is a length. That makes it impossible to interpret directly: is `0.22 m²` a good shooter? You cannot tell without converting.

Taking the square root at the end restores the units and gives **Root Mean Squared Error**:

$$
\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{0.22} \approx 0.47 \text{ meters}
$$

That is a number you can reason about — this shooter is typically off by about half a meter. Note it is meaningfully larger than the MAE of `0.32 m` computed from the identical data. RMSE always comes out at least as large as MAE, and the gap between them widens as your errors become more uneven. Two models with identical MAE but different RMSE differ in *consistency*: the one with higher RMSE is the streakier shooter.

### Step 4: The deep difference — what each loss thinks "typical" means

Here is the result that explains everything else, and it is worth deriving.

Forget the model for a moment. Suppose you must summarize a set of numbers with a single constant `c`, chosen to make the loss as small as possible. Which `c` wins?

**For MSE**, we want to minimize `Σ (c − xᵢ)²`. A function is at its minimum where its derivative is zero, so differentiate with respect to `c`:

$$
\frac{d}{dc} \sum_i (c - x_i)^2 = \sum_i 2(c - x_i) = 0
$$

Divide by 2 and split the sum:

$$
Nc - \sum_i x_i = 0 \qquad \text{which gives} \qquad c = \frac{1}{N} \sum_i x_i
$$

The best constant under MSE is **the mean**.

**For MAE**, we want to minimize `Σ |c − xᵢ|`. The derivative of `|c − xᵢ|` is `+1` when `c` is above `xᵢ` and `−1` when it is below. Setting the sum to zero:

$$
(\text{count of points below } c) - (\text{count of points above } c) = 0
$$

The best constant under MAE is whatever value splits the data in half — **the median**.

That single distinction drives every practical difference between them. MSE chases the mean, and a mean can be dragged anywhere by one extreme value. MAE chases the median, and a median barely notices extreme values at all.

### Step 5: What one bad reading does

Make it concrete. Suppose one of the five shots was recorded during a sensor glitch and reads as a 10 meter miss instead of a 0.1 meter miss.

```
   residuals:  0.2,  −0.1,  1.0,  −0.2,  10.0

   MAE  = (0.2 + 0.1 + 1.0 + 0.2 + 10.0)/5  =  2.30 m      (was 0.32)
   MSE  = (0.04 + 0.01 + 1.0 + 0.04 + 100.0)/5 = 20.22 m²  (was 0.22)
```

MAE grew about sevenfold. MSE grew ninety-fold, and that single bad point now supplies `100.0` of the `101.09` total — **99 percent of the loss comes from one glitched reading**. Any optimizer minimizing MSE will contort the entire model to accommodate a measurement that never happened.

This is the real trade-off. MSE's quadratic penalty is a feature when large errors genuinely are disproportionately bad — being off by 2 meters is usually far worse than twice as bad as being off by 1 meter. It is a liability the moment your data contains outliers, and sensor data always contains outliers.

### Step 6: Why deep learning still prefers MSE

If MAE is robust, why is MSE the default across most of machine learning? Because of what happens to the **gradient**, which is the quantity gradient descent actually consumes.

Differentiate each loss with respect to a single prediction `ŷ`:

$$
\begin{aligned}
\frac{d}{d\hat{y}} (\hat{y} - y)^2 &= 2(\hat{y} - y) && \text{proportional to the error} \\[4pt]
\frac{d}{d\hat{y}} \left| \hat{y} - y \right| &= \operatorname{sign}(\hat{y} - y) && \text{always exactly } +1 \text{ or } -1
\end{aligned}
$$

Two consequences follow.

**MSE's gradient scales with the error.** Badly wrong predictions produce large gradients and get corrected aggressively; nearly-right predictions produce small gradients and get nudged gently. The step size anneals itself automatically as training converges.

**MAE's gradient never changes size.** Whether you are off by 10 meters or 0.001 meters, the gradient is `±1`. Far from the answer it is slow; close to the answer it keeps taking the same-sized step and oscillates around the minimum instead of settling.

Worse, MAE has a **kink** at zero — the derivative jumps from `−1` to `+1` with nothing defined in between. `|x|` is not differentiable at `x = 0`, exactly where a converging model spends all its time.

> ### Math!
> A function with no sudden jumps in its derivative is called **smooth**, or `C¹` — read "C-one", meaning its first derivative exists and is itself continuous. MSE is smooth everywhere. MAE is continuous but not smooth, and that single kink at the origin is why optimizers built on derivatives find it awkward.

### Step 7: Huber loss — taking both

You do not have to choose. **Huber loss** is quadratic for small errors and linear for large ones, switching over at a threshold `δ`:

$$
\begin{aligned}
L(e) &= \tfrac{1}{2} e^2 && \text{when } |e| \leq \delta \\[4pt]
L(e) &= \delta \left( |e| - \tfrac{1}{2}\delta \right) && \text{when } |e| > \delta
\end{aligned}
$$

Near zero it is MSE, so it keeps the well-behaved shrinking gradient where convergence happens. Beyond `δ` it is MAE, so one glitched reading contributes proportionally rather than quadratically.

The second branch's odd-looking `−½δ` is not arbitrary — it is exactly the constant that makes the two pieces meet. At `e = δ` the first branch gives `½δ²`, and the second gives `δ(δ − ½δ) = ½δ²`. They agree, so the function has no step. Differentiate each branch and you find the slopes agree too, both equal to `δ` at the switchover. Huber is smooth at the seam, which is the whole point of constructing it this way.

Choosing `δ` means declaring how large an error has to be before you stop believing it. Set it to roughly the size of your genuine measurement noise, and readings beyond that get treated as suspect.

---

## 3. Solving It in Code (Python & PyTorch)

### From-Scratch Python

No libraries, no vectorization — just the arithmetic, so nothing is hidden.

```python
def mean_squared_error(predictions, actuals):
    """Average of squared residuals. Units are the square of the input's units."""
    total = 0.0
    for prediction, actual in zip(predictions, actuals):
        residual = prediction - actual
        total += residual * residual
    return total / len(actuals)


def mean_absolute_error(predictions, actuals):
    """Average of absolute residuals. Same units as the input."""
    total = 0.0
    for prediction, actual in zip(predictions, actuals):
        total += abs(prediction - actual)
    return total / len(actuals)


def huber(predictions, actuals, delta=1.0):
    """Quadratic within delta of zero, linear beyond it."""
    total = 0.0
    for prediction, actual in zip(predictions, actuals):
        residual = abs(prediction - actual)
        if residual <= delta:
            total += 0.5 * residual ** 2
        else:
            total += delta * (residual - 0.5 * delta)
    return total / len(actuals)


actuals     = [2.0, 3.0, 4.0, 5.0, 6.0]
predictions = [2.2, 2.9, 5.0, 4.8, 6.1]

mse = mean_squared_error(predictions, actuals)
print(f"MSE   {mse:.4f} m^2")          # MSE   0.2200 m^2
print(f"RMSE  {mse ** 0.5:.4f} m")     # RMSE  0.4690 m
print(f"MAE   {mean_absolute_error(predictions, actuals):.4f} m")   # MAE   0.3200 m
print(f"Huber {huber(predictions, actuals):.4f}")                   # Huber 0.1100
```

Now corrupt one reading and watch the two losses disagree about how bad things are:

```python
glitched = [2.2, 2.9, 5.0, 4.8, 16.0]     # last shot misread by 10 m

print(mean_absolute_error(glitched, actuals))   # 2.30  — grew about 7x
print(mean_squared_error(glitched, actuals))    # 20.22 — grew about 92x
print(huber(glitched, actuals))                 # 2.02  — barely flinched
```

### Production PyTorch

Every loss above ships in PyTorch. The point of this tier is that it computes **the same numbers** — verify that, and you know the library is doing what you just wrote by hand.

```python
import torch
import torch.nn as nn

actuals     = torch.tensor([2.0, 3.0, 4.0, 5.0, 6.0])
predictions = torch.tensor([2.2, 2.9, 5.0, 4.8, 6.1])

print(nn.MSELoss()(predictions, actuals).item())        # 0.2200  matches
print(nn.L1Loss()(predictions, actuals).item())         # 0.3200  matches
print(nn.HuberLoss(delta=1.0)(predictions, actuals).item())   # 0.1100  matches
```

`L1Loss` is PyTorch's name for MAE — L1 being the norm from the geometry axon, the one that sums absolute values. `MSELoss` is correspondingly the squared L2 norm.

What PyTorch adds is the derivative. Ask for the gradient and it hands back exactly the `2(ŷ − y)/N` from Step 6, without you deriving it:

```python
predictions = torch.tensor([2.2, 2.9, 5.0], requires_grad=True)
actuals     = torch.tensor([2.0, 3.0, 4.0])

loss = nn.MSELoss()(predictions, actuals)
loss.backward()

print(predictions.grad)      # tensor([0.1333, -0.0667, 0.6667])
# Check by hand: 2 * (5.0 - 4.0) / 3 = 0.6667 for the third element.
```

Note that the third prediction — the one meter miss — carries by far the largest gradient. That is Step 6's "badly wrong predictions get corrected aggressively", visible as a number. The machinery that produced `.grad` automatically is **autograd**, and Module 3 of this axon builds one from scratch.

---

## 4. Bridge to Machine Learning & Modern Autonomy

The loss function is the single most consequential design choice in a machine learning system, because it is the only thing the optimizer is told to care about. Everything the model learns is downstream of it.

In **object detection**, the models from this axon's vision module do not use plain MSE on box coordinates — they use **Smooth L1**, which is Huber under a different name. The reason is exactly Step 5: training images contain badly mislabeled boxes, and squaring their errors would let a handful of bad annotations dominate. Fast R-CNN introduced it for precisely this argument, and it remains standard.

In **large language models**, the loss is cross-entropy rather than MSE, because predicting the next token is a classification problem rather than a regression one — that is the subject of Concept 02. But the structural role is identical: one number, differentiable, that the optimizer drives downward.

The choice also encodes a value judgement about failure. A robot whose shooter model is fitted with MSE will sacrifice several close shots to avoid one catastrophic miss, because that miss is penalized quadratically. Fitted with MAE, it will accept an occasional wild miss to make the typical shot slightly better. Neither is objectively right — it depends on whether one badly missed shot costs you the match. **The loss function is where you write down what "bad" means**, and the optimizer will take you at your word with no judgement of its own.

That is not confined to shooters. When the physics axon fits the feedforward constants `kS`, `kV` and `kA` from sensor telemetry, it is minimizing a loss over recorded data — and telemetry logs are full of CAN dropouts and encoder glitches. Fitting those with MSE lets a handful of dropped frames pull your velocity constant off; fitting them with Huber does not.

---

## 5. Checkpoints & Exploration Prompts

### Checkpoint 1
A model produces residuals of `[1.0, −1.0, 1.0, −1.0]`. Compute the mean residual, the MAE, the MSE and the RMSE. Explain what the mean residual tells you that the others do not, and vice versa.

**Solution:**
1. Mean residual: `(1.0 − 1.0 + 1.0 − 1.0)/4 = 0.0`.
2. MAE: `(1 + 1 + 1 + 1)/4 = 1.0`.
3. MSE: `(1 + 1 + 1 + 1)/4 = 1.0 m²`. RMSE: `√1.0 = 1.0 m`.

The mean residual of `0.0` says the model is **unbiased** — it overshoots as often and as far as it undershoots, so there is no systematic offset to correct. That is real information the loss functions destroy by design. But taken alone it is dangerously misleading: this model misses by a full meter on every single shot. MAE and RMSE both report `1.0`, correctly describing a model that is consistently wrong. You want both diagnostics: bias tells you whether to shift the model, loss tells you whether it is any good.

---

### Checkpoint 2
Two shooter models are evaluated on the same 100 shots. Model A has `MAE = 0.30 m` and `RMSE = 0.35 m`. Model B has `MAE = 0.30 m` and `RMSE = 0.90 m`. Which would you put on the robot, and what does the difference tell you?

**Solution:**
Model A. Both miss by 0.30 m on a typical shot, so by MAE they are indistinguishable. The gap between MAE and RMSE is the tell: RMSE punishes uneven errors, so a large gap means the errors are lopsided — a few very large misses among many small ones.

For Model A the two numbers are close, so its misses are consistently around 0.3 m. For Model B, RMSE is triple its MAE, which means most shots are considerably better than 0.30 m while a handful are severely off. Model B is a streaky shooter that occasionally misses wildly.

Which you prefer genuinely depends on the game. If a wild miss merely costs you a cycle, Model B's better typical shot might win. If a wild miss risks a penalty or a lost game piece, take Model A. The point is that **no single loss number could have told you this** — you needed two, and their disagreement was the signal.

---

### Deep Dive 1
Step 4 proved MSE is minimized by the mean and MAE by the median. Investigate what loss is minimized by the **mode**, and then look up **quantile loss** — an asymmetric variant that penalizes overshoot and undershoot by different amounts. Then apply it: for a shooter where going long bounces off the field wall and scores nothing, but going short still has a chance of scoring, sketch the quantile loss you would use and argue which side should carry the heavier penalty.

### Deep Dive 2
Step 7 chose `δ` in Huber loss by appealing to "the size of your genuine measurement noise". Make that rigorous. Take a real or simulated set of shooter residuals, plot their distribution, and experiment with values of `δ` at various multiples of the spread. Observe how the fitted model moves as `δ` grows toward infinity (where Huber becomes MSE) and shrinks toward zero (where it becomes MAE, scaled). Then research **Tukey's biweight loss**, which goes further and gives sufficiently large errors a gradient of exactly zero — and consider the risk that creates if the model starts out badly initialized.

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 1: Loss & Optimization</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">ML Axon Home</a></div>
  <div><a href="../02_concept_cross_entropy_loss/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 02: Cross-Entropy Loss →</a></div>
</div>
