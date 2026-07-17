from ultralytics import YOLO

def train_model():
    # Load the pre-trained 'nano' model to fine-tune it
    model = YOLO('yolov8n.pt') 
    
    # Train the model on your custom dataset
    # 'data.yaml' will contain the paths to your images/labels
    results = model.train(data='fadal_data.yaml', epochs=50, imgsz=640)
    
    print("Training complete! Model saved in runs/detect/train/")

if __name__ == "__main__":
    train_model()