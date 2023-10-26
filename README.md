# 這是學習紀錄，flask 框架自學 與 實作
# 警告!! 會有蠻長一段的註解，~~以及贛話~~，耐心拜讀 (誤
## 日後新增: 權限管理
<!-- ## sqlite、註冊、登入功能，新增中... -->


# 目錄
   * 清單如下
        ```
        1. flask 相關模組
                |-->  Flask 基本設置 (class)
                |
                |-->  資料庫管理 (flask_sqlalchemy, flask_migrate)
                |
                |-->  登入管理  (flask_login)
                |
                |-->  加密模組 (flask_bcrypt)
                |
                |-->  表單功能 (在 form.py 引用 => flask_wtf, wtforms)
                |
                |-->  前端模板 (flask_bootstrap，也可以引用 Bootstrap 官網提供的模板，作為替代方案。)
                        P.S :如果是大神等級，額外生一個，也是一種方案 (嗯......欸?)

        2. JWT 加密模組
        3. datetime 模組
        ```

  * 模組相關說明 (如下註記)
    ```
        從 flask 引入 Flask 類別

        。 render_template 從 templates 資料夾引入 .html 檔案
                預設資料夾名稱: templates
                若要改從其他名稱的資料夾引入，使用 Flask() 的參數 => template_folder = "更改名稱"

        。 request 網頁請求方式(在 HTTP 協定有 8 種)，常見有 4 種 -> GET, POST, DELETE, UPDATE

        。 redirect 網頁的重新導向 ex: 在 XX 網頁(/平台) 填完表單後提交完，轉到別的頁面之類的...

        。 url_for 導向指定函式之頁面， url_for("函式名稱")


        登入管理模組 =>  flask_login
        。 login_manager.init_app(app)  =>  初始化 flask_login 模組

        。 login_manager.login_view = 'login'
                大概是: 未登入 或 訪客 狀態，進入需要登入才能 使用的頁面。
                        阻擋 非登入用戶，將其轉到登入頁面，做登入步驟
        
        。 login_manager.session_protection = 'strong'
                保護 cookie 用的參數，有 'basic' 與 'strong' 兩個等級
                    或是關閉該功能 'None' ，預設值為 'basic'
    ```
        

# sqlite 資料庫建立 & 欄位筆記

  * **連接資料庫**
    * 在 app.config[ 參數 ] 底下的設置
        
        1. SQLALCHEMY_DATABASE_URI  =>  資料庫路徑
            
            * 路徑設置，如下  
                  1. (Windows，3 個 / 號) ->  'sqlite:///' + 'sqlite 檔案，放在哪個資料夾底下'     
                  2. (Linux，4 個 / 號) -> 'sqlite:////' + 'sqlite 檔案，放在哪個資料夾底下'
            
            * 延伸
                * MySQL: mysql://username:password@hostname:port/database
                      1. username: 使用者名稱
                      2. password: MySQL 的密碼
                      3. hostname: 主機名 (預設是 localhost => 127.0.0.1)
                      4. port: 連接埠 (預設是 3306)
                      5. database: 要連接的資料庫

                * PostgreSQL: postgresql://username:password@hostname/database

        2. SQLALCHEMY_TRACK_MODIFICATIONS  =>  查到是寫信號

    <br>

  * 兩步驟建立資料庫
      1. 引用目標的編輯檔  >>> from 資料庫編輯檔 import db
      2. 建立資料庫  >>> db.create_all()
      
      ```
      * 註記 1: 引入的參數 db 是屬於 SQLAlchemy() 的物件，
                指令: from 資料庫編輯檔 import db
                
                這個 "資料庫編輯檔" 是有宣告 資料庫欄位、屬性的編輯檔

      * 註記 2: db.create_all() 的指令，如果已經建立好 .sqlite 檔案，
              那又 有一個 或 二個(含)以上的資料表，要新增在原檔案裡，
              再使用一次 db.create_all() 的指令，其實會在原檔案裡
              **再加蓋上去，也就是在原檔案新增，原始資料不變動，的情況下添加新的資料表**
        
        至少我操作的結果是這樣啦!
      ```
    
    <br>

  * sqlite 欄位筆記

    ```
    sqlite 建立欄位功能與型別 (簡介、懶人包)

    說明 => __tablename__ = '資料庫的 table 名稱' : 若沒有設置，預設使用 class 的名稱 (轉小寫字母)
            primary_key = True : 基本上要有主鍵
            unique = True/False : 唯一值。 在同一個 table 下的欄位(同一個欄位下)，不可以有第二個相同的值
            nullable = True/False : 允許為空值。 開啟的時候，新增資料時，該欄位可以不用新增資料(可選的欄位)
                                                反之，新增資料時，未新增到該欄位，要 debug 囉! (必填欄位)

    反正經常使用的型別，也就那幾個，當作這是個長~~~~~~~~的要命的筆記
    
    建立欄位沒使用 Column()，卻能搞出來的，
    是用了甚麼巫術，還是用了 C8764 或是 屠龍倚天劍 ，斬斷了要用 Column() 配置欄位的因果關係
    
    註1 : C8764 => 星爆氣流斬，源自於動畫刀劍神域，主角的絕招
    註2 : 屠龍倚天劍 => 武俠小說會出現的高級武器
    ```

    <br>
    
    
    | 欄位常用屬性參數  | 用途   |
    |------------|-------------|
    |primary_key | 主鍵         |
    |unique	     | 唯一值       |
    |index	     | 設置索引     |
    |nullable	 | 允許null     |
    |default	 | 設置欄位預設值|
          
    |       db.欄位功能                 | Python  資料型別 |
    |----------------------------------|------------------|
    | 1. Column() : 配置欄位            |                  |
    | 2. Integer : 32 bit 的整數        | int              |
    | 3. SmallInteger : 16 bit 的整數   | int              |
    | 4. BigInteger : 不限精度 的整數   | int              |
    | 5. Float : 浮點數                 | float            |
    | 6. String(字數) : 文字            | str              |
    | 7. Text() : 長字串                | str              |
    | 8. LargeBinary : 二進制文件       | str              |
    | 9. PickleType : 序列化文件        | object           |

      
<br>

  * 增、刪、改、查，等功能操作
    大致會用到 3 個函式:
    * db.session.add(新增資料 or 更動資料)
    * db.session.delete(要刪除的目標資料)
    * db.session.commit()  =>  提交資料更改。 前面兩種指令執行後，一定要推送，不然不會更動
    
    查詢:
    ```
        class 名稱(資料表).query.filter().功能()  =>  功能() --> all() 全抓下來 (所有查詢結果)
                                                                first() 返回第一筆資料
                                                                ......
        
        class 名稱(資料表).query.filter_by().功能() => filter_by() 做簡單查詢，有人說是語法糖
                                    
                                    P.S : 好比 SQL 的語句 where, MySQL 的 select
    ```

## **在 Python Shell (CLI) 底下的 sqlite 指令**
* 皆以使用者為例
* 這邊是 command prompt, powershell 底下的命令列操作

1. 引用目標的編輯檔
        
        引入資料表 => ``` >>> from 資料庫編輯檔 import Users, ......```


2. 增加資料
    
    1. 新增全新的資料 (ex: 註冊新帳號)

        * 從管理資料表 的 class 操作
            ```python
            user = Users(
                username = 帳號名稱,    # 資料輸入到欄位內
                email = 電子郵件,
                password = 密碼
            )
            db.session.add(user)    # 新增
            db.session.commit()     # 提交
            ```
     2. 針對已存在的資料，其他欄位的新增
           
           * 操作方式: 其實與 "**第 3 點 的 改動資料**" 的操作方式，步驟類似

           * 流程大致上為
               1. 查詢 (過濾、篩選到) "**目標使用者**"
               2. 查到的使用者，挑一下要增加的欄位
               3. 最後把資料塞進去後，提交變更
            
        **查詢 請看第 4 點: 查詢指令**

3. 改動資料
       
    * 針對已存在的資料，其他欄位的改動
         * 針對 "目標帳號" ，新增其他欄位的資料
            這邊就要用到 "查詢使用者" 的指令，來指定目標新加資料
            ```python
            user = Users.query.filter_by(查詢欄位=目標資料).first()   # 查詢目標使用者

            user.欄位 = 輸入資料    # 針對 目標的欄位
            db.session.add(user)
            db.session.commit()
            ```
       

4. 查詢指令 => >>> user = Users.query.filter_by(查詢欄位=輸入資訊).first()
    
    ```python
    PS >>> user = Users.query.filter_by(id = 1).first()
    PS >>> <User: Rex, email: admin@hotmail.com>
    ```

5. 刪除資料
   
   * 流程如下
        1. 查詢目標 => >>> user = Users.query.filter_by(查詢欄位=輸入資訊).first()
        2. 刪除資料 => >>> db.session.delete(user)
        3. 提交更動 => >>> db.session.commit()


* **Sqlite 的資料庫搬遷 (欄位改動)**
    
    * 簡介: 當 sqlite 已經用 db.create_all() 指令建立完成後，假如有要新增其他欄位，
            **在已經建好的資料表中，異動 目標欄位**
            那麼，原先的建立指令 db.create_all() 就不管用
            為什麼呢 ?
            **畢竟 db.create.all() 是用來建立 整個資料"表"**
            **而非單獨建立資料"欄"**
        
        * 假設，有一個管理使用者的資料表，那我要在原先的資料表中，新增存放個人資料的 "年齡"、"性別"、"血型"
          一共 3 個欄位，那如果使用 db.create_all() 的方式，添加在原本的"資料表"
          **那麼，我必須把原本的 .sqlite 檔案整個刪除，再用 db.create_all() 做新增才可以達成**
        
        * 因為 db.create_all() 是建立整個資料表的特性，所以要使用 flask_migrate 模組，作為 **"單獨建立資料欄"** 來解決

    * 安裝模組
        * 指令 => ```pip install flask-migrate```

    * 前置動作
        1. ```from flask_migrate import Migrate```
        2. ```migrate = Migrate(app, db)```
            * 放置參數如下
                1. app: Flask(__name__) 的網站參數操縱名稱 (指派過去的 變數名稱)
                2. db: SQLAlchemy(app) 的資料庫操作名稱 (指派過去的 變數名稱)
    
    * flask_migrate 的指令操作
    * 操作工具: Windows 命令提示字元

        * 在初始設定，總共有 4 個步驟
              1. set FLASK_APP = app.py  ----> 為主要執行的 Python 檔案 (整個程式的 entry pointer (進入點))
              2. flask db init  ----> 初始化 migrate，創建 migrations 資料夾
              3. flask db migrate -m "說明文字"  ----> 建置腳本
              4. flask db upgrade  ----> 更新版本
        
        * 之後的第 2 次、第 3 次、......
              * 基本上，就剩下 "上方的步驟 3 ~ 4 的指令"

        * 其他指令
            * flask db --help
                可以查詢相關指令
            * flask db init [–multidb]
                初始化資料庫
            * flask db migrate
                建置腳本，會自動對異動的db做腳本的建立，這時候不會影響到資料庫
            * flask db edit
                …
            * flask db upgrade
                如果沒有指定版本，則以最新版本來更新
            * flask db downgrade
                資料庫降版，如果沒有指令就以上版還原
            * flask db stamp
                …
            * flask db current
                顯示當前版本
            * flask db history
                顯示歷史歷程
            * flask db show
                顯示當前版本詳細資訊
            * flask db merge
                合併兩個版本
            * flask db heads
                顯示目前版本號
            * flask db branches
                顯示當前分支點

### 其他の筆記 如下

* ```python
    @app.route('/user/<id>')
    def user(id):
        ......
        return ......
  ```

      * |--> 帶有 <> 號是 "路由上設置的參數"，底下宣告一個 "同名稱變數" 做接收數值
      * |--> 其他設置
              1. @app.route('/your_route/<type: variable>')  =>  <型別: 變數名>
              2. flask 支援的型別有 ```str```, ```int```, ```float```, ```path```，
                    如果沒有特別定義參數型別，則預設型別為 "字串"


* ```python
    from flask import Flask

    app = Flask(__name__, 
        static_url_path="",  # 靜態檔案，在路由上訪問的路徑 (網路上)
        static_folder="",  # 靜態檔案 (CSS, JS) 檔案路徑 (本地端)
        template_folder=""  # 樣板渲染 (HTML) 檔案路徑 (本地端)
    )
  ```


* ```from flask import XXX, ooo, ......```

      * |--> render_template
                1. param template_name_or_list: 
                        1-1. 資料型別: 字串
                        1-2. 檔案名稱 (ex: "xxxooxo.html")
                2. param **context:
                        前端用的 = 後端用的
                
            實作: return render_template("xxxooo.html", Jinja2_變數名-1 = 要顯示的資訊-1, Jinja2_變數名-2 = 要顯示的資訊-2, ...)


* ```from flask_login import xxx, ooooo, ...... ```

      * |--> login_user()
                1. param user: 繼承 UserMixin 屬性的 "使用者類別"，以 object type 作為參數
                2. param remember: 記住登入狀態，以 session 的型態存取，以 boolean 開關功能
                3. param duration: 記住登入時長。 沒有設置，則承參數 remember，預設為 1 年
                                            該參數給定 "時間的資料型別"
                                            datetime 模組底下的 timedelta
                                
                                ** 就是有給，就認給的時間 ; 沒給就乖乖用 remember 存 1 年 **
                        
                    若不用 duration 這個參數，則用
                        
                        => app.permanent_session_lifetime = remember_time

                        效果是一樣的，就是控制 session 存活時間
                        注意!! 要把 permanent 屬性設為 True

                        => session.permanent = True

      * |--> @login_required 裝飾器
                4. 在登入成功後，才可以訪問的頁面。 譬如: 用戶管理、登入才能使用的功能



* ```from flask_wtf import FlaskForm```

      * |--> validate_on_submit()  表單確認
                1. return type: bool
                2. ** 所有必填選項 **  輸入完成且按下提交，返回 True，反之 False
                                   "" 非必填的項目，不在範圍內 ""



* ```from wtforms import OOO, XXX, .....```

      * flask_wtf 表單設置
        用 class 作為 "每一種頁面的表單"
        
        (使用前，先繼承老爸的能力)
        使用前先繼承 flask_wtf 模組，裡面的 class => FlaskForm

      * wtforms 底下的功能

        (防守狀態: 我方發動 XXXXX 驗證器，作為防守。 防守效果: 格式錯誤，不給通過，若對手攻擊大於 500 點，即刻反彈對手攻擊，再乘兩倍的 HP 傷害......喂!中二病發作喔!)
        在 wtforms 底下的功能，其中有驗證器檢查輸入內容
        比如說: 必填選項 => DataRequired()
                相同內容 => EqualTo()  應用場景: 註冊帳號、修改密碼 的 再輸入一次密碼
                
                其他要輸入特定格式的欄位，檢查有沒有符合格式

                ** 註: DataRequired() 與 EqualTo() ---->  在 wtforms.validators 底下

      * 導入 wtforms 模組，它底下的欄位

        欄位們: 
                1. 輸入框 -----> 單行: StringField()
                        -----> 多行: TextAreaField()
                1-1. 密碼 -----> PasswordField()
                1-2. 電子郵件 -----> EmailField()

                2. 送出按鍵 -----> SubmitField()
                ...
                ...


* Jinja2 模板引擎
      * 這邊就大概紀錄先前操作過的功能，詳細說明就到官方文檔，慢慢細品
      * 官方網站: https://jinja.palletsprojects.com/

      * 這部分是在 HTML 的操作，相關的參數 與 過濾器函式

          1. 表達式
               1. {%  %}
                 * 說明: { } 內部的兩側，以 % 號表示，是做為運算用的表示式
                 
                 * 例子: 
                      1. 樣板繼承: {% extends "繼承的檔案路徑" %}
                      2. 繼承後要在目標位置，顯示指令內容
                            目標的樣板: base.html
                                {% block 使用的名稱 %}

                            要使用的樣板: user.html
                                {% block 使用的名稱 %}
                                    樣板內容
                                {% endblock %}
                      3. for 迴圈
                            {% for item in items %}
                                {{ item }}
                            {% endfor %}

               2. {{  }}
                 * 說明: 用兩層 { } 號表示，此為行語句，透過一的 標籤(tag)來代表 表達式
                 
                 * 例子:
                      * 在 Python 這邊的路由
                            ```python
                            @app.route("/xxxx", mothods=["GET", "POST"])
                            def page():
                                ......
                                ......
                                return render_template("目標檔.html", value_1 = 運算結果-1, value_2 = 運算結果-2)
                            ```

                      * 在 HTML 檔案
                            ```html
                            <html>
                                <head> ........ </head>
                                <body>
                                    {{ value_1 }}

                                    {{ value_2 }}
                                </body>
                            </html>
                            ```

               3. {#  #}
                 * 說明: { } 內部的兩側，以 # 號表示，這是做為 Jinja2 註解使用的
                 
                 * 例子:
                      1. {# 我的註解 #}
                      2. {#
                            {% for item in items %}
                                {{ item }}
                            {% endfor %}
                          #}

      * 各式操作範例

          1. 模板繼承: 有時候，當我們把一個頁面的 HTML 內的設計，或是切版做完了，
                       但假設會有不同功能的頁面，會使用到同一個類型的切版設計，
                       難不成，要重新再打一遍 (或 Ctrl + C, Ctrl + V) 嗎 ?!
                       
                       那在使用模板繼承，至少可以省下一些步驟

                範例程式碼如下:

                * file name: base.html

                    ```html
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                            <title>{% block title %}{% endblock %}</title>
                        </head>
                        <body>
                            {% block content %}
                            {% endblock %}
                        </body>
                    </html>
                    ```

                * file name: user.html

                    ```html
                    {# 繼承模板: base.html #}
                    {% extends "base.html" %}

                    {# 作用於 base.html 的 title 標籤裡面 #}
                    {% block title %}
                        User Profile
                    {% endblock %}

                    {# 在 base.html 的 body 標籤內部，操作 #}
                    {% block content %}
                    
                    <div>
                        <!-- user.html 的內容 -->
                        ...
                    </div>

                    {% endblock %}
                    ```

