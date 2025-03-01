from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de recommandation en ligne 🚀"}

def test_recommend_not_found():
    response = client.get("/recommend/unknown_user")
    assert response.status_code == 404
