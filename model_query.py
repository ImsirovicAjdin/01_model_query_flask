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

# 13. Verify that the `users` table exists
# ```
# \dt # shows the `users` table is there
# ```
# PRACTICALLY:
# model_query=# \dt
#        List of relations
#  Schema | Name  | Type  | Owner 
# --------+-------+-------+-------
#  public | users | table | pc
# (1 row)

# model_query=# 

# 14. Verify the structure of the `users` table
# ```
# \d users # shows the structure of the `users` table
# ```
# PRACTICALLY
# model_query=# \d users
#                                  Table "public.users"
#  Column |       Type        | Collation | Nullable |              Default              
# --------+-------------------+-----------+----------+-----------------------------------
#  id     | integer           |           | not null | nextval('users_id_seq'::regclass)
#  name   | character varying |           | not null | 
# Indexes:
#     "users_pkey" PRIMARY KEY, btree (id)

# model_query=# 

# 15. Insert some name into the `users` tbale
# ```
# INSERT INTO users (name) VALUES (`Albert Einstein`);
# ```
# PRACTICALLY:
# pc@pc:~/001-FSWD-UND-NEW/02_model_query$ psql model_query 
# psql (12.6 (Ubuntu 12.6-0ubuntu0.20.04.1))
# Type "help" for help.

# model_query=# INSERT INTO users (name) VALUES ('Albert Einstein');
# INSERT 0 1
# VERIFICATION:
# model_query=# select * from users;
#  id |      name       
# ----+-----------------
#   1 | Albert Einstein
# (1 row)

# model_query=# 
