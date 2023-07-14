from app import app
from app.utils.jwt import decode_token
from functools import wraps
from flask import request, jsonify


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = decode_token(token)
            current_user = data['user_id']
        except:
            return jsonify({'message': 'Access not granted'}), 401

        return f(current_user, *args, **kwargs)

    return decorated