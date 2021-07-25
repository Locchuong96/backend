from flask import Flask,render_template, jsonify, request 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime 

# intit app, database, marshmallow
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Define models
class Store(db.Model):
    store_id = db.Column(db.Integer, primary_key = True)
    store_name = db.Column(db.String(30),unique = True)
    store_location = db.Column(db.String(100),unique = True)
    # Not display this relationship on table store
    purchases = db.relationship('Purchase',backref = 'store')

    def __repr__(self):
        return f"Store('{self.store_id}','{self.store_name}','{self.store_location}')"

class Purchase(db.Model):
    purchase_id = db.Column(db.Integer, primary_key = True)
    total = db.Column(db.Float,nullable = False)
    store_id = db.Column(db.Integer,db.ForeignKey("store.store_id"),nullable = False)

    def __repr___(self):
        return f"Purchase('{self.purchase_id}','{self.total},'{self.store_id}'"

class Store_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Store
        _include_sqlalchemy = True
    
    store_id = ma.auto_field()
    store_name = ma.auto_field()
    store_location = ma.auto_field()
    purchases = ma.auto_field()

store_schema = Store_Schema()
stores_schema = Store_Schema(many= True)

class Purchase_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Purchase
        _include_sqlalchemy = True

        purchase_id = ma.auto_field()
        total = ma.auto_field()
        store_id = ma.auto_field()
        store = ma.auto_field()

purchase_schema = Purchase_Schema()
purchases_schema = Purchase_Schema(many= True)

@app.route("/")
def home():
    return jsonify({"msg":"Hello World!"})

@app.route("/stores",methods = ['GET'])
def get_store():
    stores = Store.query.all()
    return render_template('submit_store.html')

@app.route("/stores",methods = ['POST'])
def add_store():
    store_form = request.form.values()
    #list the from 
    store_form = list(store_form)
    store_name = str(store_form[0])
    store_location = str(store_form[1])
    
    new_store = Store(store_name = store_name,store_location = store_location)
    db.session.add(new_store)
    db.session.commit()
    
    return render_template('submit_store.html',new_store = str(datetime.utcnow()) + " Add Store Success")

@app.route("/purchases",methods = ['GET'])
def get_purchase():
    return render_template('submit_purchase.html')

@app.route("/purchases",methods = ['POST'])
def add_purchase():
    purchase_form = request.form.values()
    
    purchase_form = list(purchase_form)
    store_id = int(purchase_form[0])
    total = float(purchase_form[1])
    
    new_purchase = Purchase(store_id = store_id, total = total)
    db.session.add(new_purchase)
    db.session.commit()
    
    return render_template('submit_purchase.html',new_purchase = str(datetime.utcnow()) + " Add Purchase Success")

if __name__ == "__main__":
    app.run(debug=True)