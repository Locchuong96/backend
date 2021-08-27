from flask import Flask,render_template, request, redirect, url_for,Flask
import psycopg2
import psycopg2.extras

app = Flask(__name__)

DB_HOST = 'localhost'
DB_NAME = 'students'
DB_USER = 'postgres' #owner
DB_PASS = 'superuser'

# create a conncect
conn = psycopg2.connect(dbname = DB_NAME,user = DB_USER, password = DB_PASS, host = DB_HOST)

@app.route("/",methods = ['GET'])
def home():
    #create a cursor
    cur = conn.cursor(cursor_factory= psycopg2.extras.DictCursor)
    s = """
        SELECT * FROM students
        """
    cur.execute(s) # execute the query
    students = cur.fetchall()
    return render_template('index.html', students = students)

if __name__ == "__main__":
    app.run(debug = True)



