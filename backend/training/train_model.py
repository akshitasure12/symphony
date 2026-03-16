import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X = np.load("datasets/X.npy")
y = np.load("datasets/y.npy")

print("Dataset Loaded")
print("X:", X.shape)
print("y:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42,
    n_jobs=-1
)
print("Training Random Forest...")
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Test Accuracy:", accuracy)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/chord_classifier.pkl")
print("Model saved!")