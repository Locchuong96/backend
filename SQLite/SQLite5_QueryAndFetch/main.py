import sqlite3

conn = sqlite3.connect("./SQLite5_QueryAndFetch/customer.db")

c = conn.cursor()

#Select (Query) execute
# c.fetchone
# c.fetchmany(3)
# c.fetchall()

c.execute("SELECT * FROM customers")

print(c.fetchmany(2))

conn.commit()

conn.close()