import pymongo  

client = pymongo.MongoClient('mongodb+srv://loc:1234@cluster0.clyd6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['db1']

coll = db['table']

docs = [
{"id":1,"name":"John","address":"Highway 37"},
{"id":2,"name":"Peter","address":"Lowstreet 27"},
{"id":3,"name":"Amy","address":"Apple st 652"},
{"id":4,"name":"Hannah","address":"Mountain 21"},
{"id":5,"name":"Michael","address":"Valley 345"},
{"id":6,"name":"Sandy","address":"Ocean blvd 2"},
{"id":7,"name":"Betty","address":"Green Grass 1"},
{"id":8,"name":"Richard","address":"Sky st 331"},
{"id":9,"name":"Susan","address":"One way 98"},
{"id":10,"name":"Vicky","address":"Yellow Garden 2"},
{"id":11,"name":"Ben","address":"Park Lane 38"},
{"id":12,"name":"William","address":"Central st 954"},
{"id":13,"name":"Chunk","address":"Main Road 989"},
{"id":14,"name":"Viola","address":"Sideway 1633"},
]

x = coll.insert_many(docs)

dblist = client.list_database_names()

if input('Enter DB: ') in dblist:
	print("The table exists")
else:
	print("Not Present!")

print(dblist)


