from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me?')
    sub = SubmitField('sign in')