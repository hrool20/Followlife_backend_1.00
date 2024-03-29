from datetime import datetime

from apps.db import db
from apps.models.BaseClasses import BaseMethods


class DeviceModel(db.Model, BaseMethods):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    userId = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    user = db.relationship('UserModel')

    ip = db.Column(db.String(15), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, ip, created_at):
        super(DeviceModel, self).__init__()
        self.userId = user_id
        self.ip = ip
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if (created_at is None) else created_at

    def __repr__(self):
        return 'Device: %r' % self.token

    def json(self):
        return {
            'id': self.id,
            'user': self.user.json(is_long=False),
            'ip': self.ip
        }

    @classmethod
    def find_by_ip(cls, ip):
        return cls.query.filter_by(ip=ip).first()
