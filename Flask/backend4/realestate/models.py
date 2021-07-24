from flask_restful import reqparse,abort
from realestate import app, db, ma 

#Create a class of Realestate table
class Realestate(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image_link = db.Column(db.String(200),default = "No Image")
    title = db.Column(db.String(200),nullable =False)
    address = db.Column(db.String(100),nullable = False)
    orientation = db.Column(db.String(20),nullable =False)
    detail_link = db.Column(db.String(100),default = "No Detail")
    post_id = db.Column(db.String(20),default = "No Id") # pass unique condition
    bathrooms = db.Column(db.Integer)
    bedrooms =db.Column(db.Integer)
    sqm = db.Column(db.Float, nullable = False)
    lat = db.Column(db.Float, nullable = False)
    long = db.Column(db.Float, nullable = False)
    price = db.Column(db.Float, nullable = False)
    sqm_price =db.Column(db.Float,nullable = False)
    status = db.Column(db.String(20),nullable= False,default = "For Sale")

    def __repr__(self):
        return f"Realestate('{self.id}','{self.title}','{self.address}','{self.post_id}','{self.sqm}','{self.price}','{self.sqm_price}','{self.status}')"

#Create a json type for realestate
class Realestate_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Realestate
    
    id = ma.auto_field()
    image_link = ma.auto_field()
    title = ma.auto_field()
    address = ma.auto_field()
    orientation = ma.auto_field()
    detail_link = ma.auto_field()
    post_id = ma.auto_field()
    bathrooms = ma.auto_field()
    bedrooms = ma.auto_field()
    sqm = ma.auto_field()
    lat = ma.auto_field()
    long = ma.auto_field()
    price = ma.auto_field()
    sqm_price = ma.auto_field()
    status = ma.auto_field()

realestate_schema = Realestate_Schema()
realestates_schema = Realestate_Schema(many= True)

#Make a prase args for post methods
realestate_post_args = reqparse.RequestParser()
realestate_post_args.add_argument("image_link",type = str,required = False)
realestate_post_args.add_argument("title",type = str,required = True)
realestate_post_args.add_argument("address",type = str,required = True)
realestate_post_args.add_argument("orientation",type = str,required = True)
realestate_post_args.add_argument("detail_link",type = str, required = False)
realestate_post_args.add_argument("post_id",type = str, required = False)
realestate_post_args.add_argument("bathrooms",type = int, required = True)
realestate_post_args.add_argument("bedrooms",type = int, required = True)
realestate_post_args.add_argument("sqm",type = float, required = True)
realestate_post_args.add_argument("lat",type = float, required = True)
realestate_post_args.add_argument("long",type = float, required = True)
realestate_post_args.add_argument("price",type = float, required = True)
realestate_post_args.add_argument("sqm_price",type = float, required = True)
realestate_post_args.add_argument("status",type = str, required = True)

#Make a prase args for put methods
realestate_put_args = reqparse.RequestParser()
realestate_put_args.add_argument("image_link",type = str)
realestate_put_args.add_argument("title",type = str)
realestate_put_args.add_argument("address",type = str)
realestate_put_args.add_argument("orientation",type = str)
realestate_put_args.add_argument("detail_link",type = str)
realestate_put_args.add_argument("post_id",type = str)
realestate_put_args.add_argument("bathrooms",type = int)
realestate_put_args.add_argument("bedrooms",type = int)
realestate_put_args.add_argument("sqm",type = float)
realestate_put_args.add_argument("lat",type = float)
realestate_put_args.add_argument("long",type = float)
realestate_put_args.add_argument("price",type = float)
realestate_put_args.add_argument("sqm_price",type = float)
realestate_put_args.add_argument("status",type = str)