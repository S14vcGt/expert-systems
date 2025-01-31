from flask import Flask, request, jsonify
from flask_cors import CORS
import model
app = Flask(__name__)
CORS(app)

@app.route('/answer', methods=['POST'])
def json():
    data = request.get_json()['input']
    model_answer= model.user_friendly_answer(data)
    return jsonify(model_answer)

@app.route('/list_filos')
def find_all():
    pass

@app.route('/new_filo', methods=['POST'])
def add():
    data = request.get_json()
    return model.agregar_filo(data)

@app.route('/delete_filo',methods=['DELETE'])
def delete():
    pass

if __name__ == "__main__":
    app.run()