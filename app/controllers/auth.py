from flask import request

from app import app
from app.middleware.auth_middleware import requires_auth
from app.schemas.auth import SignInSchema, SignUpSchema
from app.schemas.user_schema import GetUserSchema
from app.services.user_service import UserService


@app.route("/sign-up", methods=["POST"])
def sign_up():
    user_service = UserService(request.get_json(), SignUpSchema)
    response, status_code = user_service.create_user()
    return response, status_code


@app.route("/sign-in", methods=["POST"])
def login():
    user_service = UserService(request.get_json(), SignInSchema)
    response, status_code = user_service.login()
    return response, status_code


@app.route("/log-out", methods=["GET"])
@requires_auth
def log_out(current_user):
    user_service = UserService(current_user, GetUserSchema)
    response, status_code = user_service.log_out()
    return response, status_code
