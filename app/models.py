from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True)
    passwordhash = db.Column(db.String, index=True, unique=True)
    def set_password(self, password):
        self.passwordhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordhash, password)

    def get_id(self):
        return(id)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))




class Question(db.Model):
    QuestionID = db.Column(db.Integer, primary_key=True)
    Questionbody = db.Column(db.String(1000))
    Questionanswer = db.Column(db.String(500))
    creatorid = db.Column(db.Integer, db.ForeignKey('id'))

    def __repr__(self):
        return '<Question {}>'.format(self.body)
