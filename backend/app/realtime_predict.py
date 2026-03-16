import cv2
import numpy as np
from hand_tracker import HandTracker
from chord_mapper import process_prediction  

tracker = HandTracker()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    landmarks = tracker.extract_landmarks(frame)
    frame = tracker.draw_landmarks(frame)

    if landmarks is not None:
        print("Landmarks detected:", len(landmarks))
        chord = process_prediction(np.array(landmarks))
        print("Chord:", chord)

        cv2.putText(
            frame,
            f"Chord: {chord.replace('.wav','')}",  
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Real-Time Chord Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()