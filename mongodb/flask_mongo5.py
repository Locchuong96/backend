from flask import Flask, Response,request
import pymongo
import json

#connect mongodb
try:
	#connect to client
	client = pymongo.MongoClient(
		host = "localhost",
		port = 27017,
		serverSelectionTimeoutMS = 3000
		)

	db = client.company #create database name company

	# mongo.server_info() # trigger exception if cannot connect to db 
	print(db)
except:
	print("ERROR: Can not connect into database! ")

app = Flask(__name__)

#get and post
@app.route("/users",methods = ['POST','GET'])
def users():
	if request.method == 'POST':
		try:
			user = {"_id": request.json['_id'], "name": request.json['name'], "lastName": request.json['lastName']}
			dbResponse = db.users.insert_one(user) # point to collection users
			return Response(
				response =  json.dumps({'message':'user created',"_id": request.json['_id']}),
				status = 200,
				mimetype = "application/json"
				)
		except Exception as ex:
			print(ex)
			return {'response':'fail to post'}
	else:
		try:
			data = db.users.find()
			data = list(data)

			return Response(
					response =  json.dumps(data),
					status = 202,
					mimetype = "application/json"
					)
		except Exception as ex:
			return {"message":"can not get"}

@app.route("/users/<id>",methods = ['PUT']) # or PATCH id must be string
def update_user(id):
	try:
		myquery = {"_id":int(id)}
		myvalue = {'$set':{'name':request.json['name']}}

		# print(request.json['name'])
		dbResponse = db.users.update_one(myquery,myvalue)

		return {"message": "updated!"}
	except Exception as ex:
		return {"message":"Can not update"}

if __name__ == "__main__":
	app.run(debug = True)