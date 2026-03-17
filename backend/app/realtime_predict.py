import cv2
import numpy as np
import time
import pygame
from hand_tracker import HandTracker
from chord_mapper import process_prediction, chord_sounds

tracker = HandTracker()
cap = cv2.VideoCapture(0)

pygame.mixer.init()

current_sound = None
last_chord = None
last_prediction_time = 0

PREDICTION_COOLDOWN = 0.5  

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    landmarks = tracker.extract_landmarks(frame)
    frame = tracker.draw_landmarks(frame)

    current_time = time.time()

    if landmarks is not None:
        if current_time - last_prediction_time > PREDICTION_COOLDOWN:
            try:
                landmarks_array = np.array(landmarks)

                if landmarks_array.shape[0] == 63:
                    chord = process_prediction(landmarks_array)

                    if chord != last_chord:
                        print("Chord:", chord)

                        if current_sound:
                            current_sound.stop()

                        try:
                            current_sound = chord_sounds[chord]
                            current_sound.play()
                        except Exception as e:
                            print("Audio error:", e)

                        last_chord = chord
                        last_prediction_time = current_time

                else:
                    print("Invalid landmark shape:", landmarks_array.shape)

            except Exception as e:
                print("Prediction error:", e)

        if last_chord:
            cv2.putText(
                frame,
                f"Chord: {last_chord.replace('.wav','')}",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    else:
        if current_sound:
            current_sound.stop()
            current_sound = None

        last_chord = None

        cv2.putText(
            frame,
            "No hand detected",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    cv2.imshow("Real-Time Chord Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()