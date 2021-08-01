"""
pip install flask-wtf
pip install wtforms
Create form for web page 
Create class and fields
"""
from flask_wtf import FlaskForm #crate form
from wtforms import StringField,PasswordField,SubmitField

# Inherited class
class RegisterForm(FlaskForm):
    username= StringField(label = 'User Name:')
    email_address = StringField(label = 'Email Address:')
    password1 = PasswordField(label = 'Password:')
    password2 = PasswordField(label = 'Confirm Password:')
    submit = SubmitField(label = 'Create Account')