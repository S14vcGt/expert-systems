from flask import Flask, request, jsonify
from flask_cors import CORS
from model import user_friendly_answer
from data_acces import get_filos
model_input = []
app = Flask(__name__)
CORS(app)

@app.route("/")
def get_user():
    query = request.args.get('user')
    if query == "no":
        model_input.append(0)
    else:
        model_input.append(1)
    if len(model_input) == 23:
        model_answer= user_friendly_answer(model_answer)
        model_input.clear() 
        return model_answer
    return f'ESTADO DE LA LISTA {model_input} '

@app.route('/answer', methods=['POST'])
def json():
    data = request.get_json()['input']
    model_answer= user_friendly_answer(data)
    return jsonify(model_answer)


if __name__ == "__main__":
    app.run()