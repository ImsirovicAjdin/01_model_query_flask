# start by adding a new db in bash: createdb model_query
# mkdir model_query && cd model_query && touch model_query.py && code .

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello model query!"