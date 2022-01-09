from flask import Flask,request
from flasgger import Swagger,swag_from

app = Flask(__name__)

'''
create a template for flasgger
'''
template = {
	"swagger":"2.0",
	"info":{
		"title":"Demo add function and offline document",
		"description": "Flask and FLasgger tutorial",
		"contact":{
			"responsibleOrganization":"github.com/Iteam1",
			"responsibleDeveloper":"LocChuong"
		},
		"version":"0.1",
		"basePath":"/api",
		"schemes": ["http","https"],
	}
}

# intergate swagger into your app
swagger = Swagger(app,template = template)

# add home.yml document you just write into this route
@app.route("/")
@swag_from("./docs/home.yml")
def home():
	return "Wellcome Anu!",200

'''
Send query with 2 arguments num1 , num2 return a sum of them
default method is GET, you can also use POST if you want,
Press ctrl + P for print out the pdf document
'''
@app.route("/add",methods = ['POST'])
@swag_from("./docs/add.yml")
def add():
	if request.args:
		args = request.args
		num1 = int(args['num1'])
		num2 = int(args['num2'])
		return f"{num1} + {num2} = {num1 + num2}",202
	else:
		return "Query invalid", 401

if __name__ == "__main__":
	app.run(debug = True)