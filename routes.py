from flask_modules import app, render_template, redirect, url_for    # flask 的函式與功能
from flask_modules import login_manager, login_user, login_required, current_user, logout_user, UserMixin
from form import RegisterForm, LoginForm    # flask 表單 && wtform 模組
from sqlite import db, User

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
                remember_time = form.remember_time.data
                
                # login_user(當下登入的使用者, 記住登入(自訂時間，要設為 True), 記住登入時間長度)
                login_user(user, remember=True, duration=remember_time)

                return redirect(url_for('user'))

            else:
                return render_template("login.html", form=form, msg="密碼輸入有誤!")

        else:
            return render_template("login.html", form=form, msg="嘿嘿~~沒註冊喔")

    return render_template("login.html", form=form)

@app.route('/user')
@login_required
def user():
    return render_template("user.html")

if __name__ == "__main__": # 如果以主程式執行
    app.run(debug=True)