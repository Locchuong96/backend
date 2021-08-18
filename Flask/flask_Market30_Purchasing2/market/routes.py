from market import app, db
from market.models import Item,User
from flask import render_template,redirect,url_for,flash,get_flashed_messages,request
from market.form import RegisterForm,LoginForm,PurchaseItemForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market',methods = ["GET","POST"])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    
    if request.method == "POST":
        purchase_item = request.form.get('purchase_item')
        p_item_object = Item.query.filter_by(name = purchase_item).first()
        if p_item_object:
            p_item_object.owner = current_user.id 
            current_user.budget = current_user.budget - p_item_object.price 
            db.session.commit()
            flash(f"Congratulation! You purchased {p_item_object.name} for {p_item_object.price}")
            return redirect(url_for('market_page'))

    if request.method == "GET":
        #items = Item.query.all()
        items = Item.query.filter_by(owner = None)
        return render_template('market.html',items = items,purchase_form = purchase_form )   

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



