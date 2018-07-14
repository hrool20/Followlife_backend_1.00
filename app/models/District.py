from app.db import db
from app.models.BaseClasses import BaseMethods


class DistrictModel(db.Model, BaseMethods):
    __tablename__ = 'districts'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    addresses = db.relationship('AddressModel', lazy='dynamic')

    name = db.Column(db.String(100), nullable=False)
    shortName = db.Column(db.String(3), nullable=False)

    def __init__(self, name, short_name):
        super(DistrictModel, self).__init__()
        self.name = name
        self.shortName = short_name

    def __repr__(self):
        return 'District: %r' % self.name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'shortName': self.shortName
        }
