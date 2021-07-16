from flask import Flask,render_template
from flask_bootstrap import Bootstrap

# initialize your route
app = Flask(__name__)

# initialzie your bootstrap
bootstrap = Bootstrap(app)

@app.route('/')
def home_page():
    return render_template('bootstrap/base.html')

@app.route('/user')
def user_page():
    return render_template('users.html')

if __name__ == "__main__":
    app.run(debug = True)


