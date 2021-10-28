from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, abort

from App.models import HouseListing

house = Blueprint('house', __name__)


@house.route("/")
def index():
    return redirect(url_for("house.listing", page=1))


@house.route("/<int:page>")
def listing(page=None):
    paginate = HouseListing.query.filter_by(create_date='2021-10-22').paginate(page=page, per_page=10, error_out=False)
    houses = paginate.items
    areas = HouseListing.query.with_entities(HouseListing.area_name, HouseListing.area_id).group_by(HouseListing.area_name, HouseListing.area_id).all()
    return render_template("index.html", houses=houses, paginate=paginate, areas=areas)


@house.route('/detail/<int:house_id>')
def _detail(house_id):
    return redirect(url_for("house.detail", house_id=house_id, page=1))


@house.route("/detail/<int:house_id>/<int:page>")
def detail(house_id, page=1):
    paginate = HouseListing.query.filter_by(house_id=house_id).paginate(page=page, per_page=10, error_out=False)
    houses = paginate.items
    if not houses:
        return abort(404)
    title = houses[0].house_name
    return render_template("detail.html", paginate=paginate, houses=houses, title=title, house_id=house_id)


@house.route("/filter")
def filters():
    pass


