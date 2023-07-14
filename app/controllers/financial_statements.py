from flask import jsonify, request

from app import app
from app.middleware.auth_middleware import requires_auth
from app.schemas.financial_schema import FinancialSchema
from app.services.financial_service import calculations


@app.route("/financial", methods=["POST"])
@requires_auth
def financial(current_user):
    calc = calculations(FinancialSchema, request.get_json())
    response, status_code = calc.calculate_balance()
    return jsonify(response), status_code
