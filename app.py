from flask import Flask, request
from model.model import dumb_answer
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def get_user():
    query = request.args.get('user')
    return dumb_answer(query)

if __name__ == "__main__":
    app.run()