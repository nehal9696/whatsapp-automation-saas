import uuid

def test_register_user(client):

    email = f"{uuid.uuid4()}@test.com"

    response = client.post(
        "/auth/register",
        json={
            "email": email,
            "password": "123456"
        }
    )

    assert response.status_code == 200

def test_login_user(client):

    email = f"{uuid.uuid4()}@test.com"

    client.post(
        "/auth/register",
        json={
            "email": email,
            "password": "123456"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "123456"
        },
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data