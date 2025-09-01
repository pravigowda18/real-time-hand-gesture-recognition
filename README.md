# real-time-hand-gesture-recognition

## 👤 Author
### Praveen S

## 📌 Project Overview
This project implements a real-time hand gesture recognition system using MediaPipe and OpenCV. The system is capable of detecting a hand from a live webcam feed and classifying it into one of four distinct static gestures:
-✋ Open Palm
-✊ Fist
-✌️ Peace Sign (V-sign)
-👍 Thumbs Up
The recognized gesture is displayed on the video feed along with a bounding box around the detected hand.

## ⚙️ Technology Justification
-MediaPipe Hands
--Chosen for robust, real-time hand landmark detection.
--Provides 21 precise landmarks per hand, making it suitable for gesture classification.
--Lightweight and works efficiently even on CPU without requiring GPU.

-OpenCV
--Used for video capture, image processing, and display.
--Efficient real-time rendering of bounding boxes and gesture labels.

-NumPy
--Handles landmark coordinate computations and logical operations for gesture classification.

Together, these technologies provide a balance of accuracy, speed, and simplicity, making them ideal for this project.

