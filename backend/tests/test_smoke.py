from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_ok():
    response = client.get("/")
    assert response.status_code == 200


def test_register_and_login():
    email = "smoketest@example.com"
    password = "testpassword123"

    client.post("/auth/register", json={"email": email, "password": password})
    response = client.post("/auth/login", json={"email": email, "password": password})

    assert response.status_code == 200
    assert "access_token" in response.json()
