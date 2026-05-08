# 🚧 Road Damage Detection using YOLOv8

This project implements a complete deep learning pipeline for detecting road damage using the **YOLOv8** object detection model. It covers dataset preparation, COCO-to-YOLO conversion, model training, evaluation, and prediction visualization.

---

## 📌 Features

- Dataset extraction and preprocessing
- COCO annotation aggregation
- Train/Validation/Test split
- COCO to YOLO format conversion
- YOLOv8 model training
- Model evaluation using mAP metrics
- Prediction visualization on test images

---

## 🛠️ Tech Stack

- Python
- YOLOv8
- Ultralytics
- OpenCV
- NumPy
- Matplotlib

---

## 📂 Dataset Workflow

1. Extract dataset from `.tar` archive  
2. Merge annotations into COCO format  
3. Split dataset into:
   - 70% Train
   - 15% Validation
   - 15% Test
4. Convert COCO annotations to YOLO format  
5. Generate `dataset.yaml` for training  

---



## 📊 Evaluation

The trained model is evaluated using:

- mAP50-95
- mAP50
- Precision
- Recall

The project also visualizes predictions with bounding boxes, class labels, and confidence scores.

---




## 🔮 Future Improvements

- Real-time road monitoring
- Web/mobile deployment
- Improved low-light detection
- Segmentation-based analysis

---

## 📜 License

MIT License
