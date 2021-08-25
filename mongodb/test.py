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

data = db.users.find()

for user in data:
	print(user)
