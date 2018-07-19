from datetime import datetime

from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse
from app.models.BaseClasses import BaseResponse
from app.models.Doctor import DoctorModel
from app.models.Patient import PatientModel
from app.models.Prescription import PrescriptionModel


class PrescriptionDoctor(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('doctorId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('patientId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('prescriptionTypeId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('frequency',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('quantity',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('durationInDays',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('description',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('startedAt',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, doctor_id=None, patient_id=None, _id=None):
        if DoctorModel.find_by_id(doctor_id) is None:
            return BaseResponse.bad_request_response('Doctor does not exists.', {})
        elif PatientModel.find_by_id(patient_id) is None:
            return BaseResponse.bad_request_response('Patient does not exists.', {})

        if _id:
            prescription = PrescriptionModel.find_by_id(_id)
            if prescription:
                return BaseResponse.ok_response('Successful.', prescription.json(role_id=1))
            return BaseResponse.bad_request_response('Prescription does not exists.', {})
        else:
            prescriptions = list(map(lambda x: x.json(role_id=1),
                                     PrescriptionModel.find_by_doctor_and_patient_id(doctor_id, patient_id)))

            return BaseResponse.ok_response('Successful.', prescriptions)

    @jwt_required
    def post(self, doctor_id=None, patient_id=None):
        try:
            data = PrescriptionDoctor.parser.parse_args()

            if DoctorModel.find_by_id(doctor_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})
            elif PatientModel.find_by_id(patient_id) is None:
                return BaseResponse.bad_request_response('Patient does not exists.', {})

            prescription = PrescriptionModel(doctor_id=doctor_id, patient_id=patient_id,
                                             prescription_type_id=data['prescriptionTypeId'],
                                             frequency=data['frequency'], quantity=data['quantity'],
                                             duration_in_days=data['durationInDays'], description=data['description'],
                                             created_at=None, started_at=data['startedAt'], finished_at=None,
                                             status=None)

            prescription.save_to_db()

            return BaseResponse.created_response('Prescription created successfully.', prescription.json(role_id=1))
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))

    @jwt_required
    def put(self, doctor_id=None, patient_id=None, _id=None):
        try:
            data = PrescriptionDoctor.parser.parse_args()

            if DoctorModel.find_by_id(doctor_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})
            elif PatientModel.find_by_id(patient_id) is None:
                return BaseResponse.bad_request_response('Patient does not exists.', {})

            prescription = PrescriptionModel.find_by_id(_id)

            if prescription:
                prescription.frequency = data['frequency'] if (data['frequency'] is not None) \
                    else prescription.frequency
                prescription.quantity = data['quantity'] if (data['quantity'] is not None) else prescription.quantity
                prescription.durationInDays = data['durationInDays'] if (data['durationInDays'] is not None) \
                    else prescription.durationInDays
                prescription.description = data['description'] if (data['description'] is not None) \
                    else prescription.description
                prescription.finishedAt = data['finishedAt'] if (data['finishedAt'] is not None) \
                    else prescription.finishedAt

                prescription.save_to_db()

                return BaseResponse.created_response('Prescription updated successfully.', prescription.json(role_id=1))
            else:
                return BaseResponse.not_acceptable_response('Prescription does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))

    @jwt_required
    def delete(self, doctor_id=None, patient_id=None, _id=None):
        try:
            if DoctorModel.find_by_id(doctor_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})
            elif PatientModel.find_by_id(patient_id) is None:
                return BaseResponse.bad_request_response('Patient does not exists.', {})

            prescription = PrescriptionModel.find_by_id(_id)

            if prescription:
                prescription.status = 'INA'
                prescription.finishedAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                prescription.save_to_db()

                return BaseResponse.ok_response('Prescription deleted successfully.', {})
            else:
                return BaseResponse.not_acceptable_response('Prescription does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))


class PrescriptionPatient(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('doctorId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('patientId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('prescriptionTypeId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('frequency',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('quantity',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('durationInDays',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('description',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('startedAt',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, patient_id=None, doctor_id=None, _id=None):
        if PatientModel.find_by_id(patient_id) is None:
            return BaseResponse.bad_request_response('Patient does not exists.', {})
        elif DoctorModel.find_by_id(doctor_id) is None:
            return BaseResponse.bad_request_response('Doctor does not exists.', {})

        if _id:
            prescription = PrescriptionModel.find_by_id(_id)
            if prescription:
                return BaseResponse.ok_response('Successful.', prescription.json(role_id=2))
            return BaseResponse.bad_request_response('Prescription does not exists.', {})
        else:
            prescriptions = list(map(lambda x: x.json(role_id=2),
                                     PrescriptionModel.find_by_doctor_and_patient_id(doctor_id, patient_id)))

            return BaseResponse.ok_response('Successful.', prescriptions)

    @jwt_required
    def post(self, patient_id=None, doctor_id=None):
        pass

    @jwt_required
    def put(self, patient_id=None, doctor_id=None, _id=None):
        pass

    @jwt_required
    def delete(self, patient_id=None, doctor_id=None, _id=None):
        try:
            if PatientModel.find_by_id(patient_id) is None:
                return BaseResponse.bad_request_response('Patient does not exists.', {})
            elif DoctorModel.find_by_id(doctor_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})

            prescription = PrescriptionModel.find_by_id(_id)

            if prescription:
                prescription.status = 'INA'
                prescription.finishedAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                prescription.save_to_db()

                return BaseResponse.ok_response('Prescription deleted successfully.', {})
            else:
                return BaseResponse.not_acceptable_response('Prescription does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))
