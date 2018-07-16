from datetime import datetime

from app.db import db
from app.models.BaseClasses import BaseMethods


class PatientModel(db.Model, BaseMethods):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    userId = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    user = db.relationship('UserModel')
    planId = db.Column(db.Integer, db.ForeignKey('plans.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    plan = db.relationship('PlanModel')
    appointments = db.relationship('AppointmentModel', lazy='dynamic')
    memberships = db.relationship('MembershipModel', lazy='dynamic')
    prescriptions = db.relationship('PrescriptionModel', lazy='dynamic')
    indicators = db.relationship('IndicatorModel', lazy='dynamic')

    age = db.Column(db.Integer, nullable=False)
    bloodType = db.Column(db.String(3))
    weight = db.Column(db.Numeric(9, 3))
    sex = db.Column(db.String(10))
    height = db.Column(db.Numeric(9, 3))
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedOn = db.Column(db.DateTime)
    status = db.Column(db.String(3), server_default='ACT')

    def __init__(self, user_id, plan_id, age, blood_type, weight, sex, height, created_at, updated_on, status):
        super(PatientModel, self).__init__()
        self.userId = user_id
        self.planId = plan_id
        self.age = age
        self.bloodType = blood_type
        self.weight = weight
        self.sex = sex
        self.height = height
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (created_at is None) else created_at
        self.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (updated_on is None) else updated_on
        self.status = status

    def __repr__(self):
        return 'Patient: %r' % self.age

    def json(self):
        return {
            'id': self.id,
            'user': self.user.json(is_long=True),
            'plan': self.plan.json(),
            'age': self.age,
            'bloodType': self.bloodType,
            'weight': float(self.weight),
            'sex': self.sex,
            'height': float(self.height),
            'status': self.status
        }

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(userId=user_id).first()
