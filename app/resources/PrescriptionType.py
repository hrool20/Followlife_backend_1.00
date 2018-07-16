from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from app.models.BaseClasses import BaseResponse
from app.models.PrescriptionType import PrescriptionTypeModel


class PrescriptionType(Resource):
    @jwt_required
    def get(self, _id=None):
        if _id:
            prescription_type = PrescriptionTypeModel.find_by_id(_id)
            if prescription_type:
                return BaseResponse.ok_response('Successful.', prescription_type.json())
            return BaseResponse.bad_request_response('Prescription type does not exists.', {})
        else:
            prescriptions_type = list(map(lambda x: x.json(), PrescriptionTypeModel.find_all()))

            return BaseResponse.ok_response('Successful.', prescriptions_type)

    @jwt_required
    def post(self):
        pass

    @jwt_required
    def put(self, _id=None):
        pass

    @jwt_required
    def delete(self, _id=None):
        pass
