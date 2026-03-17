import joblib
import pygame

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

def process_prediction(landmarks):
    predicted_label = model.predict([landmarks])[0]
    chord_name = label_to_chord[predicted_label]
    return chord_name