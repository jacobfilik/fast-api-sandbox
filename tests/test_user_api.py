
from fastapi.testclient import TestClient
import json


from sql_app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_user():

    username = "AName"
    email = "aname@address.com"
    password = "password"

    response = client.post(
        "/users/",
        #headers={"X-Token": "coneofsilence"},
        json={"username": username,
              "email": email,
              "password": password},
    )

    assert response.status_code == 200
    res = response.json()

    assert res['email'] == email
    assert res['username'] == username
    assert 'id' in res
    assert 'time_created' in res
    assert 'is_active' in res

    assert 'password' not in res
    assert 'hashed_password' not in res

