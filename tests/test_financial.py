from flask import json
from tests import headers


def test_financial(client):
    data = {
        "months": ["Enero", "Febrero", "Marzo", "Abril"],
        "sales": [30500, 35600, 28300, 33900],
        "bills": [35600, 23400, 18100, 20700]
    }
    response = client.post("/financial", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 201
    result = json.loads(response.data)
    assert len(result) == 4
    assert (-5100.0) == result[0]['balance']


def test_financial_bad_length_list(client):
    data = {
        "months": ["Enero", "Febrero", "Marzo", "Abril"],
        "sales": [30500, 35600],
        "bills": [35600, 23400, 18100, 20700]
    }
    response = client.post("/financial", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 500
    result = json.loads(response.data)
    assert result['message'] == "list index out of range"


def test_financial_not_data(client):
    data = {
    }
    response = client.post("/financial", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)
    assert result[0]['field'] == "months"
    assert result[0]['message'] == "Field required"
