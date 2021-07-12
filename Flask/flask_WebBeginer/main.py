#1/ import required library
from flask import Flask,render_template 

#2/ create a root
app = Flask(__name__)

#3/ Create route
@app.route("/")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)
