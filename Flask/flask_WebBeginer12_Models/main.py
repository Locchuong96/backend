from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow

app = Flask(__name__)

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80),unique = True, nullable = False)
    email =db.Column(db.String(120),unique = True,nullable = False )

    def __repr__(self):
        return "<User %r>" % self.username

if __name__ == "__main__":
    app.run(debug = True)




