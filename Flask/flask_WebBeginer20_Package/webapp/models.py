from datetime import datetime 
from webapp import db,ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20),unique = True, nullable = False)
    passord = db.Column(db.String(60),nullable = False)
    email = db.Column(db.String(100),nullable = False)
    image_file = db.Column(db.String(40),nullable = False, default = 'default.jpg')
    posts = db.relationship('Post',backref = 'author',lazy = True)

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    date_posted = db.Column(db.DateTime,nullable = False, default = datetime.utcnow())
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.id}','{self.title}','{self.date_posted}')"

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    image_file = ma.auto_field()

class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Post
        _include_sqlalchemy = True

    id = ma.auto_field()
    title = ma.auto_field()
    date_posted = ma.auto_field()