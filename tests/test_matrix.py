from flask import json

from tests import headers


def test_matrix(client):
    data = {
        "unclassified": [3, 5, 5, 6, 8, 3, 4, 4, 7, 7, 1, 1, 2]
    }
    response = client.post("/matrix", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 201
    result = json.loads(response.data)
    assert "unclassified" in result
    assert "classified" in result
    assert result["unclassified"] == [3, 5, 5, 6, 8, 3, 4, 4, 7, 7, 1, 1, 2]
    assert result["classified"] == [1, 2, 3, 4,
                                    5, 6, 7, 8, 1, 1, 3, 3, 4, 4, 5, 5, 7, 7]


def test_empty_matrix(client):
    data = {
        "unclassified": []
    }
    response = client.post("/matrix", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)[0]
    assert "field" in result
    assert "message" in result
    assert result["field"] == "unclassified"
    assert result["message"] == "Value error, This field must be complete"


def test_none_matrix(client):
    data = {
    }
    response = client.post("/matrix", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)[0]
    assert "field" in result
    assert "message" in result
    assert result["field"] == "unclassified"
    assert result["message"] == "Field required"
