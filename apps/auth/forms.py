from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length


# 新增註冊使用者的表單類別
class SignUpForm(FlaskForm):
    # 設定使用者表單中username屬性的標籤和驗證器
    username = StringField(
        "使用者名稱",
        validators=[
            DataRequired(message="必須填寫使用者名稱"),
            length(max=30, message="請勿輸入超過30個字元"),
        ],
    )

    # 設定使用者表單中email屬性的標籤和驗證器
    email = StringField(
        "郵件位址",
        validators=[
            DataRequired(message="必須填寫郵件位址"),
            Email(message="請依照電子郵件的格式輸入"),
        ],
    )

    # 設定使用者表單中password屬性的標籤和驗證器
    password = PasswordField("密碼", validators=[DataRequired(message="必須填寫密碼")])

    # 設定使用者表單中submit的內容
    submit = SubmitField("提交表單")

class LoginForm(FlaskForm):
    email = StringField(
        "郵件位址",
        validators=[
            DataRequired("必須填寫郵件位址"),
            Email("請依照電子郵件的格式輸入"),
        ],
    )
    password = PasswordField("密碼", validators=[DataRequired("必須填寫密碼")])
    submit = SubmitField("登入")
