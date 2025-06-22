def validate_input(data):
    required = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    return all(key in data and isinstance(data[key], (int, float)) for key in required)
