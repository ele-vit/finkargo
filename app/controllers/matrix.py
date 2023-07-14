from flask import jsonify, request
from app import app
from app.services.matrix_service import  TheMatrixHasYou
from app.middleware.auth_middleware import requires_auth
from app.schemas.matrix_schema import MatrixSchema


@app.route("/matrix", methods=["POST"])
@requires_auth
def matrix(current_user):
    the_matrix_has_you = TheMatrixHasYou(MatrixSchema, request.get_json())
    response, status_code = the_matrix_has_you.sort_array()
    return jsonify(response), status_code
