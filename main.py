import cv2
import threading
import pygame.midi
import time
from cvzone.HandTrackingModule import HandDetector

#Initialise PyGame Midi
pygame.midi.init()
output_id = pygame.midi.get_default_output_id()
player = pygame.midi.Output(output_id)
player.set_instrument(0) #Predefined number for grand piano

# 0 points tot the default camera in cv2
cap = cv2.VideoCapture(0)
# The detector must be atleast 80% confident about what the hand is pointing to.
detector = HandDetector(detectionCon=0.8)

# Chord mapping
chords = {
    "left": {
        "thumb": [62, 66, 69],   # D Major (D, F#, A)
        "index": [64, 67, 71],   # E Minor (E, G, B)
        "middle": [66, 69, 73],  # F# Minor (F#, A, C#)
        "ring": [67, 71, 74],    # G Major (G, B, D)
        "pinky": [69, 73, 76]    # A Major (A, C#, E)
    },
    "right": {
        "thumb": [62, 66, 69],   # D Major (D, F#, A)
        "index": [64, 67, 71],   # E Minor (E, G, B)
        "middle": [66, 69, 73],  # F# Minor (F#, A, C#)
        "ring": [67, 71, 74],    # G Major (G, B, D)
        "pinky": [69, 73, 76]    # A Major (A, C#, E)
    }
}

# Time it remains after the finger is lowered
SUSTAIN_TIME = 2.0
# Keep track of previous states to stop chords
prevStates = {hand: {finger: 0 for finger in chords[hand]} for hand in chords}
finger_names = ["thumb", "index", "middle", "ring", "pinky"]

def playAChord(chord_notes):
    for note in chord_notes:
        player.note_on(note, 127) #Volume is 127
        
def stopChordAfterDelay(chord_notes):
    time.sleep(SUSTAIN_TIME)
    for note in chord_notes:
        player.note_off(note, 127)
        
while True:
    success, img = cap.read()
    if not success:
        raise print("❌ Camera not capturing frames")
        continue

    hands, img = detector.findHands(img, draw=True)
    if hands:
        for hand in hands:
            handType = "left" if hand["type"] == "left" else "right"
            fingers = detector.fingersUp(hand)
            
            for i, finger in enumerate(finger_names):
                if finger[i] in chords[handType]:
                    if fingers[i] == 1 and prevStates[handType][finger] == 0:
                        playAChord(chords[handType][finger])
                elif fingers[i] == 0 and prevStates[handType][finger] == 1:
                    threading.Thread(target=stopChordAfterDelay, args=(chords[handType][finger],), daemon=True).start()
                prevStates[handType][finger] = fingers[i]  # Update state 
                
    else:
        for hand in chords:
            for finger in chords[hand]:
                threading.Thread(target=stopChordAfterDelay, args=(chords[hand][finger],), daemon=True).start()
        prev_states = {hand: {finger: 0 for finger in chords[hand]} for hand in chords}
        
    cv2.imshow("Hand Tracking MIDI Chords", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
pygame.midi.quit()