import pytest
from app import app
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app)


def test_health(client):
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    assert response.json() == {"status": "TimeServer is running"}


def test_default_timezone(client):
    response = client.get("/api/v1/time/current/zone")
    data = response.json()
    assert response.status_code == 200
    assert "year" in data
    assert data["timeZone"] == "UTC"


def test_custom_timezone(client):
    response = client.get("/api/v1/time/current/zone?timeZone=Africa/Addis_Ababa")
    data = response.json()
    assert response.status_code == 200
    assert data["timeZone"] == "Africa/Addis_Ababa"


def test_invalid_timezone(client):
    response = client.get("/api/v1/time/current/zone?timeZone=Invalid/Zone")
    data = response.json()
    assert response.status_code == 404
    assert "error" in data


def test_available_timezones(client):
    response = client.get("/api/v1/time/current/zone/availableTimeZones")
    data = response.json()
    assert response.status_code == 200
    assert "Africa/Addis_Ababa" in data
