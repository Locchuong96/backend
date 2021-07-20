from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog1.db"
db = SQLAlchemy(app)
ma = Marshmallow(app)

from webapp import routes