#  AI-Powered Intelligent Vehicle Detection & Assistance System

An advanced **Artificial Intelligence and Machine Learning (AIML)** based automotive project that integrates **Object Detection**, **Lane Tracking**, and **Emergency Vehicle Recognition** to improve driver safety and road awareness.  
Developed using **Python**, **YOLOv8**, and **OpenCV**, this system can detect real-time traffic scenes and provide intelligent alerts.

---

##  Overview

The **AI-Powered Intelligent Vehicle Detection & Assistance System** is designed to simulate an autonomous driving assistant that can:

- Detect vehicles, pedestrians, and traffic lights using AI models  
-  Identify lane boundaries using computer vision  
-  Recognize emergency vehicles (ambulances, police cars, fire trucks)  
-  Provide real-time alerts for driver assistance  

Future goals include **accident prediction**, **traffic violation detection**, and a **smart dashboard**.

---

##  Features

| Feature | Description |
|----------|-------------|
| **Object Detection** | Uses YOLOv8 to detect multiple objects (cars, bikes, pedestrians, signals). |
| **Lane Detection** | Detects and highlights lane markings in real-time. |
| **Emergency Vehicle Recognition** | Recognizes ambulances and fire trucks visually. |
| **Real-Time Alerts** | Displays emergency/lane warnings dynamically. |
| **Scalable Architecture** | Easily extendable with LSTM, RL, or dashboard modules. |

---

##  System Architecture

Camera Input
│
▼
+-------------------+
| YOLOv8 Object Det.|
+-------------------+
│
▼
+-------------------+
| Lane Detection |
| (OpenCV + Canny) |
+-------------------+
│
▼
+-------------------------------+
| Emergency Vehicle Detection |
+-------------------------------+
│
▼
+-------------------+
| Alert Visualization |
+-------------------+

yaml
Copy code

---

##  Tech Stack

| Category | Tools |
|-----------|-------|
| **Language** | Python 3.9+ |
| **Libraries** | PyTorch, OpenCV, Ultralytics YOLOv8, NumPy, Matplotlib |
| **Model** | YOLOv8 (pretrained) |
| **IDE** | VS Code / Jupyter Notebook |
| **Dataset** | BDD100K, COCO (for object detection) |

---

##  Folder Structure

Smart_Automotive_AI/
│
├── data/
│ ├── test_videos/
│ ├── images/
│ └── emergency_vehicle/
│
├── models/
│ ├── yolov8s.pt
│ └── emergency_vehicle.pt
│
├── scripts/
│ ├── object_detection.py
│ ├── lane_detection.py
│ ├── emergency_vehicle_detection.py
│ └── integrate_main.py
│
├── outputs/
│ ├── detected_frames/
│ └── logs/
│
├── requirements.txt
└── README.md

yaml
Copy code

---

##  Installation & Usage

### Step 1: Clone this repository
```bash
git clone https://github.com/<your-username>/Smart_Automotive_AI.git
cd Smart_Automotive_AI
Step 2: Install dependencies
bash
Copy code
pip install -r requirements.txt
Step 3: Run the integrated system
bash
Copy code
python scripts/integrate_main.py
Step 4: (Optional) Train or fine-tune YOLOv8
python
Copy code
from ultralytics import YOLO
model = YOLO('yolov8s.pt')
model.train(data='bdd100k.yaml', epochs=50, imgsz=640)
** Expected Output
** Detects vehicles, pedestrians, and road signs
 Tracks lane lines in real-time
 Displays red “🚨 EMERGENCY VEHICLE DETECTED” alert
 Works with recorded or live camera feeds

(You can add screenshots or demo GIFs here)

 **Future Enhancements**
Accident prediction using LSTM models

Traffic violation detection (signal jump, overspeeding)

Voice-assisted driver alerts

Streamlit-based simulation dashboard

Integration with virtual driving simulators like CARLA

**References**
YOLOv8 by Ultralytics

BDD100K Dataset

OpenCV Documentation

