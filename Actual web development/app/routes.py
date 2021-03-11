from flask import render_template, session, flash, redirect, request
from time import sleep
from app import app
from app.form import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash("Login successful!")
            sleep(2)
            return redirect('/index')
        return render_template('login.html', title='Login', form=form)
    else:
        return render_template('login.html', title='Login', form=form)

