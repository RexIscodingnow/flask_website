# 從 flask 引入 Flask 類別(主要的)
# render_template 從 templates 資料夾引入 .html 檔案
# request 網頁請求方式(在 HTTP 協定有 8 種)，常用有4種 -> GET, POST, DELETE, UPDATE
# redirect 網頁的路徑導向 ex: 在 XX 網頁(/平台) 填完表單後提交完，轉到別的頁面之類的...
# url_for 導向指定函式之頁面
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from form import RegisterForm, LoginForm
# import os

app = Flask(__name__) # __name__代表目前執行的模組

#  新版本的部份預設為none，會有異常，再設置True即可。
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# #  設置sqlite檔案路徑
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
#     os.path.join(pjdir, 'data.sqlite')
# app.config['SECRET_KEY'] = 'fjfisljdqoiahf;laojdqahlwdjayfghlkjd'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

'''
    普通 sqlite 的建立的方式

    說明 => __tablename__ = '資料庫的 table 名稱' : 若沒有設置，預設使用 class 的名稱
            primary_key = True : 基本上要有主鍵

            以下是我用過 der...

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
'''
class User(db.Model):
    __tablename__ = 'users'     # sqlite 資料庫的 tablename
    id = db.Column(db.Integer, primary_key=True)    # 設定主鍵
    # String -> 文字型態  unique -> 唯一值  nullable -> True: 可空格, False: 不能為空
    # String(50) -> 最多50字
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

@app.route("/", methods=['GET', 'POST'])  # 函式的裝飾 (Decorator): 已函式為基礎，提供附加的功能
def index():
    return render_template("index.html")

# route => 代表我們要處理的網站路徑。 methods => 限制網頁請求方式，下方 "/piffle" 頁面限制只能用 GET 與 POST 請求
@app.route("/piffle", methods=['GET', 'POST'])
def pifflePage():
    return render_template("pifflePage.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        

        return redirect(url_for("login"))

    return render_template("sign_up.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        
        pass

    return render_template("login.html", form=form)


if __name__ == "__main__": # 如果以主程式執行
    app.run(debug=True)