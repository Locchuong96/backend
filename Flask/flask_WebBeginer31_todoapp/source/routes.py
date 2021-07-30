from source import app,db
from source.models import ToDo
from source.models import todo_schema,todos_schema
from flask import render_template, redirect, url_for,request
from datetime import datetime

@app.route("/")
def index():
    todo_list = ToDo.query.all()
    return render_template('base.html', todo_list = todo_list)

@app.route("/create",methods = ['POST'])
def create():
    title = request.form.get('title')
    date  = str(datetime.utcnow())
    complete = False
    todo = ToDo(title= title, date = date, complete = complete)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = ToDo.query.get(todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = ToDo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))




