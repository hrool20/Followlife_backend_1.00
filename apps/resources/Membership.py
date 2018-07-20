from datetime import datetime

from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse
from apps.models.BaseClasses import BaseResponse
from apps.models.Doctor import DoctorModel
from apps.models.Membership import MembershipModel
from apps.models.Patient import PatientModel


class MembershipDoctor(Resource):
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
    parser.add_argument('referencedEmail',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('accessCode',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, doctor_id=None, _id=None):
        doctor = DoctorModel.find_by_id(doctor_id)
        if doctor is None:
            return BaseResponse.bad_request_response('Doctor does not exists.', {})

        if _id:
            membership = MembershipModel.find_by_patient_id(_id)
            if membership:
                return BaseResponse.ok_response('Successful.', membership.json(role_id=1))
            return BaseResponse.bad_request_response('Membership does not exists.', {})
        else:
            memberships = list(map(lambda x: x.json(role_id=1), doctor.memberships))

            return BaseResponse.ok_response('Successful.', memberships)

    @jwt_required
    def post(self, doctor_id=None):
        try:
            data = MembershipDoctor.parser.parse_args()
            supposed_membership = MembershipModel.find_by_doctor_id(doctor_id)

            if DoctorModel.find_by_id(doctor_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})
            elif supposed_membership.patientId == data['patientId']:
                if supposed_membership.status == 'INA':
                    supposed_membership.status = 'ACT'

                    supposed_membership.save_to_db()

                    return BaseResponse.ok_response('Membership activated.', supposed_membership.json(role_id=1))
                return BaseResponse.bad_request_response('A membership with this patient already exists.', {})

            membership = MembershipModel(doctor_id=doctor_id, patient_id=data['patientId'],
                                         referenced_email=data['referencedEmail'], access_code=None, created_at=None,
                                         expires_at=None, updated_on=None, status=None)

            membership.save_to_db()

            return BaseResponse.created_response('Membership created successfully.', membership.json(role_id=1))
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))

    @jwt_required
    def put(self, doctor_id=None, _id=None):
        try:
            data = MembershipDoctor.parser.parse_args()

            if DoctorModel.find_by_id(doctor_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})

            membership = MembershipModel.find_by_id(_id)

            if membership:
                membership.expiresAt = data['expiresAt'] if (data['expiresAt'] is not None) else membership.expiresAt
                membership.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                membership.save_to_db()

                return BaseResponse.created_response('Membership updated successfully.', membership.json(role_id=1))
            else:
                return BaseResponse.not_acceptable_response('Membership does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))

    @jwt_required
    def delete(self, doctor_id=None, _id=None):
        try:
            if DoctorModel.find_by_id(doctor_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})

            membership = MembershipModel.find_by_id(_id)

            if membership:
                membership.status = 'INA'
                membership.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                membership.save_to_db()

                return BaseResponse.ok_response('Membership deleted successfully.', {})
            else:
                return BaseResponse.not_acceptable_response('Membership does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))


class MembershipPatient(Resource):
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
    parser.add_argument('referencedEmail',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('accessCode',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('expiredAt',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, patient_id=None, _id=None):
        patient = PatientModel.find_by_id(patient_id)
        if patient:
            return BaseResponse.bad_request_response('Patient does not exists.', {})

        if _id:
            membership = MembershipModel.find_by_doctor_id(_id)
            if membership:
                return BaseResponse.ok_response('Successful.', membership.json(role_id=2))
            return BaseResponse.bad_request_response('Membership does not exists.', {})
        else:
            memberships = list(map(lambda x: x.json(role_id=2), patient.memberships))

            return BaseResponse.ok_response('Successful.', memberships)

    @jwt_required
    def post(self, patient_id=None):
        pass

    @jwt_required
    def put(self, patient_id=None, _id=None):
        try:
            data = MembershipPatient.parser.parse_args()

            if PatientModel.find_by_id(patient_id) is None:
                return BaseResponse.bad_request_response('Patient does not exists.', {})

            membership = MembershipModel.find_by_id(_id)
            if membership:
                membership.accessCode = data['accessCode'] if (data['accessCode'] is not None) \
                    else membership.accessCode
                membership.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                membership.save_to_db()

                return BaseResponse.created_response('Membership updated successfully.', membership.json(role_id=2))
            else:
                return BaseResponse.not_acceptable_response('Membership does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))

    @jwt_required
    def delete(self, patient_id=None, _id=None):
        pass
