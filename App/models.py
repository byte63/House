from App.ext import db


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
