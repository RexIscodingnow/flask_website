'''
    
'''

from flask_wtf import FlaskForm   # 要先繼承這個類別
# 表單功能類別
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo   # 驗證器
from wtforms.fields import EmailField

# 先從繼承 FlaskForm 開始
class RegisterForm(FlaskForm):
    '''
    註冊使用者
    '''
    # 第一個值為 表單項目名(fieldname)
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
    '''
    登入的輸入框
    '''
    # 第一個值皆為 表單項目名
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
        
        # 參數 choices 為表單選項，已換算成 XXX分鐘
        choices=[(5, "5 分鐘"), (30, "30 分鐘"), (720, "12 小時")],
        
        # 限制資料型別為 int
        coerce=int
    )

    submit = SubmitField('login')

class ForgotPassword(FlaskForm):
    '''
    忘記密碼
    '''
    # 以墊子郵件作為 驗證身分用
    email = EmailField('email', 
        validators=[
            DataRequired()
    ])

    new_password = PasswordField('New Password', validators=[
        DataRequired(),
        EqualTo('password2')
    ])
    password2 = PasswordField('password2', validators=[
        DataRequired()
    ])

    submit = SubmitField('更動!!')