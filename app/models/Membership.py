from datetime import datetime, timedelta

from app.db import db
from app.models.BaseClasses import BaseMethods


class MembershipModel(db.Model, BaseMethods):
    __tablename__ = 'memberships'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    doctorId = db.Column(db.Integer, db.ForeignKey('doctors.id', onupdate='CASCADE',
                                                   ondelete='CASCADE'), nullable=False)
    doctor = db.relationship('DoctorModel')
    patientId = db.Column(db.Integer, db.ForeignKey('patients.id', onupdate='CASCADE',
                                                    ondelete='CASCADE'), nullable=False)
    patient = db.relationship('PatientModel')

    referencedEmail = db.Column(db.String(45), nullable=False)
    accessCode = db.Column(db.String(6))
    createdAt = db.Column(db.DateTime, nullable=False)
    expiresAt = db.Column(db.DateTime)
    updatedOn = db.Column(db.DateTime)
    status = db.Column(db.String(3), server_default='ACT')

    def __init__(self, doctor_id, patient_id, referenced_email, access_code, created_at, expires_at, updated_on, status):
        super(MembershipModel, self).__init__()
        self.doctorId = doctor_id
        self.patientId = patient_id
        self.referencedEmail = referenced_email
        self.accessCode = access_code
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (created_at is None) else created_at
        self.expiresAt = (datetime.now() + timedelta(hours=24)).strftime('%Y-%m-%d %H:%M:%S') if (expires_at is None) \
            else expires_at
        self.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (updated_on is None) else updated_on
        self.status = status

    def __repr__(self):
        return 'Membership: %r' % self.referencedEmail

    def json(self, role_id):
        if role_id == 1:
            return {
                'id': self.id,
                'patient': self.patient.json(),
                'referencedEmail': self.referencedEmail,
                'accessCode': self.accessCode,
                'expiredAt': self.expiresAt,
                'status': self.status
            }
        else:
            return {
                'id': self.id,
                'doctor': self.doctor.json(),
                'referencedEmail': self.referencedEmail,
                'accessCode': self.accessCode,
                'expiredAt': self.expiresAt,
                'status': self.status
            }

    @classmethod
    def find_by_patient_id(cls, patient_id):
        return cls.query.filter_by(patientId=patient_id).first()

    @classmethod
    def find_by_doctor_id(cls, doctor_id):
        return cls.query.filter_by(doctorId=doctor_id).first()
