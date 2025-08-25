from fastapi.testclient import TestClient
from src.myapp.api import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is up and running!"}

def test_greet():
    response = client.post("/greet", json={"name": "Ashitosh"})
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello, Ashitosh! Welcome to the API."}

def test_greet_invalid():
    response = client.post("/greet", json={"name": "Ashitosh123"})
    assert response.status_code == 400
