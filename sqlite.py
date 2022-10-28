from flask_modules import db, bcrypt

'''
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
'''

'''
    權限篇，日後更新
'''
##  設置中繼的關聯表
#  flask-sqlalchemy會自動的在資料庫中產生相對應的table
# relations_user_role = db.Table('relation_user_role',
#                             db.Column('user_id', db.Integer, db.ForeignKey('UserRgeisters.id')),
#                             db.Column('role_id', db.Integer, db.ForeignKey('roles.id')))

# class Role(db.Model):
#     """
#     權限角色主表
#     不需設置ForeignKey，會透過SQLAlehemy的多對多關聯機制處理
#     :parameter
#         name:角色名稱
#     """
#     __tablename__ ='roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return 'Role is %s' % self.name

class Users(db.Model):
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
        '''
            這個函式返回值，是在 terminal 執行 Python Shell 底下
            對資料庫 進行【增、刪、改、查】等指令
            所返回的 " 指定欄位資料 "
        '''
        return "<User: %s, email: %s>" % (self.username, self.email)
