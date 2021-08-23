from pymongo import MongoClient 

client = MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

coll = db['table']

# coll.drop() # drop collection

# client.drop_database('db1') # drop the database

print(client.list_database_names())