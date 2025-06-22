import joblib
import numpy as np
from config.settings import LABEL_MAP

# Load model and scaler
model = joblib.load("model/crop_model.pkl")
scaler = joblib.load("model/crop_scaler.pkl")

def predict_crop(features):
    features_np = np.array([features])
    scaled = scaler.transform(features_np)
    pred = model.predict(scaled)[0]
    return LABEL_MAP.get(int(pred), "Unknown")
