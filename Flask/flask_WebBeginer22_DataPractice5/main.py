from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Stores(db.Model):
    store_id = db.Column(db.Integer, primary_key = True)
    store_name = db.Column(db.String(40),nullable = False)
    store_location = db.Column(db.String(100),nullable = False)
    purchases = db.relationship("Purchases",backref = "store")

    def __repr__(self):
        return f"Store('{self.store_id}','{self.store_name}','{self.store_location}')"

class Purchases(db.Model):
    purchase_id = db.Column(db.Integer,primary_key = True)
    total = db.Column(db.Float,nullable = False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))

    def __repr__(self):
        return f"Purchase('{self.purchase_id}','{self.total}','{self.store_id}')"

class Store_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Stores

    store_id = ma.auto_field()
    store_name = ma.auto_field()
    store_location = ma.auto_field()
    purchases = ma.auto_field()

class Purchase_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Purchases
        _include_sqlalchemy = True

    purchase_id = ma.auto_field()
    total = ma.auto_field()
    store_id = ma.auto_field()

store_schema = Store_Schema()
stores_schema = Store_Schema(many = True)

purchase_schema = Purchase_Schema()
purchases_schema = Purchase_Schema(many = True)

@app.route('/stores',methods = ['GET'])
def get_stores():
    stores = Stores.query.all()
    return stores_schema.jsonify(stores)

@app.route('/purchases',methods = ['GET'])
def get_purchases():
    purchases = Purchases.query.all()
    return purchases_schema.jsonify(purchases)

if __name__ == "__main__":
    app.run(debug = True)







