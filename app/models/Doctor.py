from datetime import datetime

from app.db import db
from app.models.BaseClasses import BaseMethods


class DoctorModel(db.Model, BaseMethods):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    userId = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    user = db.relationship('UserModel')
    planId = db.Column(db.Integer, db.ForeignKey('plans.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    plan = db.relationship('PlanModel')
    addressId = db.Column(db.Integer, db.ForeignKey('addresses.id', onupdate='CASCADE',
                                                    ondelete='CASCADE'))
    address = db.relationship('AddressModel')
    doctorSpecialities = db.relationship('DoctorSpecialityModel', lazy='dynamic')
    appointments = db.relationship('AppointmentModel', lazy='dynamic')
    memberships = db.relationship('MembershipModel', lazy='dynamic')
    prescriptions = db.relationship('PrescriptionModel', lazy='dynamic')

    doctorIdentification = db.Column(db.String(20), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedOn = db.Column(db.DateTime)
    status = db.Column(db.String(3), server_default='ACT')

    def __init__(self, user_id, plan_id, address_id, doctor_identification, created_at, updated_on, status):
        super(DoctorModel, self).__init__()
        self.userId = user_id
        self.planId = plan_id
        self.addressId = address_id
        self.doctorIdentification = doctor_identification
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (created_at is None) else created_at
        self.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (updated_on is None) else updated_on
        self.status = status

    def __repr__(self):
        return 'Doctor: %r' % self.doctorIdentification

    def json(self):
        return {
            'id': self.id,
            'user': self.user.json(is_long=True),
            'plan': self.plan.json(),
            'address': self.address.json(doctors_list=False) if (self.addressId is not None) else None,
            'doctorIdentification': self.doctorIdentification,
            'status': self.status
        }

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(userId=user_id).first()
