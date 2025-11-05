import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    assert response.get_json() == {"status": "TimeServer Is Running"}


def test_time_default(client):
    response = client.get("/api/v1/time/current/zone")
    data = response.get_json()
    assert response.status_code == 200
    assert "year" in data
    assert data["timeZone"] == "UTC"


def test_time_custom_timezone(client):
    response = client.get("/api/v1/time/current/zone?timeZone=Africa/Addis_Ababa")
    data = response.get_json()
    assert response.status_code == 200
    assert data["timeZone"] == "Africa/Addis_Ababa"


def test_invalid_timezone(client):
    response = client.get("/api/v1/time/current/zone?timeZone=Invalid/Zone")
    data = response.get_json()
    assert response.status_code == 400
    assert "error" in data


def test_available_timezones(client):
    response = client.get("/api/v1/time/current/zone/availableTimeZones")
    data = response.get_json()
    assert response.status_code == 200
    assert "Africa/Addis_Ababa" in data
