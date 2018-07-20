from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from app.models.BaseClasses import BaseResponse
from app.models.District import DistrictModel


class District(Resource):
    @jwt_required
    def get(self, _id=None):
        if _id:
            district = DistrictModel.find_by_id(_id)
            if district:
                return BaseResponse.ok_response('Successful.', district.json())
            return BaseResponse.bad_request_response('District does not exists.', {})
        else:
            districts = list(map(lambda x: x.json(), DistrictModel.find_all()))

            return BaseResponse.ok_response('Successful.', districts)
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
