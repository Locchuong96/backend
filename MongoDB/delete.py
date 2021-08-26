from pymongo import MongoClient 

client = MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

coll = db['table']

query = {'name':{'$regex':'^S'}}

#docs = coll.delete_one(query) # delete one row
docs = coll.delete_many(query) # deleting specific single record

for record in coll.find():
	print(record)