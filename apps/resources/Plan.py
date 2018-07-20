from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from apps.models.BaseClasses import BaseResponse
from apps.models.Plan import PlanModel


class Plan(Resource):
    @jwt_required
    def get(self, _id=None):
        if _id:
            plan = PlanModel.find_by_id(_id)
            if plan:
                return BaseResponse.ok_response('Successful.', plan.json())
            return BaseResponse.bad_request_response('Plan does not exists.', {})
        else:
            plans = list(map(lambda x: x.json(), PlanModel.find_all()))

            return BaseResponse.ok_response('Successful.', plans)
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
