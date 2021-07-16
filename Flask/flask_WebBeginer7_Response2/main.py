"""
Instead for returning one, two, or three values as a tuple,
Flask view functions have the option of returning a response object, make_response()
"""
from flask import Flask, make_response

app = Flask(__name__)
@app.route('/')
def index():
    response = make_response('<h1>This is document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

if __name__=="__main__":
    app.run(debug = True)