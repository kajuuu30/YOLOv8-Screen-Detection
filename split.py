import os
import random
import shutil

# Paths
images_path = r"C:\Users\INV\Downloads\Kajal\images"   # yahan tumhari saari images hain
labels_path = r"C:\Users\INV\Downloads\Kajal\labels"   # yahan saari txt files hain
output_path = "dataset"

# Train/Val split ratio
split_ratio = 0.8  # 80% train, 20% val

# Naya dataset folder structure banao
for folder in ["images/train", "images/val", "labels/train", "labels/val"]:
    os.makedirs(os.path.join(output_path, folder), exist_ok=True)

# Saari image files list karo
images = [f for f in os.listdir(images_path) if f.endswith(".jpg") or f.endswith(".png")]
random.shuffle(images)

# Split point
split_idx = int(len(images) * split_ratio)
train_files = images[:split_idx]
val_files = images[split_idx:]

def move_files(file_list, set_name):
    for img in file_list:
        label = img.replace(".jpg", ".txt").replace(".png", ".txt")
        
        # Image move karo
        shutil.copy(os.path.join(images_path, img), os.path.join(output_path, f"images/{set_name}", img))
        
        # Label move karo (agar exist karta hai)
        if os.path.exists(os.path.join(labels_path, label)):
            shutil.copy(os.path.join(labels_path, label), os.path.join(output_path, f"labels/{set_name}", label))

# Move train/val files
move_files(train_files, "train")
move_files(val_files, "val")

print("✅ Dataset split complete!")
