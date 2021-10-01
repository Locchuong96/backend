from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restplus import Api,fields,Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['SERECT_KEY'] = True 

db =  SQLAlchemy(app)

ma = Marshmallow(app)

api = Api()
api.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','password')

user_schema = UserSchema()
users_schema = UserSchema(many= True)

# @app.route('/')
# def get():
#     return 'ok'

@api.route('/get')
class getdata(Resource):
    def get(self):
        return {'message':'working'}

@api.route('/post')
class postdata(Resource):
    def post(self):
        return {'message':'working'}

@api.route('/put/<int:id>')
class putdata(Resource):
    def put(self,id):
        return {'message':id}

@api.route('/delete/<int:id>')
class deletedata(Resource):
    def delete(self,id):
        return {'message':id}

if __name__ =="__main__":
    app.run(debug=True)