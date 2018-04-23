from . import main
from flask import render_template
from .forms import ContactForm

@main.route('/')
def index():
    return render_template('index.html', active = 'home')

@main.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form, active =  'contact')

@main.route('/about')
def about():
    return render_template('about.html', active = 'about')