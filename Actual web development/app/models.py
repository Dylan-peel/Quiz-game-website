from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True)
    password = db.Column(db.String, index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class question(db.Model):
    QuestionID = db.Column(db.Integer, primary_key=True)
    Questionbody = db.Column(db.String(1000))
    Questionanswer = db.Column(db.String(500))
    creatorid = db.Column(db.Integer, db.ForeignKey('id'))

    def __repr__(self):
        return '<Question {}>'.format(self.body)