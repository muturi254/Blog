from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('username', validators=[Required()])
    pasword = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')



class RegisterForm(FlaskForm):
    firstname = StringField('Firstname', validators=[Required()])
    lastname = StringField('Lastname', validators=[Required()])
    username = StringField('Username', validators=[Required()])
    email = StringField('Emil', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(),
                                                      EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField(
        'Confirm Passwords', validators=[Required()])
    submit = SubmitField('SignUp')
