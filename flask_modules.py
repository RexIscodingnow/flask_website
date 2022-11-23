'''
    模組區
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