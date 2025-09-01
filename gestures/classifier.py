import numpy as np

def classify_gesture(landmarks, handedness="Right"):
    # Get the coordinates of the hand landmarks
    coords = np.array([(lm.x, lm.y) for lm in landmarks])
    # print(coords)
    tips_ids = [4, 8, 12, 16, 20]
    base_ids = [3, 6, 10, 14, 18]

    fingers = []

    # Thumb logic
    if handedness == "Right":
        # Right hand: thumb is extended if its tip is further right than the base
        fingers.append(1 if coords[tips_ids[0]][0] < coords[base_ids[0]][0] else 0)
    else:
        # Left hand: thumb is extended if its tip is further left than the base
        fingers.append(1 if coords[tips_ids[0]][0] > coords[base_ids[0]][0] else 0)

    # Other fingers
    for i in range(1, 5):
        fingers.append(1 if coords[tips_ids[i]][1] < coords[base_ids[i]][1] else 0)

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
