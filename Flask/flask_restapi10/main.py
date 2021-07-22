from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

users = {"Tim"  : {"age":20, "gender": "male"},
        "Bill" : {"age":30, "gender": "male"},
        "Jam"  : {"age":24, "gender": "male"},
        "Lisa" : {"age":56, "gender": "female"}
}

class User(Resource):
    def get(self,name):
        return users[name]

api.add_resource(User,"/user/<string:name>")

if __name__ == "__main__":
    app.run(debug = True)
