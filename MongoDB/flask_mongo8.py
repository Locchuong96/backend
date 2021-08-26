from flask import Flask, request, jsonify,make_response, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash,check_password_hash
from bson import json_util
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost/pythonmongodb"

client = PyMongo(app) # This is a table name pythonmongodb

#db name pythonmongodb

@app.errorhandler(404)
def not_found(error = None):
	message = {'message':'Resource Not Found ' + request.url,
				'status': 404}
	return jsonify(message)

@app.route("/users",methods = ['POST','GET'])
def create_user():

	if request.method == "POST":
		#Receiving data
		username = request.json['username']
		password = request.json['password']
		email = request.json['email']

		#if have enough data field
		if username and password and email:
			
			#generate the password hash
			hashed_password = generate_password_hash(password)
			
			#Add collector name users in database
			id = client.db.users.insert({ "username":username,"password":hashed_password,"email":email})

			#response
			response = make_response(
				jsonify({'_id': str(id),'username':username,'password':hashed_password,'email':email}),
				202
				)

			return response
		else:
			return not_found()

	else:
		users = client.db.users.find()

		print(users)

		response = json_util.dumps(users)

		return Response(response,mimetype= "application/json" )

@app.route("/users/<id>",methods = ['GET'])
def get_user(id):
	user = client.db.users.find_one({"_id":ObjectId(id)})
	response = json_util(user)
	return Response(response= response,mimetype = 'application/json')

@app.route("/users/<id>",methods = ['DELETE'])
def delete_user(id):
	user = client.db.users.delete_one({"_id":ObjectId(id)})
	return {"message":f" User {id} deleted!"}

# 6126856bcf476e8be67e3870
@app.route("/users/<id>",methods = ['PUT'])
def update_user(id):
	username = request.json['username']
	#password = request.json['password']
	email = request.json['email']

	myquery = {"_id":ObjectId(id)}
	myvalues = {"$set":{"username":username,"email":email}}

	client.db.users.update_one(myquery,myvalues)

	return {"message":"updated!"}

if __name__ == "__main__":
	app.run(debug = True)
