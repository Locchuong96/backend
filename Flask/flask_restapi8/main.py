from flask import Flask, request 
from flask_restful import Resource,Api 

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    
    def get(self,name):
        return {'app_say':'Hello {}'.format(name)}
    
    def post(self):
        return {'app_say':'Posted!'}

api.add_resource(HelloWorld,"/<string:name>")

if __name__ == "__main__":
    app.run(debug = True)
