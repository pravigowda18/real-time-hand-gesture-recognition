import cv2
from mediapipe_utils.hands_detector import get_hands_detector, draw_hand_landmarks
from gestures.classifier import classify_gesture
from gestures.utils import get_bounding_box, draw_label

def run_webcam():
    cap = cv2.VideoCapture(0)
    
    # Initialize the MediaPipe hands detector
    hands = get_hands_detector()

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the image horizontally for a mirror effect
        image = cv2.flip(image, 1)
        # Convert the image to RGB for MediaPipe processing
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Process the image to detect hands
        results = hands.process(image_rgb)
        # Convert the image back to BGR for OpenCV display
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            # Iterate through each detected hand and its handedness
            for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                label = hand_handedness.classification[0].label  # 'Left' or 'Right'
                # Draw hand landmarks on the image
                draw_hand_landmarks(image, hand_landmarks)

                # Classify the gesture based on landmarks and handedness
                gesture = classify_gesture(hand_landmarks.landmark, handedness=label)
                # Get the bounding box coordinates for the hand
                x_min, y_min, x_max, y_max = get_bounding_box(image, hand_landmarks)

                # Draw a rectangle around the detected hand
                cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 255, 255), 2)
                # Draw the label (handedness and gesture) above the bounding box
                draw_label(image, f"{label} - {gesture}", x_min, y_min)

        # Display the processed image in a window
        cv2.imshow("Hand Gesture Recognition", image)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()
