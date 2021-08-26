from flask import Flask, Response,request
import pymongo
import json
# from bson.objectid import ObjectId # for ObjectID mongoDB

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

@app.route("/users",methods = ['POST','GET'])
def users():
	if request.method == 'POST':
		try:
			#user = {"name": request.form['name'], "lastName": request.form['lastName']}
			user = {"name": request.json['name'], "lastName": request.json['lastName']}
			dbResponse = db.users.insert_one(user) # point to collection users
			return Response(
				response =  json.dumps({'message':'user created',"id":f"{dbResponse.inserted_id}"}),
				status = 200,
				mimetype = "application/json"
				)
		except Exception as ex:
			print(ex)
			return {'response':'fail to post'}
	else:
		print("here")
		try:
			data = db.users.find()
			data = list(data)

			for user in data:
				user["_id"] = str(user["_id"])

			print(data)

			return Response(
					response =  json.dumps(data),
					status = 202,
					mimetype = "application/json"
					)
		except Exception as ex:
			return {"message":"fail to get"}

if __name__ == "__main__":
	app.run(debug = True)