"""
set FLASK_APP = market.py
flask run
"""
from flask import Flask

app = Flask(__name__)

# This is a decorator in python
@app.route('/')
def hello_world():
    return "Helo world!"

if __name__ == "__main__":
    app.run()
