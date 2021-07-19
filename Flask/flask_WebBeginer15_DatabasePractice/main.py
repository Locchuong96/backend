from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#app.config['SECRET_KEY']  ='fs5345fsdfsdfsf45643'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

'''
Create a one to many relationship
Because one user can have so many post, but the post can only one author
'''

"""
Post,User: referencing to table name
user.id  : referencing to table name "user" and to the column "id"
"""
#Create a post table
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120),unique = True, nullable = False)
    image_file = db.Column(db.String(20),nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60),nullable = False)
    """
    One to many relationship , THIS IS NOT a column
    'Post'  : meaning point to a Post model
    backref : adding another column  name 'author' to the post POST model,
    When we created a post, we can simply use author attribute to get the user who created the post
    lazy : define when SQL alchemy loads the database
    """
    posts = db.relationship('Post',backref = 'author',lazy = True)

    def __repr__(self):
        '''
        This specifically is how a object in table is printed
        '''
        return f"User('{self.username}','{self.email}','{self.image_file}')"

# Create Post table
class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title =db.Column(db.String(100),nullable = False)
    date_posted = db.Column(db.DateTime,nullable = False,default = datetime.utcnow())
    content =db.Column(db.Text,nullable = False)
    """
    Create a user_id column to the post relationship
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"






