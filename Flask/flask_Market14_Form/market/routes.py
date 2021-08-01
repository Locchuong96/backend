from market import app, db
from market.models import Item, User
from market.forms import RegisterForm 
from flask import render_template

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items = items)

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html',form = form)





