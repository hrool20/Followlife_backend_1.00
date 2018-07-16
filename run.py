# coding=utf-8
from flask_migrate import Migrate
from flask_restful import Api

from app import *
from app.db import db
from app.resources.Address import Address
from app.resources.Appointment import AppointmentDoctor, AppointmentPatient
from app.resources.Device import Device
from app.resources.District import District, DistrictModel
from app.resources.Doctor import Doctor
from app.resources.DoctorSpeciality import DoctorSpeciality
from app.resources.Indicator import Indicator
from app.resources.IndicatorEntry import IndicatorEntry
from app.resources.IndicatorType import IndicatorType
from app.resources.MedicalSpeciality import MedicalSpeciality, MedicalSpecialityModel
from app.resources.Membership import MembershipDoctor, MembershipPatient
from app.resources.Patient import Patient
from app.resources.Plan import Plan, PlanModel
from app.resources.Prescription import Prescription
from app.resources.PrescriptionType import PrescriptionType, PrescriptionTypeModel
from app.resources.Role import Role, RoleModel
from app.resources.UnitsOfMeasure import UnitOfMeasure, UnitOfMeasureModel
from app.resources.User import User
from app.resources.Login import Login
from config.DevelopmentEnvironment import DevelopmentEnvironment
from config.LocalEnvironment import LocalEnvironment

APP_CONFIG_FILE = '../config/LocalEnvironment.py'

app_config = {
    'local': LocalEnvironment,
    'development': DevelopmentEnvironment
}

app = create_app(app_config['local'], APP_CONFIG_FILE)
api = Api(app)
migrate = Migrate(app, db)


def load_tables():
    # District
    district1 = DistrictModel('Callao', 'CAL')
    district2 = DistrictModel('Bellavista', 'BEL')
    district3 = DistrictModel('Carmen De La Legua Reynoso', 'CLR')
    district4 = DistrictModel('La Perla', 'LPE')
    district5 = DistrictModel('La Punta', 'LPU')
    district6 = DistrictModel('Ventanilla', 'VEN')
    district7 = DistrictModel('Cusco', 'CUS')
    district8 = DistrictModel('Ccorca', 'CCO')
    district9 = DistrictModel('Poroy', 'POR')
    district10 = DistrictModel('San Jeronimo', 'SJE')
    district11 = DistrictModel('San Sebastian', 'SSE')
    district12 = DistrictModel('Santiago', 'SAN')
    district13 = DistrictModel('Saylla', 'SAY')
    district14 = DistrictModel('Wanchaq', 'WAN')
    district15 = DistrictModel('Lima', 'LIM')
    district16 = DistrictModel('Ancon', 'ANC')
    district17 = DistrictModel('Ate', 'ATE')
    district18 = DistrictModel('Barranco', 'BAR')
    district19 = DistrictModel('Breña', 'BRE')
    district20 = DistrictModel('Carabayllo', 'CAR')
    district21 = DistrictModel('Chaclacayo', 'CHC')
    district22 = DistrictModel('Chorrillos', 'CHO')
    district23 = DistrictModel('Cieneguilla', 'CIE')
    district24 = DistrictModel('Comas', 'COM')
    district25 = DistrictModel('El Agustino', 'EAG')
    district26 = DistrictModel('Independencia', 'IND')
    district27 = DistrictModel('Jesus Maria', 'JEM')
    district28 = DistrictModel('La Molina', 'LMO')
    district29 = DistrictModel('La Victoria', 'LVI')
    district30 = DistrictModel('Lince', 'LIN')
    district31 = DistrictModel('Los Olivos', 'LOL')
    district32 = DistrictModel('Lurigancho', 'LRG')
    district33 = DistrictModel('Lurin', 'LUR')
    district34 = DistrictModel('Magdalena Del Mar', 'MGM')
    district35 = DistrictModel('Magdalena Vieja', 'MGV')
    district36 = DistrictModel('Miraflores', 'MIR')
    district37 = DistrictModel('Pachacamac', 'PAC')
    district38 = DistrictModel('Pucusana', 'PUC')
    district39 = DistrictModel('Puente Piedra', 'PUP')
    district40 = DistrictModel('Punta Hermosa', 'PUH')
    district41 = DistrictModel('Punta Negra', 'PUN')
    district42 = DistrictModel('Rimac', 'RIM')
    district43 = DistrictModel('San Bartolo', 'SBA')
    district44 = DistrictModel('San Borja', 'SBO')
    district45 = DistrictModel('San Isidro', 'SIS')
    district46 = DistrictModel('San Juan De Lurigancho', 'SJL')
    district47 = DistrictModel('San Juan De Miraflores', 'SJM')
    district48 = DistrictModel('San Luis', 'SAL')
    district49 = DistrictModel('San Martin De Porres', 'SMP')
    district50 = DistrictModel('San Miguel', 'SMI')
    district51 = DistrictModel('Santa Anita', 'SNT')
    district52 = DistrictModel('Santa Maria Del Mar', 'SMM')
    district53 = DistrictModel('Santa Rosa', 'SAR')
    district54 = DistrictModel('Santiago De Surco', 'SAS')
    district55 = DistrictModel('Surquillo', 'SUR')
    district56 = DistrictModel('Villa El Salvador', 'VES')
    district57 = DistrictModel('Villa Maria Del Triunfo', 'VMT')

    districts = [district1, district2, district3, district4, district5, district6, district7, district8, district9,
                 district10, district11, district12, district13, district14, district15, district16, district17,
                 district18, district19, district20, district21, district22, district23, district24, district25,
                 district26, district27, district28, district29, district30, district31, district32, district33,
                 district34, district35, district36, district37, district38, district39, district40, district41,
                 district42, district43, district44, district45, district46, district47, district48, district49,
                 district50, district51, district52, district53, district54, district55, district56, district57]

    for obj_district in districts:
        obj_district.save_to_db()
        pass

    # Plan
    plan1 = PlanModel('General Patient', 'GEP', 'You can be monitored by your doctor through the application', None, 0)
    plan2 = PlanModel('Premium Patient', 'PRP', 'You can sync your wearable with the application', None, 9.99)
    plan3 = PlanModel('General Doctor', 'GED', 'You can take care of 10 patients', 10, 39.99)
    plan4 = PlanModel('Premium Doctor', 'PRD', 'You can take care of 20 patients and grant access to dashboard.', 20,
                      59.99)
    plan5 = PlanModel('Extra Plan', 'EXT', 'You can add 10 more patients to your plan', 10, 9.99)

    plans = [plan1, plan2, plan3, plan4, plan5]

    for obj_plan in plans:
        obj_plan.save_to_db()
        pass

    # Role
    role1 = RoleModel('Doctor', 'DOC')
    role2 = RoleModel('Patient', 'PAT')

    roles = [role1, role2]

    for obj_role in roles:
        obj_role.save_to_db()
        pass

    # Medical Speciality
    med_spec1 = MedicalSpecialityModel('Anatomia Patologica', 'APA')
    med_spec2 = MedicalSpecialityModel('Alergologia', 'ALE')
    med_spec3 = MedicalSpecialityModel('Cardiologia', 'CAR')
    med_spec4 = MedicalSpecialityModel('Cirugia Cardiaca', 'CCA')
    med_spec5 = MedicalSpecialityModel('Cirugia General', 'CGE')
    med_spec6 = MedicalSpecialityModel('Cirugia Plastica', 'CPL')
    med_spec7 = MedicalSpecialityModel('Dermatologia', 'DER')
    med_spec8 = MedicalSpecialityModel('Endocrinologia', 'END')
    med_spec9 = MedicalSpecialityModel('Nutricion', 'NUT')
    med_spec10 = MedicalSpecialityModel('Gastroenterologia', 'GAS')
    med_spec11 = MedicalSpecialityModel('Geriatra', 'GER')
    med_spec12 = MedicalSpecialityModel('Ginecologia', 'GIN')
    med_spec13 = MedicalSpecialityModel('Hematologia', 'HEM')
    med_spec14 = MedicalSpecialityModel('Hepatologia', 'HEP')
    med_spec15 = MedicalSpecialityModel('Enfermedas Infecciosas', 'EIN')
    med_spec16 = MedicalSpecialityModel('Medicina Interna', 'MIN')
    med_spec17 = MedicalSpecialityModel('Nefrología', 'NEF')
    med_spec18 = MedicalSpecialityModel('Neumologia', 'NEU')
    med_spec19 = MedicalSpecialityModel('Neurologia', 'NER')
    med_spec20 = MedicalSpecialityModel('Neurocirugia', 'NCI')
    med_spec21 = MedicalSpecialityModel('Oftalmologia', 'OFT')
    med_spec22 = MedicalSpecialityModel('Otorrinolaringologia', 'OTO')
    med_spec23 = MedicalSpecialityModel('Oncologia', 'ONC')
    med_spec24 = MedicalSpecialityModel('Pediatra', 'PED')
    med_spec25 = MedicalSpecialityModel('Proctologia', 'PRC')
    med_spec26 = MedicalSpecialityModel('Psiquiatra', 'PSI')
    med_spec27 = MedicalSpecialityModel('Rehabilitacion', 'REH')
    med_spec28 = MedicalSpecialityModel('Reumatologia', 'REU')
    med_spec29 = MedicalSpecialityModel('Traumatologia', 'TRA')
    med_spec30 = MedicalSpecialityModel('Urologia', 'URO')

    med_specialities = [med_spec1, med_spec2, med_spec3, med_spec4, med_spec5, med_spec6, med_spec7, med_spec8,
                        med_spec9, med_spec10, med_spec11, med_spec12, med_spec13, med_spec14, med_spec15, med_spec16,
                        med_spec17, med_spec18, med_spec19, med_spec20, med_spec21, med_spec22, med_spec23, med_spec24,
                        med_spec25, med_spec26, med_spec27, med_spec28, med_spec29, med_spec30]

    for obj_med_spec in med_specialities:
        obj_med_spec.save_to_db()
        pass

    # Prescription Type
    prescription_type1 = PrescriptionTypeModel('Medication', 'MED')
    prescription_type2 = PrescriptionTypeModel('Activity', 'ACV')
    prescription_type3 = PrescriptionTypeModel('Diet', 'DIE')
    prescription_type4 = PrescriptionTypeModel('Other', 'OTH')

    prescriptions_type = [prescription_type1, prescription_type2, prescription_type3, prescription_type4]

    for obj_prescription_type in prescriptions_type:
        obj_prescription_type.save_to_db()
        pass

    # Unit of Measure
    unit_of_m1 = UnitOfMeasureModel('Millimeter', 'mm')
    unit_of_m2 = UnitOfMeasureModel('Centimeter', 'cm')
    unit_of_m3 = UnitOfMeasureModel('Metre', 'm')
    unit_of_m4 = UnitOfMeasureModel('Kilometer', 'km')
    unit_of_m5 = UnitOfMeasureModel('Mile', 'mi')
    unit_of_m6 = UnitOfMeasureModel('Milligram', 'mg')
    unit_of_m7 = UnitOfMeasureModel('Gram', 'g')
    unit_of_m8 = UnitOfMeasureModel('Kilogram', 'kg')
    unit_of_m9 = UnitOfMeasureModel('Pound', 'lb')
    unit_of_m10 = UnitOfMeasureModel('Ounce', 'oz')
    unit_of_m11 = UnitOfMeasureModel('Ampere', 'A')
    unit_of_m12 = UnitOfMeasureModel('Celsius', '°C')
    unit_of_m13 = UnitOfMeasureModel('Kelvin', 'K')
    unit_of_m14 = UnitOfMeasureModel('Candela', 'cd')
    unit_of_m15 = UnitOfMeasureModel('Mole', 'mol')
    unit_of_m16 = UnitOfMeasureModel('Liter', 'l')

    units_of_m = [unit_of_m1, unit_of_m2, unit_of_m3, unit_of_m4, unit_of_m5, unit_of_m6, unit_of_m7, unit_of_m8,
                  unit_of_m9, unit_of_m10, unit_of_m11, unit_of_m12, unit_of_m13, unit_of_m14, unit_of_m15, unit_of_m16]

    for obj_unit_of_m in units_of_m:
        obj_unit_of_m.save_to_db()
        pass
    pass


# It help to create tables before first request
# @app.before_first_request
# def create_tables():
#     dd = db.get_tables_for_bind()
#     if db.get_tables_for_bind():
#         db.reflect(app=app)
#     else:
#     db.create_all(app=app)
#     load_tables()


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
# api.add_resource(Device, '/api/v1/users', '/api/v1/users/<string:_id>')
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
# api.add_resource(Prescription, '/api/v1/users', '/api/v1/users/<string:_id>')
api.add_resource(PrescriptionType, '/api/v1/prescriptions_type',
                 '/api/v1/prescriptions_type/',
                 '/api/v1/prescriptions_type/<string:_id>')
# api.add_resource(Role, '/api/v1/users', '/api/v1/users/<string:_id>')
# api.add_resource(UnitOfMeasure, '/api/v1/users', '/api/v1/users/<string:_id>')
api.add_resource(User, '/api/v1/users',
                 '/api/v1/users/',
                 '/api/v1/users/<string:_id>')
api.add_resource(Login, '/api/v1/login',
                 '/api/v1/login/',
                 '/api/v1/auth')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
