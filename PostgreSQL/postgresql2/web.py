from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

#create datbase                                      #owner    #password           #database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:superuser@localhost/users'
db = SQLAlchemy(app)

#Create model for user table
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(40),nullable= False)
    email = db.Column(db.String(60),nullable = False)

    def __init__(self,username,email):
        self.username = username
        self.email = email 


@app.route("/", methods = ['GET'])
def resigter():
    return render_template('index.html')

@app.route("/submit",methods = ['POST'])
def submit():
    #read info from form
    username = request.form['username']
    email = request.form['email']
    #create user
    user = User(username = username, email= email)
    #add to database
    db.session.add(user)
    db.session.commit()

    return render_template('success.html',name= username)

if __name__ == "__main__":
    app.run(debug = True)