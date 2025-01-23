# Helmet Detection using YOLO

This project demonstrates a **helmet detection system** using the YOLO (You Only Look Once) object detection model. The script detects objects in an image and classifies them as "With Helmet" or "Without Helmet". The implementation is based on Python and uses libraries such as OpenCV, `cvzone`, and the `ultralytics` YOLO framework.

---

## Features
- Detects objects in an image.
- Classifies objects into two categories: **With Helmet** and **Without Helmet**.
- Displays bounding boxes, confidence scores, and labels on detected objects.
- User-friendly display and interaction, with the ability to close the result window by pressing `q`.

---

## Requirements

### **Libraries**
Ensure you have the following libraries installed:

- Python 3.8+
- OpenCV
- math (built-in)
- cvzone
- ultralytics

### **Installing Dependencies**
Install the required libraries via pip:
```bash
pip install opencv-python cvzone ultralytics
```

---

## Project Structure

```plaintext
.
|-- Weights/
|   |-- best.pt            # YOLO model weights (trained on helmet dataset)
|-- Media/
|   |-- test2.jpg          # Sample image for testing
|-- helmet_detection.py    # Main script
|-- README.md              # Project documentation
```

---

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mayur112005/IBM-Project.git
   cd helmet-detection-yolo
   ```

2. **Prepare the Weights**:
   Place your YOLO model weights file (`best.pt`) in the `Weights/` directory. If you don't have the weights file, train the YOLO model on your dataset or obtain a pre-trained model for helmet detection.

3. **Run the Script**:
   Execute the script to detect helmets in an image:
   ```bash
   python helmet_detection.py
   ```

4. **View Results**:
   - The processed image with bounding boxes and labels will be displayed in a new window.
   - Press `q` to close the window.

---

## Code Explanation

The script performs the following steps:

1. **Load YOLO Model**:
   Loads the YOLO model using the custom-trained weights file (`best.pt`).

2. **Define Class Labels**:
   Specifies the object classes: "With Helmet" and "Without Helmet".

3. **Process Image**:
   - Reads the input image.
   - Passes the image to the YOLO model for detection.

4. **Draw Bounding Boxes**:
   For each detected object, draws a bounding box with a label and confidence score.

5. **Display Image**:
   Shows the annotated image in a window and waits for user interaction.

---
