from datetime import datetime

from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse
from app.models.BaseClasses import BaseResponse
from app.models.Doctor import DoctorModel
from app.models.DoctorSpeciality import DoctorSpecialityModel


class DoctorSpeciality(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('doctorId',
                        type=int,
                        required=True,
                        help='This field cannot be left blank.')
    parser.add_argument('medicalSpecialityId',
                        type=int,
                        required=True,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, _id=None, doc_spec_id=None):
        if DoctorModel.find_by_id(_id):
            return BaseResponse.bad_request_response('Doctor does not exists.', {})

        if doc_spec_id:
            doctor_speciality = DoctorSpecialityModel.find_by_id(doc_spec_id)
            if doctor_speciality:
                return BaseResponse.ok_response('Successful.', doctor_speciality.json())
            return BaseResponse.bad_request_response('Doctor Speciality does not exists.', {})
        else:
            doctor = DoctorModel.find_by_id(_id)
            doctor_specialities = list(map(lambda x: x.json(), doctor.doctorSpecialities))

            return BaseResponse.ok_response('Successful.', doctor_specialities)

    @jwt_required
    def post(self, _id=None):
        try:
            data = DoctorSpeciality.parser.parse_args()

            if DoctorModel.find_by_id(_id):
                return BaseResponse.bad_request_response('Doctor does not exists.', {})
            elif DoctorSpecialityModel.verify_doctor_speciality(data['doctorId'], data['medicalSpecialityId']):
                return BaseResponse.bad_request_response('This doctor already have this specialities.', {})

            doctor_speciality = DoctorSpecialityModel(doctor_id=data['doctorId'],
                                                      medical_speciality_id=data['medicalSpecialityId'])

            doctor_speciality.save_to_db()

            return BaseResponse.created_response('Doctor speciality created successfully.', doctor_speciality.json())
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))

    @jwt_required
    def put(self, _id=None, doc_spec_id=None):
        try:
            data = DoctorSpeciality.parser.parse_args()

            if DoctorModel.find_by_id(_id):
                return BaseResponse.bad_request_response('Doctor does not exists.', {})

            doctor_speciality = DoctorSpecialityModel.find_by_id(doc_spec_id)
            if doctor_speciality:
                doctor_speciality.doctorId = data['doctorId'] if (data['doctorId'] is not None) \
                    else doctor_speciality.doctorId
                doctor_speciality.medicalSpecialityId = data['medicalSpecialityId'] \
                    if (data['medicalSpecialityId'] is not None) else doctor_speciality.medicalSpecialityId

                doctor_speciality.save_to_db()

                return BaseResponse.created_response('Doctor speciality updated successfully.',
                                                     doctor_speciality.json())
            else:
                return BaseResponse.not_acceptable_response('Doctor speciality does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))

    @jwt_required
    def delete(self, _id=None, doc_spec_id=None):
        try:
            if DoctorModel.find_by_id(_id):
                return BaseResponse.bad_request_response('Doctor does not exists.', {})

            doctor_speciality = DoctorSpecialityModel.find_by_id(doc_spec_id)
            if doctor_speciality:
                doctor_speciality.delete_from_db()

                return BaseResponse.ok_response('Doctor speciality deleted successfully.', {})
            else:
                return BaseResponse.not_acceptable_response('Doctor speciality does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))
