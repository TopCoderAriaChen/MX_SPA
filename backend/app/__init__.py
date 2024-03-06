import os

from dotenv import load_dotenv
from flask import Blueprint, Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flask_restx import Api

from app.campus.controller import api as campus_api
from app.core.encoder import CustomEncoder
from app.course.controller import api as course_api
from app.exceptions import register_resources_exception_handler
from app.order.controller import api as order_api
from app.user import register_user_lookup
from app.user.controller import (
    admins_api,
    auth_api,
    students_api,
    teachers_api,
    users_api,
)

from .log import config_log

load_dotenv("./.env")

api_bp = Blueprint("api", os.getenv("FLASK_APP_NAME"), url_prefix="/api/v1")
api = Api(api_bp)

api.add_namespace(campus_api)
api.add_namespace(auth_api)
api.add_namespace(users_api)
api.add_namespace(admins_api)
api.add_namespace(teachers_api)
api.add_namespace(students_api)
api.add_namespace(course_api)
api.add_namespace(order_api)


def create_app():
    app = Flask(os.getenv("FLASK_APP_NAME"))
    app.config.from_prefixed_env()
    app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
    app.json_encoder = CustomEncoder
    app.config["RESTX_JSON"] = {"cls": CustomEncoder}

    # Log
    config_log(app)
    
    # DB
    MongoEngine(app)
    
    # CORS
    CORS(app)

    # JWT
    jwt = JWTManager(app)
    register_user_lookup(jwt)


    app.register_blueprint(api_bp)
    register_resources_exception_handler(api)


    return app