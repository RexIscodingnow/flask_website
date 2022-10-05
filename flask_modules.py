'''
    模組區

    清單如下
        1. flask 相關模組
                |-->  Flask 基本設置 (class)
                |
                |-->  資料庫管理 (flask_sqlalchemy)
                |
                |-->  登入管理  (flask_login)
                |
                |-->  加密模組 (flask_bcrypt)
                |
                |-->  表單功能 (在 form.py 引用 => flask_wtf, wtforms)
                |
                |-->  前端模板 (flask_bootstrap，也可以引用 Bootstrap 官網提供的模板，作為替代方案。 P.S : 如果是大神等級，額外生一個，也是一種方案 (嗯......欸?)

        2. JWT 加密模組
        3. datetime 模組


    模組相關說明 (如下註記)

        從 flask 引入 Flask 類別
        。 render_template 從 templates 資料夾引入 .html 檔案
                預設資料夾名稱: templates
                若要改從其他名稱的資料夾引入，使用 Flask() 的參數 => template_folder = "更改名稱"
        。 request 網頁請求方式(在 HTTP 協定有 8 種)，常見有 4 種 -> GET, POST, DELETE, UPDATE
        。 redirect 網頁的重新導向 ex: 在 XX 網頁(/平台) 填完表單後提交完，轉到別的頁面之類的...
        。 url_for 導向指定函式之頁面， url_for("函式名稱")
'''
from flask import Flask, render_template, request, redirect, url_for
# from flask_bootstrap import Bootstrap   # 前端模板: 以 Jinja2 模板引擎，做一個引用

# 由左至右，依序為 => 初始化與登入管理、狀態紀錄器、驗證登入狀態、當前使用者身分、登出函式、狀態回傳
from flask_login import LoginManager, login_user, login_required, current_user, logout_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from configuration import Config
# import os

app = Flask(__name__) # __name__代表目前執行的模組

#  新版本的部份預設為none，會有異常，再設置True即可。
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# #  設置sqlite檔案路徑
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
#     os.path.join(pjdir, 'data.sqlite')
# app.config['SECRET_KEY'] = 'fjfisljdqoiahf;laojdqahlwdjayfghlkjd'

app.config.from_object(Config)

db = SQLAlchemy(app)
# 加密用
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'   # 還沒登入的狀態，去打開要登入 才可以使用 的頁面，會直接開啟 login() 函式底下的頁面 (就是登入畫面)

# bootstrap = Bootstrap(app)   # (贛話注意) 青菜蘿菠各有喜好