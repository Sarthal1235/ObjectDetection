from ultralytics import YOLO

# Download and load YOLOv8 model
model = YOLO('yolov8n.pt')  # Downloads the model

# Export model to ONNX format (optional, for optimization)
model.export(format='onnx')

print("Model downloaded and exported successfully!")
