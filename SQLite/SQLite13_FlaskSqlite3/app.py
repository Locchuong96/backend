from flask import Flask, jsonify,request 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db = SQLAlchemy(app)

#create a class
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40),nullable = False)
    age = db.Column(db.Integer, nullable = False)
    score = db.Column(db.Float)

    def __repr__(self):
        return f"User('{self.name}','{self.age}','{self.score}')"

ma = Marshmallow(app)

class User_Schema(ma.SQLAlchemySchema):
    
    class Meta:
        model =User

    id = ma.auto_field()
    name = ma.auto_field()
    age = ma.auto_field()
    score = ma.auto_field()

user_schema = User_Schema()
users_schema = User_Schema(many = True)

@app.route("/",methods = ['GET'])
def base():
    return jsonify({"msg":"Hello World!"})

@app.route("/User",methods = ['GET'])
def get_all():
    users = User.query.all()
    return users_schema.jsonify(users)

@app.route("/User/<int:id>",methods = ['GET'])
def get_one(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@app.route("/User",methods = ['POST'])
def create():
    name = request.json["name"]
    age  = request.json["age"]
    score = request.json["score"]
    new = User(name = name,age = age, score = score) 
    db.session.add(new)
    db.session.commit()
    return user_schema.jsonify(new)

@app.route("/User/<int:id>",methods =['PUT'])
def update(id):
    user=  User.query.get(id)
    name = request.json["name"]
    age = request.json["age"]
    score = request.json["score"]
    user.name = name
    user.age = age 
    user.score = score
    db.session.commit()

    return user_schema.jsonify(user)

@app.route("/User/<int:id>",methods = ['DELETE'])
def remove(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

if __name__ == "__main__":
    app.run(debug = True)
