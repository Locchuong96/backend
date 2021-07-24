from flask import jsonify
from flask_restful import reqparse,abort
from realestate import app,db
from realestate.models import Realestate
from realestate.models import realestate_schema,realestates_schema
from realestate.models import realestate_post_args,realestate_put_args

@app.route("/",methods = ['GET'])
def home_page():
    return jsonify({"msg":"Hello World!"})

@app.route("/realestate",methods = ['GET'])
def get_all():
    result = Realestate.query.all()
    return realestates_schema.jsonify(result)

@app.route("/realestate/<int:id>",methods = ['GET'])
def get_one(id):
    result = Realestate.query.get(id)
    if not result:
        abort(402,message = "Result Not Found")
    return realestate_schema.jsonify(result)

@app.route("/realestate",methods = ['POST'])
def create():
    args = realestate_post_args.parse_args()
    #Get necessary param
    title = args["title"]
    address = args["address"]
    orientation = args["orientation"]
    bathrooms = args["bathrooms"]
    bedrooms = args["bedrooms"]
    sqm = args["sqm"]
    lat = args["lat"]
    long = args["long"]
    price = args["price"]
    sqm_price = args["sqm_price"]
    status = args["status"]

    #Get  unnecessary param
    if args["image_link"]:
        image_link = args["image_link"]
    else:
        image_link = "No Image"
    
    if args["detail_link"]:
        detail_link = args["detail_link"]
    else:
        detail_link = "No Detail"
    
    if args["post_id"]:
        post_id = args["post_id"]
    else:
        post_id = "No Id"

    new = Realestate(image_link = image_link, title = title, address = address, orientation = orientation,
                        detail_link = detail_link, post_id = post_id, bathrooms = bathrooms, bedrooms = bedrooms,
                        sqm = sqm, lat = lat,long = long, price = price, sqm_price = sqm_price, status = status)
    
    #return realestate_schema.jsonify(new) no id because have not add to table yet

    db.session.add(new)
    db.session.commit()

    return realestate_schema.jsonify(new)

@app.route("/realestate/<int:id>",methods = ['PUT'])
def update(id):
    args = realestate_put_args.parse_args()
    result = Realestate.query.get(id)

    if not result:
        abort(404,message = "Result Not Found")
    
    if args["image_link"]:
        result.image_link = args["image_link"]
    if args["title"]:
        result.title = args["title"]
    if args["address"]:
        result.address = args["address"]
    if args["orientation"]:
        result.orientation = args["orientation"]
    if args["detail_link"]:
        result.detail_link = args["detail_link"]
    if args["post_id"]:
        result.post_id = args["post_id"]
    if args["bathrooms"]:
        result.bathrooms = args["bathrooms"]
    if args["bedrooms"]:
        result.bedrooms = args["bedrooms"]
    if args["sqm"]:
        result.sqm = args["sqm"]
    if args["lat"]:
        result.lat = args["long"]
    if args["long"]:
        result.long = args["long"]
    if args["price"]:
        result.price = args["price"]
    if args["sqm_price"]:
        result.sqm_price = args["sqm_price"]
    if args["status"]:
        result.status = args["status"]
    db.session.commit()

    return realestate_schema.jsonify(result)
    
@app.route("/realestate/<int:id>",methods = ['DELETE'])
def remove(id):
    result = Realestate.query.get(id)

    if not result:
        abort(405,message = "Result Not Found")
    
    db.session.delete(result)
    db.session.commit()
    return realestate_schema.jsonify(result)
