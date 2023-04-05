from flask_modules import db, bcrypt, UserMixin


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

class Users(db.Model, UserMixin):
    __tablename__ = 'users'     # sqlite 資料庫的 tablename
    id = db.Column(db.Integer, primary_key=True)    # 設定主鍵
    # String -> 文字型態  unique -> 唯一值  nullable -> True: 可空格, False: 不能為空
    # String(50) -> 最多50字
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profile = db.Column(db.String(100))

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


class OtherData(db.Model):
    '''
    其他資訊
    '''
    __tablename__ = 'N_goods'
    id = db.Column(db.Integer, primary_key=True)
    numbers = db.Column(db.String(50))
    titles = db.Column(db.String(150))

    def __repr__(self):
        return "<numbers: %s, title: %s>" % (self.numbers, self.titles)

