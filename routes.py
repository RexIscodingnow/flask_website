'''
    網站路由管理
'''

# Flask 的函式與功能
from flask_modules import app, render_template, redirect, url_for, request, session, Response
# 身分驗證 的函式與功能
from flask_modules import login_manager, login_user, login_required, current_user, logout_user, UserMixin

# 限速器
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from form import RegisterForm, LoginForm, ForgotPassword, GoodsPageForm    # flask 表單 && wtform 模組
from sqlite import db, Users, OtherData    # 資料庫管理

from datetime import timedelta, datetime


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=['50 per hour', '10 per minute']
)


@login_manager.user_loader
def load_user(user_id):
    '''
    回傳給 LoginManager 底下的 user_loader
    登入時要做驗證使用者 der~
    '''
    # 回傳使用者資訊
    return Users.query.get(int(user_id))

@app.route("/")  # 函式的裝飾 (Decorator): 以函式為基礎，提供附加的功能
def index():
    return render_template("index.html")

# route() => 代表我們要處理的網站路徑。 methods => 限制網頁請求方式，下方 "/piffle" 頁面限制只能用 GET 與 POST 請求
@app.route("/piffle", methods=['GET', 'POST'])
def pifflePage():
    return render_template("pifflePage.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    '''
        註冊功能，新增到資料庫
    '''
    # 已經登入過，則重新導向到 首頁
    if "user" in session:
        return redirect(url_for("index"))

    # 表單項目。 用 render_template() 的參數 **context 丟給目標 .html 檔案，呈現表單項目
    form = RegisterForm()
    
    # validate_on_submit() => 返回布林值， ** 所有必填選項 **  輸入完成且按下提交，返回 True，反之 False
    if form.validate_on_submit():
        # 用 form.表單項目名.data 取得輸入資訊
        username = form.username.data
        password = form.password.data
        email = form.email.data
        # 信箱已被註冊的提示訊息
        exist_user = Users.query.filter_by(email=email).first()
        if exist_user:
            return render_template("sign_up.html", form=form, msg='該信箱已被註冊!')

        user = Users(
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
    if "user" in session:
        return redirect(url_for("index"))

    form = LoginForm()

    if form.validate_on_submit():
        # 做一次搜尋 "使用者資料表"，判斷是否在資料庫內
        user = Users.query.filter_by(email=form.email.data).first()   # 以電子郵件欄位，作為搜尋條件
        if user:
            if user.check_password(form.password.data):
                # session.permanent = True
                remember_time = timedelta(minutes=form.remember_time.data)
                # session['user'] = form.email.data   # 新增一個 session

                # login_user(當下登入的使用者, 記住登入(自訂時間，要設為 True), 記住登入時間長度)
                login_user(user, remember=True, duration=remember_time)
                next = request.args.get('next')
                if not next_is_valid(next):
                    return "uhhhhhhhhhh.......uhhhhhhhhhhhhhhhhh......."

                return redirect(url_for("index") or next)

            else:
                return render_template("login.html", form=form, msg="密碼輸入有誤!")

        else:
            return render_template("login.html", form=form, msg="嘿嘿~~沒註冊喔")

    return render_template("login.html", form=form)

def next_is_valid(url):
    # print(url)
    return True

@app.route('/user')
@login_required
def user():
    '''
        @login_required 裝飾器
        是用在需要登入，才能訪問的頁面
    '''
    # print(request.cookies.get("remember_token"))
    return render_template("user.html")


def manageGoods(number):
    if number == 0:
        form = GoodsPageForm()
        messages = ["該車(牌)號(碼)", "該標題", " 已經紀錄了"]
        msg = ""
        if form.validate_on_submit():
            n_number = form.n_number.data
            n_title = form.n_title.data

            exist_number = OtherData.query.filter_by(numbers = n_number).first()
            exist_title = OtherData.query.filter_by(titles = n_title).first()
            if exist_number:
                msg = messages[0] + messages[2]
            elif exist_title:
                msg = messages[1] + messages[2]

            else:
                datas = OtherData()
                datas.numbers = n_number
                datas.titles = n_title

                db.session.add(datas)
                db.session.commit()

        return render_template("goods_home.html", form=form, msg=msg)

    elif number == 1:
        return render_template("goods_addInfo.html")

# 網址: /goods/1
@app.route("/goods/<int:number>", methods=['GET', 'POST'])
def goods(number=0):
    return manageGoods(number)


@app.route('/logout')
@login_required
def logout():
    '''
    登出功能 => logout_user()
    清除伺服端的標識 (cookie) => session.pop() 
    '''
    logout_user()
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route('/forgot_pw', methods=['GET', 'POST'])
def forgotPw():
    '''
    忘記密碼 之頁面
    後續調整
    '''
    form = ForgotPassword()

    if form.validate_on_submit():
        # 取的(查詢) 用戶的資訊
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            password = form.new_password.data
            user.password_hash = password   # 把用戶的密碼，做更改
            
            db.session.add(user)
            db.session.commit()

    return render_template("forgot_password.html", form = form)
