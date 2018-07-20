from apps.db import db
from apps.models.BaseClasses import BaseMethods


class PlanModel(db.Model, BaseMethods):
    __tablename__ = 'plans'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    patients = db.relationship('PatientModel', lazy='dynamic')
    doctors = db.relationship('DoctorModel', lazy='dynamic')

    name = db.Column(db.String(50))
    shortName = db.Column(db.String(3))
    description = db.Column(db.String(150))
    acceptedPatients = db.Column(db.Integer)
    price = db.Column(db.Numeric(9, 3))

    def __init__(self, name, short_name, description, accepted_patients, price):
        super(PlanModel, self).__init__()
        self.name = name
        self.shortName = short_name
        self.description = description
        self.acceptedPatients = accepted_patients
        self.price = price

    def __repr__(self):
        return 'Plan: %r' % self.name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'shortName': self.shortName,
            'description': self.description,
            'acceptedPatients': self.acceptedPatients,
            'price': float(self.price)
        }
