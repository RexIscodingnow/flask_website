from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from wtforms.fields import EmailField

class RegisterForm(FlaskForm):

    username = StringField('username', validators=[
        DataRequired()
    ])
    password = PasswordField('password', validators=[
        DataRequired(),
        EqualTo('password2')
    ])
    password2 = PasswordField('password_again', validators=[
        DataRequired()
    ])
    email = EmailField('email', validators=[
        DataRequired()
    ])
    submit = SubmitField('register')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired()
    ])
    email = EmailField('email', validators=[
        DataRequired()
    ])
    password = PasswordField('password', validators=[
        DataRequired()
    ])
    submit = SubmitField('login')