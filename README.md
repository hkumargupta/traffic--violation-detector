# traffic--violation-detector
AI based traffic violation detection system
# 🚦 Traffic Violation Detector

An AI-based Traffic Violation Detection System that automatically detects traffic rule violations using computer vision and deep learning.

---

## 📌 Problem Statement
Manual traffic monitoring is time-consuming, error-prone, and limited by human resources. Many traffic violations such as helmetless riding and red-light jumping go undetected, leading to accidents and poor traffic management.

---

## 💡 Solution
This project uses AI-based object detection to automatically monitor traffic through camera footage and detect violations in real time. When a violation is detected, the system captures evidence and logs the details.

---

## ⚙️ Technology Stack
- Python  
- OpenCV  
- YOLO (Ultralytics YOLOv8)  
- PyTorch  
- NumPy  

---

## 📊 Dataset Used
- COCO Dataset (for vehicle and person detection)
- Custom Helmet Detection Dataset
- Traffic Signal Dataset  
(All datasets are annotated in YOLO format)

---

## 🏗️ System Architecture / Workflow
1. Capture video from CCTV / webcam  
2. Extract frames using OpenCV  
3. Detect objects using YOLO  
4. Apply traffic rule logic  
5. Detect violation  
6. Save evidence and generate report  

---

## 🚨 Violations Detected
- Helmet violation  
- Red light violation  
- Wrong-way driving (optional)  

---

## ▶️ How to Run the Project
1. Clone the repository
