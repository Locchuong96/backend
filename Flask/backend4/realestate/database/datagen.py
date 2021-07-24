import pandas as pd 
import sqlite3 

#Read excel file
df = pd.read_excel("./result.xlsx")
#Drop the Unname: 0
df = df.drop(["Unnamed: 0"],axis =1)
#Create a connect into database
conn = sqlite3.connect('db1.db')
#Make a cursor
c = conn.cursor()
#Create a table in database

c.execute(""" 
CREATE TABLE Realestate(
    id INTEGER PRIMARY KEY,
    image_link TEXT,
    title TEXT,
    address TEXT,
    orientation TEXT,
    detail_link TEXT,
    post_id TEXT,
    bathrooms INTEGER,
    bedrooms INTEGER,
    sqm FLOAT,
    lat FLOAT,
    long FLOAT,
    price FLOAT,
    sqm_price FLOAT,
    status TEXT
)
""")

for i in range(len(df)):
	#List the row
	l = list(df.loc[i])
	#Change type of integer numpy into python type
	l[6] = int(l[6]) #bathrooms
	l[7] = int(l[7]) #bedrooms
	l[12] =  float(l[12]) # sqm_price
	#Add id into id value
	l.insert(0,i)
	#Tuple list
	a = tuple(l)
	#Add into table
	print(i,"\n",a)
	c.execute("INSERT INTO Realestate VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",a)

	conn.commit()

conn.close()

print("Database exported!")

