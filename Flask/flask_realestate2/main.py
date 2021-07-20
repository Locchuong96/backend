from flask import Flask ,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

# init app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init database
db = SQLAlchemy(app)

# define model Realestate
class Realestate(db.Model):
    id          = db.Column(db.Integer,primary_key = True)
    image_link  = db.Column(db.String(200),default = "No Image")
    title       = db.Column(db.String(200),nullable = False,default = 'No Title')     # required input post 
    address     = db.Column(db.String(100),nullable =False)                           # required input post 
    orientation = db.Column(db.String(20),default = 'Unknown')                        # required input post  
    detail_link = db.Column(db.String(100),nullable = False,default = 'Auto') 
    post_id     = db.Column(db.String(20),nullable = False, default = 'Auto')
    bathrooms   = db.Column(db.Integer)                                               # required input post 
    bedrooms    = db.Column(db.Integer)                                               # required input post 
    sqm         = db.Column(db.Float,nullable = False)                                # required input post 
    lat         = db.Column(db.Float,nullable = False)                                # required input post 
    long        = db.Column(db.Float,nullable = False)                                # required input post 
    price       = db.Column(db.Float,nullable = False)                                # required input post
    sqm_price   = db.Column(db.Float,nullable = False)                                # required input post
    status      = db.Column(db.String(20),nullable = False, default = 'for sale')     # required input post

    def __repr__(self):
        return f"Object('{self.title}','{self.address}','{self.orientation}',\
                        '{self.bathrooms}','{self.bedrooms}','{self.sqm}','{self.lat}',\
                        '{self.long}','{self.price}','{self.sqm_price}','{self.status}')"

#init schema
ma = Marshmallow(app)

class RealestateSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Realestate

    id              = ma.auto_field()
    image_link      = ma.auto_field()
    title           = ma.auto_field()
    address         = ma.auto_field()
    orientation     = ma.auto_field()
    detail_link     = ma.auto_field()
    post_id         = ma.auto_field()
    bathrooms       = ma.auto_field()
    bedrooms        = ma.auto_field()
    sqm             = ma.auto_field()
    lat             = ma.auto_field()
    long            = ma.auto_field()
    price           = ma.auto_field()
    sqm_price       = ma.auto_field()
    status          = ma.auto_field()

realestate_schema = RealestateSchema()
realestates_schema = RealestateSchema(many = True)

@app.route("/",methods = ['GET'])
def home_page():
    return "<h4>Real estate Demo v1!</h4>"

@app.route("/realestate",methods = ['GET'])
def get_all():
    all = Realestate.query.all() 
    return realestates_schema.jsonify(all)

@app.route("/realestate/<int:id>",methods = ['GET'])
def getby_index(id):
    one = Realestate.query.get(id) 
    return realestate_schema.jsonify(one)

@app.route("/realestate",methods = ['POST'])
def create_one():
    title       = request.json["title"]       
    address     = request.json["address"]     
    orientation = request.json["orientation"] 
    bathrooms   = request.json["bathrooms"]   
    bedrooms    = request.json["bedrooms"]    
    sqm         = request.json["sqm"]         
    lat         = request.json["lat"]         
    long        = request.json["long"]        
    price       = request.json["price"]
    sqm_price   = request.json["sqm_price"]
    status      = request.json["status"]
    id          = request.json["id"]

    new_one = Realestate(title = title,address = address, orientation = orientation,
                    bathrooms = bathrooms, bedrooms = bedrooms, sqm = sqm, lat = lat, long = long,
                    price = price,sqm_price = sqm_price,status = status,id = id)
    
    db.session.add(new_one)
    db.session.commit()

    return str(new_one)
if __name__ == "__main__":
    app.run(debug = True)
