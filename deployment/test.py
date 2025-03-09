from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Initialize FastAPI
app = FastAPI()

# Load YOLO model
model = YOLO("yolov8n.pt")  # Use 'yolov8s.pt' for better accuracy

# API Endpoint: Upload Image for Object Detection
@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    # Read image
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Run YOLOv8 Detection
    results = model(image)

    # Extract detections
    objects_detected = []
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = results[0].names[int(box.cls)]
        confidence = float(box.conf[0])
        objects_detected.append({"label": label, "confidence": confidence, "bbox": [x1, y1, x2, y2]})

    return {"detections": objects_detected}

# Run API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)