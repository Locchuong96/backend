from market import app, db
from market.models import Item,User
from flask import render_template,redirect,url_for
from market.form import RegisterForm

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

@app.route('/register',methods = ['GET','POST'])
def register_page():
    form = RegisterForm()
    #validdate the form when you click the submit button
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                                email_address = form.email_address.data,
                                password_hash = form.password1.data )

        db.session.add(user_to_create)
        db.session.commit()

        return redirect(url_for('market_page'))

    if form.errors != {}: # If there are errors from the validators
        for err_msg in form.errors.values():
            print(f"There was an error with creating account: {err_msg}")
            
    return render_template('register.html', form = form)




