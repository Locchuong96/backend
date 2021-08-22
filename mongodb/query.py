import pymongo

client = pymongo.MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

collection = db['users']

# results = collection.find({"name":"loc"})

# results = collection.find({'_id':0})

# result = collection.find_one({"name":"loc"})
# print(result)

results = collection.find({})

for result in results:
	print(result)

