from datetime import datetime

from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse
from app.models.BaseClasses import BaseResponse
from app.models.Appointment import AppointmentModel
from app.models.Doctor import DoctorModel
from app.models.Patient import PatientModel


class AppointmentDoctor(Resource):
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
    parser.add_argument('appointmentDate',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('reason',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('canceledAt',
                        type=datetime,
                        required=False,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, _id=None, appointment_id=None):
        doctor = DoctorModel.find_by_id(_id)
        if doctor is None:
            return BaseResponse.bad_request_response('Doctor does not exists.', {})

        if appointment_id:
            appointment = AppointmentModel.find_by_id(appointment_id)
            if appointment:
                return BaseResponse.ok_response('Successful.', appointment.json(role_id=1))
            return BaseResponse.bad_request_response('Appointment does not exists.', {})
        else:
            appointments = list(map(lambda x: x.json(role_id=1), doctor.appointments))

            return BaseResponse.ok_response('Successful.', appointments)

    @jwt_required
    def post(self, _id=None):
        try:
            data = AppointmentDoctor.parser.parse_args()

            if DoctorModel.find_by_id(_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})
            elif AppointmentModel.find_by_appointment_date(data['appointmentDate']):
                return BaseResponse.bad_request_response('An appointment is already scheduled in that date.', {})

            appointment = AppointmentModel(doctor_id=_id, patient_id=data['patientId'],
                                           appointment_date=data['appointmentDate'], reason=data['reason'],
                                           created_at=None, canceled_at=data['canceledAt'], updated_on=None,
                                           status=None)

            appointment.save_to_db()

            return BaseResponse.created_response('Appointment created successfully.', appointment.json(role_id=1))
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))

    @jwt_required
    def put(self, _id=None, appointment_id=None):
        try:
            data = AppointmentDoctor.parser.parse_args()

            if DoctorModel.find_by_id(_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})

            appointment = AppointmentModel.find_by_id(appointment_id)
            if appointment:
                appointment.appointmentDate = data['appointmentDate'] if (data['appointmentDate'] is not None) \
                    else appointment.appointmentDate
                appointment.reason = data['reason'] if (data['reason'] is not None) else appointment.reason
                appointment.canceledAt = data['canceledAt'] if (data['canceledAt'] is not None) \
                    else appointment.canceledAt
                appointment.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                appointment.save_to_db()

                return BaseResponse.created_response('Appointment updated successfully.', appointment.json(role_id=1))
            else:
                return BaseResponse.not_acceptable_response('Appointment does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(str(e))

    @jwt_required
    def delete(self, _id=None, appointment_id=None):
        try:
            if DoctorModel.find_by_id(_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})

            appointment = AppointmentModel.find_by_id(appointment_id)
            if appointment:
                appointment.status = 'INA'
                appointment.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                appointment.canceledAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                appointment.save_to_db()

                return BaseResponse.ok_response('Appointment deleted successfully.', {})
            else:
                return BaseResponse.not_acceptable_response('Appointment does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(str(e))


class AppointmentPatient(Resource):
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
    parser.add_argument('appointmentDate',
                        type=datetime,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('reason',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('canceledAt',
                        type=datetime,
                        required=False,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, _id=None, appointment_id=None):
        patient = PatientModel.find_by_id(_id)
        if patient is None:
            return BaseResponse.bad_request_response('Patient does not exists.', {})

        if appointment_id:
            appointment = AppointmentModel.find_by_id(appointment_id)
            if appointment:
                return BaseResponse.ok_response('Successful.', appointment.json(role_id=2))
            return BaseResponse.bad_request_response('Appointment does not exists.', {})
        else:
            appointments = list(map(lambda x: x.json(role_id=2), patient.appointments))

            return BaseResponse.ok_response('Successful.', appointments)

    @jwt_required
    def post(self, _id=None):
        try:
            data = AppointmentPatient.parser.parse_args()

            if PatientModel.find_by_id(_id) is None:
                return BaseResponse.bad_request_response('Patient does not exists.', {})
            elif AppointmentModel.find_by_appointment_date(data['appointmentDate']):
                return BaseResponse.bad_request_response('An appointment already exists in that date.', {})

            appointment = AppointmentModel(doctor_id=data['doctorId'], patient_id=_id,
                                           appointment_date=data['appointmentDate'], reason=data['reason'],
                                           created_at=None, canceled_at=data['canceledAt'], updated_on=None,
                                           status='INA')

            appointment.save_to_db()

            return BaseResponse.created_response('Appointment registered successfully.', appointment.json(role_id=2))
        except Exception as e:
            return BaseResponse.server_error_response(str(e))

    @jwt_required
    def put(self, _id=None, appointment_id=None):
        try:
            data = AppointmentPatient.parser.parse_args()

            if PatientModel.find_by_id(_id) is None:
                return BaseResponse.bad_request_response('Patient does not exists.', {})

            appointment = AppointmentModel.find_by_id(appointment_id)
            if appointment:
                appointment.appointmentDate = data['appointmentDate'] if (data['appointmentDate'] is not None) \
                    else appointment.appointmentDate
                appointment.reason = data['reason'] if (data['reason'] is not None) else appointment.reason
                appointment.canceledAt = data['canceledAt'] if (data['canceledAt'] is not None) \
                    else appointment.canceledAt
                appointment.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                appointment.save_to_db()

                return BaseResponse.created_response('Appointment updated successfully.', appointment.json(role_id=2))
            else:
                return BaseResponse.not_acceptable_response('Appointment does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(str(e))

    @jwt_required
    def delete(self, _id=None, appointment_id=None):
        try:
            if PatientModel.find_by_id(_id) is None:
                return BaseResponse.bad_request_response('Patient does not exists.', {})

            appointment = AppointmentModel.find_by_id(appointment_id)
            if appointment:
                appointment.status = 'INA'
                appointment.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                appointment.canceledAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                appointment.save_to_db()

                return BaseResponse.ok_response('Appointment deleted successfully.', {})
            else:
                return BaseResponse.not_acceptable_response('Appointment does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(str(e))
