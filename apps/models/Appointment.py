from datetime import datetime, timedelta

from apps.db import db
from apps.models.BaseClasses import BaseMethods


class AppointmentModel(db.Model, BaseMethods):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    doctorId = db.Column(db.Integer, db.ForeignKey('doctors.id', onupdate='CASCADE', ondelete='CASCADE')
                         , nullable=False)
    doctor = db.relationship('DoctorModel')
    patientId = db.Column(db.Integer, db.ForeignKey('patients.id', onupdate='CASCADE', ondelete='CASCADE')
                          , nullable=False)
    patient = db.relationship('PatientModel')

    appointmentDate = db.Column(db.DateTime, nullable=False)
    reason = db.Column(db.String(200))
    createdAt = db.Column(db.DateTime, nullable=False)
    canceledAt = db.Column(db.DateTime)
    updatedOn = db.Column(db.DateTime)
    status = db.Column(db.String(3), server_default='ACT')

    def __init__(self, doctor_id, patient_id, appointment_date, reason, created_at, canceled_at, updated_on, status):
        super(AppointmentModel, self).__init__()
        self.doctorId = doctor_id
        self.patientId = patient_id
        self.appointmentDate = (datetime.now() + timedelta(hours=2)) if (appointment_date is None) else appointment_date
        self.reason = reason
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (created_at is None) else created_at
        self.canceledAt = canceled_at
        self.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (updated_on is None) else updated_on
        self.status = status

    def __repr__(self):
        return 'Appointment: %r' % self.reason

    def json(self, role_id):
        if role_id == 1:
            return {
                'id': self.id,
                'patient': self.patient.json(),
                'appointmentDate': self.appointmentDate,
                'reason': self.reason,
                'canceledAt': self.canceledAt,
                'status': self.status
            }
        else:
            return {
                'id': self.id,
                'doctor': self.doctor.json(),
                'appointmentDate': self.appointmentDate,
                'reason': self.reason,
                'canceledAt': self.canceledAt,
                'status': self.status
            }

    @classmethod
    def find_by_patient_id(cls, patient_id):
        return cls.query.filter_by(patientId=patient_id).all()

    @classmethod
    def find_by_doctor_id(cls, doctor_id):
        return cls.query.filter_by(doctorId=doctor_id).all()

    @classmethod
    def find_by_appointment_date(cls, appointment_date):
        return cls.query.filter_by(appointmentDate=appointment_date).first()
