# Helper to create a label file manually if you know coordinates
# Format: class_id x_center y_center width height (0 to 1 scale)
label_file = "datasets/fadal_parts/train/labels/IMG_20250605_234721320_HDR.txt"
# Example: Class 0 (coolant_tank), center 0.5, 0.5, width 0.2, height 0.2
content = "0 0.5 0.5 0.2 0.2" 

with open(label_file, "w") as f:
    f.write(content)
    
print(f"Created label for {label_file}")