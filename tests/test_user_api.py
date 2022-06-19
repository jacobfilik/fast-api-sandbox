
from fastapi.testclient import TestClient
import json
from sql_app.main import app


client = TestClient(app)


def assert_user_response(res, email, username, id_num=None):

    assert res['email'] == email
    assert res['username'] == username
    assert 'id' in res
    assert 'time_created' in res
    assert 'is_active' in res

    assert 'password' not in res
    assert 'hashed_password' not in res

    if id_num:
        assert res['id'] == id_num


def test_create_user():

    username = "AName"
    email = "aname@address.com"
    password = "password"

    response = client.post(
        "/users/",
        json={"username": username,
              "email": email,
              "password": password},
    )

    assert response.status_code == 200
    res = response.json()

    assert_user_response(res, email, username)

    response = client.get("/users/" + str(res["id"]))
    get_res = response.json()
    assert response.status_code == 200

    assert_user_response(get_res, email, username, id_num = res["id"])

    #response = client.delete("/users/" + str(res["id"]))
    #assert response.status_code == 405

    response = client.delete("/users/" + str(res["id"]) + "?secret=foobar")
    assert response.status_code == 204

