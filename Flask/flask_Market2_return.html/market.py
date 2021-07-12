"""
"/" is rule
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello Change text</h1>'

if __name__ == "__main__":
    """
    Turn on the debug mode and you will never start your web server again
    Save it and reload
    """
    app.run(debug = True)
