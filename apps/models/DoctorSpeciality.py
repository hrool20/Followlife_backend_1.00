from apps.db import db
from apps.models.BaseClasses import BaseMethods


class DoctorSpecialityModel(db.Model, BaseMethods):
    __tablename__ = 'doctor_specialities'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    doctorId = db.Column(db.Integer, db.ForeignKey('doctors.id', onupdate='CASCADE',
                                                   ondelete='CASCADE'), nullable=False)
    doctor = db.relationship('DoctorModel')
    medicalSpecialityId = db.Column(db.Integer, db.ForeignKey('medical_specialities.id', onupdate='CASCADE',
                                                              ondelete='CASCADE'), nullable=False)
    medicalSpeciality = db.relationship('MedicalSpecialityModel')

    def __init__(self, doctor_id, medical_speciality_id):
        super(DoctorSpecialityModel, self).__init__()
        self.doctorId = doctor_id
        self.medicalSpecialityId = medical_speciality_id

    def __repr__(self):
        return 'Doctor Speciality: %r' % self.doctorId

    def json(self, only_spec=bool):
        if only_spec:
            return {
                'id': self.id,
                'medicalSpeciality': self.medicalSpeciality.json()
            }
        else:
            return {
                'id': self.id,
                'doctor': self.doctor.json(),
                'medicalSpeciality': self.medicalSpeciality.json()
            }

    @classmethod
    def verify_doctor_speciality(cls, doctor_id, med_speciality):
        return cls.query.filter_by(doctorId=doctor_id).filter_by(medicalSpecialityId=med_speciality).first()
