from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route("/")
def home():
	return "HomePage",200


@app.route("/query")
def query():

	#127.0.0.1:5000/query?foo=foo&bar=bar&baz=baz&title=query+strings+with+flask

	# args = request.args

	# for k,v in args.items():
	# 	print(f"{k} : {v}")

	# if "foo" in args:
	# 	foo = args.get("foo")
	# 	print(foo)

	# if request.args:
	# 	args = request.args
	# 	return args,202

	# if request.args:
	# 	args = request.args
	# 	if "title" in args:
	# 		title = args.get('title')
	# 		#print(type(title))
	# 		return title,202

	if request.args:
		args = request.args 
		serialized = ", ".join(f"{k} : {v}" for k, v in args.items())

		return serialized,202		

	else:
		return "Query received", 204

if __name__ == "__main__":
	app.run(debug = True)


