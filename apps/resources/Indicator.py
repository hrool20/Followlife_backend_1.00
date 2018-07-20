from datetime import datetime

from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse
from apps.models.BaseClasses import BaseResponse
from apps.models.Indicator import IndicatorModel


class Indicator(Resource):
    @jwt_required
    def get(self, _id=None):
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
