import sqlite3

# Query and return all
def show_all():   

    conn = sqlite3.connect('./SQLite18_Function/customer.db')

    c = conn.cursor()

    c.execute("SELECT rowid,*FROM customers")

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()

    conn.close()

# Add a row
def add_one(first_name,last_name,email):

    conn = sqlite3.connect('./SQLite18_Function/customer.db')

    c = conn.cursor()

    #command = "INSERT INTO customers VALUES (?,?,?)",(first_name,last_name,email)

    command = "INSERT INTO customers VALUES ('{0}','{1}','{2}')".format(first_name,last_name,email)
    
    c.execute(command)
    
    conn.commit()

    conn.close()

# Add many row
def add_multi(many_data):

    conn = sqlite3.connect('./SQLite18_Function/customer.db')

    c = conn.cursor()

    command = "INSERT INTO customers VALUES (?,?,?)"
    
    c.executemany(command,many_data)
    
    conn.commit()

    conn.close()

# Add many row
def delete(id):

    conn = sqlite3.connect('./SQLite18_Function/customer.db')

    c = conn.cursor()

    #c.execute("DELETE FROM customers WHERE rowid = (?)",id)

    c.execute("""
    DELETE FROM customers WHERE rowid = {}
    """.format(id))
    
    conn.commit()

    conn.close()

#Lookup mail
# Query and return mail
def email_lookup(email):   

    conn = sqlite3.connect('./SQLite18_Function/customer.db')

    c = conn.cursor()

    c.execute("SELECT rowid,*FROM customers WHERE email LIKE '%{}'".format(email))

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()

    conn.close()
