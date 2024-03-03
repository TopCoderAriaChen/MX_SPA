from flask import request
from flask_jwt_extended import jwt_required
from flask_pydantic import validate
from flask_restx import Namespace, Resource

from app.order.schema import OrderCreateSchema, OrderListSchema
from app.order.service import order_service
from app.user import permission_required

api: Namespace = Namespace("orders")

@api.route("")
class OrdersApi(Resource):
    @permission_required("order_admin")
    def get(self):
        orders = order_service().list_orders()
        return OrderListSchema.from_orm(orders)

    @permission_required("order_admin")
    @validate()
    def post(self, body: OrderCreateSchema):
        order_id = str(order_service().place_order(body).id)
        return order_id, 201
