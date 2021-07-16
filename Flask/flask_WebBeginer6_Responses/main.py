from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Bad Request</h1>'

if __name__ == "__main__":
    app.run(debug = True)