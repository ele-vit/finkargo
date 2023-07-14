from flask import json
from tests import headers


def test_create_user(client):
    data = {
        "username": "carlos",
        "email": "c@c.com",
        "password": "password"
    }
    response = client.post("/user", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 201
    result = json.loads(response.data)
    assert result['username'] == data['username']

def test_create_user_already_exist(client):
    data = {
        "username": "carlos",
        "email": "c@c.com",
        "password": "password"
    }
    response = client.post("/user", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 409
    result = json.loads(response.data)
    assert 'duplicate key' in result['message']

def test_create_user_value_error(client):
    data = {
        "username": "",
        "email": "",
        "password": ""
    }
    response = client.post("/user", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)
    assert 'Value error' in result[0]['message']

def test_create_user_not_data(client):
    data = {
    }
    response = client.post("/user", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)
    assert 'Field required' in result[0]['message']