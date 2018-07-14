from datetime import datetime

from app.db import db
from app.models.BaseClasses import BaseMethods


class IndicatorModel(db.Model, BaseMethods):
    __tablename__ = 'indicators'

    id = db.Column(db.Integer, primary_key=True)

    # Relationship
    patientId = db.Column(db.Integer, db.ForeignKey('patients.id', onupdate='CASCADE',
                                                    ondelete='CASCADE'), nullable=False)
    patient = db.relationship('PatientModel')
    indicatorTypeId = db.Column(db.Integer, db.ForeignKey('indicators_type.id', onupdate='CASCADE',
                                                          ondelete='CASCADE'), nullable=False)
    indicatorType = db.relationship('IndicatorTypeModel')
    indicatorsEntry = db.relationship('IndicatorEntryModel', lazy='dynamic')

    quantity = db.Column(db.Numeric(9, 3))
    frequency = db.Column(db.String(200))
    createdAt = db.Column(db.DateTime, nullable=False)

    def __init__(self, patient_id, indicator_typ_id, quantity, frequency, created_at):
        super(IndicatorModel, self).__init__()
        self.patientId = patient_id
        self.indicatorTypeId = indicator_typ_id
        self.quantity = quantity
        self.frequency = frequency
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (created_at is None) else created_at

    def __repr__(self):
        return 'Indicator %r' % self.frequency

    def json(self):
        return {
            'id': self.id,
            'patient': self.patient.json(),
            'indicatorType': self.indicatorType.json(),
            'quantity': self.quantity,
            'frequency': self.frequency
        }
