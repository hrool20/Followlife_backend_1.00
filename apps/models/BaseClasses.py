import base64

from flask.helpers import make_response
from flask.json import jsonify

from apps.db import db


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

    @staticmethod
    def encode(key, value):
        enc = []
        for i in range(len(value)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(value[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        return base64.urlsafe_b64encode("".join(enc))

    @staticmethod
    def decode(key, encoded_value):
        dec = []
        encoded_value = base64.urlsafe_b64decode(encoded_value)
        for i in range(len(encoded_value)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(encoded_value[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        return "".join(dec)

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
