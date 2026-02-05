import pytest
from fastapi.testclient import TestClient
from webapp.main import app

client = TestClient(app)

def test_get_cities_spain():
    response = client.get("/api/cities?country=Spain")
    assert response.status_code == 200
    data = response.json()
    assert data["country"] == "Spain"
    assert data["cities"] == ["Seville"]
