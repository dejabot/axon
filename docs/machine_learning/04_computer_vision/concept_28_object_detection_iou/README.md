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

## 2. Python Implementation: IoU & NMS

Here is how IoU and Non-Maximum Suppression are computed in pure Python:

```python
def compute_iou(boxA, boxB):
    # box format: [x1, y1, x2, y2]
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # Compute area of intersection
    inter_area = max(0, xB - xA) * max(0, yB - yA)

    # Compute area of both boxes
    boxA_area = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxB_area = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    # IoU = Intersection / Union
    union_area = boxA_area + boxB_area - inter_area
    return inter_area / union_area if union_area > 0 else 0.0

def non_max_suppression(boxes_with_conf, iou_threshold=0.45):
    # Sort boxes by confidence score descending
    sorted_boxes = sorted(boxes_with_conf, key=lambda b: b['conf'], reverse=True)
    kept_boxes = []

    while sorted_boxes:
        best_box = sorted_boxes.pop(0)
        kept_boxes.append(best_box)

        # Eliminate any remaining box with high overlap (IoU > threshold)
        sorted_boxes = [
            b for b in sorted_boxes
            if compute_iou(best_box['coords'], b['coords']) < iou_threshold
        ]

    return kept_boxes
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
