from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#connect to postgredatabase
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/students'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:superuser@localhost/students'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key = True)
    fname = db.Column(db.String(40),nullable = False)
    lname = db.Column(db.String(40),nullable = False)
    pet = db.Column(db.String(40))

    def __init__(self,fname,lname,pet):
        self.fname = fname
        self.lname = lname
        self.pet = pet

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods = ['POST'])
def submit():
    # get the infomation of the form
    fname = request.form['fname']
    lname = request.form['lname']
    pet = request.form['pets']
    #create a student 
    student = Student(fname = fname,lname= lname,pet = pet)
    #query
    student_result = db.session.query(Student).filter(Student.id == 1)
    #add to database
    db.session.add(student)
    db.session.commit()
    return render_template('success.html',name = lname)


if __name__ == "__main__":
    app.run(debug = True)