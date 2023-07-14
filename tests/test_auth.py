from flask import json

from tests import headers


def test_signup_user(client):
    data = {
        "username": "userr",
        "email": "u@u.com",
        "password": "password"
    }
    response = client.post("/sign-up", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 201
    result = json.loads(response.data)
    assert result['username'] == data['username']


def test_signup_user_already_exist(client):
    data = {
        "username": "carlosss",
        "email": "c@css.com",
        "password": "password"
    }
    client.post("/sign-up", data=json.dumps(data),
                headers=headers, content_type="application/json")
    response = client.post("/sign-up", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 409
    result = json.loads(response.data)
    assert 'duplicate key' in result['message']


def test_signup_user_value_error(client):
    data = {
        "username": "",
        "email": "",
        "password": ""
    }
    response = client.post("/sign-up", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)
    assert 'Value error' in result[0]['message']


def test_signup_user_not_data(client):
    data = {
    }
    response = client.post("/sign-up", data=json.dumps(data),
                           headers=headers, content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)
    assert 'Field required' in result[0]['message']


def test_signin_user(client):
    first_data = {
        "username": "other_user",
        "email": "c@otheruser.com",
        "password": "password"
    }
    client.post("/sign-up", data=json.dumps(first_data),
                content_type="application/json")
    data = {
        "email": "c@otheruser.com",
        "password": "password"
    }
    response = client.post("/sign-in", data=json.dumps(data),
                           content_type="application/json")
    assert response.status_code == 201
    result = json.loads(response.data)
    assert 'token' in result


def test_signin_user_not_exist(client):
    data = {
        "email": "xxxxx@xxxxxx.com",
        "password": "password"
    }
    response = client.post("/sign-in", data=json.dumps(data),
                           content_type="application/json")
    assert response.status_code == 401
    result = json.loads(response.data)
    assert 'message' in result


def test_signin_user_not_data(client):
    data = {
    }
    response = client.post("/sign-in", data=json.dumps(data),
                           content_type="application/json")
    assert response.status_code == 400
    result = json.loads(response.data)
    assert 'Field required' in result[0]['message']
