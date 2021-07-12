from flask import Flask, render_template,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/custom/<user_name>/<user_age>")
def custom(user_name,user_age):
    return render_template('custom.html',your_name = user_name,your_age = user_age)

if __name__ == "__main__":
    app.run(debug = True)