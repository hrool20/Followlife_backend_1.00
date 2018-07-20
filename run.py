# coding=utf-8

from apps.app import app
from apps.db import db
from apps.models.District import DistrictModel
from apps.models.Doctor import DoctorModel
from apps.models.MedicalSpeciality import MedicalSpecialityModel
from apps.models.Patient import PatientModel
from apps.models.Plan import PlanModel
from apps.models.PrescriptionType import PrescriptionTypeModel
from apps.models.Role import RoleModel
from apps.models.UnitsOfMeasure import UnitOfMeasureModel
from apps.models.User import UserModel


db.init_app(app)


def load_tables():
    db.engine.execute("SET @@auto_increment_increment=1;")
    db.engine.execute("SET @@auto_increment_offset=1;")

    # District
    if DistrictModel.query.first() is None:
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
        pass

    # Plan
    if PlanModel.query.first() is None:
        plan1 = PlanModel('General Patient', 'GEP', 'You can be monitored by your doctor through the application',
                          None, 0)
        plan2 = PlanModel('Premium Patient', 'PRP', 'You can sync your wearable with the application', None, 9.99)
        plan3 = PlanModel('General Doctor', 'GED', 'You can take care of 10 patients', 10, 39.99)
        plan4 = PlanModel('Premium Doctor', 'PRD', 'You can take care of 20 patients and grant access to dashboard.',
                          20, 59.99)
        plan5 = PlanModel('Extra Plan', 'EXT', 'You can add 10 more patients to your plan', 10, 9.99)

        plans = [plan1, plan2, plan3, plan4, plan5]

        for obj_plan in plans:
            obj_plan.save_to_db()
            pass
        pass

    # Role
    if RoleModel.query.first() is None:
        role1 = RoleModel('Doctor', 'DOC')
        role2 = RoleModel('Patient', 'PAT')

        roles = [role1, role2]

        for obj_role in roles:
            obj_role.save_to_db()
            pass
        pass

    # Medical Speciality
    if MedicalSpecialityModel.query.first() is None:
        med_spec1 = MedicalSpecialityModel('Pathological Anatomy', 'PAA')
        med_spec2 = MedicalSpecialityModel('Allergology', 'ALE')
        med_spec3 = MedicalSpecialityModel('Cardiology', 'CAR')
        med_spec4 = MedicalSpecialityModel('Cardiac surgery', 'CRS')
        med_spec5 = MedicalSpecialityModel('General Surgery', 'GNS')
        med_spec6 = MedicalSpecialityModel('Plastic Surgery', 'PLS')
        med_spec7 = MedicalSpecialityModel('Dermatology', 'DER')
        med_spec8 = MedicalSpecialityModel('Endocrinology', 'END')
        med_spec9 = MedicalSpecialityModel('Nutrition', 'NUT')
        med_spec10 = MedicalSpecialityModel('Gastroenterology', 'GAS')
        med_spec11 = MedicalSpecialityModel('Geriatrician', 'GER')
        med_spec12 = MedicalSpecialityModel('Gynecology', 'GYN')
        med_spec13 = MedicalSpecialityModel('Hematology', 'HEM')
        med_spec14 = MedicalSpecialityModel('Hepatology', 'HEP')
        med_spec15 = MedicalSpecialityModel('Infectious Diseases', 'IDS')
        med_spec16 = MedicalSpecialityModel('Internal Medicine', 'INM')
        med_spec17 = MedicalSpecialityModel('Nephrology', 'NEP')
        med_spec18 = MedicalSpecialityModel('Pulmonology', 'PUL')
        med_spec19 = MedicalSpecialityModel('Neurology', 'NEU')
        med_spec20 = MedicalSpecialityModel('Neurosurgery', 'NRS')
        med_spec21 = MedicalSpecialityModel('Ophthalmology', 'OPH')
        med_spec22 = MedicalSpecialityModel('Otolaryngology', 'OTO')
        med_spec23 = MedicalSpecialityModel('Oncology', 'ONC')
        med_spec24 = MedicalSpecialityModel('Pediatrician', 'PED')
        med_spec25 = MedicalSpecialityModel('Proctology', 'PRC')
        med_spec26 = MedicalSpecialityModel('Psychiatrist', 'PSY')
        med_spec27 = MedicalSpecialityModel('Rehabilitation', 'REH')
        med_spec28 = MedicalSpecialityModel('Rheumatology', 'RHE')
        med_spec29 = MedicalSpecialityModel('Traumatology', 'TRA')
        med_spec30 = MedicalSpecialityModel('Urology', 'URO')

        med_specialities = [med_spec1, med_spec2, med_spec3, med_spec4, med_spec5, med_spec6, med_spec7, med_spec8,
                            med_spec9, med_spec10, med_spec11, med_spec12, med_spec13, med_spec14, med_spec15,
                            med_spec16, med_spec17, med_spec18, med_spec19, med_spec20, med_spec21, med_spec22,
                            med_spec23, med_spec24, med_spec25, med_spec26, med_spec27, med_spec28, med_spec29,
                            med_spec30]

        for obj_med_spec in med_specialities:
            obj_med_spec.save_to_db()
            pass
        pass

    # Prescription Type
    if PrescriptionTypeModel.query.first() is None:
        prescription_type1 = PrescriptionTypeModel('Medication', 'MED')
        prescription_type2 = PrescriptionTypeModel('Activity', 'ACV')
        prescription_type3 = PrescriptionTypeModel('Diet', 'DIE')
        prescription_type4 = PrescriptionTypeModel('Other', 'OTH')

        prescriptions_type = [prescription_type1, prescription_type2, prescription_type3, prescription_type4]

        for obj_prescription_type in prescriptions_type:
            obj_prescription_type.save_to_db()
            pass
        pass

    # Unit of Measure
    if UnitOfMeasureModel.query.first() is None:
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
                      unit_of_m9, unit_of_m10, unit_of_m11, unit_of_m12, unit_of_m13, unit_of_m14, unit_of_m15,
                      unit_of_m16]

        for obj_unit_of_m in units_of_m:
            obj_unit_of_m.save_to_db()
            pass
        pass

    # User
    if UserModel.query.first() is None:
        user1 = UserModel(1, 'admin',
                          'pbkdf2:sha256:50$XJfN5axB$9085ca50638eb956ab238f650b11896a6810887fa3e13f063406b838ddc1ff3b',
                          'Hugo Andres', 'Rosado Oliden', '944479181', None, '01.02.03.04', None, None, None)
        user2 = UserModel(1, 'dani@hotmail.com',
                          'pbkdf2:sha256:50$6N2VRxhu$15d2e00aecff3ab9a797532efa8e11129f6c6ada6157fbbeef8818efb1ad9bcf',
                          'Dani Alonso', 'Romera Alves', '987654321', None, '04.03.02.01', None, None, None)
        user3 = UserModel(2, 'patient@hotmail.com',
                          'pbkdf2:sha256:50$6N2VRxhu$15d2e00aecff3ab9a797532efa8e11129f6c6ada6157fbbeef8818efb1ad9bcf',
                          'José María', 'Zapata Giménez', '91827364', None, '05.06.07.08', None, None, None)
        user4 = UserModel(2, 'patient',
                          'pbkdf2:sha256:50$4wQeHHga$4b178248f66a23a25ab58c32ecc982a8ad7602e4bcf51406ce01908910b8bd42',
                          'Rosa Luz', 'Ramirez Falcón', '647382915', None, '08.07.06.05', None, None, None)

        users = [user1, user2, user3, user4]

        for obj_user in users:
            obj_user.save_to_db()
            pass
        pass

    # Doctor
    if DoctorModel.query.first() is None:
        doctor1 = DoctorModel(1, 3, None, 'ASDFG12345', None, None, None)
        doctor2 = DoctorModel(2, 4, None, '12345ASDFG', None, None, None)

        doctors = [doctor1, doctor2]

        for obj_doctor in doctors:
            obj_doctor.save_to_db()
            pass
        pass

    # Patient
    if PatientModel.query.first() is None:
        patient1 = PatientModel(3, 1, 20, 'O+', 60.00, 'Male', 1.84, None, None, None)
        patient2 = PatientModel(4, 2, 26, 'AB+', 72.00, 'Female', 1.95, None, None, None)
        patients = [patient1, patient2]

        for obj_patient in patients:
            obj_patient.save_to_db()
            pass
        pass
    pass


# It help to create tables before first request
@app.before_first_request
def create_tables():
    db.create_all(app=app)
    load_tables()
