from pathlib import Path

basedir = Path(__file__).parent.parent

# 建立BaseConfig類別
class BaseConfig:
    SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ"
    WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f"

#    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))

# 繼承BaseConfig，建立LocalConfig類別
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user1:password@34.172.156.246:3306/gcpproject"
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://luke:1qaz2wsx@35.184.152.217:3306/PRICE2"
    #SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

# 繼承BaseConfig，建立TestingConfig類別
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user1:password@34.172.156.246:3306/gcpproject"
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://luke:1qaz2wsx@35.184.152.217:3306/PRICEPRO"
    #SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    # UPLOAD_FOLDER = str(Path(basedir, "tests", "detector", "images"))


# 建立config字典
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
