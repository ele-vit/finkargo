from flask import json
from tests import headers


def test_update_user(client):
    data = {
        "username": "carloss",
        "email": "c@cs.com",
        "password": "password"
    }
    response = client.put("/user/1", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 201
    result = json.loads(response.data)
    assert result['message'] == 'Updated user successfully'

def test_update_user_already_exist(client):
    data_o = {
        "username": "carlos",
        "email": "c@c.com",
        "password": "password"
    }
    client.post("/user", data=json.dumps(data_o),
                           headers=headers, content_type="application/json")
    data_t = {
        "username": "c",
        "email": "cc@cc.com",
        "password": "password"
    }
    client.post("/user", data=json.dumps(data_t),
                           headers=headers, content_type="application/json")
    response = client.put("/user/1", data=json.dumps(data_t),
                           headers=headers, content_type="application/json")
    assert response.status_code == 409
    result = json.loads(response.data)
    assert 'duplicate key' in result['message']

def test_update_user_value_error(client):
    data = {
        "username": "",
        "email": "",
        "password": ""
    }
    response = client.put("/user/1", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)
    assert 'value is not a valid email address:' in result[0]['message']

def test_update_user_not_data(client):
    data = {
    }
    response = client.put("/user/1", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)
    assert 'Field required' in result[0]['message']