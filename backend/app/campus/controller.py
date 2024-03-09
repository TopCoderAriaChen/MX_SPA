from flask_restx import Namespace, Resource

from app.campus.schema import CampusListSchema

from .model import Campus

api = Namespace("campus")


@api.route("")
class CampusListApi(Resource):
    def get(self):
        campus_list = list(Campus.objects())
        return CampusListSchema.from_orm(campus_list)
