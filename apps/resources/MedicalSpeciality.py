from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from apps.models.BaseClasses import BaseResponse
from apps.models.MedicalSpeciality import MedicalSpecialityModel


class MedicalSpeciality(Resource):
    @jwt_required
    def get(self, _id=None):
        if _id:
            medical_speciality = MedicalSpecialityModel.find_by_id(_id)
            if medical_speciality:
                return BaseResponse.ok_response('Successful.', medical_speciality.json())
            return BaseResponse.bad_request_response('Medical speciality does not exists.', {})
        else:
            medical_specialities = list(map(lambda x: x.json(), MedicalSpecialityModel.find_all()))

            return BaseResponse.ok_response('Successful.', medical_specialities)
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
