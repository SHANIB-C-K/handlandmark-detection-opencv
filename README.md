# Hand Landmark Detection using OpenCV & MediaPipe



## 📌 Overview

This project implements real-time hand landmark detection using OpenCV and MediaPipe. It captures video from the webcam, detects hand landmarks, and overlays them on the video feed.

## 🛠️ Features

- Real-time hand landmark detection
- Draws landmarks and connections on the detected hand
- Smooth video processing using OpenCV
- Press 'q' to exit the application

## 📦 Requirements

Make sure you have the following dependencies installed:

```sh
pip install opencv-python mediapipe
```

## 🚀 Installation & Usage

1. Clone this repository:

```sh
git clone https://github.com/SHANIB-C-K/handlandmark-detection-opencv.git
cd handlandmark-detection-opencv
```

2. Run the script:

```sh
python main.py
```

## 📜 Code Explanation

- **OpenCV** is used for video capturing and displaying the processed frames.
- **MediaPipe Hands** model detects hand landmarks in real-time.
- **Flip & Convert**: The frame is flipped horizontally for a mirror effect and converted to RGB before processing.
- **Drawing Landmarks**: The detected landmarks are drawn using MediaPipe's built-in drawing utility.
- **Exit Mechanism**: Pressing 'q' will close the window.

## 📷 Demo

You can see the hand tracking in action by running the script. Example output:



## 🤝 Contribution

Feel free to contribute by improving the code, fixing bugs, or adding new features!

## 📜 License

This project is licensed under the MIT License.

---

Made with ❤️ using OpenCV & MediaPipe.

