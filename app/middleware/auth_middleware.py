from functools import wraps

from flask import jsonify, request

from app.repositories.user_repository import UserRepository
from app.utils.jwt import decode_token


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = decode_token(token)
            current_user = data['user_id']
            user_repository = UserRepository()
            user = user_repository.find_token(token, current_user)
            if not user:
                return jsonify({'message': 'Access not granted'}), 401
        except BaseException:
            return jsonify({'message': 'Access not granted'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
