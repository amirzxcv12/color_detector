<h1 align="center">🎨 Real-Time Color Detector</h1>

<p align="center">
  A simple real-time color detection project built with Python, OpenCV and NumPy.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/Status-Active-2EA44F?style=for-the-badge" alt="Status">
</p>

---

## About

Real-Time Color Detector uses your webcam to analyze the colors visible in the camera feed.

The program converts each frame into the HSV color space, classifies its pixels, and displays the most common colors with their approximate percentages.

This project was made as a small hands-on exercise in Python and computer vision.

## Features

- Live webcam color detection
- HSV-based color classification
- Percentage calculation for detected colors
- Colors sorted by frequency
- Lightweight processing using a smaller image
- Simple keyboard control

## Supported Colors

Red, Orange, Yellow, Green, Cyan, Blue, Purple, Pink, Black, White and Gray.

## Requirements

- Python 3
- A working webcam

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/color-detector.git
cd color-detector
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run

```bash
python color_detector.py
```

A webcam window should open. Press **Q** to close the program.

## How It Works

1. OpenCV captures an image from the webcam.
2. The image is flipped horizontally for a mirror-like view.
3. The frame is converted from BGR to HSV.
4. A smaller copy of the frame is used to speed up processing.
5. Each pixel is assigned a basic color name using its HSV values.
6. The program counts the pixels for each color and calculates their percentages.
7. The results are displayed on the live camera feed.

## Project Structure

```text
color-detector/
├── color_detector.py
├── README.md
└── requirements.txt
```

## Possible Improvements

- More accurate color ranges
- Color detection in selected areas
- A live color chart
- Custom color calibration

## Creator

**Amir**

Made with Python and OpenCV 💜
