import pygame
import time
import joblib

model = joblib.load("models/chord_classifier.pkl")

label_to_chord = {
    0: "C.wav",
    1: "Dm.wav",
    2: "Em.wav",
    3: "F.wav",
    4: "G.wav",
    5: "Am.wav",
    6: "D.wav",
    7: "E.wav",
    8: "A.wav",
    9: "Bm.wav",
    10: "Gm.wav",
    11: "Fm.wav"
}

pygame.mixer.init()
chord_sounds = {
    chord: pygame.mixer.Sound(f"assets/chords/{chord}")
    for chord in label_to_chord.values()
}

current_chord = None
last_play_time = 0
PLAY_DURATION = 1.0  

def process_prediction(landmarks):
    global current_chord, last_play_time
    predicted_label = model.predict([landmarks])[0]
    chord_name = label_to_chord[predicted_label]

    now = time.time()
    if chord_name != current_chord:
        pygame.mixer.stop()
        chord_sounds[chord_name].play()
        current_chord = chord_name
        last_play_time = now
    return chord_name