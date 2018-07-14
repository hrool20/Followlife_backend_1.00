from app.db import db
from app.models.BaseClasses import BaseMethods


class MedicalSpecialityModel(db.Model, BaseMethods):
    __tablename__ = 'medical_specialities'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    doctorSpecialities = db.relationship('DoctorSpecialityModel', lazy='dynamic')

    name = db.Column(db.String(70))
    shortName = db.Column(db.String(3))

    def __init__(self, name, short_name):
        super(MedicalSpecialityModel, self).__init__()
        self.name = name
        self.shortName = short_name

    def __repr__(self):
        return 'Medical Speciality: %r' % self.name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'shortName': self.shortName
        }
