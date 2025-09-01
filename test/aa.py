import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=2,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Function to classify gestures
def classify_gesture(landmarks, handedness="Right"):
    coords = np.array([(lm.x, lm.y) for lm in landmarks])
    # print(coords)
    
    tips_ids = [4, 8, 12, 16, 20]   # Thumb, Index, Middle, Ring, Pinky tips
    base_ids = [3, 6, 10, 14, 18]   # Their base joints

    fingers = []

    # Thumb logic depends on left/right hand
    if handedness == "Right":
        if coords[tips_ids[0]][0] < coords[base_ids[0]][0]:
            fingers.append(1)
        else:
            fingers.append(0)
    else:  # Left hand
        if coords[tips_ids[0]][0] > coords[base_ids[0]][0]:
            fingers.append(1)
        else:
            fingers.append(0)

    # Other 4 fingers: check y-axis
    for i in range(1, 5):
        if coords[tips_ids[i]][1] < coords[base_ids[i]][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    # Gesture classification
    if fingers == [0, 0, 0, 0, 0]:
        return "Fist"
    elif fingers == [1, 1, 1, 1, 1]:
        return "Open Palm"
    elif fingers == [0, 1, 1, 0, 0]:
        return "Peace Sign"
    elif fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up"
    else:
        return "Unknown"


# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image horizontally for a selfie-view display.
    image = cv2.flip(image, 1)

    # Convert BGR image to RGB.
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_rgb.flags.writeable = False

    # Process the image and find hands.
    results = hands.process(image_rgb)

    image_rgb.flags.writeable = True
    image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            
            label = hand_handedness.classification[0].label  # 'Left' or 'Right'

            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Classify gesture with hand info
            gesture = classify_gesture(hand_landmarks.landmark, handedness=label)

            # Display
            # h, w, _ = image.shape
            # x_min, y_min = int(min([lm.x for lm in hand_landmarks.landmark]) * w), int(min([lm.y for lm in hand_landmarks.landmark]) * h)
            
            h, w, c = image.shape
            x_min, y_min = w, h
            x_max, y_max = 0, 0

            for lm in hand_landmarks.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                x_min = min(x_min, x)
                y_min = min(y_min, y)
                x_max = max(x_max, x)
                y_max = max(y_max, y)

            # Add padding to the bounding box
            padding = 20
            x_min = max(0, x_min - padding)
            y_min = max(0, y_min - padding)
            x_max = min(w, x_max + padding)
            y_max = min(h, y_max + padding)
            
            # Draw bounding box
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 255, 255), 2)

            
            cv2.putText(image, f"{label} - {gesture}", (x_min, y_min - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Hand Gesture Recognition", image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()