"""
http://www.jimshapedcoding.com/courses/Flask%20Full%20Series
Sending a data from template
Jinja is a web templating systax we can use to access the html,designed for python web framework
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
"""
Try to send some random data into this route
"""
@app.route('/market')
def market_page():
    #return render_template('market.html')
    return render_template('market.html',item_name ='Phone')

if __name__ == "__main__":
    app.run(debug = True)
