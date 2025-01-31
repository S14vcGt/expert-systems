from flask import Flask, request
from flask_cors import CORS
from model.model import user_friendly_answer
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

if __name__ == "__main__":
    app.run()