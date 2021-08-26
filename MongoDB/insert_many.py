import pymongo

client = pymongo.MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

collection = db['users']

post_list = [{'_id':3,'name':'john','age':12},{'_id':4,'name':'kendy','age':30}]

collection.insert_many(post_list)