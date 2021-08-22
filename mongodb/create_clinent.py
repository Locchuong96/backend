import pymongo  

client = pymongo.MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

collection = db['users']

post = {'_id':2,'name':'tim','age':106}

collection.insert_one(post)

print('success post the record!')