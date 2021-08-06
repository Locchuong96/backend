from source import app ,db, ma
import pickle
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
    area = db.Column(db.String(60),nullable= False,default = "Unknown")
    post_time = db.Column(db.String(60),nullable= False,default = "Unknown")

    def __repr__(self):
        return f"Realestate('{self.id}','{self.title}','{self.address}','{self.post_id}','{self.sqm}','{self.price}','{self.sqm_price}','{self.status}','{self.area}','{self.post_time}')"

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
    area = ma.auto_field()
    post_time = ma.auto_field()

realestate_schema = Realestate_Schema()
realestates_schema = Realestate_Schema(many= True)

class Api(db.Model):
    id = db.Column(db.Integer , primary_key =True)
    author = db.Column(db.String(60),nullable = False)
    type = db.Column(db.String(100),nullable = False)
    url = db.Column(db.String(100),nullable = False)
    params = db.Column(db.String(500))
    example = db.Column(db.String(700))
    date = db.Column(db.String(100),nullable = False)
    comment = db.Column(db.String(700))

    def __repr__(self):
        return f"Api('{self.id}','{self.author}','{self.type}','{self.url}','{self.date}')"

class Api_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Api
    
    id = ma.auto_field()
    author = ma.auto_field()
    url = ma.auto_field()
    date = ma.auto_field()
    params = ma.auto_field()
    example = ma.auto_field()
    comment = ma.auto_field()

api_schema = Api_Schema()
apis_schema = Api_Schema(many = True)

predictor = pickle.load(open('./source/predict/clf.pkl','rb'))
