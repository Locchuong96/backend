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

@app.route("/add_student",methods = ['GET','POST'])
def add():
    if request.method == 'POST':
        # create a cursor
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        # read data from a form
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        gpa = request.form['gpa']
        # create a query and execute it
        cur.execute("INSERT INTO students (fname,lname,age,gpa) VALUES (%s,%s,%s,%s)",(fname,lname,age,gpa))
        # commit to the connection
        conn.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add_new.html')

@app.route("/delete/<int:id>",methods = ['GET'])
def delete_student(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("DELETE FROM students WHERE id = {}".format(id))
    conn.commit()
    return redirect(url_for('home'))

@app.route("/edit/<id>",methods = ['GET'])
def edit_student(id):
    #create a cursor
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    #execute , doesn't take string
    cur.execute('SELECT * FROM students WHERE id = {}'.format(id)) 
    data = cur.fetchall()
    cur.close()
    student = data[0]
    #print(student)
    return render_template('update.html',student = student)

@app.route("/update/<int:id>",methods = ['POST'])
def update_student(id):

    # get student
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    #execute , doesn't take string
    cur.execute('SELECT * FROM students WHERE id ='+str(id)) 
    data = cur.fetchall()
    cur.close()
    student = data[0]
    print(student[0])
    
    # update infomation
    if request.form['fname']:
        fname = request.form['fname']
    else:
        fname = student[1]

    if request.form['lname']:
        lname = request.form['lname']
    else:
        lname = student[2]
    
    if request.form['age']:
        age = request.form['age']
    else:
        age = student[3]

    if request.form['gpa']:
        gpa = request.form['gpa']
    else:
        gpa = student[4]
    
    # create a cursor
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    
    # execute
    cur.execute("""
    UPDATE students
    SET fname = %s,
        lname = %s,
        age   = %s,
        gpa   = %s
    WHERE id  = %s
    """,(fname,lname,age,gpa,id))
    
    conn.commit()
    
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug = True)



