import pymongo  

client = pymongo.MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

collection = db['users']

post_count = collection.count_documents({})

print(post_count)

