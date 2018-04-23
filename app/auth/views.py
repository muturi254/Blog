from flask import render_template, redirect, url_for, request, flash
from . import auth
from .forms import LoginForm, RegisterForm
from ..models import User
from flask_login import login_user, logout_user, login_required
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login = LoginForm()
    if  login.validate_on_submit():
        user = User.query.filter_by(username = login.username.data).first()

        if user is not None and user.verify_password(login.password.data):
            login_user(user, login.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password.')
    return render_template('auth/login.html', login = login, active = 'login')


@auth.route('/signup', methods= ['GET', 'POST'])
def signup():
    signup = RegisterForm()
    if signup.validate_on_submit():
        user = User(firstname = signup.firstname.data, lastname = signup.lastname.data, username= signup.username.data, email = signup.email.data, password = signup.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    flash('New user created enter credentials.')
        
    return render_template('auth/signup.html', signup= signup, active = 'signup')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
