from flask import jsonify, request
from app import app
from app.services.user_service import UserService
from app.middleware.auth_middleware import requires_auth
from app.utils.exceptions import MyCustomException
from app.schemas.auth import SignUpSchema
from app.schemas.user_schema import (
    GetUserSchema,
    UpdateUserSchema
)


@app.route("/user", methods=["POST"])
@requires_auth
def create_user(current_user):
    user_service = UserService(request.get_json(), SignUpSchema)
    response, status_code = user_service.create_user()
    return response, status_code


@app.route("/user/<user_id>", methods=["GET"])
@requires_auth
def get_user(current_user, user_id):
    user_service = UserService(user_id, GetUserSchema)
    response, status_code = user_service.get_user()
    return response, status_code


@app.route("/user/<user_id>", methods=["PUT"])
@requires_auth
def update_user(current_user, user_id):
    data = request.get_json()
    data['id'] = user_id
    user_service = UserService(data, UpdateUserSchema)
    response, status_code = user_service.update_user()
    return response, status_code


@app.route("/user/<user_id>", methods=["DELETE"])
@requires_auth
def delete_user(current_user, user_id):
    user_service = UserService(user_id, GetUserSchema)
    response, status_code = user_service.delete_user()
    return response, status_code
