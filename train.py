from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO("models/yolov8n.pt")

# Train the model on the custom dataset
model.train(data="data.yaml", epochs=50, imgsz=640)

# Save trained modelcls
model.export(format="onnx")

print("Training complete! The model is saved in runs/detect/train/weights/best.pt")
