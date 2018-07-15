from datetime import datetime

from app.db import db
from app.models.BaseClasses import BaseMethods


class AddressModel(db.Model, BaseMethods):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    districtId = db.Column(db.Integer, db.ForeignKey('districts.id'), nullable=False)
    district = db.relationship('DistrictModel')
    doctors = db.relationship('DoctorModel', lazy='dynamic')

    street = db.Column(db.String(100))
    neighborhood = db.Column(db.String(100))
    complement = db.Column(db.String(100))
    number = db.Column(db.String(5))
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedOn = db.Column(db.DateTime)
    status = db.Column(db.String(3), server_default='ACT')

    def __init__(self, district_id, street, neighborhood, complement, number, created_at, updated_on, status):
        super(AddressModel, self).__init__()
        self.districtId = district_id
        self.street = street
        self.neighborhood = neighborhood
        self.complement = complement
        self.number = number
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (created_at is None) else created_at
        self.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (updated_on is None) else updated_on
        self.status = status

    def __repr__(self):
        return 'Address: %r' % self.street

    def json(self, doctors_list=bool):
        if doctors_list:
            return {
                'doctors': list(map(lambda x: x.json(), self.doctors)),
                'district': self.district.json(),
                'street': self.street,
                'neighborhood': self.neighborhood,
                'complement': self.complement,
                'number': self.number
            }
        else:
            return {
                'district': self.district.json(),
                'street': self.street,
                'neighborhood': self.neighborhood,
                'complement': self.complement,
                'number': self.number
            }

    @classmethod
    def find_by_number(cls, number):
        return cls.query.filter_by(number=number).first()
