from datetime import datetime

from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse

from apps.models.BaseClasses import BaseResponse
from apps.models.Device import DeviceModel
from apps.models.User import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('roleId',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('email',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('password',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('fullName',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('lastName',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('phoneNumber',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('profilePicture',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('lastIPConnection',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, _id=None):
        if _id:
            user = UserModel.find_by_id(_id)
            if user:
                return BaseResponse.ok_response('Successful.', user.json(is_long=True))
            return BaseResponse.bad_request_response('User does not exists.', {})
        else:
            users = list(map(lambda x: x.json(is_long=True), UserModel.find_all()))

            return BaseResponse.ok_response('Successful.', users)

    @staticmethod
    def post():
        try:
            data = User.parser.parse_args()

            if UserModel.find_by_email(data['email']):
                return BaseResponse.bad_request_response('This email already exists.', {})
            elif UserModel.find_by_phone(data['phoneNumber']):
                return BaseResponse.bad_request_response('This phone number already exists.', {})

            hash_password = UserModel.hash_password(data['password'])
            user = UserModel(role_id=data['roleId'], email=data['email'], password=hash_password,
                             full_name=data['fullName'], last_name=data['lastName'], phone_number=data['phoneNumber'],
                             profile_picture=data['profilePicture'], last_ip_connection=data['lastIPConnection'],
                             created_at=None, updated_on=None, status=None)

            user.save_to_db()

            if user.lastIPConnection and DeviceModel.find_by_ip(user.lastIPConnection) is None:
                device = DeviceModel(user_id=user.id, ip=user.lastIPConnection,
                                     created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                device.save_to_db()

            return BaseResponse.created_response('User created successfully.', user.json(is_long=True))
        except Exception as e:
            return BaseResponse.server_error_response(str(e))

    @jwt_required
    def put(self, _id=None):
        try:
            data = User.parser.parse_args()

            user = UserModel.find_by_id(_id)
            if user:
                hash_password = UserModel.hash_password(data['password'])

                user.roleId = data['roleId'] if (data['roleId'] is not None) else user.roleId
                user.email = data['email'] if (data['email'] is not None) else user.email
                user.password = hash_password if (data['password'] is not None) else user.password
                user.fullName = data['fullName'] if (data['fullName'] is not None) else user.fullName
                user.lastName = data['lastName'] if (data['lastName'] is not None) else user.lastName
                user.phoneNumber = data['phoneNumber'] if (data['phoneNumber'] is not None) else user.phoneNumber
                user.profilePicture = data['profilePicture'] if (data['profilePicture'] is not None) \
                    else user.profilePicture
                user.lastIPConnection = data['lastIPConnection'] if (data['lastIPConnection'] is not None) \
                    else user.lastIPConnection
                user.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                user.save_to_db()

                if user.lastIPConnection and DeviceModel.find_by_ip(user.lastIPConnection) is None:
                    device = DeviceModel(user_id=user.id, ip=user.lastIPConnection,
                                         created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    device.save_to_db()

                return BaseResponse.ok_response('User updated successfully.', user.json(is_long=True))
            else:
                return BaseResponse.not_acceptable_response('User does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(str(e))

    @jwt_required
    def delete(self, _id=None):
        try:
            user = UserModel.find_by_id(_id)
            if user:
                user.status = 'INA'
                user.updatedOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                user.save_to_db()

                return BaseResponse.ok_response('User deleted successfully.', {})
            else:
                return BaseResponse.not_acceptable_response('User does not exists.', [])
        except Exception as e:
            return BaseResponse.server_error_response(str(e))
