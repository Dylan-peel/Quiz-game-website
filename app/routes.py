from flask import render_template, session, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app
from app.form import LoginForm, QuestionForm, RegisterForm
from app import db
from app.models import account, Question

@app.route('/')
@app.route('/index')
def index():
    return render_template('basepage.html', title='Index')

@app.route('/login', methods=['GET', 'POST'])
def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))#user will not load if they are already logged in
        form = LoginForm()
        if form.validate_on_submit():
            user = account.query.filter_by(username=form.user.data).first()#searches through user DB for matching user
            #if user is None or not user.check_password(form.passwd.data):#if user is not valid or password is incorrect
                #flash("Invalid Username or password")
                #return redirect(url_for(login))
            if user.check_password(form.passwd.data) and user is not None:
                print("Database lookup success")
                login_user(user)
            else:
                flash("Invalid Username or password")
                return redirect(url_for(login))
            return redirect(url_for('index'))#redirects back to index page after succesfull login
        else:
            return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = account(username=form.user.data, password=form.passwd.data)
        db.session.add(user)
        db.session.commit()
        flash('New user has been registered')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registration', form=form)




@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(index))



@app.route('/question', methods=['GET', 'POST'])
def question():
    form = QuestionForm() #These brackets were missing at the end of QuestionForm, which was causing the error
    if request.method == 'POST':
        if form.validate_on_submit():
            flash("Question Posted")
            return redirect(url_for('/question'))
        return render_template('question.html', form=form)
    else:
        return render_template('question.html', title='Questions', form=form)