import os
from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config
from flask_login import LoginManager
from flask_mail import Mail

# 建立SQLAlchemy實體
db = SQLAlchemy()
# Flask-WTF防CSRF功能實體
csrf = CSRFProtect()
# 建立LoginManager實體
login_manager = LoginManager()
# 在login_view屬性，指定未登入時重新導向的端點
login_manager.login_view = "auth.signup"
# 在login_view屬性，指定登入後顯示的訊息，設為空值不顯示任何內容
# 若未編寫login_manager.login_message，會輸出預設的英文訊息
login_manager.login_message = ""
# 建立Mail實體
mail = Mail()

#def create_app(config_key):
def create_app():
    app = Flask(__name__)
    # 加載config_key配對的環境組態類別(以from_object設定應用程式組態)
    #app.config.from_object(config[config_key])
    # 以from_mapping設定應用程式SQLAlchemy組態
    app.config.from_mapping(
        SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ",
        WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f",
        SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user1:password@34.172.156.246:3306/gcpproject",
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        SQLALCHEMY_ECHO = True
    )
    # 增加Mail類別的組態
    app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
    app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
    app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
    app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")
    # 連結SQLAlchemy和應用程式
    db.init_app(app)
    # 連結Migrate和應用程式
    Migrate(app, db)
    # 連結Flask-WTF防CSRF功能和應用程式
    csrf.init_app(app)
    # 連結login_manager和應用程式
    login_manager.init_app(app)
    # 由apps/crud/views.py import views
    from apps.crud import views as crud_views
    # 使用register_blueprint，將views的crud登錄至應用程式
    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    # 由apps/crud/views.py import views
    from apps.auth import views as auth_views
    # 使用register_blueprint，將views的auth登錄至應用程式
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    from apps.home import views as home_views
    # 使用register_blueprint，將views的home登錄至應用程式
    app.register_blueprint(home_views.home, url_prefix="/home")

    # 連結Mail和應用程式
    mail.init_app(app)
    return app
