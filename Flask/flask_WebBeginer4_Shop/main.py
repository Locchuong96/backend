from flask import Flask,render_template
from werkzeug.exceptions import abort 

products = {
    'ipad_mini': {'name':'IPad Mini','category':'Tablets','price':'549'},
    'iphone'   : {'name':'Iphone 5S','category':'Phones','price':'699'},
    'samsung'  : {'name':'Samsung Galaxy 5','category':'Phones','price':'649'},
    'ipad_air' : {'name':'IPad Air','category':'Tablets','price':'629'}
}

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html',items = products)

@app.route('/product/<key>')
def product(key):
    your_product = products.get(key)
    
    if not your_product:
        abort(404)

    return render_template('product.html', item = your_product)


if __name__ == "__main__":
    app.run(debug = True)