from apps.db import db
from apps.models.BaseClasses import BaseMethods


class RoleModel(db.Model, BaseMethods):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)

    # Relationships
    users = db.relationship('UserModel', lazy='dynamic')

    name = db.Column(db.String(60), nullable=False)
    shortName = db.Column(db.String(3), nullable=False)

    def __init__(self, name, short_name):
        super(RoleModel, self).__init__()
        self.name = name
        self.shortName = short_name

    def __repr__(self):
        return 'Role: %r' % self.name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'shortName': self.shortName
        }
