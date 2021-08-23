from pymongo import MongoClient 

client = MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

coll = db['table']

docs = coll.find().sort('address',-1)

for doc in docs:
	print(doc)
