import pymongo  

client = pymongo.MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

collection = db['users']

# result = collection.update_one({"_id":1},{"$set":{"age":10,"name":"tom"}})

# result = collection.update_one({"_id":1},{"$set":{"say":"hello"}}) # add new field with $set

# result = collection.update_many({'_id':1},{"$inc":{"say":5}}) # add current field with $inc

result = collection.update_one({"name":"tim"},{"$set":{"say":"hello"}})

results = collection.find({})

for result in results:
	print(result)

