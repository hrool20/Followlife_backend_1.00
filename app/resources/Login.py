from flask_jwt_extended.utils import create_access_token, create_refresh_token, get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_refresh_token_required

from app import Security
from app.models.BaseClasses import BaseResponse
from flask_restful import Resource, reqparse


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

    def post(self):
        data = Login.parser.parse_args()

        if data['email']:
            user = Security.authenticate_by_email(data['email'], data['password'])
        else:
            user = Security.authenticate_by_phone(data['phoneNumber'], data['password'])
            pass

        if user:
            access_token = create_access_token(identity=user.json(is_long=False), fresh=True)
            refresh_token = create_refresh_token(identity=user.json(is_long=False))
            return BaseResponse.ok_response('Login successfully.', {
                'accessToken': access_token,
                'refreshToken': refresh_token,
                'user': user.json(is_long=False)
            })
        return BaseResponse.bad_request_response('Incorrect credentials.', {})


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user, fresh=True)
        return BaseResponse.ok_response('Access token refreshed.', {'accessToken': access_token})
