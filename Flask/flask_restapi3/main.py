from flask import Flask, jsonify , request 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# config database for app
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///product.db"
# app.config['SQLALHEMY_TRACK_MODIFICATIONS'] =False

#init database
db = SQLAlchemy(app)
# create model
class Product(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    name        = db.Column(db.String(60), nullable = False,unique = True)
    price       = db.Column(db.Float,nullable = False)
    qty         = db.Column(db.Integer, nullable =False)
    description = db.Column(db.String(200))

    def __init__(self,id,name,price,qty,description):
        self.id          = id
        self.name        = name
        self.price       = price 
        self.qty         = qty 
        self.description = description

#Product schema
ma = Marshmallow()
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description','price','qty')

product_schema = ProductSchema()
products_schema = ProductSchema(many = True)

@app.route("/")
def home_page():
    return jsonify({"msg":"Hello World"})

"""
GET all product
"""
@app.route("/product", methods = ["GET"])
def get_products():
    products = Product.query.all()
    results = products_schema.dump(products)
    return products_schema.jsonify(results)

"""
GET product by id
"""
@app.route("/product/<int:id>", methods = ["GET"])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

"""
POST add new product
your model will NOT automaticly generate a id number for new product
"""
@app.route("/product", methods = ["POST"])
def add_product():
    name        = request.json["name"]
    price       = request.json["price"]
    description = request.json["description"]
    qty         = request.json["qty"]
    id          = request.json["id"]
    
    # create new product via the model def __init__(self,id,name,price,qty,description):
    new_product = Product(id,name,price,qty,description)
    # add new product into database
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

"""
PUT update product
"""
@app.route("/product/<int:id>",methods = ["PUT"])
def update_product(id):

    product = Product.query.get(id)
    
    name        = request.json["name"]
    qty         = request.json["qty"]
    description = request.json["description"]
    price       = request.json['price']
    
    product.name        = name
    product.qty         = qty
    product.description = description
    product.price       = price

    db.session.commit()
    return product_schema.jsonify(product)

"""
DELETE remove a product
"""
@app.route("/product/<int:id>",methods = ["DELETE"] )
def remove_product(id):
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)

if __name__ == "__main__":
    app.run(debug = True)