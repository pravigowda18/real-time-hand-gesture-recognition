# real-time-hand-gesture-recognition

## 👤 Author
Praveen S

## 📌 Project Overview
This project implements a real-time hand gesture recognition system using MediaPipe and OpenCV. The system is capable of detecting a hand from a live webcam feed and classifying it into one of four distinct static gestures:
- ✋ Open Palm
- ✊ Fist
- ✌️ Peace Sign (V-sign)
- 👍 Thumbs Up

The recognized gesture is displayed on the video feed along with a bounding box around the detected hand.

## ⚙️ Technology Justification
- MediaPipe Hands
  - Chosen for robust, real-time hand landmark detection.
  - Provides 21 precise landmarks per hand, making it suitable for gesture classification.
  - Lightweight and works efficiently even on CPU without requiring GPU.

- OpenCV
  - Used for video capture, image processing, and display.
  - Efficient real-time rendering of bounding boxes and gesture labels.

- NumPy
  - Handles landmark coordinate computations and logical operations for gesture classification.

Together, these technologies provide a balance of accuracy, speed, and simplicity, making them ideal for this project.

## 🧠 Gesture Logic Explanation
The system uses the relative positions of hand landmarks to determine whether each finger is open or closed.
1. Thumb Detection
    - Checked along the x-axis depending on left/right hand.
    - If the thumb tip is farther away (left for right-hand, right for left-hand) than its base joint, the thumb is considered "open."

2. Other Fingers (Index, Middle, Ring, Pinky)
    - Compared along the y-axis.
    - If the fingertip is above its base joint, the finger is considered "open."

3. Gesture Classification Rules
    - Fist → All fingers closed [0,0,0,0,0]
    - Open Palm → All fingers open [1,1,1,1,1]
    - Peace Sign → Index + Middle open, others closed [0,1,1,0,0]
    - Thumbs Up → Only thumb open [1,0,0,0,0]

## 🚀 Setup and Execution Instructions
### 1️⃣ Clone Repository
```sh
git clone https://github.com/your-username/hand-gesture-recognition.git
cd hand-gesture-recognition
```
### 2️⃣ Create Virtual Environment (recommended)
```sh
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```
 ### 3️⃣ Install Dependencies

 ```sh 
 pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
python main.py
```
### 5️⃣ Controls
- The webcam will open and display live gesture recognition.
- Press ESC to exit


## 🎥 Demonstration
<!-- Displays the demo GIF showing real-time hand gesture recognition in action -->
<img src="demo.gif" alt="Demo of Hand Gesture Recognition"

## 📂 Project Structure

hand_gesture_recognition/
│── main.py                 # Entry point
│── requirements.txt
│── README.md
│
├── gestures/
│   ├── classifier.py        # Gesture classification logic
│   └── utils.py             # Helper functions
│
├── mediapipe_utils/
│   └── hands_detector.py    # Hand detection wrapper
│
├── app/
│   └── webcam_app.py        # Webcam streaming & recognition
│
└── config/
    └── settings.py          # Configuration parameters
