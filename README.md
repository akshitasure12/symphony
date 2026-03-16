# symphony
I JUST WANNA BE PART OF YOUR SYMPHONY . . . 

## Backend

### Architecture

```
User Hand Gesture
        │
        ▼
Webcam Capture (Frontend)
        │
        ▼
Backend API (FastAPI)
        │
        ▼
MediaPipe Hand Tracking
        │
        ▼
Landmark Extraction
(21 hand landmarks → 42 features)
        │
        ▼
Gesture Classification Neural Network
        │
        ▼
Chord Prediction
        │
        ▼
Frontend Audio Engine
(WebAudio API)
```

Phase 1 → Project Setup
Phase 2 → Hand Tracking (MediaPipe)
Phase 3 → Dataset Collection
Phase 4 → Train Classifier
Phase 5 → Real-Time Gesture Prediction
Phase 6 → Chord Audio Mapping
Phase 7 → Web Integration

### Project Structure

```
symphony/
│
├── frontend/                 # Website interface
│
├── backend/
│   │
│   ├── app/
│   │   ├── main.py           # FastAPI server
│   │   ├── hand_tracker.py   # MediaPipe hand detection
│   │   ├── predict.py        # Model inference
│   │
│   ├── training/
│   │   ├── collect_dataset.py
│   │   ├── train_model.py
│   │
│   ├── models/               # Trained ML models
│   │
│   ├── datasets/             # Gesture dataset
│   │
│   └── requirements.txt
```