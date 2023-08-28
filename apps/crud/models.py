from datetime import datetime

from apps.app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# 建立繼承db.Model與UserMixin的User類別
class User(db.Model, UserMixin):
    # 指定表格名稱
    __tablename__ = "users"
    # 定義直欄內容
    # for SQLit
    #id = db.Column(db.Integer, primary_key=True)
    # for MySQL
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # 設置密碼的屬性
    @property
    def password(self):
        raise AttributeError("無法加載")
    # 藉由設置密碼的setter函數，設定經過hash處理的密碼
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # 檢測密碼
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 檢測郵件位址是否已有人使用
    def is_duplicate_email(self):
        return User.query.filter_by(email=self.email).first() is not None

# 建立取得登入使用者資訊的函數
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Price(db.Model):
    # 指定表格名稱
    __tablename__ = "price_record"
    # 定義直欄內容
    # for MySQL
    update_date = db.Column(db.DateTime, primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    pxgo_price = db.Column(db.Integer)
    pxbox_price = db.Column(db.Integer)
    rmart_price = db.Column(db.Integer)
    crf_price = db.Column(db.Integer)