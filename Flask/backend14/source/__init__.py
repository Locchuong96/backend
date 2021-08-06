from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import  Marshmallow
from flask_cors import  CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database/db1.db"

'''
Allow all routes and resources r"/*" can access by any domain else
'''

cors = CORS(app,resources = {
	r"/*": {"origins":"*"}
	})

db = SQLAlchemy(app)

ma = Marshmallow(app)

from source import routes