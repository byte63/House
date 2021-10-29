from App.ext import db
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    _password = db.Column(db.String(256))

    @property
    def password(self):
        raise Exception("Can't access")

    @password.setter
    def password(self, val):
        self._password = generate_password_hash(val)

    def check_password(self, val):
        return check_password_hash(self._password, password=val)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            return False


class HouseListing(db.Model):
    __tablename__ = 'house_listing'
    __table_args__ = (
        db.Index('EVERY_DAY', 'house_id', 'area_id', 'create_date'),
    )

    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer)
    house_name = db.Column(db.String(256))
    status = db.Column(db.String(32), info='状态： 在售， 未售')
    nature = db.Column(db.String(32), info='性质： 住宅')
    price = db.Column(db.String(256), info='价格')
    address = db.Column(db.String(256), info='所在地')
    hx = db.Column(db.String(256), info='户型')
    desc = db.Column(db.String(256), info='描述')
    detail_url = db.Column(db.String(256))
    area_id = db.Column(db.Integer)
    area_name = db.Column(db.String(64))
    city = db.Column(db.String(64))
    create_stamp = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.FetchedValue())
    create_date = db.Column(db.Date)

    __mapper_args__ = {
        "order_by": -create_date
    }
