import sqlite3 

#Make a connection
conn = sqlite3.connect('customer.db')

#Create a cursor
c = conn.cursor()

#Create a Table by doc string and define the table
c.execute("""
CREATE TABLE customers (
first_name text,
last_name text,
email text
)
""")

#Commit our command
conn.commit()

#Close the connection
conn.close()


