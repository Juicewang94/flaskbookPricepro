from pathlib import Path

basedir = Path(__file__).parent.parent

# 建立BaseConfig類別
class BaseConfig:
    SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ"
    WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f"

#    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))

#    LABELS = [
#        "unlabeled",
#        "person",
#        "bicycle",
#        "car",
#        "motorcycle",
#        "airplane",
#        "bus",
#        "train",
#        "truck",
#        "boat",
#        "traffic light",
#        "fire hydrant",
#        "street sign",
#        "stop sign",
#        "parking meter",
#        "bench",
#        "bird",
#        "cat",
#        "dog",
#        "horse",
#        "sheep",
#        "cow",
#        "elephant",
#        "bear",
#        "zebra",
#        "giraffe",
#        "hat",
#        "backpack",
#        "umbrella",
#        "shoe",
#        "eye glasses",
#        "handbag",
#        "tie",
#        "suitcase",
#        "frisbee",
#        "skis",
#        "snowboard",
#        "sports ball",
#        "kite",
#        "baseball bat",
#        "baseball glove",
#        "skateboard",
#        "surfboard",
#        "tennis racket",
#        "bottle",
#        "plate",
#        "wine glass",
#        "cup",
#        "fork",
#        "knife",
#        "spoon",
#        "bowl",
#        "banana",
#        "apple",
#        "sandwich",
#        "orange",
#        "broccoli",
#        "carrot",
#        "hot dog",
#        "pizza",
#        "donut",
#        "cake",
#        "chair",
#        "couch",
#        "potted plant",
#        "bed",
#        "mirror",
#        "dining table",
#        "window",
#        "desk",
#        "toilet",
#        "door",
#        "tv",
#        "laptop",
#        "mouse",
#        "remote",
#        "keyboard",
#        "cell phone",
#        "microwave",
#        "oven",
#        "toaster",
#        "sink",
#        "refrigerator",
#        "blender",
#        "book",
#        "clock",
#        "vase",
#        "scissors",
#        "teddy bear",
#        "hair drier",
#        "toothbrush",
#    ]


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
