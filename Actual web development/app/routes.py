from flask import render_template
from app import app
from app.form import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)