from apps.db import db
from apps.models.BaseClasses import BaseMethods


class IndicatorTypeModel(db.Model, BaseMethods):
    __tablename__ = 'indicators_type'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    unitOfMeasureId = db.Column(db.Integer, db.ForeignKey('units_of_measure.id', onupdate='CASCADE',
                                                          ondelete='CASCADE'), nullable=False)
    unitOfMeasure = db.relationship('UnitOfMeasureModel')
    indicators = db.relationship('IndicatorModel', lazy='dynamic')

    name = db.Column(db.String(100))
    shortName = db.Column(db.String(3))

    def __init__(self, unit_of_measure_id, name, short_name):
        super(IndicatorTypeModel, self).__init__()
        self.unitOfMeasureId = unit_of_measure_id
        self.name = name
        self.shortName = short_name

    def __repr__(self):
        return 'Role: %r' % self.name

    def json(self):
        return {
            'id': self.id,
            'unitOfMeasure': self.unitOfMeasure.json(),
            'name': self.name,
            'shortName': self.shortName
        }
