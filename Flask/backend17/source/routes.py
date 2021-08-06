from operator import and_
from source import app, db
from source.models import Realestate,Api
from source.models import realestate_schema, realestates_schema,api_schema,apis_schema
from source.models import predictor
from flask import render_template, redirect, url_for, request,jsonify
from sqlalchemy import and_
from datetime import datetime
import numpy as np

"""
Index all api, url of backend
"""
@app.route("/")
def index():
    api_list = Api.query.all()
    count =len(api_list)
    return render_template('index.html',api_list = list(api_list),count = count)

"""
Add new api to api's table
"""
@app.route("/api_add",methods = ['POST'])
def api_add():
    author = request.form.get('author')
    type = request.form.get('type')
    url = request.form.get('url')
    params = request.form.get('params')
    example = request.form.get('example')
    comment = request.form.get('comment')
    date  = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    new_api = Api(author = author, type = type , url = url , params = params, example = example, comment = comment, date = date)
    db.session.add(new_api)
    db.session.commit()
    return redirect(url_for('index'))

"""
Delete api record in api's table
"""
@app.route("/api_delete/<int:api_id>")
def api_delete(api_id):
    api = Api.query.get(api_id)
    db.session.delete(api)
    db.session.commit()
    return redirect(url_for('index'))

"""
Get all real estate json format
"""
@app.route("/realestate",methods = ['GET'])
def get_all():
    result = Realestate.query.all()
    return realestates_schema.jsonify(result)

"""
Search real estate page
"""
@app.route("/realestate_search",methods= ['GET','POST'])
def search():
    if request.method == 'POST':
        keys = request.form.keys()
        for key in keys:

            if key.startswith("keyword"):
                result= []
                keyword = request.form.get("keyword")
                data_list = Realestate.query.all()
                for data in data_list:
                    if (keyword.lower() in data.address.lower()) or (keyword.lower() in data.title.lower()):
                        result.append(data)
                return realestates_schema.jsonify(result)

            if key.startswith("area"):
                result = Realestate.query.filter_by(area = request.form.get('area'))
                return realestates_schema.jsonify(result)
                
            if key.startswith("max_sqm"):
                max_sqm = request.form.get("max_sqm")
                min_sqm = request.form.get("min_sqm")
                result = Realestate.query.filter(and_(Realestate.sqm > min_sqm,Realestate.sqm < max_sqm))
                return realestates_schema.jsonify(result)

            if key.startswith("max_price"):
                max_price = request.form.get("max_price")
                min_price = request.form.get("min_price")
                result = Realestate.query.filter(and_(Realestate.price > min_price, Realestate.price < max_price))
                return realestates_schema.jsonify(result)
                
    else:
        return render_template('search.html')

"""
Predict price
"""
@app.route("/predict", methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        bathrooms=  request.form.get('bathrooms')
        bedrooms = request.form.get('bedrooms')
        sqm = request.form.get('sqm')
        input = np.array([[bathrooms,bedrooms,sqm]])
        output = predictor.predict(input)
        return jsonify({'price':output[0]})
        
    else:
        return render_template("predict.html")

"""
Add new real estate
"""
@app.route("/add_new",methods = ['GET','POST'])
def add_new():
    if request.method == 'POST':
        title = request.form.get('title')
        address = request.form.get('address')
        orientation = request.form.get('orientation')
        bathrooms = request.form.get('bathrooms')
        bedrooms = request.form.get('bedrooms')
        sqm = request.form.get('sqm')
        lat = request.form.get('lat')
        long = request.form.get('long')
        price = request.form.get('price')
        sqm_price = float(price)/float(sqm)
        date  = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        new = Realestate(title= title, address = address, orientation = orientation, bathrooms= bathrooms,
        bedrooms = bedrooms, sqm = sqm, lat = lat, long =long, price = price, sqm_price = sqm_price,post_time = date)

        db.session.add(new)
        db.session.commit()

        return realestate_schema.jsonify(new)

    else:
        return render_template('add.html')
