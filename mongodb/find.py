from pymongo import MongoClient 

client = MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

coll = db['table']

#query = {"name":"John"}

query = {"name":{"$regex":"^S"}} # Using regex find all name start with S

#results = coll.find_one(my_query)
results = coll.find(query)

for result in results:
	print(result)