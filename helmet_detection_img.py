import cv2
import math
import cvzone
from ultralytics import YOLO

# Load YOLO model
yolo_model = YOLO("Weights/best.pt")

# Define class labels
class_labels = ['With Helmet', 'Without Helmet']

# Load image
image_path = "Media/test3.jpeg"
img = cv2.imread(image_path)

# Get YOLO model results
results = yolo_model(img)

for r in results:
    boxes = r.boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        # Compute width and height
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h))

        # Confidence and class
        conf = math.ceil((box.conf[0] * 100)) / 100
        cls = int(box.cls[0])

        # Draw text below the bounding box
        if conf > 0.1 and class_labels[cls] == "With Helmet":
            cvzone.putTextRect(img, f'{class_labels[cls]} {conf}', (x1, y2 + 10), scale=0.8, thickness=1, colorR=(255, 0, 0))
        else:
            cvzone.putTextRect(img, f'{class_labels[cls]} {conf}', (x1, y2 + 10), scale=0.8, thickness=1, colorR=(0, 0, 255))

# Display the image
cv2.imshow("Image", img)

# Close window when 'q' button is pressed
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.waitKey(1)
