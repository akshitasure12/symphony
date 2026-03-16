import cv2
import mediapipe as mp
import numpy as np


class HandTracker:
    """
    HandTracker uses MediaPipe Hands to detect hand landmarks
    and extract (x, y, z) coordinates for gesture recognition.
    """

    def __init__(
        self,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5,
    ):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

    def extract_landmarks(self, frame):
        """
        Extract (x, y, z) coordinates from detected hand.
        Returns:
            numpy array of shape (63,) or None if no hand detected
        """

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        if not results.multi_hand_landmarks:
            return None

        landmarks = []

        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                landmarks.append(lm.x)
                landmarks.append(lm.y)
                landmarks.append(lm.z)

        landmarks = np.array(landmarks)

        return landmarks

    def draw_landmarks(self, frame):
        """
        Draw detected hand skeleton on the frame.
        """

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                )

        return frame

    def extract_landmarks_normalized(self, frame):
        """
        Extract normalized landmark coordinates.
        Normalization improves ML performance by removing scale differences.
        """

        landmarks = self.extract_landmarks(frame)

        if landmarks is None:
            return None

        # Normalize values between 0 and 1
        landmarks = landmarks - np.min(landmarks)
        if np.max(landmarks) != 0:
            landmarks = landmarks / np.max(landmarks)

        return landmarks