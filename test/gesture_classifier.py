import numpy as np

# Function to classify gestures

def classify_gesture(landmarks):

   
    
    coords = np.array([(lm.x, lm.y) for lm in landmarks])
    # print(coords)
    tips_ids = [4, 8, 12, 16, 20]   # Thumb, Index, Middle, Ring, Pinky tips
    base_ids = [3, 6, 10, 14, 18]   # Their base joints

    fingers = []

    # Thumb: check x-axis
    if coords[tips_ids[0]][0] < coords[base_ids[0]][0]:
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

