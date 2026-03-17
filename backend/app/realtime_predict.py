import cv2
import numpy as np
from hand_tracker import HandTracker
from chord_mapper import process_prediction  
import os
import sys
os.environ["QT_QPA_PLATFORM"] = "xcb"
os.environ["PYTHONPATH"] = ""
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["JACK_NO_START_SERVER"] = "1"

tracker = HandTracker()
if sys.platform == "linux":
    cap = cv2.VideoCapture(
        "libcamerasrc ! videoconvert ! video/x-raw,format=BGR ! appsink drop=true sync=false",
        cv2.CAP_GSTREAMER
    )
else:
    # macOS and Windows — plain index works fine
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