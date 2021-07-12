"""
Display multible value with jinja syntax, change the infomation into a list
http://www.jimshapedcoding.com/courses/Flask%20Full%20Series
Sending a data from template
Jinja is a web templating systax we can use to access the html,designed for python web framework
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
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
    """
    Add a dynamics to
    """
    items = [ 
                {'id':1,'name':'Phone'   ,'barcode':'893212299897','price':500},
                {'id':2,'name':'Laptop'  ,'barcode':'123985473165','price':700},
                {'id':3,'name':'Keyboard','barcode':'231937483764','price':100},
            ]
    return render_template('market.html',items = items)

if __name__ == "__main__":
    app.run(debug = True)
