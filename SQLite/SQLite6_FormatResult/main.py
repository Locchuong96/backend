import sqlite3

conn = sqlite3.connect('./SQLite6_FormatResult/customer.db')

c = conn.cursor()

c.execute("SELECT * FROM customers")

# print(type(c.fetchone()))
# print(c.fetchone())

# a = c.fetchone()
# print(a[0])

# items = c.fetchall()
# for item in items:
#     print(item)

items = c.fetchall()
for item in items:
    print(item[0]+ "\t" + item[1] + "\t" +item[2])

conn.commit()

conn.close()