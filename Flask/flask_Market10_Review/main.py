from flask import Flask, render_template 

items = [ 
            {'id':1,'name':'Phone'    ,'barcode':'893212299897','price':500},
            {'id':2,'name':'Laptop'   ,'barcode':'123985473165','price':700},
            {'id':3,'name':'Keyboard' ,'barcode':'231937483764','price':100},
            {'id':4,'name':'Mouse'    ,'barcode':'423534443764','price':50},
            {'id':5,'name':'Headphone','barcode':'554565544414','price':30},
        ]

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    return render_template('market.html',items = items)

if __name__ == "__main__":
    app.run(debug = True)
