from ultralytics import YOLO

def train_model():
  
    model = YOLO('yolov8n.pt') 
    
  
    results = model.train(data='fadal_data.yaml', epochs=50, imgsz=640)
    
    print("Training complete! Model saved in runs/detect/train/")

if __name__ == "__main__":
    train_model()
