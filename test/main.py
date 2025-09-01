import cv2
import mediapipe as mp
from gesture_classifier import classify_gesture

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,  # track only one hand
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip for selfie-view
    image = cv2.flip(image, 1)

    # Convert BGR → RGB
    image.flags.writeable = False
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    # Draw results
    image.flags.writeable = True
    image = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

    gesture = "No Hand"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw with MediaPipe styles
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
               
            )

            # Classify gesture
            gesture = classify_gesture(hand_landmarks.landmark)

    # Overlay gesture text
    cv2.putText(image, gesture, (50, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)

    cv2.imshow("Hand Gesture Recognition", image)

    if cv2.waitKey(5) & 0xFF == 27:  # press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
