from flask import Flask 
from flask_pymongo import PyMongo

app = Flask(__name__)

# pymongo connects to the mongoDB server running on port 27017 on local server, to the database named myDatabase

# mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

app.config['MONGO_URI'] = 'mongodb://localhost:27017/myDatabase'

mongo = PyMongo(app)

print(mongo)

