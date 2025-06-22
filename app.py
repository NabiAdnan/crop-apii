from flask import Flask
from flask_cors import CORS
from api.routes import api

app = Flask(__name__)
CORS(app)

# Register blueprint
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
