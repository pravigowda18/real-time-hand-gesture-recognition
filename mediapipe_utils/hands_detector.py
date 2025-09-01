import mediapipe as mp
from config import settings

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def get_hands_detector():
    # Initialize the MediaPipe Hands module
    return mp_hands.Hands(
        max_num_hands=settings.MAX_HANDS,
        model_complexity=settings.MODEL_COMPLEXITY,
        min_detection_confidence=settings.MIN_DETECTION_CONFIDENCE,
        min_tracking_confidence=settings.MIN_TRACKING_CONFIDENCE
    )

def draw_hand_landmarks(image, hand_landmarks):
    # Draw hand landmarks on the image
    mp_drawing.draw_landmarks(
        image,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS
    )
