# YOLOv8-Screen-Detection
YOLOv8 model for detecting screens in images (mobile, laptop, tablet).


# 📱 Screen Detection using YOLOv8

This project uses a **custom-trained YOLOv8 model** to detect screens (mobile phones, laptops, tablets, etc.) in images.  
It includes the dataset structure, training pipeline, and inference scripts.  

---

## 🚀 Features
- Custom dataset for screen detection  
- Trained YOLOv8 model (`best.pt`)  
- Scripts for training, testing, and inference  
- Works on both **Google Colab** and **local environment (Visual Studio / Jupyter Notebook)**  

---

## 📂 Project Structure

Main_SD_Project <br>
│ <br>
├── 📁 dataset/ # Dataset (images + labels) <br>
├── 📁 labels/ # YOLO annotation labels <br>
│ <br>
├── 📄 best.pt # Final trained YOLOv8 model <br>
├── 📄 last.pt # Last epoch model <br>
├── 📄 data.yaml # Dataset configuration file <br>
├── 📄 classes.txt # Class names <br>
├── 📄 notes.json # Notes / metadata <br>
│ <br>
├── 📝 Screen_Detection.ipynb # Jupyter Notebook for training & testing <br>
├── 🐍 split.py # Script to split dataset <br>
└── 🐍 data.py # Additional script <br>


## Installation Instructions
pip install ultralytics


## 📊 Model Accuracy

| Metric              | Score   |
|----------------------|---------|
| Precision (B)        | 0.9457  |
| Recall (B)           | 0.9266  |
| mAP50 (B)            | 0.9733 |
| mAP50-95 (B)         | 0.8359 |

- **Classes Detected:** Laptop, Phone, Tab  
- **Training Time:** ~1.5 hours (on Colab Tesla T4 GPU)  
- **Dataset Size:** 2751 images   


