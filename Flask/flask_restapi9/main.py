from flask import Flask,request 
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self,name,age):

        return {"app_say":"Hello {0} You are {1}".format(name,age)}

api.add_resource(HelloWorld,"/<string:name>/<int:age>")

if __name__ == "__main__":
    app.run(debug = True)