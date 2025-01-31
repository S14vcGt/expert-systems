from flask import Flask, request, jsonify
from flask_cors import CORS
from model import user_friendly_answer
from data_acces import get_filos
app = Flask(__name__)
CORS(app)

@app.route('/answer', methods=['POST'])
def json():
    data = request.get_json()['input']
    model_answer= user_friendly_answer(data)
    return jsonify(model_answer)


if __name__ == "__main__":
    app.run()