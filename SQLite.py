from app import db

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