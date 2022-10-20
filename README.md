# 這是學習紀錄，flask 框架自學 與 實作
## 日後新增: 權限管理
## sqlite、註冊、登入功能，新增中...
# 警告! 會有蠻長一段的註解，以及~~贛話~~，耐心拜讀 (誤

* **sqlite 資料庫建立**
  * 總共兩步驟
        * 引用目標的編輯檔  >>> from 資料庫編輯檔 import db
        
        * 建立資料庫  >>> db.create_all()

* **在 Python Shell 底下的 sqlite 指令**
    1. 引用目標的編輯檔 => >>> from 資料庫編輯檔 import db
               引入資料表 => >>> from 資料庫編輯檔 import Users, ......
    
    2. 查詢指令 (以查詢使用者為例) => >>> user = Users.query.filter_by(查詢欄位=輸入資訊).first()
        
        * >>> user = Users.query.filter_by(id = 1).first()
        * <User: Rex, email: admin@hotmail.com>

    3. 增加資料