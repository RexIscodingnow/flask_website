from app import db

'''
    普通 sqlite 的建立的方式

    說明 => __tablename__ = '資料庫的 table 名稱' : 若沒有設置，預設使用 class 的名稱
            primary_key = True : 基本上要有主鍵

            以下是我用過 der...

            db.欄位功能                   | Python
       |----------------------------------|------------------|
       | 1. Column() : 配置欄位            |                  |
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
'''
class User(db.Model):
    __tablename__ = 'users'     # sqlite 資料庫的 tablename
    id = db.Column(db.Integer, primary_key=True)    # 設定主鍵
    # String -> 文字型態  unique -> 唯一值  nullable -> True: 可空格, False: 不能為空
    # String(50) -> 最多50字
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

'''
    權限篇，日後更新
'''
##  設置中繼的關聯表
#  flask-sqlalchemy會自動的在資料庫中產生相對應的table
relations_user_role = db.Table('relation_user_role',
                            db.Column('user_id', db.Integer, db.ForeignKey('UserRgeisters.id')),
                            db.Column('role_id', db.Integer, db.ForeignKey('roles.id')))

class Role(db.Model):
    """
    權限角色主表
    不需設置ForeignKey，會透過SQLAlehemy的多對多關聯機制處理
    :parameter
        name:角色名稱
    """
    __tablename__ ='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Role is %s' % self.name