from market import app, db
from market.models import Item, User
from market.forms import RegisterForm 
from flask import render_template,redirect, url_for

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

"""
CROSS SITE REQUEST FORGERY (CSRF)
{{ form.hidden_tag() generate token }}
"""
@app.route('/register',methods = ['GET','POST'])
def register_page():
    """
    If the validation fail so form.validate_on_submit false
    """
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                                email_address = form.email_address.data,
                                password_hash = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: # If there are errors from the validations
        for err_msg in form.errors.values():
            print(f'There wa an error with creating a user: {err_msg}')
    return render_template('register.html',form = form)





