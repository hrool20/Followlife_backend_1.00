from flask.helpers import make_response
from flask.json import jsonify

from app.db import db


class BaseResponse:
    def __init__(self):
        pass

    @staticmethod
    def json(status, status_code, message, result):
        return make_response(jsonify({
            'status': status,
            'statusCode': status_code,
            'message': message,
            'result': result
        }), status_code)

    @staticmethod
    def created_response(message, result):
        return BaseResponse.json('Created',
                                 201,
                                 message,
                                 result)

    @staticmethod
    def ok_response(message, result):
        return BaseResponse.json('Ok',
                                 200,
                                 message,
                                 result)

    @staticmethod
    def bad_request_response(message, result):
        return BaseResponse.json('Bad Request',
                                 400,
                                 message,
                                 result)

    @staticmethod
    def not_acceptable_response(message, result):
        return BaseResponse.json('Not Acceptable',
                                 406,
                                 message,
                                 result)

    @staticmethod
    def unauthorized_response(message=None):
        return BaseResponse.json('Authorization Required',
                                 401,
                                 'Request does not contain an access header.' if (message is None) else message,
                                 {})

    @staticmethod
    def server_error_response(error):
        return BaseResponse.json('Error: ' + error,
                                 500,
                                 'An internal server occurred. Please try again in a few minutes.',
                                 {})


class BaseMethods:
    def __init__(self):
        pass

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
