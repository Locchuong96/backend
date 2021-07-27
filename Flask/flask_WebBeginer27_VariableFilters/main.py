from flask import Flask,render_template 

app = Flask(__name__)

def my_function():
    return True

@app.route("/")
def index():
    return render_template('index.html', var1 = my_function )

if __name__ == "__main__":
    app.run(debug = True)