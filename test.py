from app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.init_app(app)

pw = str(input("pw: "))
db_pw = '1234'
generate_pw = bcrypt.generate_password_hash(db_pw)
pw_check = bcrypt.check_password_hash(generate_pw, pw)
print(pw, generate_pw, pw_check)

class Test:
    name = 'haash'

print(Test.name)