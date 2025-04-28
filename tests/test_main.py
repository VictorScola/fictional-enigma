from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)

def test_bola8():
    response = client.get("/bola8", params={"pergunta": "Vou passar no teste?"})
    assert response.status_code == 200
    json_data = response.json()
    assert "pergunta" in json_data
    assert "resposta" in json_data
    assert json_data["pergunta"] == "Vou passar no teste?"
