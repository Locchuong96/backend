from operator import and_
from source import app, db
from source.models import Realestate,Api
from source.models import realestate_schema, realestates_schema,api_schema,apis_schema
from flask import render_template, redirect, url_for, request
from sqlalchemy import and_
from datetime import datetime

@app.route("/")
def index():
    api_list = Api.query.all()
    count =len(api_list)
    return render_template('index.html',api_list = list(api_list),count = count)

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

@app.route("/api_delete/<int:api_id>")
def api_delete(api_id):
    api = Api.query.get(api_id)
    db.session.delete(api)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/realestate",methods = ['GET'])
def get_all():
    result = Realestate.query.all()
    return realestates_schema.jsonify(result)

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
