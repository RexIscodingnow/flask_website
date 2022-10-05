import os

class Config():
    # 取得目前文件資料夾路徑
    pjdir = os.path.abspath(os.path.dirname(__file__))
    # 新版本的部份預設為none，會有異常，再設置True即可。
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 設置sqlite檔案路徑
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(pjdir, 'data.sqlite')

    SECRET_KEY = 'fjfisljdqoiahf;laojdqahlwdjayfghlkjd'