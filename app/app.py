from datetime import timedelta

from flask.app import Flask
from flask_jwt_extended.jwt_manager import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from models.BaseClasses import BaseResponse
from resources.Address import Address
from resources.Appointment import AppointmentDoctor, AppointmentPatient
from resources.Device import Device
from resources.District import District
from resources.Doctor import Doctor
from resources.DoctorSpeciality import DoctorSpeciality
from resources.Indicator import Indicator
from resources.IndicatorEntry import IndicatorEntry
from resources.IndicatorType import IndicatorType
from resources.MedicalSpeciality import MedicalSpeciality
from resources.Membership import MembershipDoctor, MembershipPatient
from resources.Patient import Patient
from resources.Plan import Plan
from resources.Prescription import PrescriptionDoctor, PrescriptionPatient
from resources.PrescriptionType import PrescriptionType
from resources.Role import Role
from resources.UnitsOfMeasure import UnitOfMeasure
from resources.User import User
from resources.Login import Login
from config.DevelopmentEnvironment import DevelopmentEnvironment
from config.LocalEnvironment import LocalEnvironment

APP_CONFIG_FILE = 'config/DevelopmentEnvironment.py'

app_config = {
    'local': LocalEnvironment,
    'development': DevelopmentEnvironment
}


def configure_environment(flask_app, my_env, my_path):
    # MySQL configurations
    flask_app.config.from_object(my_env)
    flask_app.config.from_pyfile('Config.py', silent=False)
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + my_env.DATABASE_USER + ':' + \
                                                  my_env.DATABASE_PASSWORD + '@' + my_env.DATABASE_HOST + '/' + \
                                                  my_env.DATABASE_DB

app = Flask(__name__, instance_relative_config=True)
configure_environment(app, app_config['development'], APP_CONFIG_FILE)
# JWT
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_SECRET_KEY'] = 'followlife'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
# noinspection PyTypeChecker
api = Api(app)
jwt = JWTManager(app)


@jwt.expired_token_loader
def expired_token_callback():
    return BaseResponse.unauthorized_response('Expired token.')


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return BaseResponse.unauthorized_response('Invalid token: ' + error)


@jwt.unauthorized_loader
def unauthorized_callback(error):
    return BaseResponse.unauthorized_response(error)


# noinspection PyTypeChecker
api.add_resource(Address, '/api/v1/addresses',
                 '/api/v1/addresses/',
                 '/api/v1/addresses/<string:_id>',
                 '/api/v1/addresses/<string:_id>/doctors')
api.add_resource(AppointmentDoctor, '/api/v1/doctors/<string:_id>/appointments',
                 '/api/v1/doctors/<string:_id>/appointments/',
                 '/api/v1/doctors/<string:_id>/appointments/<string:appointment_id>')
api.add_resource(AppointmentPatient, '/api/v1/patients/<string:_id>/appointments',
                 '/api/v1/patients/<string:_id>/appointments/',
                 '/api/v1/patients/<string:_id>/appointments/<string:appointment_id>')
api.add_resource(Device, '/api/v1/devices',
                 '/api/v1/devices/',
                 '/api/v1/devices/<string:_id>')
api.add_resource(District, '/api/v1/districts',
                 '/api/v1/districts/',
                 '/api/v1/districts/<string:_id>')
api.add_resource(Doctor, '/api/v1/doctors',
                 '/api/v1/doctors/',
                 '/api/v1/doctors/<string:_id>')
api.add_resource(DoctorSpeciality, '/api/v1/doctors/<string:_id>/doctor_specialities',
                 '/api/v1/doctors/<string:_id>/doctor_specialities/',
                 '/api/v1/doctors/<string:_id>/doctor_specialities/<string:doc_spec_id>')
# api.add_resource(Indicator, '/api/v1/users', '/api/v1/users/<string:_id>')
# api.add_resource(IndicatorEntry, '/api/v1/users', '/api/v1/users/<string:_id>')
# api.add_resource(IndicatorType, '/api/v1/users', '/api/v1/users/<string:_id>')
api.add_resource(MedicalSpeciality, '/api/v1/medical_specialities',
                 '/api/v1/medical_specialities/',
                 '/api/v1/medical_specialities/<string:_id>')
api.add_resource(MembershipDoctor, '/api/v1/doctors/<string:doctor_id>/membership',
                 '/api/v1/doctors/<string:doctor_id>/membership/',
                 '/api/v1/doctors/<string:doctor_id>/patients',
                 '/api/v1/doctors/<string:doctor_id>/patients/',
                 '/api/v1/doctors/<string:doctor_id>/patients/<string:_id>')
api.add_resource(MembershipPatient, '/api/v1/patients/<string:patient_id>/membership',
                 '/api/v1/patients/<string:patient_id>/membership/',
                 '/api/v1/patients/<string:patient_id>/doctors',
                 '/api/v1/patients/<string:patient_id>/doctors/',
                 '/api/v1/patients/<string:patient_id>/doctors/<string:_id>')
api.add_resource(Patient, '/api/v1/patients',
                 '/api/v1/patients/',
                 '/api/v1/patients/<string:_id>')
api.add_resource(Plan, '/api/v1/plans',
                 '/api/v1/plans/',
                 '/api/v1/plans/<string:_id>')
api.add_resource(PrescriptionDoctor, '/api/v1/doctors/<string:doctor_id>/patients/<string:patient_id>/prescriptions',
                 '/api/v1/doctors/<string:doctor_id>/patients/<string:patient_id>/prescriptions/',
                 '/api/v1/doctors/<string:doctor_id>/patients/<string:patient_id>/prescriptions/<string:_id>')
api.add_resource(PrescriptionPatient, '/api/v1/patients/<string:patient_id>/doctors/<string:doctor_id>/prescriptions',
                 '/api/v1/patients/<string:patient_id>/doctors/<string:doctor_id>/prescriptions/',
                 '/api/v1/patients/<string:patient_id>/doctors/<string:doctor_id>/prescriptions/<string:_id>')
api.add_resource(PrescriptionType, '/api/v1/prescriptions_type',
                 '/api/v1/prescriptions_type/',
                 '/api/v1/prescriptions_type/<string:_id>')
api.add_resource(Role, '/api/v1/roles',
                 '/api/v1/roles',
                 '/api/v1/roles/<string:_id>')
api.add_resource(UnitOfMeasure, '/api/v1/units_of_measure',
                 '/api/v1/units_of_measure/',
                 '/api/v1/units_of_measure/<string:_id>')
api.add_resource(User, '/api/v1/users',
                 '/api/v1/users/',
                 '/api/v1/users/<string:_id>')
api.add_resource(Login, '/api/v1/login',
                 '/api/v1/login/',
                 '/api/v1/auth')

if __name__ == '__main__':
    from app.db import db
    db.init_app(app)
    migrate = Migrate(app, db)
    app.run(debug=app_config['development'].DEBUG)
