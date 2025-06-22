from flask import Blueprint, request, jsonify
from model.predictor import predict_crop
from utils.helpers import validate_input

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return "✅ Crop Recommendation Microservice is UP!"

@api.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not validate_input(data):
            return jsonify({"error": "Missing or invalid fields"}), 400

        features = [
            data["N"], data["P"], data["K"],
            data["temperature"], data["humidity"],
            data["ph"], data["rainfall"]
        ]
        prediction = predict_crop(features)
        return jsonify({"recommended_crop": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
