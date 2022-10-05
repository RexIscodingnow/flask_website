'''
    從 flask 引入 Flask 類別
    。 render_template 從 templates 資料夾引入 .html 檔案
            預設資料夾名稱: templates
            若要改從其他名稱的資料夾引入，使用 Flask() 的參數 => template_folder = "更改名稱"
    。 request 網頁請求方式(在 HTTP 協定有 8 種)，常見有 4 種 -> GET, POST, DELETE, UPDATE
    。 redirect 網頁的重新導向 ex: 在 XX 網頁(/平台) 填完表單後提交完，轉到別的頁面之類的...
    。 url_for 導向指定函式之頁面， url_for("函式名稱")
'''
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from form import RegisterForm, LoginForm
from configuration import Configuration
# import os

app = Flask(__name__) # __name__代表目前執行的模組

#  新版本的部份預設為none，會有異常，再設置True即可。
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# #  設置sqlite檔案路徑
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
#     os.path.join(pjdir, 'data.sqlite')
# app.config['SECRET_KEY'] = 'fjfisljdqoiahf;laojdqahlwdjayfghlkjd'

app.config.from_object(Configuration)

db = SQLAlchemy(app)
# 加密用
bcrypt = Bcrypt(app)
bootstrap = Bootstrap(app)

'''
    sqlite 建立欄位功能與型別

    說明 => __tablename__ = '資料庫的 table 名稱' : 若沒有設置，預設使用 class 的名稱
            primary_key = True : 基本上要有主鍵
            unique = True/False : 唯一值。 在同一個 table 下的欄位(同一個欄位下)，不可以有第二個相同的值
            nullable = True/False : 允許為空值。 開啟的時候，新增資料時，該欄位可以不用新增資料(可選的欄位)
                                                反之，新增資料時，未新增到該欄位，要 debug 囉! (必填欄位)

            以下是欄位型別 與 功能

            db.欄位功能                   | Python
       |----------------------------------|------------------|
       | 1. Column() : 配置欄位            |                  |
       | 2. Integer : 32 bit 的整數        | int              |
       | 3. SmallInteger : 16 bit 的整數   | int              |
       | 4. BigInteger : 不限精度 的整數   | int              |
       | 5. Float : 浮點數                 | float            |
       |-----------------------------------|------------------|
       | 6. String(字數) : 文字            | str              |
       | 7. Text() : 長字串                | str              |
       | 8. LargeBinary : 二進制文件       | str              |
       | 9. PickleType : 序列化文件        | object           |
       |-----------------------------------------------------|

       增、刪、改、查，等功能操作
       
        大致會用到: db.session.add(新增資料、更動資料)
                   db.session.delete(要刪除的目標資料)
                   db.session.commit()  =>  提交資料。 前面兩種指令執行後，一定要推送，不然不會更動
            
            查詢:  class 名稱(資料表).query.filter().功能()  =>  功能() --> all() 全抓下來 (所有查詢結果)
                                                                           first() 返回第一筆資料
                                                                           ......
                   
                   class 名稱(資料表).query.filter_by().功能() => filter_by() 做簡單查詢，有人說是語法糖
                                            
                                            P.S : 好比 SQL 的語句 where
'''
class User(db.Model):
    __tablename__ = 'users'     # sqlite 資料庫的 tablename
    id = db.Column(db.Integer, primary_key=True)    # 設定主鍵
    # String -> 文字型態  unique -> 唯一值  nullable -> True: 可空格, False: 不能為空
    # String(50) -> 最多50字
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    # 密碼加密  使用 @property 設為不可讀取
    @property
    def password_hash(self):
        raise AttributeError("password is not readable attribute!!")

    # 設置 setter 新增資料
    @password_hash.setter
    def password_hash(self, password):
        '''
        密碼加密，這邊使用 flask_bcrypt 模組\n
        : parameter 如下\n
        : password: 使用者輸入的密碼
        '''
        self.password = bcrypt.generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        '''
        密碼驗證，驗證使用者輸入的密碼跟資料庫的加密密碼是否相符\n
        : param password: 使用者輸入的密碼\n
        : return: True/False\n
        '''
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return "<User: %s, email: %s>" % (self.username, self.email)

@app.route("/", methods=['GET', 'POST'])  # 函式的裝飾 (Decorator): 已函式為基礎，提供附加的功能
def index():
    return render_template("index.html")

# route => 代表我們要處理的網站路徑。 methods => 限制網頁請求方式，下方 "/piffle" 頁面限制只能用 GET 與 POST 請求
@app.route("/piffle", methods=['GET', 'POST'])
def pifflePage():
    return render_template("pifflePage.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    '''
        註冊功能，新增到資料庫
    '''
    # 表單項目。 用 render_template() 的參數 **context 丟給目標 .html 檔案，呈現表單項目
    form = RegisterForm()
    
    # validate_on_submit() => 返回布林值，所有選項輸入完成 且 按下提交，返回 True，反之 False
    if form.validate_on_submit():
        # 用 form.表單項目名.data 取得輸入資訊
        username = form.username.data
        password = form.password.data
        email = form.email.data
        # 信箱已被註冊的提示訊息
        exist_user = User.query.filter_by(email=email).first()
        if exist_user:
            return render_template("sign_up.html", form=form, msg='該信箱已被註冊!')

        user = User(
            username=username,
            password_hash=password,   # 使用 被裝飾器 @property 設成【唯寫】屬性的變數，新增用戶密碼
            email=email
        )
        db.session.add(user)   # 新增欄位內資訊
        db.session.commit()    # 推送更動資訊

        return redirect(url_for("login"))

    return render_template("sign_up.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()        
        if user:
            if user.check_password(form.password.data):

                return redirect(url_for('user'))

    return render_template("login.html", form=form)

@app.route('/user')
def user():
    return render_template("user.html")

if __name__ == "__main__": # 如果以主程式執行
    app.run(debug=True)