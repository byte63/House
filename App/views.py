from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, abort, request, jsonify, session
from sqlalchemy import or_

from App.models import HouseListing, User

house = Blueprint('house', __name__)


def login_require(func):
    def wrapper(*args, **kwargs):
        if not session.get("name"):
            return redirect(url_for("house.login"))
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper


@house.route("/")
def index():
    return redirect(url_for("house.listing", page=1))


@house.route("/<int:page>")
@login_require
def listing(page=None):
    last_date = HouseListing.query.with_entities(HouseListing.create_date).order_by(HouseListing.create_date.desc()).first()
    paginate = HouseListing.query.filter_by(create_date=last_date[0]).order_by(HouseListing.area_name.asc()).paginate(page=page, per_page=10, error_out=False)
    houses = paginate.items
    areas = HouseListing.query.with_entities(HouseListing.area_name, HouseListing.area_id).group_by(HouseListing.area_name, HouseListing.area_id).all()
    return render_template("listing.html", houses=houses, paginate=paginate, areas=areas)


@house.route("/search/<int:page>",)
@login_require
def search(page=1):
    # paginate = HouseListing.query.filter(or_(HouseListing.house_name.like("%{}%".format(house_name)), HouseListing.area_name.like("%{}%".format(house_name)))).paginate(page=page, per_page=10, error_out=False)
    house_name = request.args.get("house_name") or ""
    houses = HouseListing.query.filter(or_(HouseListing.house_name.like("%{}%".format(house_name)), HouseListing.area_name.like("%{}%".format(house_name)))).distinct().all()
    _id = []
    _house_id = []
    for house in houses:
        if house.house_id in _house_id:
            continue
        _id.append(house.id)
        _house_id.append(house.house_id)

    paginate = HouseListing.query.filter(HouseListing.id.in_(_id)).paginate(page=page, per_page=10, error_out=False)
    houses = paginate.items
    return render_template("search.html", paginate=paginate, houses=houses, house_name=house_name)


@house.route('/detail/<int:house_id>')
@login_require
def _detail(house_id):
    return redirect(url_for("house.detail", house_id=house_id, page=1))


@house.route("/detail/<int:house_id>/<int:page>")
@login_require
def detail(house_id, page=1):
    paginate = HouseListing.query.filter_by(house_id=house_id).paginate(page=page, per_page=10, error_out=False)
    houses = paginate.items
    if not houses:
        return abort(404)
    title = houses[0].house_name
    return render_template("info.html", paginate=paginate, houses=houses, title=title, house_id=house_id)


@house.route("/check_user", methods=["POST"])
def check_user():
    user_name = request.form.get("user_name")
    return jsonify({"status": False})


@house.route("/register", methods=["POST"])
@login_require
def register():
    email = request.json.get("email")
    password = request.json.get("password")
    if not email or not password:
        return jsonify({"status": 400, 'msg': "缺少必要参数!"}), 400
    user = User()
    user.email = email
    user.password = password
    if not user.save():
        return jsonify({"status": 401, "msg": "注册失败!"}), 401
    return jsonify({"status": 200, "msg": "注册成功!"}), 200


def get_user(email):
    user = User.query.filter(User.email == email).first()
    if not user:
        return False
    return user


@house.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"status": 400, 'msg': "请检查用户名密码!"}), 200

    user = get_user(email)
    if not user:
        return jsonify({"status": 400, 'msg': "请检查用户名密码!"}), 200

    if not user.check_password(password):
        return jsonify({"status": 400, 'msg': "请检查用户名密码!"}), 200

    session["name"] = email
    session.permanent = True
    return jsonify({"status": 200, 'msg': "登陆成功!"}), 200
