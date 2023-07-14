from flask import json
from tests import headers


def test_get_user(client):
    data = {
        "username": "otheeeer1",
        "email": "ccccc@cccc1.com",
        "password": "password"
    }
    user = client.post("/user", data=json.dumps(data),
                           headers=headers, content_type="application/json").json
    response = client.get("/user/"+str(user['id']), headers=headers,
                             content_type="application/json")
    assert response.status_code == 201
    result = json.loads(response.data)
    assert data['email'] == result['email']


def test_get_user_not_exist(client):
    response = client.get("/user/99999999", headers=headers,
                             content_type="application/json")
    assert response.status_code == 404
    result = json.loads(response.data)
    assert result['message'] == 'User not found'


def test_get_user_id_not_valid(client):
    response = client.get("/user/xxxxxxx", headers=headers,
                             content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)
    assert 'Input should be a valid integer' in result[0]['message']