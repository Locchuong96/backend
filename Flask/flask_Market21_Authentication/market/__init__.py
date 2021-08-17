from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"

app.config['SECRET_KEY'] = 'a8de3250642b130bd575c88a'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from market import routes