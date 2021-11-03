from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
migrate = Migrate()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["5 per minute"]
)


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)
