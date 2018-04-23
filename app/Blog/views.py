from . import blog
from flask import render_template

@blog.route('/blog')
def index():
    return render_template('blog/blog.html')

