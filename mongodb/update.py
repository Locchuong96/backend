from pymongo import MongoClient 

client = MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

coll = db['table']

myquery = {'name':{'$regex':'^M'}}

myvalue = {'$set':{'address':'Mansion Street 105'}}

results = coll.find(myquery)

print("Before update: \n")

for result in results:
	print(result)

# coll.update_one(myquery,myvalue)

coll.update_many(myquery,myvalue)

results = coll.find(myquery)

print("After update \n")

for result in results:
	print(result)