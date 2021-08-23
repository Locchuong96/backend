from flask import Flask 
from flask_restful import Resource,Api,reqparse,abort,fields,marshal_with

app = Flask(__name__)

api = Api(app)

app.config['MONODB_SETTINGS'] = {
	'db':'todomodel',
	'host':'localhost',
	'port':27017
}

db.MongoEngine()

db.init_app(app)