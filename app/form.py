from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from app.models import account, Question

class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember user')
    sub = SubmitField('sign in')

class QuestionForm(FlaskForm):
    Question = StringField('Question', validators=[DataRequired()])
    Answer = StringField('Answer', validators=[DataRequired()])
    sub = SubmitField('Post question')

class RegisterForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    repeatpass = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('passwd')])
    sub = SubmitField('sign in')

    def uservalidation(self, user):
        user = account.query.filter_by(username=user.data)
        if user is not None:
            raise ValidationError('Please enter a different username as this has been used previously')