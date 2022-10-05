from flask_wtf import FlaskForm   # 要先繼承這個類別
# 表單功能類別
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo   # 驗證器
from wtforms.fields import EmailField

# 先從繼承 FlaskForm 開始
class RegisterForm(FlaskForm):
    # 左值皆為 表單項目名(fieldname)
    username = StringField('username', validators=[
        DataRequired()   # 設為必填項目
    ])
    password = PasswordField('password', validators=[
        DataRequired(),
        EqualTo('password2')  # 要比對的項目，以字串型式當參數
    ])
    password2 = PasswordField('password_again', validators=[
        DataRequired()
    ])
    email = EmailField('email', validators=[
        DataRequired()
    ])
    submit = SubmitField('register')

class LoginForm(FlaskForm):
    # 左值皆為 表單項目名
    username = StringField('username', validators=[
        DataRequired()
    ])
    email = EmailField('email', validators=[
        DataRequired()
    ])
    password = PasswordField('password', validators=[
        DataRequired()
    ])
    remember_time = SelectField(
        validators=[DataRequired()],
        
        # 已換算成 XXX分鐘
        choices=[(5, "5 分鐘"), (30, "30 分鐘"), (720, "12 小時")],
        
        # 限制型別為 int
        coerce=int
    )

    submit = SubmitField('login')