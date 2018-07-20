from apps.db import db
from apps.models.BaseClasses import BaseMethods


class PrescriptionTypeModel(db.Model, BaseMethods):
    __tablename__ = 'prescriptions_type'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    prescriptions = db.relationship('PrescriptionModel', lazy='dynamic')

    name = db.Column(db.String(60), nullable=False)
    shortName = db.Column(db.String(3), nullable=False)

    def __init__(self, name, short_name):
        super(PrescriptionTypeModel, self).__init__()
        self.name = name
        self.shortName = short_name

    def __repr__(self):
        return 'Prescription Type: %r' % self.name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'shortName': self.shortName
        }
