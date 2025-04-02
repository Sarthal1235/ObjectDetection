import os
import random
import shutil

# Define paths
data_dir = "dataset/images"
label_dir = "dataset/labels"

train_image_dir = "dataset/images/train"
val_image_dir = "dataset/images/val"
train_label_dir = "dataset/labels/train"
val_label_dir = "dataset/labels/val"

# Create directories if they don't exist
for d in [train_image_dir, val_image_dir, train_label_dir, val_label_dir]:
    os.makedirs(d, exist_ok=True)

# Get all image files
images = [f for f in os.listdir(data_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(images)

# Split (80% train, 20% val)
split_index = int(len(images) * 0.8)
train_images = images[:split_index]
val_images = images[split_index:]

# Move files to corresponding directories
for img in train_images:
    shutil.move(os.path.join(data_dir, img), os.path.join(train_image_dir, img))
    label_file = img.replace(img.split('.')[-1], 'txt')  # Get corresponding label
    if os.path.exists(os.path.join(label_dir, label_file)):
        shutil.move(os.path.join(label_dir, label_file), os.path.join(train_label_dir, label_file))

for img in val_images:
    shutil.move(os.path.join(data_dir, img), os.path.join(val_image_dir, img))
    label_file = img.replace(img.split('.')[-1], 'txt')
    if os.path.exists(os.path.join(label_dir, label_file)):
        shutil.move(os.path.join(label_dir, label_file), os.path.join(val_label_dir, label_file))

print("Dataset successfully split into training and validation sets!")
