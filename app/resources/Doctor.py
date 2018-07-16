from datetime import datetime

from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse
from app.models.BaseClasses import BaseResponse
from app.models.Doctor import DoctorModel


class Doctor(Resource):
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
    parser.add_argument('addressId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('doctorIdentification',
                        type=str,
                        required=False,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, _id=None):
        if _id:
            doctor = DoctorModel.find_by_id(_id)
            if doctor:
                return BaseResponse.ok_response('Successful.', doctor.json())
            return BaseResponse.bad_request_response('Doctor does not exists.', {})
        else:
            doctors = list(map(lambda x: x.json(), DoctorModel.find_all()))

            return BaseResponse.ok_response('Successful.', doctors)

    @staticmethod
    def post():
        try:
            data = Doctor.parser.parse_args()

            if DoctorModel.find_by_user_id(data['userId']):
                return BaseResponse.bad_request_response('This doctor already exists.', {})

            doctor = DoctorModel(user_id=data['userId'], plan_id=data['planId'], address_id=data['addressId'],
                                 doctor_identification=data['doctorIdentification'], created_at=None,
                                 updated_on=None, status=None)

            doctor.save_to_db()

            return BaseResponse.created_response('Doctor created successfully.', doctor.json())
        except Exception as e:
            return BaseResponse.server_error_response(str(e))

    @jwt_required
    def put(self, _id=None):
        try:
            data = Doctor.parser.parse_args()

            if _id:
                doctor = DoctorModel.find_by_id(_id)
                if doctor:
                    doctor.userId = data['userId'] if (data['userId'] is not None) else doctor.userId
                    doctor.planId = data['planId'] if (data['planId'] is not None) else doctor.planId
                    doctor.addressId = data['addressId'] if (data['addressId'] is not None) else doctor.addressId
                    doctor.doctorIdentification = data['doctorIdentification'] if \
                        (data['doctorIdentification'] is not None) else doctor.doctorIdentification
                    doctor.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    doctor.save_to_db()

                    return BaseResponse.ok_response('User updated successfully.', doctor.json())
                else:
                    return BaseResponse.not_acceptable_response('Doctor does not exists.', {})
            else:
                return BaseResponse.bad_request_response('Doctor id is not given.', {})
        except Exception as e:
            return BaseResponse.server_error_response(str(e))

    @jwt_required
    def delete(self, _id=None):
        try:
            if _id:
                doctor = DoctorModel.find_by_id(_id)
                if doctor:
                    doctor.status = 'INA'
                    doctor.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    doctor.save_to_db()

                    return BaseResponse.ok_response('User deleted successfully.', doctor.json())
                else:
                    return BaseResponse.not_acceptable_response('Doctor does not exists.', {})
            else:
                return BaseResponse.bad_request_response('Doctor id is not given.', {})
        except Exception as e:
            return BaseResponse.server_error_response(str(e))
