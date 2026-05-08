import uuid

def get_auth_token(client):

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

    data = response.json()

    return data["access_token"]

def test_create_business(client):

    token = get_auth_token(client)

    response = client.post(
        "/api/business",
        json={
            "name": "Test Business"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200