# 這是學習紀錄，flask 框架自學 與 實作
## 日後新增: 權限管理
## sqlite、註冊、登入功能，新增中...
# 警告! 會有蠻長一段的註解，以及~~贛話~~，耐心拜讀 (誤

* **sqlite 資料庫建立**
    * 總共兩步驟
        * 引用目標的編輯檔  >>> from 資料庫編輯檔 import db
        * 建立資料庫  >>> db.create_all()

* **在 Python Shell 底下的 sqlite 指令**
    * (皆以使用者為例)

    1. 引用目標的編輯檔 => >>> ```from 資料庫編輯檔 import db```
            引入資料表 => >>> ```from 資料庫編輯檔 import Users, ......```
    
    2. 查詢指令 => >>> user = Users.query.filter_by(查詢欄位=輸入資訊).first()
        
        ```
        * |>>> user = Users.query.filter_by(id = 1).first()
        * | <User: Rex, email: admin@hotmail.com>
        ```

    3. 增加資料
        
           1. 新增全新的資料 (ex: 註冊新帳號)
               
               * 從管理資料表 的 class 操作
                   ```
                   user = Users(
                       username = 帳號名稱,    # 資料輸入到欄位內
                       email = 電子郵件,
                       password = 密碼
                   )
                   db.session.add(user)    # 新增
                   db.session.commit()     # 提交
                   ```

           2. 已存在的資料，其他欄位新增

               * 針對 "目標帳號" ，新增其他欄位的資料
                   - 這邊就要用到 "查詢使用者" 的指令，來指定目標新加資料
                       ```
                       user = Users.query.filter_by(查詢欄位=輸入資訊).first()   # 查詢目標使用者

                       user.欄位 = 新增資料    # 針對 目標的欄位
                       db.session.add(user)
                       db.session.commit()
                       ```

    4. 改動資料

           1. 


