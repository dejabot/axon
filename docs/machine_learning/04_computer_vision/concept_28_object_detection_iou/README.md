# Concept 28: Object Detection, Anchor Boxes & IoU

How does an autonomous robot detect, classify, and track field objects—like scoring game pieces, opposing robots, or human player stations—from a raw camera stream at 60 FPS?

Modern object detection models (like **YOLO**) solve this using **Bounding Boxes**, **Intersection over Union (IoU)**, and **Non-Maximum Suppression (NMS)**.

> Open the interactive demo below to adjust the confidence and NMS IoU overlap thresholds, and watch how duplicate bounding box detections are filtered into clean object targets.

<iframe src="demo.html" width="100%" height="600" style="border: 1px solid var(--line, #232b3b); border-radius: 12px; margin: 20px 0; background: var(--panel, #141923);" title="Object Detection & IoU Visualizer"></iframe>

---

## The Everyday Robot Problem

When a vision model (like YOLO) scans a camera frame, its grid cells predict thousands of potential bounding boxes across the field:

```python
# Predicted bounding box format: [center_x, center_y, width, height, confidence]
box1 = [320, 240, 80, 80, 0.95] # 95% confident it's a Note
box2 = [324, 238, 82, 78, 0.88] # 88% confident (same Note!)
box3 = [318, 242, 79, 81, 0.72] # 72% confident (same Note!)
```

Because adjacent grid cells all see the same orange game piece, the model outputs 3 overlapping boxes for a single physical object. 

To clean this up, we need two tools:
1. **Intersection over Union (IoU):** Measures how much two bounding boxes overlap.
2. **Non-Maximum Suppression (NMS):** Keeps the highest-confidence box and deletes duplicate overlapping boxes.

---

## 1. Intersection over Union (IoU)

IoU divides the area where two boxes overlap by the total combined area of both boxes:

```text
IoU = Area of Overlap / Area of Union
```

* **`IoU = 1.0`:** The two boxes match perfectly (100% overlap).
* **`IoU = 0.0`:** The two boxes do not touch at all (0% overlap).
* **`IoU > 0.5`:** Strong overlap—almost certainly detecting the exact same object.

---

## 2. Solving It in Code (Java)

### First-Principles Java: IoU & Non-Maximum Suppression (NMS)
```java
import java.util.*;

public class YoloNMS {
    public record Box(double x1, double y1, double x2, double y2, double conf, String label) {}

    public static double computeIoU(Box a, Box b) {
        double interX1 = Math.max(a.x1, b.x1);
        double interY1 = Math.max(a.y1, b.y1);
        double interX2 = Math.min(a.x2, b.x2);
        double interY2 = Math.min(a.y2, b.y2);

        double interArea = Math.max(0, interX2 - interX1) * Math.max(0, interY2 - interY1);
        double areaA = (a.x2 - a.x1) * (a.y2 - a.y1);
        double areaB = (b.x2 - b.x1) * (b.y2 - b.y1);

        double unionArea = areaA + areaB - interArea;
        return unionArea > 0 ? interArea / unionArea : 0.0;
    }

    public static List<Box> nonMaxSuppression(List<Box> boxes, double iouThreshold) {
        List<Box> sorted = new ArrayList<>(boxes);
        sorted.sort((a, b) -> Double.compare(b.conf, a.conf)); // Descending

        List<Box> kept = new ArrayList<>();
        while (!sorted.isEmpty()) {
            Box best = sorted.remove(0);
            kept.add(best);
            sorted.removeIf(other -> other.label.equals(best.label) && computeIoU(best, other) >= iouThreshold);
        }
        return kept;
    }
}
```

---

## 3. Math! Translation Sidebar

In set theory and geometry, IoU is known as the **Jaccard Index**:

```text
IoU(A, B) = |A ∩ B| / |A ∪ B| = |A ∩ B| / (|A| + |B| - |A ∩ B|)
```

### How to Read This Out Loud:
* `|A ∩ B|` ("size of A intersection B"): The shared overlapping pixel area between box `A` and box `B`.
* `|A ∪ B|` ("size of A union B"): The total combined pixel area covered by either box `A` or box `B`.

---

## 4. Bridge to Modern Robotics & YOLO

* **Real-Time Coprocessors:** Teams deploy compact YOLO models on onboard coprocessors (like an Orange Pi 5, Raspberry Pi 5, or Nvidia Jetson) running TensorRT or ONNX Runtime.
* **From 2D Bounding Box to 3D Field Coordinates:** Once NMS delivers a single clean bounding box `[x, y, w, h]`, the robot uses the camera's focal length and target height to calculate the exact 3D distance and bearing angle to intake the game piece!

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../concept_27_spatial_convolutions/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Concept 27: 2D Convolutions</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">Module 4 Overview</a></div>
  <div><a href="../../../large_language_models/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Next Axon: Large Language Models →</a></div>
</div>
