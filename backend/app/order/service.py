from typing import List
from flask_jwt_extended import get_current_user
from app.core.service import BaseService
from app.course.model import Course
from app.order.model import Order
from app.order.schema import OrderCreateSchema
from app.user.model import Student, User

class OrderService(BaseService):
    def __init__(self, user: User):
        super().__init__(OrderService.__name__, user)

    def place_order(self, order: OrderCreateSchema) -> Order:
        self.logger.info("Placing orders", order.dict())
        Student.objects(id=order.student).first_or_404("Student not exists")
        course = Course.objects(id=order.course).first_or_404("Course not exists")
        order.original_price = course.original_price
        return Order(**order.dict(exclude_none=True)).save()

    def list_orders(
        self, user: str = None, course: str = None, campus: str = None
    ) -> List[Order]:
        self.logger.info("Listing orders")
        querys: dict = {}
        if user is not None:
            querys["user"] = user
        if course is not None:
            querys["course"] = course
        if campus is not None:
            querys["campus"] = campus
        return list(Order.objects(**querys))
    
    def get_order(self, order_id) -> Order:
        return Order.objects(id=order_id).first_or_404("Order not exists")

    def delete_order(self, order_id) -> int:
        order = Order.objects(id=order_id).first_or_404("Order not exists")
        return order.delete()


def order_service():
    return OrderService(get_current_user())