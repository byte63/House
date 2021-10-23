from flask import Flask
from App.settings import envs

# extension
from App.ext import init_ext

# Model
from App.models import HouseListing

from App.views import house


def init_view(app):
    app.register_blueprint(house,)


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_view(app)
    return app
