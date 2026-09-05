
label_file = "datasets/fadal_parts/train/labels/IMG_20250605_234721320_HDR.txt"

content = "0 0.5 0.5 0.2 0.2" 

with open(label_file, "w") as f:
    f.write(content)
    
print(f"Created label for {label_file}")
