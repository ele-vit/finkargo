from flask import jsonify, request
from app import app
from app.services.user_service import UserService
from app.schemas.auth import SignUpSchema, SignInSchema

@app.route("/sign-up", methods=["POST"])
def sign_up():
    user_service = UserService(request.get_json(), SignUpSchema)
    message, status_code = user_service.create_user()
    return jsonify({'message': message}), status_code


@app.route("/sign-in", methods=["POST"])
def login():
    user_service = UserService(request.get_json(), SignInSchema)
    token, status_code = user_service.login()
    return jsonify({'token': token}), status_code