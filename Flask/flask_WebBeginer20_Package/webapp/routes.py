from webapp.models import User, Post
from webapp.models import UserSchema, PostSchema
from webapp import app, ma

user_schema = UserSchema()
users_schema = UserSchema(many = True)

post_schema = PostSchema()
posts_schema = PostSchema(many = True)

@app.route("/")
def index():
    return "<h3>Hello Worlds</h3>"

@app.route("/user",methods = ["GET"])
def get_all():
    users = User.query.all()
    return users_schema.jsonify(users)

@app.route("/user/<int:id>",methods = ["GET"])
def get_one(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)
    
    


