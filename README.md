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

│── dataset/     # Dataset (images + labels) <br>
│── labels/      # Class labels
│── best.pt      # Final trained YOLOv8 model
│── last.pt      # Last epoch trained model
│── data.yaml    # Dataset configuration file
│── classes.txt  # Class names
│── Screen_Detection.ipynb   # Jupyter Notebook for training/testing
│── split.py     # Script to split dataset
│── notes.json   # Notes/metadata

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


