"""
http://www.jimshapedcoding.com/courses/Flask%20Full%20Series
Styling framework (bootstrap this is the most) https://getbootstrap.com/docs/4.5/getting-started/introduction/
Templates (just name the template ex home.html) 
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
#@app.route('/home')
def home_page():
    """
    import render template from flask
    """
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)
