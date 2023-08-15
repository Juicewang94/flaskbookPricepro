
from apps.app import db, mail
from apps.auth.forms import SignUpForm, LoginForm
from apps.crud.models import User
from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_login import login_user, logout_user
from flask_mail import Message

# 使用Blueprint產生auth
auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")

# 建立index端點
@auth.route("/")
def index():
    return render_template("auth/index.html")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    # 建立SignUpForm的實體
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        # 檢測郵件位址是否已有人使用
        if user.is_duplicate_email():
            flash("這個郵件位址已經註冊過，請更換郵件位址")
            return redirect(url_for("auth.signup"))

        # 登錄使用者資訊
        db.session.add(user)
        db.session.commit()
        # 使用者資訊存到session 
        login_user(user)

        # 傳送郵件
        #send_emailmessage(
        #password 在crud/model.py設置為hash，會無法加載到其他函數
        print(user.email, user.username)
        send_email(
            user.email,
            "Thank you for the registration",
            user.username,
        )
        # 重新導向contact端點
        # flash("內容已傳送，您會收到一封註冊確認信，請至註冊郵件中查看，感謝您的註冊!")

        # 若GET參數的next鍵沒有值，則重新導向使用者的列表頁面
        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            #next_ = url_for("crud.users")
            next_ = url_for("home.index")
        return redirect(next_)

    return render_template("auth/signup.html", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    # 建立LoginForm的實體
    form = LoginForm()
    if form.validate_on_submit():
        # 由郵件位址取得使用者
        user = User.query.filter_by(email=form.email.data).first()

        # 若使用者存在且密碼一致，則允許登入
        if user is not None and user.verify_password(form.password.data):
            # 將使用者資訊存至session
            login_user(user)
            # 重新導向使用者的列表頁面
            print("--------Debug info--------:", user)
            print("--------Debug info--------:", form.email.data)
            if form.email.data == "juicewang94@gmail.com": #set manage account
                return redirect(url_for("crud.users"))
            else:
                return redirect(url_for("home.index"))
        
        if user is None:
            # 設定登入失敗的提示訊息
            flash("郵件位址不正確或尚未註冊")
        else:
            # 設定登入失敗的提示訊息
            flash("密碼不正確")
    return render_template("auth/login.html", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    #return redirect(url_for("auth.login"))
    return redirect(url_for("home.index"))  

#def send_email(to, subject, template, **kwargs):
#    """傳送郵件的函數"""
#    msg = Message(subject, recipients=[to])
#    msg.body = render_template(template + ".txt", **kwargs)
#    msg.html = render_template(template + ".html", **kwargs)
#    mail.send(msg)

def send_email(to, subject, username):
    """傳送郵件的函數"""
    msg = Message(subject, recipients=[to])
    msg.body = f'Hello {username} 您好! \n\n您的郵件位址已完成確認，感謝您的註冊!'
    mail.send(msg)
