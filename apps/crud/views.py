from apps.app import db
from apps.crud.forms import UserForm
from apps.crud.models import User
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

# 使用Blueprint建立crud應用程式
crud = Blueprint("crud", __name__, template_folder="templates", static_folder="static")

# 建立index端點並返回index.html
@crud.route("/")
@login_required
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
@login_required
def sql():
    db.session.query(User).all()
    return "請確認控制台日誌"

@crud.route("/users/new", methods=["GET", "POST"])
@login_required
def create_user():
    # 建立UserForm實體
    form = UserForm()
    # 驗證表單值
    if form.validate_on_submit():
        # 建立使用者
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        # 增加並提交使用者
        db.session.add(user)
        db.session.commit()
        # 重新導向使用者列表頁面
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)

@crud.route("/users")
@login_required
def users():
    """取得user列表"""
    users = User.query.all()
    return render_template("crud/index.html", users=users)

# methods指定GET和POST
@crud.route("/users/<user_id>", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    form = UserForm()

    # 利用User模型取得使用者
    # for SQLite
    #user = User.query.filter_by(id=user_id).first()
    # for MySQL
    user = User.query.filter_by(id=user_id).first()

    # 發送表單後，修改內容並重新導向使用者列表頁面
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    # Method為GET時，回傳edit HTML檔案
    return render_template("crud/edit.html", user=user, form=form)

@crud.route("/users/<user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    # for SQLite
    #user = User.query.filter_by(id=user_id).first()
    # for MySQL
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))
