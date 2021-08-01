from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY'] = '508c0ff0a0184d8669ff5b34'
db = SQLAlchemy(app)

from market import routes