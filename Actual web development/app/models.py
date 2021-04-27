from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user, login_user

class account(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True)
    passwordhash = db.Column(db.String, index=True, unique=True)


    def check_password(self, password):
        return check_password_hash(self.passwordhash, password)

    def get_id(self):
        return(id)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def __init__(self, username, password):
        self.username = username
        self.passwordhash = generate_password_hash(password)

@login.user_loader
def load_user(id):
    return account.query.get(id)




class Question(db.Model):
    QuestionID = db.Column(db.Integer, primary_key=True)
    Questionbody = db.Column(db.String(1000))
    Questionanswer = db.Column(db.String(500))
    creatorid = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __repr__(self):
        return '<Question {}>'.format(self.body)
