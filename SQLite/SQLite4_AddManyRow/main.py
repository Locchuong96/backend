import sqlite3 

conn = sqlite3.connect("./SQLite4_AddManyRow/customer.db")

c = conn.cursor()

many_customer = [('Wes','Brown','wes@brown.com'),
                ('Steph','Kuewa','steph@kuewa.com'),
                ('Dan','Pas','dan@pas.com'),
                ]

c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customer)

print("Completed Add Many Rows")

conn.commit()

conn.close()