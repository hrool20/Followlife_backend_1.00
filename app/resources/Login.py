from datetime import datetime

from flask_jwt_extended.utils import create_access_token, create_refresh_token, get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_refresh_token_required

from app.models.BaseClasses import BaseResponse
from flask_restful import Resource, reqparse

from app.models.Device import DeviceModel
from app.models.User import UserModel


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phoneNumber',
                        type=str,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('email',
                        type=str,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be left blank.')
    parser.add_argument('lastIPConnection',
                        type=unicode,
                        required=False,
                        help='This field cannot be left blank.')

    @staticmethod
    def post():
        try:
            data = Login.parser.parse_args()

            if data['email']:
                user = UserModel.find_by_email(data['email'])
            else:
                user = UserModel.find_by_phone(data['phoneNumber'])
                pass

            if data['lastIPConnection'] and DeviceModel.find_by_ip(data['lastIPConnection']) is None:
                user.lastIPConnection = data['lastIPConnection'] if (data['lastIPConnection'] is not None) \
                    else user.lastIPConnection
                user.save_to_db()

                device = DeviceModel(user_id=user.id, ip=data['lastIPConnection'],
                                     created_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                device.save_to_db()

            if user and user.check_password(data['password']):
                access_token = create_access_token(identity=user.json(is_long=False), fresh=True)
                refresh_token = create_refresh_token(identity=user.json(is_long=False))
                return BaseResponse.ok_response('Login successfully.', {
                    'accessToken': access_token,
                    'refreshToken': refresh_token,
                    'user': user.json(is_long=False)
                })
            return BaseResponse.bad_request_response('Incorrect credentials.', {})
        except Exception as e:
            return BaseResponse.server_error_response(str(e))


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user, fresh=True)
        return BaseResponse.ok_response('Access token refreshed.', {'accessToken': access_token})
