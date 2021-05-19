# start by adding a new db in bash: createdb model_query
# mkdir model_query && cd model_query && touch model_query.py && code .

from flask import Flask # 01. Import flask
from flask_sqlalchemy import SQLAlchemy # 05. Import the SQLAlchemy module

app = Flask(__name__) # 02. Instantiate the app
db = SQLAlchemy(app) # 06. Instantiate the db and pass in this flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///model_query' # 08. Connect to the db from our Flask app (by setting a configuration variable)

# 09. Add a User class that inherits from db.Model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

@app.route('/') # 03. With at app decorator, listen to root route
def index(): # 04. Define the index method...
    return "Hello model query!" # 04. ... and return a string from it

db.create_all() # 10. With db.create_all, create tables in our db for all the models that we have decalres using db.Model previously

# 11. Run the app with FLASK_APP=model_query.py FLASK_DEBUG=true flask run (open on localhost:5000)

# 12. Run psql
# ```
# psql model_query
# ```