from flask import render_template
from app import thing

@thing.route('/')
@thing.route('/index')
def index():
    return render_template('home.html', title = 'home')