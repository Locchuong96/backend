from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy, _include_sqlalchemy
from flask_marshmallow import Marshmallow 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    
class Reward(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    reward_name = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User",backref = "rewards")

# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('id','name') 
#  
# class RewardSchema(ma.Schema):
#     class Meta:
#         fields = ('id','reward_name','user_id')

# class UserSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = User  
#   
# class RewardSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Reward

# class UserSchema(ma.SQLAlchemyAutoSchema):
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    rewards = ma.auto_field()

class RewardSchema(ma.SQLAlchemySchema):
#class RewardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reward
        _include_sqlalchemy = True

user_schema = UserSchema()
users_schema = UserSchema(many =True) 

reward_schema = RewardSchema()
rewards_schema = RewardSchema(many =True) 

@app.route("/")
def index():
    return jsonify({'in':'progress'})

@app.route("/user",methods = ["GET"])
def get_all():
    users = User.query.all()
    return users_schema.jsonify(users)

@app.route("/user/<int:id>", methods = ["GET"])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

if __name__ == "__main__":
    app.run(debug = True)

