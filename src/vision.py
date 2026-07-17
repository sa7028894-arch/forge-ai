import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO

# Load the model once when the server starts
print("Loading YOLO model...")
model = YOLO('yolov8n.pt') 

def detect_part_in_image(image):
    """
    Takes an image from Streamlit, runs YOLO inference,
    and returns the annotated image and the detected class name.
    """
    # 1. Run YOLO inference directly on the uploaded image
    results = model(image)
    
    # 2. Get the first result (since we only upload one image at a time)
    result = results[0]
    
    # 3. .plot() automatically draws the bounding boxes and returns a numpy array (BGR format)
    annotated_image_bgr = result.plot()
    
    # 4. Convert BGR colors back to RGB so Streamlit renders it correctly
    annotated_image_rgb = cv2.cvtColor(annotated_image_bgr, cv2.COLOR_BGR2RGB)
    
    # 5. Extract the name of the detected object
    detected_component = ""
    
    if len(result.boxes) > 0:
        # Grab the class ID of the highest confidence detection
        class_id = int(result.boxes.cls[0].item())
        # Convert the ID to the actual text name (e.g., 'person', 'car', or 'Spindle')
        detected_component = result.names[class_id]
        
    return annotated_image_rgb, detected_component