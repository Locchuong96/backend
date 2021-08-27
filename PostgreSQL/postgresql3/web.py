from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

#'postgresql://postgres:superuser@localhost/users'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:superuser@localhost/students'
db = SQLAlchemy(app)
# Create model
class Student(db.Model):
    __tablename__ = 'students'
    id    = db.Column(db.Integer,primary_key = True)
    fname = db.Column(db.String(60),nullable = False)
    lname = db.Column(db.String(60),nullable = False)
    age   = db.Column(db.Integer,nullable = False)
    gpa   = db.Column(db.Float)

    def __init__(self,fname,lname,age,gpa):
        self.fname = fname
        self.lname = lname
        self.age   = age  
        self.gpa   = gpa 
 
# CRUD
# CREATE - POST
@app.route("/",methods = ['GET'])
def home():
    return render_template('index.html')

@app.route("/add_student", methods = ['POST'])
def add_student():
    fname = request.form['fname']
    lname = request.form['lname']
    age   = request.form['age']
    if request.form['gpa']:
        gpa  = request.form['gpa']
    else:
        gpa = None

    student = Student(fname = fname,lname = lname,age = age,gpa = gpa)
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('home'))

# READ - GET
@app.route("/get_student/<int:id>",methods =['GET'])
def get_student(id):
    result = Student.query.get(id)
    return render_template('result.html',student= result)

# UPDATE - PUT
@app.route("/update_update",methods = ['GET','POST'])
def update_student():
    if request.method == 'POST':
        #Get the student by the id in the dabase
        student = Student.query.get(request.form['id'])  
        #Get the infomation in the form
        if request.form['fname']:
            student.fname= request.form['fname']
        if request.form['lname']:
            student.lname= request.form['lname']
        if request.form['age']:
            student.age= request.form['age']
        if request.form['gpa']:
            student.gpa= request.form['gpa']
        # commit
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('update.html')

# DELETE - DELETE
@app.route("/delete_student/<int:id>",methods =['GET'])
def delate_student(id):
    result = Student.query.get(id)
    db.session.delete(result)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug = True)