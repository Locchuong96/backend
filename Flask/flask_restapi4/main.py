from flask import Flask,jsonify, request 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

#Init app
app = Flask(__name__)
#Config app SQLALCHEMY 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///product.db" # The name of the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Auto generate a id number for new product

#Init database
db = SQLAlchemy(app)
#Create model
class Product(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False, unique = True)
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    descript = db.Column(db.String(200))
    
    def __init__(self,name,price,qty,descript):
        self.name = name
        self.price = price 
        self.qty = qty 
        self.descript = descript

#Init marshallow
ma = Marshmallow(app)
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','price','qty','descript')
#Create schema for a product
product_schema = ProductSchema()
#Create schema for all product
products_schema = ProductSchema(many = True)

#Create route
@app.route("/")
def home():
    return jsonify({"msg":"Hello world!"})

#POST a product
@app.route("/product",methods = ["POST"])
def post():
    name = request.json["name"]
    price = request.json["price"]
    qty = request.json["qty"]
    descript = request.json["descript"]
    new_product = Product(name,price,qty,descript)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

#GET all product
@app.route("/product", methods =["GET"])
def get_all():
    products = Product.query.all()
    return products_schema.jsonify(products)

#GET a product
@app.route("/product/<int:id>",methods = ["GET"])
def get_one(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

#PUT a product
@app.route("/product/<int:id>",methods = ["PUT"])
def update(id):
    name = request.json["name"]
    price = request.json["price"]
    qty = request.json["qty"]
    descript = request.json["descript"]
    product = Product.query.get(id)
    product.name = name
    product.price = price 
    product.qty = qty 
    product.descript = descript 
    db.session.commit()
    return product_schema.jsonify(product)

#DELETE a product
@app.route("/product/<int:id>",methods = ["DELETE"])
def remove(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)

if __name__ == "__main__":
    app.run(debug = True)


