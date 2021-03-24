from flask import render_template, session, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app
from app.form import LoginForm, QuestionForm
from app import db
from app.models import User, Question

@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.user.data).first()
        if user is None or not user.check_password(form.passwd.data):
            flash("Invalid Username or password")
            return redirect(url_for(login))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for(index))
    else:
        return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(index))

@app.route('/register')
def register():



@app.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    form = QuestionForm
    if request.method == 'POST':
        if form.validate_on_submit():
            flash("Question Posted")
            return redirect(url_for('/question'))
        return render_template('question.html', form=form)
    else:
        data=Question.query.filter_by(creatorid=User.get_id())
