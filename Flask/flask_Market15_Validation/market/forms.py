"""
pip install flask-wtf
pip install wtforms
Create form for web page 
Create class and fields
"""
from flask_wtf import FlaskForm #crate form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

# Inherited class
"""
Write some validation to make sure data is valid with the database'policy
"""
class RegisterForm(FlaskForm):
    username= StringField(label = 'User Name:',validators= [ Length(min = 2,max =30),DataRequired() ] )
    email_address = StringField(label = 'Email Address:', validators = [ Email(), DataRequired()] )
    password1 = PasswordField(label = 'Password:', validators = [Length(min = 6),DataRequired()] )
    password2 = PasswordField(label = 'Confirm Password:',validators = [EqualTo('password1'),DataRequired()] )
    submit = SubmitField(label = 'Create Account')