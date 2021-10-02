from flask import Flask, jsonify 
from flasgger import Swagger 

app = Flask(__name__)

template = {
    "swagger":"2.0",
    "info":{
        "title": "My API",
        "description":"API for my data",
        "contact":{
            "responsibleOrganization":"ME",
            "responsibleDeveloper": "Me",
            "email": "me@me.com",
            "url":"www.me.com",
        },
        "termsOfService":"http://me.com/terms",
        "version":"0.0.1",
    },
    "host": "mysite.com",
    "basePath": "/api",
    "schemes":["http","https"],
    "operationId":"getmyData"
}
swagger = Swagger(app,template = template)

if __name__ == "__main__":
    app.run(debug = True)