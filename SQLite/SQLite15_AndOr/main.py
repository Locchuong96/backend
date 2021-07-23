import sqlite3 

conn = sqlite3.connect("./SQLite14_OrderBy/customer.db")

c = conn.cursor()

# c.execute("""
# SELECT rowid, *FROM customers WHERE last_name ="Loc" AND first_name LIKE 'Ch%'
# """)

c.execute("SELECT rowid, *FROM customers WHERE rowid = 4 OR first_name LIKE 'Jo%'")

items  = c.fetchall()

print(items)

conn.commit()

conn.close()