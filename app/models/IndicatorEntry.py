from datetime import datetime

from app.db import db
from app.models.BaseClasses import BaseMethods


class IndicatorEntryModel(db.Model, BaseMethods):
    __tablename__ = 'indicators_entry'

    id = db.Column(db.Integer, primary_key=True)

    # Relationship
    indicatorId = db.Column(db.Integer, db.ForeignKey('indicators.id', onupdate='CASCADE',
                                                      ondelete='CASCADE'), nullable=False)
    indicator = db.relationship('IndicatorModel')

    value = db.Column(db.String(20))
    createdAt = db.Column(db.DateTime, nullable=False)

    def __init__(self, indicator_id, value, created_at):
        super(IndicatorEntryModel, self).__init__()
        self.indicatorId = indicator_id
        self.value = value
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (created_at is None) else created_at

    def __repr__(self):
        return 'Indicator Entry: %r' % self.value

    def json(self):
        return {
            'id': self.id,
            'indicator': self.indicator.json(),
            'value': self.value
        }
