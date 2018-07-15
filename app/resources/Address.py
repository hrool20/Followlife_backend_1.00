from datetime import datetime

from flask.globals import request
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse
from app.models.BaseClasses import BaseResponse
from app.models.Address import AddressModel
from app.models.Doctor import DoctorModel


class Address(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('districtId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('street',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('neighborhood',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('complement',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('number',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, _id=None, ):
        if _id:
            address = AddressModel.find_by_id(_id)
            doctors_list = True if 'doctors' in request.path else False
            if address:
                return BaseResponse.ok_response('Successful.', address.json(doctors_list=doctors_list))
            return BaseResponse.bad_request_response('Address does not exists.', {})
        else:
            return BaseResponse.bad_request_response('It is necessary an address id.', {})

    @jwt_required
    def post(self):
        try:
            data = Address.parser.parse_args()

            if AddressModel.find_by_number(data['number']):
                return BaseResponse.bad_request_response('This address already exists.', {})

            address = AddressModel(district_id=data['districtId'], street=data['street'],
                                   neighborhood=data['neighborhood'], complement=data['complement'],
                                   number=data['number'], created_at=None, updated_on=None, status=None)

            address.save_to_db()

            return BaseResponse.created_response('Address created successfully.', address.json(doctors_list=False))
        except Exception as e:
            return BaseResponse.server_error_response(str(e))

    @jwt_required
    def put(self, _id=None):
        try:
            data = Address.parser.parse_args()

            address = AddressModel.find_by_id(_id)
            doctors_list = True if 'doctors' not in request.path else False
            if address and doctors_list:
                address.districtId = data['districtId'] if (data['district'] is not None) else address.districtId
                address.street = data['street'] if (data['street'] is not None) else address.street
                address.neighborhood = data['neighborhood'] if (data['neighborhood'] is not None) \
                    else address.neighborhood
                address.complement = data['complement'] if (data['complement'] is not None) else address.complement
                address.number = data['number'] if (data['number'] is not None) else address.number
                address.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                address.save_to_db()

                return BaseResponse.ok_response('Address updated successfully.', address.json(doctors_list=False))
            elif doctors_list is False:
                return BaseResponse.not_acceptable_response('Url request is not acceptable.', {})
            else:
                return BaseResponse.not_acceptable_response('Address does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(str(e))

    @jwt_required
    def delete(self, _id=None):
        try:
            address = AddressModel.find_by_id(_id)
            doctors_list = True if 'doctors' not in request.path else False

            if address and doctors_list:
                address.status = 'INA'
                address.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                address.save_to_db()

                return BaseResponse.ok_response('Address deleted successfully.', {})
            elif doctors_list is False:
                return BaseResponse.not_acceptable_response('Url request is not acceptable.', {})
            else:
                return BaseResponse.not_acceptable_response('Address does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(str(e))
