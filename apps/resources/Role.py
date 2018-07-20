from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from apps.models.BaseClasses import BaseResponse
from apps.models.Role import RoleModel


class Role(Resource):
    @jwt_required
    def get(self, _id=None):
        if _id:
            role = RoleModel.find_by_id(_id)
            if role:
                return BaseResponse.ok_response('Successful.', role.json())
            return BaseResponse.bad_request_response('Role does not exists.', {})
        else:
            roles = list(map(lambda x: x.json(), RoleModel.find_all()))

            return BaseResponse.ok_response('Successful.', roles)

    @jwt_required
    def post(self):
        pass

    @jwt_required
    def put(self, _id=None):
        pass

    @jwt_required
    def delete(self, _id=None):
        pass
