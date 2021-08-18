from market import app, db
from market.models import Item,User
from flask import render_template,redirect,url_for,flash,get_flashed_messages
from market.form import RegisterForm,LoginForm
from flask_login import login_user, logout_user, login_required

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
@login_required
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
                                password = form.password1.data )

        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)

        return redirect(url_for('market_page'))

    if form.errors != {}: # If there are errors from the validators
        for err_msg in form.errors.values():
            #print(f"There was an error with creating account: {err_msg}")
            flash(f"Error: {err_msg}",category='danger')

    return render_template('register.html', form = form)

@app.route("/login",methods = ["GET","POST"])
def login_page():

    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username= form.username.data).first()
        if attempted_user and attempted_user.password_check_correction(password_to_check= form.password.data):
            login_user(attempted_user)
            flash(f" Wellcome {attempted_user.username} !",category = "success")
            return redirect(url_for('market_page'))
        else:
            flash("Username or password incorrect, please try again", category= "danger")

    return render_template('login.html',form = form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash("You have been logout", category = "success")
    return redirect(url_for('home_page'))



