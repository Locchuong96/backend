"""
for more information: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#models
"""
from flask import Flask, jsonify 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    '''
    Go to the Address table and take values or value in it, return it into addresses
    backref is a simple way to also declare a new prop
    '''
    addresses = db.relationship('Address',backref = "person",lazy = True)

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(50),nullable = False)
#     addresses = db.relationship('Address',lazy = 'select',backref = db.backref('person',lazy = 'joined'))

class Address(db.Model):
    '''
    db.relationship() function returns a new property that can do multiple  things 
    SQLAlchemy guesses a useful defualt from your declaration
    If you want to have a one-one relationship you can pass uselist = Fasle to relationship()
    '''
    id = db.Column(db.Integer,primary_key = True)
    person_id = db.Column(db.Integer,db.ForeignKey('person.id'),nullable = False) 
    email = db.Column(db.String(120),nullable = False)

if __name__ == "__main__":
    app.run(debug = True)


    

