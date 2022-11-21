# 這是學習紀錄，flask 框架自學 與 實作
## 日後新增: 權限管理
## sqlite、註冊、登入功能，新增中...
# 警告! 會有蠻長一段的註解，以及~~贛話~~，耐心拜讀 (誤


### 其他の筆記 如下

* ```from flask_login import xxx, ooooo, ...... ```
      * |--> login_user()
                1. param user: 繼承 UserMixin 屬性的 "使用者類別"，以 object type 作為參數
                2. param remember: 記住登入狀態，以 session 的型態存取，以 boolean 開關功能
                3. param duration: 記住登入時長。 沒有設置，則承參數 remember，預設為 1 年
                                    該參數給定 "時間的資料型別"，也就是 "時間長度"
                                
                                ** 就是有給，就認給的時間 ; 沒給就乖乖用 remember 存 1 年 **
      * |--> @login_required 裝飾器
                4. 在登入成功後，才可以訪問的頁面。 譬如: 用戶管理、登入才能使用的功能


* **sqlite 資料庫建立 & 欄位筆記**
    * 總共兩步驟
        * 引用目標的編輯檔  >>> from 資料庫編輯檔 import db
        * 建立資料庫  >>> db.create_all()

    
    * sqlite 欄位筆記
        反正經常使用的型別，也就那幾個，當作這是個長~~~~~~~~的要命的筆記

        sqlite 建立欄位功能與型別

        說明 => __tablename__ = '資料庫的 table 名稱' : 若沒有設置，預設使用 class 的名稱 (轉小寫字母)
                primary_key = True : 基本上要有主鍵
                unique = True/False : 唯一值。 在同一個 table 下的欄位(同一個欄位下)，不可以有第二個相同的值
                nullable = True/False : 允許為空值。 開啟的時候，新增資料時，該欄位可以不用新增資料(可選的欄位)
                                                    反之，新增資料時，未新增到該欄位，要 debug 囉! (必填欄位)

                    欄位設置 Column() 沒設置，卻能用的，是用了甚麼巫術
            還是用了 C8764 或是 屠龍倚天劍 ，斬斷了要用 Column() 配置欄位的因果關係         (C8764 = 星爆氣流斬)

                以下是欄位型別 與 功能

                db.欄位功能                   | Python
        |----------------------------------|------------------|
        | 1. Column() : 配置欄位            |                  |   **  後面設置多更多
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

* **在 Python Shell 底下的 sqlite 指令**
    * (皆以使用者為例)

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


    3. 改動資料
           1. 針對已存在的資料，其他欄位的改動

               * 針對 "目標帳號" ，新增其他欄位的資料
                   - 這邊就要用到 "查詢使用者" 的指令，來指定目標新加資料
                       ```python
                       user = Users.query.filter_by(查詢欄位=輸入資訊).first()   # 查詢目標使用者

                       user.欄位 = 新增資料    # 針對 目標的欄位
                       db.session.add(user)
                       db.session.commit()
                       ```
           

    4. 查詢指令 => >>> user = Users.query.filter_by(查詢欄位=輸入資訊).first()
        
        ```
        * |>>> user = Users.query.filter_by(id = 1).first()
        * | <User: Rex, email: admin@hotmail.com>
        ```


