import pymongo

client = pymongo.MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

collection = db['users']

results = collection.delete_one({"_id":0})

# results = collection.delete_many({})

# results = collection.delete_many({"name":"loc"})

results =  collection.find({})

for result in results:
	print(result)

