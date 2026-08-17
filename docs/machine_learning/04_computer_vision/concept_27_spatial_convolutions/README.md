# Concept 27: 2D Spatial Convolutions & Feature Maps

A standard 1080p robot camera captures over 2 million pixels every frame. If we connected every pixel directly to a dense linear layer, our model would require hundreds of millions of weights and fail whenever a game piece moved 2 pixels to the side.

To detect visual patterns efficiently, computer vision models use **2D Spatial Convolutions**.

> Open the interactive demo below to slide custom 3×3 convolution filters (Sobel Edge, Sharpen, Blur) across an image and watch feature maps extract boundaries in real time.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="2D Convolutions Interactive Visualizer"></iframe>

---

## The Everyday Robot Problem

How does an autonomous vision camera find the edges of a scoring reef target or the boundary of an orange game piece on the carpet?

Instead of looking at the whole image at once, the algorithm slides a tiny 3×3 grid of numbers (called a **Filter** or **Kernel**) across the image. At every pixel location, it multiplies matching pixels and adds them up:

```text
Output Pixel = ∑ (Image_Pixel · Kernel_Weight)
```

---

## 1. How a 3×3 Edge Filter Works

Consider a **Vertical Sobel Edge Filter**:

```text
Kernel K = [
  [-1,  0, +1],
  [-2,  0, +2],
  [-1,  0, +1]
]
```

What happens when this kernel slides over different regions of an image?

1. **Flat Uniform Floor (All pixels = 100):**
   * Left side: `(-1·100) + (-2·100) + (-1·100) = -400`
   * Center: `0`
   * Right side: `(+1·100) + (+2·100) + (+1·100) = +400`
   * Total sum: `-400 + 400 = 0.0` (Black pixel → No edge detected!).

2. **Vertical Boundary (Left pixels = 20, Right pixels = 200):**
   * Left side: `(-1·20) + (-2·20) + (-1·20) = -80`
   * Right side: `(+1·200) + (+2·200) + (+1·200) = +800`
   * Total sum: `-80 + 800 = +720` (Bright white pixel → Strong vertical edge detected!).

---

## 2. Solving It in Code (Java)

### First-Principles Java: 2D Spatial Convolution Window
```java
public class Convolution2D {
    public static double[][] conv2d(double[][] image, double[][] kernel) {
        int imgH = image.length;
        int imgW = image[0].length;
        int kH = kernel.length;
        int kW = kernel[0].length;

        int outH = imgH - kH + 1;
        int outW = imgW - kW + 1;
        double[][] featureMap = new double[outH][outW];

        for (int r = 0; r < outH; r++) {
            for (int c = 0; c < outW; c++) {
                double pixelSum = 0.0;
                for (int kr = 0; kr < kH; kr++) {
                    for (int kc = 0; kc < kW; kc++) {
                        pixelSum += image[r + kr][c + kc] * kernel[kr][kc];
                    }
                }
                featureMap[r][c] = pixelSum;
            }
        }
        return featureMap;
    }
}
```

---

## 3. Math! Translation Sidebar

In continuous mathematics and signal processing, 2D discrete convolution is denoted by the asterisk operator `*`:

```text
S(i, j) = (I * K)(i, j) = ∑_m ∑_n I(i - m, j - n) · K(m, n)
```

### How to Read This Out Loud:
* `(I * K)` ("I star K" or "I convolved with K"): The resulting **Feature Map** `S`.
* `I(i, j)`: The input image pixel value at row `i`, column `j`.
* `K(m, n)`: The kernel weight at filter coordinate `(m, n)`.

---

## 4. Bridge to Machine Learning & CNNs

* **Convolutional Neural Networks (CNNs):** In classical computer vision (OpenCV), humans hand-designed filters like Sobel. In deep learning (CNNs), the weights of the kernels are **learned automatically** via gradient descent and backpropagation!
* **Hierarchical Features:**
  * Layer 1 learns simple edges and color gradients.
  * Layer 2 combines edges into corners and circles.
  * Layer 3 combines shapes into full game pieces, AprilTags, and robots!

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 4: Computer Vision</a></div>
  <div><a href="../../" style="color: var(--muted, #94a3b8); text-decoration: none;">ML Axon Home</a></div>
  <div><a href="../concept_28_object_detection_iou/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 28: Object Detection & IoU →</a></div>
</div>
