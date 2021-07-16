# this is flask
from flask import Flask, render_template 
# this is the extension of flask
from flask_sqlalchemy import SQLAlchemy

# items = [ 
#             {'id':1,'name':'Phone'    ,'barcode':'893212299897','price':500},
#             {'id':2,'name':'Laptop'   ,'barcode':'123985473165','price':700},
#             {'id':3,'name':'Keyboard' ,'barcode':'231937483764','price':100},
#             {'id':4,'name':'Mouse'    ,'barcode':'423534443764','price':50},
#             {'id':5,'name':'Headphone','barcode':'554565544414','price':30},
#         ]

app = Flask(__name__)
#This statement make a database into app, URI standfor Uniform Resource Identifier
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
#Create a database
my_db = SQLAlchemy(app)
#Create model name item
class Item(my_db.Model):
    id          = my_db.Column(my_db.Integer()          ,primary_key = True            ) # identify is primary key
    name        = my_db.Column(my_db.String(length=30)  ,nullable = False,unique = True)
    price       = my_db.Column(my_db.Integer()          ,nullable = False              )
    barcode     = my_db.Column(my_db.String(length=12)  ,nullable = False,unique = True)
    descript    = my_db.Column(my_db.String(length=1024),nullable = False,unique = True)

    def __repr__(self):
        return f'Item {self.name}'

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items = items)

if __name__ == "__main__":
    app.run(debug = True)
