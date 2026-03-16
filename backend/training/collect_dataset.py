import cv2
import numpy as np
import os
import time
from app.hand_tracker import HandTracker

tracker = HandTracker()
cap = cv2.VideoCapture(0)

data = []
labels = []

TARGET_SAMPLES = 300

chords = [
    "C","Dm","Em","F","G","Am",
    "D","E","A","Bm","Gm","Fm"
]

sample_counts = {i:0 for i in range(len(chords))}

current_label = 0
frame_count = 0
capture_interval = 8

buffer_mode = False
buffer_start = 0
BUFFER_TIME = 5

print("\nDataset Collection Started")
print("Show gesture for:", chords[current_label])

while True:

    ret, frame = cap.read()
    if not ret:
        break

    landmarks = tracker.extract_landmarks(frame)
    frame = tracker.draw_landmarks(frame)

    if not buffer_mode and landmarks is not None:
        frame_count += 1
        if frame_count % capture_interval == 0:
            if sample_counts[current_label] < TARGET_SAMPLES:
                data.append(landmarks)
                labels.append(current_label)
                sample_counts[current_label] += 1

                print(
                    f"{chords[current_label]}: "
                    f"{sample_counts[current_label]}/{TARGET_SAMPLES}",
                    end="\r"
                )
            if sample_counts[current_label] == TARGET_SAMPLES:
                print(f"\n✓ Completed {chords[current_label]}")
                buffer_mode = True
                buffer_start = time.time()

    if buffer_mode:
        elapsed = int(time.time() - buffer_start)
        remaining = BUFFER_TIME - elapsed
        cv2.putText(
            frame,
            f"Switch gesture in: {remaining}",
            (10,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2
        )
        if remaining <= 0:
            current_label += 1
            buffer_mode = False
            if current_label >= len(chords):
                print("\nAll chords recorded!")
                break
            print("\nNext chord:", chords[current_label])

    chord_name = chords[current_label] if current_label < len(chords) else "Done"
    chord_count = sample_counts.get(current_label, 0)

    cv2.putText(
        frame,
        f"Chord: {chord_name}",
        (10,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Samples: {chord_count}/{TARGET_SAMPLES}",
        (10,120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("Dataset Collector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

X = np.array(data)
y = np.array(labels)

os.makedirs("datasets", exist_ok=True)

np.save("datasets/X.npy", X)
np.save("datasets/y.npy", y)

print("\nDataset saved!")
print("X shape:", X.shape)
print("y shape:", y.shape)

print("\nSamples per chord:")
for i in range(len(chords)):
    print(f"{chords[i]} : {sample_counts[i]}")