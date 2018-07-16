from datetime import datetime

from app.db import db
from app.models.BaseClasses import BaseMethods


class PrescriptionModel(db.Model, BaseMethods):
    __tablename__ = 'prescriptions'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    doctorId = db.Column(db.Integer, db.ForeignKey('doctors.id', onupdate='CASCADE',
                                                   ondelete='CASCADE'), nullable=False)
    doctor = db.relationship('DoctorModel')
    patientId = db.Column(db.Integer, db.ForeignKey('patients.id', onupdate='CASCADE',
                                                    ondelete='CASCADE'), nullable=False)
    patient = db.relationship('PatientModel')
    prescriptionTypeId = db.Column(db.Integer, db.ForeignKey('prescriptions_type.id', onupdate='CASCADE',
                                                             ondelete='CASCADE'), nullable=False)
    prescriptionType = db.relationship('PrescriptionTypeModel')

    frequency = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    durationInDays = db.Column(db.Integer)
    description = db.Column(db.String(250))
    createdAt = db.Column(db.DateTime, nullable=False)
    startedAt = db.Column(db.DateTime)
    finishedAt = db.Column(db.DateTime)
    status = db.Column(db.String(3), server_default='ACT')

    def __init__(self, doctor_id, patient_id, prescription_type_id, frequency, quantity, duration_in_days, description,
                 created_at, started_at, finished_at, status):
        super(PrescriptionModel, self).__init__()
        self.doctorId = doctor_id
        self.patientId = patient_id
        self.prescriptionTypeId = prescription_type_id
        self.frequency = frequency
        self.quantity = quantity
        self.durationInDays = duration_in_days
        self.description = description
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (created_at is None) else created_at
        self.startedAt = started_at
        self.finishedAt = finished_at
        self.status = status

    def __repr__(self):
        return 'Prescription: %r' % self.description

    def json(self, role_id):
        if role_id == 1:
            return {
                'id': self.id,
                'patient': self.patient.json(),
                'prescriptionType': self.prescriptionType.json(),
                'frequency': self.frequency,
                'quantity': self.quantity,
                'durationInDays': self.durationInDays,
                'description': self.description,
                'startedAt': self.startedAt,
                'finishedAt': self.finishedAt,
                'status': self.status
            }
        else:
            return {
                'id': self.id,
                'doctor': self.doctor.json(),
                'prescriptionType': self.prescriptionType.json(),
                'frequency': self.frequency,
                'quantity': self.quantity,
                'durationInDays': self.durationInDays,
                'description': self.description,
                'startedAt': self.startedAt,
                'finishedAt': self.finishedAt,
                'status': self.status
            }
