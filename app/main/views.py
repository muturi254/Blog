from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html', active="home")

@main.route('/about')
def about():
    return render_template('about.html',  active="about")

@main.route('/contact')
def contact():
    return render_template('contact.html', active="contact")
