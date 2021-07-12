#1/ import library
from flask import Flask, render_template

#2/ create your app
app = Flask(__name__)

#3/ create a route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',my_name = name)

#4/ Run app route
if __name__ == '__main__':
    app.run(debug = True)