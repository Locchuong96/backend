from flask import Flask, render_template 

def load_user(id):
    users = {
        "1" : "Tom"  ,
        "2" : "Jimmy",
        "3" : "Emily",
        "4" : "Daine",
        "5" : "Harry"
    }
    return users.get(id)

my_list =['Jimmy',"Henry","Tommy","Emily","Kelly","June"]
my_comment =["Good","Not Bad","Bad","Really Good","Great!"]
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<id>')
def user(id):
    name = load_user(id)
    return render_template('user.html',name = name)

@app.route('/list')
def list():
    return render_template('list.html',list =my_list)

@app.route('/comment2')
def macro2():
    return render_template('comment2.html',comments = my_comment)

@app.route('/comment1')
def macro1():
    return render_template('comment1.html',comments = my_comment)

@app.route('/inheritane')
def inheritane():
    return render_template('inheritane.html')

if __name__ == ("__main__"):
    app.run(debug = True)