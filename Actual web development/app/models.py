from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True)
    password = db.Column(db.String, index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)