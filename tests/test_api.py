from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de recommandation en ligne"}

def test_recommend_not_found():
    response = client.get("/recommend/0")
    assert response.status_code == 404

def test_recommend():
    response = client.get("/recommend/123")
    assert response.status_code == 200
    assert "recommendations" in response.json()

def test_get_user_interests():
    response = client.get("/interests/123")
    assert response.status_code == 200
    assert "interests" in response.json()
