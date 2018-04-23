from flask import render_template
from . import auth
from .forms import LoginForm, RegisterForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login = LoginForm()
    return render_template('auth/login.html', login = login, active = 'login')


@auth.route('/signup', methods= ['GET', 'POST'])
def signup():
    signup = RegisterForm()
    return render_template('auth/signup.html', signup= signup, active = 'signup')
