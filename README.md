# Gas Meter Reading ML Model

## Overview

The **Gas Meter Reading ML Model** is a deep learning-based computer vision system designed to automatically extract numerical readings from gas meter images. The project combines image preprocessing, digit recognition, and post-processing techniques to generate accurate meter readings with minimal human intervention.

The system is designed for real-world deployment in smart utility monitoring, automated billing systems, and IoT-enabled infrastructure.

---

## Features

* Automated gas meter reading from images
* Image preprocessing for enhanced digit visibility
* Region of Interest (ROI) extraction
* Digit recognition using deep learning models
* Post-processing and digit validation
* Robust performance under varying lighting conditions
* Modular and scalable architecture
* Suitable for smart utility and IoT applications

---

## Project Workflow

```text
Input Meter Image
        │
        ▼
Image Preprocessing
(Grayscale, Denoising, Thresholding)
        │
        ▼
ROI Extraction
(Meter Display Detection)
        │
        ▼
Digit Segmentation
        │
        ▼
Digit Recognition Model
(MNIST-trained CNN)
        │
        ▼
Post-processing & Validation
        │
        ▼
Final Meter Reading
```

---

## Technologies Used

* Python
* OpenCV
* TensorFlow / PyTorch
* NumPy
* EasyOCR (optional OCR-based approach)
* Matplotlib

---

## Dataset

### Training Dataset

**MNIST Handwritten Digit Dataset**

* 70,000 digit images
* 60,000 training samples
* 10,000 testing samples
* Digits ranging from 0–9

### Testing Dataset

* Custom gas meter images
* Real-world meter photographs captured under different conditions
* Images containing varying lighting, angles, blur, and distortions

---

## Model Architecture

The digit recognition model is based on a Convolutional Neural Network (CNN).

### Pipeline

1. Image acquisition
2. Preprocessing
3. ROI extraction
4. Digit segmentation
5. CNN-based digit classification
6. Reading reconstruction
7. Validation and correction

---

## Image Preprocessing

The preprocessing stage improves recognition accuracy by:

* Converting images to grayscale
* Noise reduction
* Contrast enhancement
* Thresholding
* Edge detection
* Digit isolation

Example OpenCV operations:

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)[1]
```

---

## Results

| Metric                     | Value             |
| -------------------------- | ----------------- |
| Digit Recognition Accuracy | 98%+              |
| Training Dataset           | MNIST             |
| OCR Confidence             | High              |
| Processing Time            | Real-Time Capable |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/gas-meter-reading-ml.git
cd gas-meter-reading-ml
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Required Libraries

```bash
pip install opencv-python
pip install tensorflow
pip install torch
pip install numpy
pip install matplotlib
pip install easyocr
```

---

## Usage

### Run Meter Reading Script

```bash
python meter_reading.py
```

### Input

Place gas meter images inside:

```text
meter_images/
```

Example:

```text
meter_images/
├── id_1_value_13_116.jpg
├── id_2_value_54_221.jpg
```

### Output

```text
Detected text: 13116
Confidence: 0.98
```

Annotated image with bounding boxes:

```text
┌─────────────────┐
│     13116       │
└─────────────────┘
```

---

## Applications

* Smart Utility Monitoring
* Automated Billing Systems
* Industrial Meter Inspection
* IoT-Based Energy Management
* Smart City Infrastructure
* Remote Meter Reading

---

## Future Improvements

* YOLO-based meter display detection
* Support for analog meters
* Edge deployment on Raspberry Pi
* Mobile application integration
* Real-time video stream processing
* Cloud-based monitoring dashboard

---

## Project Structure

```text
Gas-Meter-Reading-ML/
│
├── meter_images/
│   ├── sample1.jpg
│   ├── sample2.jpg
│
├── models/
│   ├── digit_classifier.h5
│
├── meter_reading.py
├── train_model.py
├── requirements.txt
├── README.md
│
└── results/
    ├── predictions/
```

---

## Author

**Arshia Anand**

Computer Vision • Machine Learning • Deep Learning

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it for educational and research purposes.
