# Module 4: Computer Vision & Object Detection

Welcome to **Module 4: Computer Vision & Object Detection**. In this module, we bridge neural networks to raw camera streams—from 2D spatial convolution kernels that extract edges and textures to real-time object detection models like YOLO that output labeled bounding boxes for robot navigation.

---

## Concepts in this Module
* **[Concept 01: 2D Spatial Convolutions & Feature Maps](01_concept_spatial_convolutions/)**
  * *The Everyday Problem:* How does a robot camera extract vertical tape lines, circular targets, and game piece edges from raw RGB pixel grids?
  * *Code & Math:* 3×3 convolution kernels, element-wise sliding window products, Sobel edge filters, and feature maps.

* **[Concept 02: Object Detection, Anchor Boxes & IoU](02_concept_object_detection_iou/)**
  * *The Everyday Problem:* How does an autonomous vision model (like YOLO) draw bounding boxes around game pieces and filter out duplicate overlapping boxes?
  * *Code & Math:* Bounding box coordinates `[x, y, w, h]`, Intersection over Union (`IoU = Area_intersection / Area_union`), and Non-Maximum Suppression (NMS).

---

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--line, #232b3b);">
  <div><a href="../03_backpropagation/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">← Module 3: Backpropagation</a></div>
  <div><a href="../" style="color: var(--muted, #94a3b8); text-decoration: none;">ML Axon Home</a></div>
  <div><a href="01_concept_spatial_convolutions/" style="color: var(--accent, #38bdf8); text-decoration: none; font-weight: 600;">Concept 27: 2D Convolutions →</a></div>
</div>
