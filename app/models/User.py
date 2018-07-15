from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db
from app.models.BaseClasses import BaseMethods


class UserModel(db.Model, BaseMethods):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    roleId = db.Column(db.Integer, db.ForeignKey('roles.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    role = db.relationship('RoleModel')
    patient = db.relationship('PatientModel', lazy='dynamic')
    doctor = db.relationship('DoctorModel', lazy='dynamic')
    devices = db.relationship('DeviceModel', lazy='dynamic')

    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    fullName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(13))
    profilePicture = db.Column(db.String(250))
    lastIPConnection = db.Column(db.String(100))
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedOn = db.Column(db.DateTime)
    status = db.Column(db.String(3), server_default='ACT')

    def __init__(self, role_id, email, password, full_name, last_name, phone_number, profile_picture,
                 last_ip_connection, created_at, updated_on, status):
        super(UserModel, self).__init__()
        self.roleId = role_id
        self.email = email
        self.password = password
        self.fullName = full_name
        self.lastName = last_name
        self.phoneNumber = phone_number
        self.profilePicture = profile_picture
        self.lastIPConnection = last_ip_connection
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (created_at is None) else created_at
        self.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (updated_on is None) else updated_on
        self.status = status

    def __repr__(self):
        return 'User: %r' % self.fullName

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password, method='pbkdf2:sha256:50')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def json(self, is_long):
        if is_long:
            return {
                'id': self.id,
                'role': self.role.json(),
                'fullName': self.fullName,
                'lastName': self.lastName,
                'phoneNumber': self.phoneNumber,
                'profilePicture': self.profilePicture
            }
        else:
            return {
                'id': self.id,
                'fullName': self.fullName,
                'lastName': self.lastName
            }

    @classmethod
    def find_by_full_name(cls, full_name):
        return cls.query.filter_by(fullName=full_name).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_phone(cls, phone):
        return cls.query.filter_by(phoneNumber=phone).first()
