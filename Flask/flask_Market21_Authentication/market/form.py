from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length,EqualTo, Email,DataRequired, ValidationError
from market.models import User 

class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        """
        Check username already exist in  Database
        def validate_username FlaskForm auto search def start with validate and check next part after the _ is username and execute
        """
        user = User.query.filter_by(username = username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try different username')

    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists!')

    username = StringField(label = 'User Name', validators = [Length(min = 2,max = 30),DataRequired()])
    email_address = StringField(label = 'Email Address', validators = [Email(),DataRequired()])
    password1 = PasswordField(label = 'Password', validators = [Length(min = 6),DataRequired()])
    password2 = PasswordField(label = 'Confirm Password',validators = [EqualTo('password1'),DataRequired()])
    submit = SubmitField(label = 'Submit')




