'''
    flask_wtf 表單設置

    用 class 作為 "每一種頁面的表單"
    
    (使用前，先繼承老爸的能力)
    使用前先繼承 flask_wtf 模組，裡面的 class => FlaskForm

    (防守狀態: 我方發動 XXXXX 驗證器，作為防守。 防守效果: 格式錯誤，不給通過，若對手攻擊大於 500 點，即刻反彈對手攻擊，再乘兩倍的 HP 傷害......喂!中二病發作喔!)
    在 wtforms 底下的功能，其中有驗證器檢查輸入內容
    比如說: 必填選項 => DataRequired()
            相同內容 => EqualTo()  應用場景: 註冊帳號、修改密碼 的 再輸入一次密碼
            
            其他要輸入特定格式的欄位，檢查有沒有符合格式

            ** 註: DataRequired() 與 EqualTo() ---->  在 wtforms.validators 底下

    導入 wtforms 模組，它底下的欄位

    欄位們: 
            1. 輸入框 -----> 單行: StringField()
                      -----> 多行: TextAreaField()
            1-1. 密碼 -----> PasswordField()
            1-2. 電子郵件 -----> EmailField()

            3. 送出按鍵 -----> SubmitField()
            ...
            ...
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