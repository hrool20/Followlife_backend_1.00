from apps.db import db
from apps.models.BaseClasses import BaseMethods


class UnitOfMeasureModel(db.Model, BaseMethods):
    __tablename__ = 'units_of_measure'

    id = db.Column(db.Integer, primary_key=True)

    # Relationship
    indicators_type = db.relationship('IndicatorTypeModel', lazy='dynamic')

    name = db.Column(db.String(60), nullable=False)
    shortName = db.Column(db.String(3), nullable=False)

    def __init__(self, name, short_name):
        super(UnitOfMeasureModel, self).__init__()
        self.name = name
        self.shortName = short_name

    def __repr__(self):
        return 'Unit of Measure: %r' % self.name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'shortName': self.shortName
        }
