import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO


print("Loading YOLO model...")
model = YOLO('yolov8n.pt') 

def detect_part_in_image(image):
    """
    Takes an image from Streamlit, runs YOLO inference,
    and returns the annotated image and the detected class name.
    """
    
    results = model(image)
    
    
    result = results[0]
    
   
    annotated_image_bgr = result.plot()
    
  
    annotated_image_rgb = cv2.cvtColor(annotated_image_bgr, cv2.COLOR_BGR2RGB)
    
  
    detected_component = ""
    
    if len(result.boxes) > 0:
    
        class_id = int(result.boxes.cls[0].item())
        
        detected_component = result.names[class_id]
        
    return annotated_image_rgb, detected_component
