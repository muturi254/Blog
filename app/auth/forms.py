from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo, ValidationError
from ..models import User


class LoginForm(FlaskForm):
    username = StringField('username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')



class RegisterForm(FlaskForm):
    firstname = StringField('Firstname', validators=[Required()])
    lastname = StringField('Lastname', validators=[Required()])
    username = StringField('Username', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(),
                                                      EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField(
        'Confirm Passwords', validators=[Required()])
    submit = SubmitField('SignUp')

    # vlidate email if exist
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    # check if username exists
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')