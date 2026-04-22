import sys
sys.stdout.reconfigure(encoding='utf-8')  # Fix UnicodeEncodeError on Windows terminals

import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# === Step 1: Set image path ===
image_path = 'meter_images/id_1_value_13_116.jpg'

# === Step 2: Read image ===
img = cv2.imread(image_path)

# === Step 3: Create OCR reader (no GPU, no verbose bar) ===
reader = easyocr.Reader(['en'], gpu=False, verbose=False)

# === Step 4: Detect text ===
text_ = reader.readtext(img)

# === Step 5: Visualize results ===
threshold = 0.25
for t in text_:
    bbox, text, score = t
    print(f"Detected text: {text} (Confidence: {score:.2f})")

    if score > threshold:
        # Draw bounding box
        cv2.rectangle(img, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 2)
        # Draw text
        cv2.putText(img, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

# === Step 6: Show image ===
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

