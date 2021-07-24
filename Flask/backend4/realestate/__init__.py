from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

#Create app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database/db1.db"

#Create database
db = SQLAlchemy(app)

#Create Json Marshmallow
ma = Marshmallow(app)

from realestate import routes
