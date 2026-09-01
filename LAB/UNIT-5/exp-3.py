from ultralytics import YOLO

model = YOLO("yolo11n.pt")

img = input("Enter image path: ")
results = model(img)

for r in results:
    print("Detected objects:")
    for c in r.boxes.cls:
        print(model.names[int(c)])
