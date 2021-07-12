"""
Create a dynamic 
"""
from flask import Flask

app  = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello World</h1>'

"""
Dynamic route receive any string after the about page
"""
@app.route("/about/<user>")
def about_page(user):
    return f'<h1> This is about of {user}</h1>'

if __name__ == "__main__":
    app.run(debug = True)