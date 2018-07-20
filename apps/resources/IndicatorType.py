from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from apps.models.BaseClasses import BaseResponse
from apps.models.IndicatorType import IndicatorTypeModel


class IndicatorType(Resource):
    @jwt_required
    def get(self, _id=None):
        if _id:
            indicator_type = IndicatorTypeModel.find_by_id(_id)
            if indicator_type:
                return BaseResponse.ok_response('Successful.', indicator_type.json())
            return BaseResponse.bad_request_response('Indicator type does not exists.', {})
        else:
            indicators_type = list(map(lambda x: x.json(), IndicatorTypeModel.find_all()))

            return BaseResponse.ok_response('Successful.', indicators_type)

    @jwt_required
    def post(self):
        pass

    @jwt_required
    def put(self, _id=None):
        pass

    @jwt_required
    def delete(self, _id=None):
        pass
