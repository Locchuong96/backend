from flask import Flask, jsonify 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///site.db"

db = SQLAlchemy(app)

class Author(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(255))
    books = db.relationship("Book",backref = "books")

    def __repr__(self):
        return f"Author(''{self.id}',{self.name}')"

class Book(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer,db.ForeignKey("author.id"))
    #author =db.relationship("Author",backref = "author")

    def __repr__(self):
        return f"Book('{self.id}','{self.title}','{self.author_id}')"
