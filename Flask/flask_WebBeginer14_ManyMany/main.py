'''
If you want to use many-to-many relationships you will need to define a helper table that is used for the relationship,
For this helper table it is strongly recommended to not use a model but an actual table
'''
from flask import Flask,jsonify 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

db = SQLAlchemy(app)

tags = db.Table('tags',
                db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key = True),
                db.Column('page_id',db.Integer,db.ForeignKey('page.id'),primary_key = True)
                )

class Page(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    tags = db.relationship('Tag',secondary = tags, lazy =  'subquery',
    backref = db.backref('pages',lazy =True))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key =True)

if __name__ == "__main__":
    app.run(debug = True)