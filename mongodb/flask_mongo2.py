from flask import Flask, Response
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

@app.route("/users",methods = ['POST'])
def create_user():
	try:
		user = {"name": "A", "lastname": "AA"}
		dbResponse = db.users.insert_one(user) # point to collection users
		# print(dbResponse.inserted_id)
		# for attr in dir(dbResponse): # return a list of function or class
		return Response(
			response =  json.dumps({'message':'user created',"id":f"{dbResponse.inserted_id}"}),
			status = 200,
			mimetype = "application/json"
			)
	except Exception as ex:
		print(ex)
		return {'response':'fail'}

if __name__ == "__main__":
	app.run(debug = True)