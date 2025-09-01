import cv2
from config import settings

def get_bounding_box(image, hand_landmarks):
    """Get the bounding box coordinates for the detected hand landmarks.

    Keyword arguments:
    image -- the input image
    hand_landmarks -- the detected hand landmarks
    Return: (x_min, y_min, x_max, y_max) coordinates of the bounding box
    """
    
    h, w, _ = image.shape
    x_min, y_min, x_max, y_max = w, h, 0, 0

    for lm in hand_landmarks.landmark:
        x, y = int(lm.x * w), int(lm.y * h)
        x_min, y_min = min(x_min, x), min(y_min, y)
        x_max, y_max = max(x_max, x), max(y_max, y)

    # Add padding
    x_min = max(0, x_min - settings.BOUNDING_BOX_PADDING)
    y_min = max(0, y_min - settings.BOUNDING_BOX_PADDING)
    x_max = min(w, x_max + settings.BOUNDING_BOX_PADDING)
    y_max = min(h, y_max + settings.BOUNDING_BOX_PADDING)

    return (x_min, y_min, x_max, y_max)

def draw_label(image, text, x_min, y_min):
    # Draw a label with the gesture name above the bounding box
    cv2.putText(image, text, (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2, cv2.LINE_AA)
