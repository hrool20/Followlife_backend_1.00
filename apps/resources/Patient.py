from datetime import datetime

from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse

from apps.models.BaseClasses import BaseResponse
from apps.models.Patient import PatientModel


class Patient(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('userId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('planId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('age',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('bloodType',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('weight',
                        type=float,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('sex',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('height',
                        type=float,
                        required=False,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, _id=None):
        if _id:
            patient = PatientModel.find_by_id(_id)
            if patient:
                return BaseResponse.ok_response('Successful.', patient.json())
            return BaseResponse.bad_request_response('Patient does not exists.', {})
        else:
            patients = list(map(lambda x: x.json(), PatientModel.find_all()))

            return BaseResponse.ok_response('Successful.', patients)

    @staticmethod
    def post():
        data = Patient.parser.parse_args()

        if PatientModel.find_by_user_id(data['userId']):
            return BaseResponse.bad_request_response('This patient already exists.', {})

        patient = PatientModel(user_id=data['userId'], plan_id=data['planId'], age=data['age'],
                               blood_type=data['bloodType'], weight=data['weight'], sex=data['sex'],
                               height=data['height'], created_at=None, updated_on=None, status=None)
        try:
            patient.save_to_db()
        except Exception as e:
            return BaseResponse.server_error_response(str(e))

        return BaseResponse.created_response('Patient created successfully.', patient.json())

    @jwt_required
    def put(self, _id=None):
        data = Patient.parser.parse_args()

        if _id:
            patient = PatientModel.find_by_id(_id)
            if patient:
                patient.userId = data['userId'] if (data['userId'] is not None) else patient.userId
                patient.planId = data['planId'] if (data['planId'] is not None) else patient.planId
                patient.age = data['age'] if (data['age'] is not None) else patient.age
                patient.bloodType = data['bloodType'] if (data['bloodType'] is not None) else patient.bloodType
                patient.weight = data['weight'] if (data['weight'] is not None) else patient.weight
                patient.sex = data['sex'] if (data['sex'] is not None) else patient.sex
                patient.height = data['height'] if (data['height'] is not None) else patient.height
                patient.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                try:
                    patient.save_to_db()
                except Exception as e:
                    return BaseResponse.server_error_response(str(e))

                return BaseResponse.ok_response('Patient updated successfully.', patient.json())
            else:
                return BaseResponse.not_acceptable_response('Patient does not exists.', {})
        else:
            return BaseResponse.bad_request_response('Patient id is not given.', {})
        pass

    @jwt_required
    def delete(self, _id=None):
        if _id:
            patient = PatientModel.find_by_id(_id)
            if patient:
                patient.status = 'INA'
                patient.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                try:
                    patient.save_to_db()
                except Exception as e:
                    return BaseResponse.server_error_response(str(e))

                return BaseResponse.ok_response('Patient deleted successfully.', patient.json())
            else:
                return BaseResponse.not_acceptable_response('Patient does not exists.', {})
        else:
            return BaseResponse.bad_request_response('Patient id is not given.', {})
