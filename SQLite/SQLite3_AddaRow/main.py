import sqlite3 

#connect to database 
conn = sqlite3.connect('./SQLite3_Addarow/customer.db')

#create a cursor
c = conn.cursor()

#add row
c.execute("INSERT INTO customers VALUES ('Mary','Brown','mary@codemy.com')")

conn.commit()

conn.close()
