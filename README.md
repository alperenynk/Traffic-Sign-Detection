# Traffic Sign Detection with YOLOv8

Real-time detection of **18 traffic sign classes** (speed limits, turn/no-turn signs, stop, parking, traffic lights, and more) using a **YOLOv8s** model trained on a custom Roboflow dataset. Developed as a project for the **ISE 462 – Computer Vision** course.

The model reaches **mAP@0.5 = 0.919** and **mAP@0.5:0.95 = 0.856** on the validation set, with roughly **10 ms** inference per image on a Tesla T4 GPU, and works on images, video files, and a live webcam stream.

<p align="center">
  <img src="20220205045_Alperen_Yan%C4%B1k/runs/detect/predict2/30hiz2.jpg" width="32%" alt="Speed limit 30 detection">
  <img src="20220205045_Alperen_Yan%C4%B1k/runs/detect/predict2/dur1.jpg" width="32%" alt="Stop sign detection">
  <img src="20220205045_Alperen_Yan%C4%B1k/runs/detect/predict2/soladonulmez1.jpg" width="32%" alt="No left turn detection">
</p>

---

## Table of Contents

- [Features](#features)
- [Repository Structure](#repository-structure)
- [Detected Classes](#detected-classes)
- [Dataset](#dataset)
- [Training](#training)
- [Results](#results)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Retraining the Model](#retraining-the-model)
- [Limitations and Future Work](#limitations-and-future-work)
- [Tech Stack](#tech-stack)
- [References](#references)

---

## Features

- Detects 18 traffic sign / traffic light classes with bounding boxes and confidence scores
- Runs on single images, folders of images, video files, and a live camera feed
- Pre-trained weights (`best.pt`) included, so inference works out of the box
- Reproducible Google Colab notebook covering dataset download, training, and validation
- Sample images, test videos, and pre-generated prediction outputs included

## Repository Structure

```
Traffic-Sign-Detection/
├── .gitattributes
└── 20220205045_Alperen_Yanık/
    ├── ISE462_Computer_Vision.ipynb   # Colab notebook: dataset download, training, validation
    ├── test.py                        # Inference script (image / folder / video / webcam)
    ├── best.pt                        # Trained YOLOv8s weights (best epoch)
    ├── yolov8n.pt                     # Pre-trained YOLOv8 nano weights (not used by the notebook)
    ├── imgs/                          # Sample test images
    ├── videos/                        # Sample test videos (.mp4)
    ├── runs/detect/
    │   ├── predict/                   # Prediction results on videos (.avi)
    │   └── predict2/                  # Prediction results on images (.jpg)
    ├── ISE462 Computer Vision.docx    # Project report
    └── Açıklamalar.txt                # Short notes on the files (Turkish)
```

## Detected Classes

Class names in the model and dataset are in Turkish. English equivalents:

| ID | Model label | Meaning |
|----|-------------|---------|
| 0 | `20_hiz_limiti` | Speed limit 20 |
| 1 | `30_hiz_limiti` | Speed limit 30 |
| 2 | `30_hiz_limiti_sonu` | End of speed limit 30 |
| 3 | `dur` | Stop |
| 4 | `durak` | Bus stop |
| 5 | `girilmez` | No entry |
| 6 | `ileri_ve_saga` | Go straight or turn right |
| 7 | `ileri_ve_sola` | Go straight or turn left |
| 8 | `kapali_yol` | Road closed |
| 9 | `park_yasak` | No parking |
| 10 | `park_yeri` | Parking area |
| 11 | `saga_don` | Turn right |
| 12 | `saga_donulmez` | No right turn |
| 13 | `sola_don` | Turn left |
| 14 | `sola_donulmez` | No left turn |
| 15 | `trafik_isigi_kirmizi` | Traffic light: red |
| 16 | `trafik_isigi_sari` | Traffic light: yellow |
| 17 | `trafik_isigi_yesil` | Traffic light: green |

> The IDs above follow the order of the classes in the validation report. Check `data.yaml` in the downloaded dataset if you need the exact index mapping.

## Dataset

- **Source:** Roboflow Universe project `tabela_v1.2` (workspace `computer-vision-vjcku`), version 1, exported in **YOLOv8** format
- **Size:** 3,308 images in total (per the project report), with preprocessing of auto-orientation and resizing to 640 × 640
- **Splits used in training logs:** 2,313 training images and 666 validation images (754 labeled instances in the validation set)

The dataset is not stored in this repository. The notebook downloads it directly from Roboflow.

## Training

| Setting | Value |
|---------|-------|
| Framework | Ultralytics YOLOv8 (`ultralytics==8.0.196`) |
| Base weights | `yolov8s.pt` (COCO pre-trained, transfer learning) |
| Epochs | 50 |
| Image size | 640 |
| Batch size | 16 |
| Hardware | Google Colab, NVIDIA Tesla T4 |
| Training time | ≈ 0.87 hours |
| Model size | 168 layers (fused), 11.1 M parameters, 28.5 GFLOPs |

## Results

Validation results of `best.pt` (666 images, 754 instances):

| Metric | Value |
|--------|-------|
| Precision | 0.866 |
| Recall | 0.916 |
| mAP@0.5 | 0.919 |
| mAP@0.5:0.95 | 0.856 |
| Inference speed | ≈ 10 ms / image (Tesla T4) |

<details>
<summary><b>Per-class results</b></summary>

| Class | Instances | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|-------|----------:|----------:|-------:|--------:|-------------:|
| `20_hiz_limiti` | 34 | 0.985 | 1.000 | 0.995 | 0.988 |
| `30_hiz_limiti` | 29 | 0.983 | 1.000 | 0.995 | 0.985 |
| `30_hiz_limiti_sonu` | 38 | 0.962 | 1.000 | 0.995 | 0.982 |
| `dur` | 44 | 0.989 | 1.000 | 0.995 | 0.898 |
| `durak` | 40 | 0.987 | 0.975 | 0.982 | 0.957 |
| `girilmez` | 44 | 0.989 | 1.000 | 0.995 | 0.980 |
| `ileri_ve_saga` | 51 | 0.979 | 0.924 | 0.990 | 0.975 |
| `ileri_ve_sola` | 52 | 0.850 | 1.000 | 0.989 | 0.939 |
| `kapali_yol` | 35 | 0.986 | 1.000 | 0.995 | 0.967 |
| `park_yasak` | 40 | 0.999 | 1.000 | 0.995 | 0.917 |
| `park_yeri` | 47 | 0.989 | 1.000 | 0.995 | 0.950 |
| `saga_don` | 66 | 0.850 | 0.894 | 0.949 | 0.932 |
| `saga_donulmez` | 51 | 0.825 | 0.926 | 0.945 | 0.928 |
| `sola_don` | 55 | 0.724 | 0.953 | 0.920 | 0.904 |
| `sola_donulmez` | 61 | 0.842 | 0.918 | 0.967 | 0.908 |
| `trafik_isigi_kirmizi` | 54 | 0.899 | 0.987 | 0.988 | 0.707 |
| `trafik_isigi_sari` | 1 | 0.000 | 0.000 | 0.000 | 0.000 |
| `trafik_isigi_yesil` | 12 | 0.752 | 0.917 | 0.858 | 0.489 |

</details>

Speed limit signs, no entry, stop, and parking signs are detected almost perfectly. Directional signs (turn / no turn) show slightly lower precision, and traffic lights are the weakest group, mainly because of very few examples (see [Limitations](#limitations-and-future-work)).

Qualitative results are available in `runs/detect/predict2/` (images) and `runs/detect/predict/` (videos).

## Getting Started

### Prerequisites

- Python 3.9 or newer (the project was developed with Python 3.12 locally and Python 3.10 on Colab)
- A CUDA-capable GPU is recommended for training; inference also runs on CPU
- A webcam (optional, for live detection)

### Installation

```bash
git clone https://github.com/alperenynk/Traffic-Sign-Detection.git
cd Traffic-Sign-Detection/20220205045_Alperen_Yanık

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install ultralytics==8.0.196
```

## Usage

The trained weights (`best.pt`) are already in the project folder. The examples below use the Ultralytics Python API, the same approach as `test.py`.

### Detect on a single image

```python
from ultralytics import YOLO

model = YOLO("best.pt")
model.predict(source="imgs/30hiz1.jpg", save=True)
```

### Detect on a video

```python
model.predict(source="videos/dur.mp4", save=True)
```

### Live webcam

```python
model.predict(source="0", show=True)
```

### Process all images or videos in a folder

```python
import os
from ultralytics import YOLO

model = YOLO("best.pt")

for folder, exts in [("imgs", (".jpg", ".jpeg", ".png")),
                     ("videos", (".mp4", ".avi", ".mov"))]:
    for name in os.listdir(folder):
        if name.lower().endswith(exts):
            path = os.path.join(folder, name)
            print(f"Processing {path}...")
            model.predict(source=path, save=True)
```

Outputs are saved under `runs/detect/predict*/`.

### Command line alternative

```bash
yolo task=detect mode=predict model=best.pt source=imgs/30hiz1.jpg save=True
```

> **Note:** the commented-out loops in `test.py` contain absolute Windows paths (`C:/Users/...`). Replace them with relative paths such as `imgs` and `videos` before running.

## Retraining the Model

The full pipeline is in `ISE462_Computer_Vision.ipynb` and is designed for **Google Colab**:

1. Open the notebook in Colab and set **Runtime → Change runtime type → T4 GPU**.
2. Install Ultralytics (`pip install ultralytics==8.0.196`).
3. Download the dataset from Roboflow. Replace the API key in the notebook with **your own** key, or load it from an environment variable or Colab secret.
4. Train:
   ```bash
   yolo task=detect mode=train model=yolov8s.pt data=<dataset>/data.yaml epochs=50 imgsz=640 plots=True
   ```
5. Validate:
   ```bash
   yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=<dataset>/data.yaml
   ```
6. Download `runs/detect/train/weights/best.pt` and place it next to `test.py`.

To use your own dataset, export it from Roboflow (or any tool) in YOLOv8 format and point `data=` to its `data.yaml`. Adjust `imgsz` to match the dataset preprocessing.

## Limitations and Future Work

- **Rare classes:** the yellow traffic light has only one validation instance and is not detected (mAP 0). The green light (12 instances) also scores noticeably lower. More examples of these classes are needed.
- **Localization quality of traffic lights:** red and green lights have good mAP@0.5 but lower mAP@0.5:0.95, which suggests less precise boxes on small objects.
- **Directional signs:** precision for `sola_don`, `saga_donulmez`, and `sola_donulmez` is lower than for other classes, likely due to visual similarity between mirrored signs.
- **Evaluation scope:** quantitative results come from a single validation split. Video results are qualitative only.
- **Future work:** more data for rare classes, testing in adverse weather and night conditions, more sign categories, and deployment on edge devices (the lighter `yolov8n` model is a natural candidate).

## Tech Stack

- Python, Ultralytics YOLOv8 (PyTorch)
- Roboflow (dataset management and export)
- Google Colab (training)
- OpenCV (via Ultralytics, for image and video I/O)

## References

1. J. Redmon, S. Divvala, R. Girshick, A. Farhadi, "You Only Look Once: Unified, Real-Time Object Detection," *CVPR*, 2016, pp. 779–788.
2. A. Bochkovskiy, C.-Y. Wang, H.-Y. M. Liao, "YOLOv4: Optimal Speed and Accuracy of Object Detection," arXiv:2004.10934, 2020.
3. Ultralytics YOLOv8 documentation: <https://docs.ultralytics.com>

## Author

**Alperen Yanık** — [@alperenynk](https://github.com/alperenynk)
