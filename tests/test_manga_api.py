from fastapi.testclient import TestClient
from app.main import app
from fastapi import HTTPException

client = TestClient(app)

def test_search_manga():
    response = client.get("/api/v1/search?title=Naruto")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "title" in data[0]

def test_get_manga_info():
    manga_id = "a77742b1-befd-49a4-bff0-62c5c3ad57e6"  # ID Naruto
    response = client.get(f"/api/v1/manga/{manga_id}")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Manga not found"
    
def test_get_manga_info_invalid_id():
    response = client.get("/api/v1/manga/invalid_id")
    assert response.status_code == 404