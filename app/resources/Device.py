from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from app.models.BaseClasses import BaseResponse
from app.models.Device import DeviceModel


class Device(Resource):
    @jwt_required
    def get(self, _id=None):
        if _id:
            device = DeviceModel.find_by_id(_id)
            if device:
                return BaseResponse.ok_response('Successful.', device.json())
            return BaseResponse.bad_request_response('Device does not exists.', {})
        else:
            devices = list(map(lambda x: x.json(), DeviceModel.find_all()))

            return BaseResponse.ok_response('Successful.', devices)

    @jwt_required
    def post(self):
        pass

    @jwt_required
    def put(self, _id=None):
        pass

    @jwt_required
    def delete(self, _id=None):
        pass
