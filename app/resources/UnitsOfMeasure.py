from datetime import datetime

from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse
from app.models.BaseClasses import BaseResponse
from app.models.UnitsOfMeasure import UnitOfMeasureModel


class UnitOfMeasure(Resource):
    @jwt_required
    def get(self, _id=None):
        if _id:
            unit_of_measure = UnitOfMeasureModel.find_by_id(_id)
            if unit_of_measure:
                return BaseResponse.ok_response('Successful.', unit_of_measure.json())
            return BaseResponse.bad_request_response('Unit of measure does not exists.', {})
        else:
            units_of_measure = list(map(lambda x: x.json(), UnitOfMeasureModel.find_all()))

            return BaseResponse.ok_response('Successful.', units_of_measure)
        pass

    @jwt_required
    def post(self):
        pass

    @jwt_required
    def put(self, _id=None):
        pass

    @jwt_required
    def delete(self, _id=None):
        pass
