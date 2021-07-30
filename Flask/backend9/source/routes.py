from source import app, db
from source.models import Realestate,Api
from source.models import realestate_schema, realestates_schema,api_schema,apis_schema
from flask import render_template, redirect, url_for, request 
from datetime import datetime

@app.route("/")
def index():
    api_list = Api.query.all()
    count =len(api_list)
    return render_template('index.html',api_list = list(api_list),count = count)

@app.route("/api_add",methods = ['POST'])
def api_add():
    type = request.form.get('type')
    url = request.form.get('url')
    params = request.form.get('params')
    example = request.form.get('example')
    comment = request.form.get('comment')
    date  = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    new_api = Api(type = type , url = url , params = params, example = example, comment = comment, date = date)
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